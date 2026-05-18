import React from "react";

type Props = {
  total: number;
  onConfirm: () => void;
};

const CartBar = ({ total, onConfirm }: Props) => {

  const showButton = total>0;
  return (
    <div className="fixed bottom-0 left-0 w-full dark:bg-gray-900  bg-gray-200 shadow-lg border-t p-4 flex space-x-4 place-content-center items-center z-50">
      <p className="font-bold text-lg">Total: ₺{total}</p>

      <button
        id="cart-btn"
        onClick={onConfirm}
        className={`bg-green-600 text-white px-8 py-3 hover:bg-green-600/90  transition-all rounded-full font-semibold ${showButton ? 'inline-block': 'hidden'}`}
      >
        Confirm Cart
      </button>
    </div>
  );
};

export default CartBar;