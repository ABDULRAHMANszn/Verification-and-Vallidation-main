from books2 import Book
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel,Field

from connection import engine , Base ,seed_meals , SessionLocal ,Meal,User
from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.middleware.cors import CORSMiddleware
from connection import Order, OrderItem
from pydantic import BaseModel
from typing import List

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

def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/meals")
async def get_meals(db: db_dependency):
    return db.query(Meal).all()

# @app.get("/ordersall")
# async def get_orders(db: db_dependency):
#     return db.query(Order).all()
# @app.get("/orderitemssall/{user_id}/{order_id}")
# async def get_orders(order_id:int,user_id :int,db: db_dependency):
#     return db.query(OrderItem).filter(Order.user_id == user_id , OrderItem.order_id ==order_id).all()

@app.get("/meals/{id}")
async def get_meal(db :db_dependency ,  id : int = Path(gt=0)):
    meal = db.query(Meal).filter(Meal.meal_id == id).first()
    if meal is not None:
        return meal
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)




from pydantic import BaseModel

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
        email=f"{data.username}@app.com",  # placeholder
        password=data.password,            # plain text, simple
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
        User.password == data.password   # plain text check
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "user_id": user.user_id,
        "username": user.username,
        "role": user.role,
    }







class OrderItemRequest(BaseModel):
    meal_id: int
    quantity: int
    price: float

class CreateOrderRequest(BaseModel):
    user_id: int
    items: List[OrderItemRequest]
    notes: str | None = None

@app.post("/orders")
async def create_order(data: CreateOrderRequest, db: db_dependency):
    # 1. Calculate total
    total = sum(item.price * item.quantity for item in data.items)

    # 2. Create the order
    new_order = Order(
        user_id=data.user_id,
        total_price=total,
        notes=data.notes,
        status="accepted",
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # 3. Create order items
    for item in data.items:
        order_item = OrderItem(
            order_id=new_order.order_id,
            meal_id=item.meal_id,
            quantity=item.quantity,
            price=item.price,
            subtotal=item.price * item.quantity,
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
    # Get all orders for this user
    orders = db.query(Order).filter(Order.user_id == user_id).all()

    result = []
    for order in orders:
        # For each order, get items joined with meal info
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




@app.get("/orders/user/{user_id}/full")
async def get_user_orders_full(user_id: int, db: db_dependency):
    # Get all orders for this user
    orders = db.query(Order).filter(Order.user_id == user_id).all()

    result = []
    for order in orders:
        # For each order, get items joined with meal info
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