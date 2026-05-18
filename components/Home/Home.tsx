'use client'
import React, { useEffect, useState } from 'react'
import Hero from './Hero/Hero'
import Restaurants from './Restaurants/Restaurants'
import Category from './Category/Category'
import About from './About/About'
import Feature from './Feature/Feature'
import CartBar from './Cart/CartBar'
import CartModal from './Cart/CartModal'
import ResponsiveNav from '@/app/Navbar/ResponsiveNav'
import AOS from 'aos';
import 'aos/dist/aos.css';
import { getMeals, Meal } from '@/constant/api'

type CartItem = {
  meal_id: number; 
  title: string;
  price: number;
  quantity: number;
  image: string;
};

const Home = () => {
  const [cart, setCart] = useState<CartItem[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [meals, setMeals] = useState<Meal[]>([]);
  const [loading, setLoading] = useState(true);
  const [mealsError, setMealsError] = useState("");

  // ── Fetch meals from FastAPI on mount ──
  useEffect(() => {
    getMeals()
      .then(setMeals)
      .catch(() => setMealsError("Could not load meals. Make sure the server is running."))
      .finally(() => setLoading(false));
  }, []);

  // ── AOS animation init ──
  useEffect(() => {
    AOS.init({
      easing: 'ease',
      duration: 1000,
      once: true,
    });
  }, []);

  const clearCart = () => {
    setCart([]);
  };

  const updateCart = (
    meal_id: number,
    title: string,
    price: number,
    quantity: number,
    image: string
  ) => {
    setCart((prev) => {
    const existing = prev.find((item) => item.meal_id === meal_id);  // 👈 by id

    if (quantity === 0) {
      return prev.filter(item => item.meal_id !== meal_id);
    }

    if (existing) {
      return prev.map((item) =>
        item.meal_id === meal_id ? { ...item, quantity } : item
      );
    }

    return [...prev, { meal_id, title, price, quantity, image }];
  });
};

  const total = parseFloat(
    cart.reduce((sum, item) => sum + item.price * item.quantity, 0).toFixed(2)
  );

  return (
    <div className='overflow-hidden'>

      <ResponsiveNav openCart={() => setShowModal(true)} />
      <Hero />

      {/* ── Meals section: show loader, error, or grid ── */}
      {loading ? (
        <div className='flex justify-center items-center py-24'>
          <p className='text-xl font-semibold text-gray-500 animate-pulse'>
            Loading meals...
          </p>
        </div>
      ) : mealsError ? (
        <div className='flex justify-center items-center py-24'>
          <p className='text-lg font-semibold text-red-500'>{mealsError}</p>
        </div>
      ) : (
        <Restaurants
          id="restaurants"
          updateCart={updateCart}
          cart={cart}
          meals={meals}
        />
      )}

      <Category />
      <About />
      <Feature />

      {/* ── Cart Bar ── */}
      <CartBar total={total} onConfirm={() => setShowModal(true)} />

      {/* ── Cart Modal ── */}
      {showModal && (
        <CartModal
          cart={cart}
          total={total}
          onClose={() => setShowModal(false)}
          clearCart={clearCart}
          updateCart={updateCart}
        />
      )}

    </div>
  )
}

export default Home