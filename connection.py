from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SERVER = "localhost\\SQLEXPRESS"
DB_NAME = "food_app"
DRIVER = "ODBC Driver 17 for SQL Server"

DATABASE_URL = f"mssql+pyodbc://@{SERVER}/{DB_NAME}?driver={DRIVER.replace(' ', '+')}&Trusted_Connection=yes"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# =========================
# Base & Models
# =========================

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id    = Column(Integer, primary_key=True, autoincrement=True)
    username   = Column(String(100), nullable=False, unique=True)
    email      = Column(String(150), nullable=False, unique=True)
    password   = Column(String(255), nullable=False)
    phone      = Column(String(20))
    address    = Column(String(255))
    role       = Column(String(20), default="user")

class Meal(Base):
    __tablename__ = "meals"

    meal_id      = Column(Integer, primary_key=True, autoincrement=True)
    meal_name    = Column(String(150), nullable=False)
    description  = Column(Text)
    ingredients  = Column(Text)
    price        = Column(Numeric(10, 2), nullable=False)
    image_path   = Column(String(255))
    category     = Column(String(50))
    is_available = Column(Integer, default=1)

class Order(Base):
    __tablename__ = "orders"

    order_id    = Column(Integer, primary_key=True, autoincrement=True)
    user_id     = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    order_date  = Column(DateTime, default=func.now())
    status      = Column(String(50), default="Pending")
    total_price = Column(Numeric(10, 2), default=0)
    notes       = Column(Text)

class OrderItem(Base):
    __tablename__ = "order_items"

    item_id  = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    meal_id  = Column(Integer, ForeignKey("meals.meal_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price    = Column(Numeric(10, 2), nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)

# =========================
# Init & Seed
# =========================

def init_database():
    Base.metadata.create_all(engine)
    print("Database جاهزة")

def seed_meals():
    with SessionLocal() as session:
        if session.query(Meal).count() > 0:
            print("⚠️ meals already seeded")
            return

        meals = [
            Meal(meal_name='Pizza Hut Delicious Pizza',    description='Delicious pizza from Pizza Hut',           ingredients='Dough, Tomato Sauce, Mozzarella, Pepperoni, Bell Peppers', price=120.00, image_path='/images/r1.png',    category='Pizza',   is_available=1),
            Meal(meal_name='Chipotle Mexican Grill',        description='Fresh Mexican grill',                      ingredients='Rice, Black Beans, Salsa, Guacamole, Sour Cream, Tortilla',  price=80.00,  image_path='/images/r2.png',    category='Mexican', is_available=1),
            Meal(meal_name="McDonald's Burgers",            description="Classic McDonald's burgers",               ingredients='Beef Patty, Sesame Bun, Lettuce, Tomato, Pickles, Ketchup',  price=100.00, image_path='/images/r3.png',    category='Burgers', is_available=1),
            Meal(meal_name='The Baked Bear San Francisco',  description='Specialty baked goods',                    ingredients='Flour, Sugar, Butter, Eggs, Vanilla Extract, Chocolate',      price=150.00, image_path='/images/r4.png',    category='Bakery',  is_available=1),
            Meal(meal_name='Shake Shack',                   description='Premium burgers and shakes',               ingredients='Beef Patty, Potato Bun, Cheddar Cheese, Shack Sauce, Lettuce',price=180.00, image_path='/images/r5.png',    category='Burgers', is_available=1),
            Meal(meal_name='Chubby Noodle Chinese Takeout', description='Chinese noodle takeout',                   ingredients='Wheat Noodles, Pork Broth, Scallions, Soy Sauce, Sesame Oil', price=135.00, image_path='/images/r6.png',    category='Chinese', is_available=1),
            Meal(meal_name='Turkish Pilav With Chickpea',   description='Traditional Turkish rice with chickpea',   ingredients='Rice, Chickpeas, Onion, Butter, Cumin, Black Pepper',         price=110.00, image_path='/images/pilav.png', category='Turkish', is_available=1),
            Meal(meal_name='Lentil Soup',                   description='Warm homemade lentil soup',                ingredients='Red Lentils, Onion, Carrot, Cumin, Olive Oil, Lemon',         price=75.00,  image_path='/images/soup.png',  category='Soup',    is_available=1),
            Meal(meal_name='Grilled Salmon',                description='Fresh grilled salmon',                     ingredients='Salmon Fillet, Lemon, Garlic, Olive Oil, Dill, Capers',       price=200.00, image_path='/images/salmon.png',category='Seafood', is_available=1),
        ]

        session.add_all(meals)
        session.commit()
        print(f"Inserted {len(meals)} meals successfully")

CORRECT_INGREDIENTS = {
    'Pizza Hut Delicious Pizza':    'Dough, Tomato Sauce, Mozzarella, Pepperoni, Bell Peppers',
    'Chipotle Mexican Grill':       'Rice, Black Beans, Salsa, Guacamole, Sour Cream, Tortilla',
    "McDonald's Burgers":           'Beef Patty, Sesame Bun, Lettuce, Tomato, Pickles, Ketchup',
    'The Baked Bear San Francisco': 'Flour, Sugar, Butter, Eggs, Vanilla Extract, Chocolate',
    'Shake Shack':                  'Beef Patty, Potato Bun, Cheddar Cheese, Shack Sauce, Lettuce',
    'Chubby Noodle Chinese Takeout':'Wheat Noodles, Pork Broth, Scallions, Soy Sauce, Sesame Oil',
    'Turkish Pilav With Chickpea':  'Rice, Chickpeas, Onion, Butter, Cumin, Black Pepper',
    'Lentil Soup':                  'Red Lentils, Onion, Carrot, Cumin, Olive Oil, Lemon',
    'Grilled Salmon':               'Salmon Fillet, Lemon, Garlic, Olive Oil, Dill, Capers',
}

def update_meal_ingredients():
    """Correct wrong ingredients on already-seeded meals."""
    with SessionLocal() as session:
        for name, ingredients in CORRECT_INGREDIENTS.items():
            meal = session.query(Meal).filter(Meal.meal_name == name).first()
            if meal and meal.ingredients != ingredients:
                meal.ingredients = ingredients
        session.commit()