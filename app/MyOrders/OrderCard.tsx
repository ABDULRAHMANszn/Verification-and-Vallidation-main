'use client';

import React from "react";
import Image from "next/image";
import { Order } from "./mockOrders";

type Props = {
  order: Order;
};

const OrderCard = ({ order }: Props) => {
  const orderTotal = order.items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-md border border-gray-200 dark:border-gray-800 p-5">
      <div className="flex items-center justify-between gap-4 mb-4">
        <div>
          <h2 className="text-lg sm:text-xl font-bold text-black dark:text-white">
            Order <span className="text-pink-600">{order.id}</span>
          </h2>
          <p className="text-sm text-green-600 font-semibold">
            Date: {order.date}
          </p>
        </div>

        <div className="text-right">
          <p className="text-sm text-gray-500 dark:text-gray-400">Total</p>
          <p className="text-lg font-bold text-green-600">${orderTotal}</p>
        </div>
      </div>

      <div className="space-y-4">
        {order.items.map((item, index) => (
          <div
            key={index}
            className="flex items-center justify-between gap-4 rounded-xl bg-gray-50 dark:bg-gray-800 p-3"
          >
            <div className="flex items-center gap-3 min-w-0">
              <Image
                src={item.image}
                alt={item.title}
                width={60}
                height={60}
                className="w-14 h-14 rounded-lg object-cover"
              />

              <div className="min-w-0">
                <h3 className="font-semibold text-black dark:text-white truncate">
                  {item.title}
                </h3>
                <p className="text-sm text-orange-500">
                  ${item.price} × {item.quantity}
                </p>
              </div>
            </div>

            <p className="font-bold text-black dark:text-white">
              ${item.price * item.quantity}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default OrderCard;