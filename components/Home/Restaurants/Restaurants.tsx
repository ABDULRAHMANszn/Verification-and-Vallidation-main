import React from "react";
import RestaurantCard from "./RestaurantCard";
import { Meal } from "@/constant/api";

type CartItem = {
  meal_id: number;          // 👈 add
  title: string;
  price: number;
  quantity: number;
  image: string;
};

type Props = {
  id?: string;
  updateCart: (
    meal_id: number,        // 👈 add
    title: string,
    price: number,
    quantity: number,
    image: string,
  ) => void;
  cart: CartItem[];
  meals: Meal[];
};

const Restaurants = ({ id, updateCart, cart, meals }: Props) => {
  return (
    <div className="pt-2 pb-16" id={id}>
      <div className="text-xl sm:text-2xl text-center font-extrabold">
        Available Meals Nearby Area
      </div>

      <div className="w-[80%] mx-auto grid md:grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-10 mt-14">
        {meals.map((meal) => (
          <RestaurantCard
            key={meal.meal_id}
            meal_id={meal.meal_id}
            image={meal.image_path}
            title={meal.meal_name}
            price={Number(meal.price)}
            category={meal.category}
            updateCart={updateCart}
            cart={cart}
          />
        ))}
      </div>
    </div>
  );
};

export default Restaurants;