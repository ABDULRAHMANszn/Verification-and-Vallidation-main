'use client';

import React, { useEffect, useState } from "react";
import OrderCard from "./OrderCard";
import { getUserOrders, getUser, Order } from "@/constant/api";
import { useRouter } from "next/navigation";

const OrdersPage = () => {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const router = useRouter();

  useEffect(() => {
    const user = getUser();

    // ── Redirect to login if not signed in ──
    if (!user) {
      router.push("/login");
      return;
    }

    // ── Fetch orders from FastAPI ──
    getUserOrders(user.user_id)
      .then(setOrders)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [router]);

  // ── Calculate grand total across all orders ──
  const allOrdersTotal = orders.reduce((sum, order) => {
    const orderTotal = order.items.reduce(
      (orderSum, item) => orderSum + item.price * item.quantity,
      0
    );
    return sum + orderTotal;
  }, 0);

  return (
    <div className="min-h-screen bg-gray-300 dark:bg-black pt-24 pb-16">
      <div className="w-[90%] xl:w-[80%] mx-auto">

        {/* ── Header ── */}
        <div className="mb-10">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-black dark:text-white">
            My Orders
          </h1>
          <p className="mt-2 text-blue-950 dark:text-gray-300 font-semibold">
            Here you can see your previous orders with the details.
          </p>
        </div>

        {/* ── Loading state ── */}
        {loading && (
          <p className="text-center text-xl font-semibold text-gray-700 dark:text-gray-300 animate-pulse py-12">
            Loading your orders...
          </p>
        )}

        {/* ── Error state ── */}
        {error && (
          <p className="text-center text-red-500 bg-red-50 p-4 rounded-lg">
            {error}
          </p>
        )}

        {/* ── No orders ── */}
        {!loading && !error && orders.length === 0 && (
          <div className="bg-white dark:bg-gray-900 rounded-2xl p-10 text-center">
            <p className="text-xl font-semibold text-gray-600 dark:text-gray-300">
              You haven&apos;t placed any orders yet.
            </p>
          </div>
        )}

        {/* ── Orders list ── */}
        {!loading && !error && orders.length > 0 && (
          <>
            <div className="grid gap-6">
              {orders.map((order) => (
                <OrderCard key={order.id} order={order} />
              ))}
            </div>

            {/* ── Grand total ── */}
            <div className="mt-8 bg-blue-950 text-white rounded-2xl p-5 flex items-center justify-between">
              <p className="text-base sm:text-lg font-medium">All Orders Total</p>
              <p className="text-xl sm:text-2xl font-bold">${allOrdersTotal}</p>
            </div>
          </>
        )}

      </div>
    </div>
  );
};

export default OrdersPage;