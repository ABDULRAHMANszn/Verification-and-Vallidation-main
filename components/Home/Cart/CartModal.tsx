'use client'
import React, { useState } from "react";
import { FaCheckCircle, FaPlus, FaMinus } from "react-icons/fa";
import { CgClose } from "react-icons/cg";
import { createOrder, getUser } from "@/constant/api";
import { useRouter } from "next/navigation";

type CartItem = {
  meal_id: number;
  title: string;
  price: number;
  quantity: number;
  image: string;
};

type Props = {
  cart: CartItem[];
  total: number;
  onClose: () => void;
  clearCart: () => void;
  updateCart: (
    meal_id: number,
    title: string,
    price: number,
    quantity: number,
    image: string
  ) => void;
};

const CartModal = ({ cart, total, onClose, clearCart, updateCart }: Props) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const router = useRouter();

  const handleConfirm = async () => {
    const user = getUser();

    if (!user) {
      setError("Please sign in to place an order");
      setTimeout(() => router.push("/login"), 1500);
      return;
    }

    if (cart.length === 0) {
      setError("Your cart is empty");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const items = cart.map(item => ({
        meal_id: item.meal_id,
        quantity: item.quantity,
      }));

      const result = await createOrder(user.user_id, items);
      console.log("Order created:", result);

      alert(`✅ Order #${result.order_id} placed successfully!`);
      clearCart();
      onClose();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Failed to place order");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div id="cart-modal" className="fixed inset-0 bg-black/40 flex justify-center items-center z-50">
      <div className="bg-white dark:bg-gray-900 rounded-xl p-6 w-[90%] max-w-md relative">

        <CgClose
          id="close-cart-btn"
          onClick={onClose}
          className="absolute top-4 right-4 w-6 h-6 cursor-pointer text-black dark:text-white"
        />

        <h2 className="text-xl font-bold mb-4 text-black dark:text-white">
          Your Order
        </h2>

        {error && (
          <p id="cart-error" className="text-red-500 text-sm bg-red-50 p-2 rounded-lg mb-3">
            {error}
          </p>
        )}

        <div className="space-y-4 max-h-[300px] overflow-y-auto">
          {cart.length === 0 && (
            <p className="text-center text-gray-500">Your cart is empty</p>
          )}

          {cart.map((item) => (
            <div key={item.meal_id} id={`cart-item-${item.meal_id}`} className="flex items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <img src={item.image} alt={item.title} className="w-12 h-12 rounded-lg object-cover" />
                <div>
                  <p className="text-black dark:text-white font-medium">{item.title}</p>
                  <div className="flex items-center gap-2 mt-1">
                    <button
                      id={`decrease-${item.meal_id}`}
                      onClick={() =>
                        updateCart(item.meal_id, item.title, item.price, item.quantity - 1, item.image)
                      }
                      className="bg-red-500 text-white p-1 rounded-full"
                    >
                      <FaMinus size={10} />
                    </button>
                    <span className="text-black dark:text-white font-bold">{item.quantity}</span>
                    <button
                      id={`increase-${item.meal_id}`}
                      onClick={() =>
                        updateCart(item.meal_id, item.title, item.price, item.quantity + 1, item.image)
                      }
                      className="bg-blue-950 text-white p-1 rounded-full"
                    >
                      <FaPlus size={10} />
                    </button>
                  </div>
                </div>
              </div>
              <p className="text-black dark:text-white font-medium">
                ₺{(item.price * item.quantity).toFixed(2)}
              </p>
            </div>
          ))}
        </div>

        <hr className="my-4" />

        <p className="font-bold text-lg text-black dark:text-white">
          Total: <span id="cart-total-price" className="text-green-600">₺{total}</span>
        </p>

        <div className="mt-4 flex items-center gap-2 text-green-600 font-medium">
          <FaCheckCircle />
          <span>Payment will be made at the door upon delivery</span>
        </div>

        <button
          id="place-order-btn"
          onClick={handleConfirm}
          disabled={loading || cart.length === 0}
          className="mt-5 w-full bg-blue-950 text-white py-2 rounded-lg hover:bg-black transition disabled:opacity-50"
        >
          {loading ? "Placing order..." : "Confirm"}
        </button>
      </div>
    </div>
  );
};

export default CartModal;