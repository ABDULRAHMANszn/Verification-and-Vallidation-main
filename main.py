from typing import Annotated, List
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from connection import engine, Base, seed_meals, SessionLocal, Meal, User
from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.middleware.cors import CORSMiddleware
from connection import Order, OrderItem

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


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

class RegisterRequest(BaseModel):
    username: str = Field(min_length=4)
    password: str
    phone: str
    address: str


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/auth/register")
async def register(data: RegisterRequest, db: db_dependency):
    existing = db.query(User).filter(User.username == data.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    user = User(
        username=data.username,
        email=f"{data.username}@app.com",
        password=data.password,  # ⚠️ TODO: hash with bcrypt
        phone=data.phone,
        address=data.address,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role,
    }


@app.post("/auth/login")
async def login(data: LoginRequest, db: db_dependency):
    user = db.query(User).filter(
        User.username == data.username,
        User.password == data.password  # ⚠️ TODO: use bcrypt verify
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role,
    }


# ─────────────────────────────────────────────
#  ORDERS
# ─────────────────────────────────────────────

class OrderItemRequest(BaseModel):
    meal_id: int
    quantity: int


class CreateOrderRequest(BaseModel):
    user_id: int
    items: List[OrderItemRequest]
    notes: str | None = None


@app.post("/orders")
async def create_order(data: CreateOrderRequest, db: db_dependency):
    # FIX: price is now fetched from DB, not trusted from frontend
    total = 0.0
    resolved_items = []

    for item in data.items:
        meal = db.query(Meal).filter(Meal.meal_id == item.meal_id).first()
        if not meal:
            raise HTTPException(
                status_code=404,
                detail=f"Meal with id {item.meal_id} not found"
            )
        if not meal.is_available:
            raise HTTPException(
                status_code=400,
                detail=f"Meal '{meal.meal_name}' is currently unavailable"
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

    # Create the order
    new_order = Order(
        user_id=data.user_id,
        total_price=total,
        notes=data.notes,
        status="accepted",
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # Create order items
    for item in resolved_items:
        order_item = OrderItem(
            order_id=new_order.order_id,
            meal_id=item["meal_id"],
            quantity=item["quantity"],
            price=item["price"],
            subtotal=item["subtotal"],
        )
        db.add(order_item)

    db.commit()

    return {
        "order_id": new_order.order_id,
        "total_price": float(new_order.total_price),
        "status": new_order.status,
    }


@app.get("/orders/user/{user_id}")
async def get_user_orders(user_id: int, db: db_dependency):
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders


@app.get("/orders/user/{user_id}/full")
async def get_user_orders_full(user_id: int, db: db_dependency):
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
            ]
        })

    return result