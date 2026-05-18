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
  updateCart: (
    meal_id: number,
    title: string,
    price: number,
    quantity: number,
    image: string
  ) => void;
  cart: CartItem[];
};

const RestaurantCard = ({ meal_id, image, title, price, category, updateCart, cart }: Props) => {

  // ✅ Find this meal in the cart by meal_id
  const itemInCart = cart.find(item => item.meal_id === meal_id);
  const count = itemInCart ? itemInCart.quantity : 0;

  const handleAdd = () => {
    const newQuantity = count + 1;
    updateCart(meal_id, title, price, newQuantity, image);
  };

  const handleRemove = () => {
    if (count === 0) return;
    const newQuantity = count - 1;
    updateCart(meal_id, title, price, newQuantity, image);
  };

  const totalPrice = parseFloat((count * price).toFixed(2));

  return (
    <div>
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
        <p className="font-bold mt-4 text-orange-600 text-base sm:text-lg">
          ₺{price}
        </p>
      </div>

      <div className="flex items-center mt-3 justify-between">

        <div className="flex space-x-2">
          <p className="bg-blue-950 px-3 py-1.5 rounded-full text-white">{category}</p>
        </div>

        {/* CONTROLS */}
        <div className="flex items-center gap-2 mr-2">

          <button
            id={`remove-from-cart-${meal_id}`}
            onClick={handleRemove}
            className="bg-red-600 p-2 rounded-full text-white"
          >
            <FaMinus />
          </button>

          <span className="font-bold w-6 text-center" id="quantityOfMeal">{count}</span>

          <button
            id={`add-to-cart-${meal_id}`}
            onClick={handleAdd}
            className="bg-green-600 p-2 rounded-full text-white"
          >
            <FaPlus />
          </button>
        </div>
      </div>

      {count > 0 && (
        <p className="mt-2 font-semibold text-green-700">
          Subtotal: ₺{totalPrice}
        </p>
      )}
    </div>
  );
};

export default RestaurantCard;