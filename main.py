from typing import Annotated, List, Optional
from typing_extensions import TypeAlias
import re
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field, field_validator
from fastapi import FastAPI, HTTPException, Depends, Path, Header
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from jose import jwt, JWTError

from connection import (
    engine, Base, seed_meals, update_meal_ingredients,
    SessionLocal, Meal, User, Order, OrderItem,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)
seed_meals()
update_meal_ingredients()


# ─────────────────────────────────────────────
#  Security helpers
# ─────────────────────────────────────────────

# NOTE: change SECRET_KEY to a random value and load from env in production
SECRET_KEY = "food-app-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(user_id: int, username: str, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "username": username, "role": role, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(authorization: Optional[str] = Header(default=None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
            "user_id": int(payload["sub"]),
            "username": payload["username"],
            "role": payload["role"],
        }
    except (JWTError, KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid or expired token")


CurrentUser: TypeAlias = Annotated[dict, Depends(get_current_user)]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency: TypeAlias = Annotated[Session, Depends(get_db)]


# ─────────────────────────────────────────────
#  MEALS
# ─────────────────────────────────────────────

@app.get("/meals")
async def get_meals(db: db_dependency):
    return db.query(Meal).all()


@app.get("/meals/{id}")
async def get_meal(db: db_dependency, id: int = Path(gt=0)):
    meal = db.query(Meal).filter(Meal.meal_id == id).first()
    if meal is not None:
        return meal
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# ─────────────────────────────────────────────
#  AUTH
# ─────────────────────────────────────────────

PHONE_REGEX = re.compile(r"^\+?[0-9]{7,15}$")


class RegisterRequest(BaseModel):
    username: str = Field(min_length=4, max_length=100)
    password: str = Field(min_length=6)
    phone: str
    address: str
    email: Optional[str] = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not PHONE_REGEX.match(v.strip()):
            raise ValueError("Phone must be 7–15 digits, optionally prefixed with '+'")
        return v.strip()


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/auth/register", status_code=201)
async def register(data: RegisterRequest, db: db_dependency):
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    email = data.email.strip() if data.email else f"{data.username}@app.com"

    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already in use")

    user = User(
        username=data.username,
        email=email,
        password=hash_password(data.password),
        phone=data.phone,
        address=data.address,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(user.user_id, user.username, user.role)
    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role,
        "token": token,
    }


@app.post("/auth/login")
async def login(data: LoginRequest, db: db_dependency):
    user = db.query(User).filter(User.username == data.username).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(user.user_id, user.username, user.role)
    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role,
        "token": token,
    }


# ─────────────────────────────────────────────
#  ORDERS
# ─────────────────────────────────────────────

class OrderItemRequest(BaseModel):
    meal_id: int
    quantity: int = Field(gt=0)


class CreateOrderRequest(BaseModel):
    user_id: int
    items: List[OrderItemRequest]
    notes: Optional[str] = None


@app.post("/orders", status_code=201)
async def create_order(
    data: CreateOrderRequest,
    db: db_dependency,
    current_user: CurrentUser,
):
    if current_user["user_id"] != data.user_id:
        raise HTTPException(status_code=403, detail="Cannot create orders for another user")

    if not db.query(User).filter(User.user_id == data.user_id).first():
        raise HTTPException(status_code=404, detail="User not found")

    total = 0.0
    resolved_items = []

    for item in data.items:
        meal = db.query(Meal).filter(Meal.meal_id == item.meal_id).first()
        if not meal:
            raise HTTPException(
                status_code=404,
                detail=f"Meal with id {item.meal_id} not found",
            )
        if not meal.is_available:
            raise HTTPException(
                status_code=400,
                detail=f"Meal '{meal.meal_name}' is currently unavailable",
            )
        price = float(meal.price)
        subtotal = price * item.quantity
        total += subtotal
        resolved_items.append({
            "meal_id": item.meal_id,
            "quantity": item.quantity,
            "price": price,
            "subtotal": subtotal,
        })

    new_order = Order(
        user_id=data.user_id,
        total_price=total,
        notes=data.notes,
        status="accepted",
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in resolved_items:
        db.add(OrderItem(
            order_id=new_order.order_id,
            meal_id=item["meal_id"],
            quantity=item["quantity"],
            price=item["price"],
            subtotal=item["subtotal"],
        ))

    db.commit()

    return {
        "order_id": new_order.order_id,
        "total_price": float(new_order.total_price),
        "status": new_order.status,
    }


@app.get("/orders/user/{user_id}")
async def get_user_orders(user_id: int, db: db_dependency, current_user: CurrentUser):
    if current_user["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
    return db.query(Order).filter(Order.user_id == user_id).all()


@app.get("/orders/user/{user_id}/full")
async def get_user_orders_full(user_id: int, db: db_dependency, current_user: CurrentUser):
    if current_user["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    orders = db.query(Order).filter(Order.user_id == user_id).all()

    result = []
    for order in orders:
        items = (
            db.query(OrderItem, Meal)
            .join(Meal, OrderItem.meal_id == Meal.meal_id)
            .filter(OrderItem.order_id == order.order_id)
            .all()
        )
        result.append({
            "id": order.order_id,
            "date": order.order_date.isoformat() if order.order_date else None,
            "status": order.status,
            "items": [
                {
                    "title": meal.meal_name,
                    "price": float(item.price),
                    "quantity": item.quantity,
                    "image": meal.image_path,
                }
                for item, meal in items
            ],
        })

    return result
