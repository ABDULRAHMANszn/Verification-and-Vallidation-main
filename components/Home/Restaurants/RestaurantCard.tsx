'use client'
import React from "react";
import Image from "next/image";
import { FaPlus, FaMinus } from "react-icons/fa6";

type CartItem = {
  meal_id: number;
  title: string;
  price: number;
  quantity: number;
  image: string;
};

type Props = {
  meal_id: number;
  image: string;
  title: string;
  price: number;
  category: string;
  is_available: number;
  updateCart: (
    meal_id: number,
    title: string,
    price: number,
    quantity: number,
    image: string
  ) => void;
  cart: CartItem[];
};

const RestaurantCard = ({ meal_id, image, title, price, category, is_available, updateCart, cart }: Props) => {

  const available = is_available === 1;

  // ✅ Find this meal in the cart by meal_id
  const itemInCart = cart.find(item => item.meal_id === meal_id);
  const count = itemInCart ? itemInCart.quantity : 0;

  const handleAdd = () => {
    if (count >= 10) return;
    updateCart(meal_id, title, price, count + 1, image);
  };

  const handleRemove = () => {
    if (count === 0) return;
    const newQuantity = count - 1;
    updateCart(meal_id, title, price, newQuantity, image);
  };

  const totalPrice = parseFloat((count * price).toFixed(2));

  return (
    <div id={`meal-card-${meal_id}`}>
      <Image
        src={image}
        width={400}
        height={400}
        alt={title}
        className="w-full h-[250px] object-cover"
      />

      <div className="flex justify-between">
        <h1 className="mt-4 font-bold text-base sm:text-lg">
          {title}
        </h1>
        <p id={`meal-price-${meal_id}`} className="font-bold mt-4 text-orange-600 text-base sm:text-lg">
          ₺{price}
        </p>
      </div>

      <div className="flex items-center mt-3 justify-between">

        <div className="flex space-x-2">
          <p className="bg-blue-950 px-3 py-1.5 rounded-full text-white">{category}</p>
          {!available && (
            <p className="bg-red-100 text-red-600 px-3 py-1.5 rounded-full text-sm font-semibold">
              Unavailable
            </p>
          )}
        </div>

        {/* CONTROLS */}
        <div className="flex items-center gap-2 mr-2">

          <button
            id={`remove-from-cart-${meal_id}`}
            onClick={handleRemove}
            disabled={!available}
            className="bg-red-600 p-2 rounded-full text-white disabled:opacity-40 disabled:cursor-not-allowed"
          >
            <FaMinus />
          </button>

          <span className="font-bold w-6 text-center" id="quantityOfMeal">{count}</span>

          <button
            id={`add-to-cart-${meal_id}`}
            onClick={handleAdd}
            disabled={!available}
            className="bg-green-600 p-2 rounded-full text-white disabled:opacity-40 disabled:cursor-not-allowed"
          >
            <FaPlus />
          </button>
        </div>
      </div>

      {count > 0 && (
        <p id={`meal-subtotal-${meal_id}`} className="mt-2 font-semibold text-green-700">
          Subtotal: ₺{totalPrice}
        </p>
      )}
    </div>
  );
};

export default RestaurantCard;