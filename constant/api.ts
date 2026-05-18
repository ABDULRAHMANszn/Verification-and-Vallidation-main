const BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export type Meal = {
  meal_id: number;
  meal_name: string;
  price: number;
  image_path: string;
  description: string;
  category: string;
  is_available: number;
};

// Get all meals
export async function getMeals() {
  const res = await fetch(`${BASE_URL}/meals`);
  if (!res.ok) throw new Error("Failed to fetch meals");
  return res.json();
}

// Get single meal by ID
export async function getMeal(id: number) {
  const res = await fetch(`${BASE_URL}/meals/${id}`);
  if (!res.ok) throw new Error(`Meal ${id} not found`);
  return res.json();
}

export type UserSession = {
  user_id: number;
  username: string;
  role: string;
  token: string;
};

function parseDetail(detail: unknown, fallback: string): string {
  if (!detail) return fallback;
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail))
    return detail.map((d: { msg?: string }) => (d.msg ?? "").replace("Value error, ", "")).join("; ");
  return fallback;
}

export async function loginUser(username: string, password: string): Promise<UserSession> {
  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(parseDetail(err.detail, "Login failed"));
  }
  return res.json();
}

export async function registerUser(
  username: string, password: string,
  phone: string, address: string,
  email?: string,
): Promise<UserSession> {
  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password, phone, address, email }),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(parseDetail(err.detail, "Registration failed"));
  }
  return res.json();
}

// Helper functions for localStorage
export function saveUser(user: UserSession) {
  localStorage.setItem("user", JSON.stringify(user));
  window.dispatchEvent(new Event("userChanged"));
}

export function logoutUser() {
  localStorage.removeItem("user");
  window.dispatchEvent(new Event("userChanged"));
}

export function getUser(): UserSession | null {
  const data = localStorage.getItem("user");
  return data ? JSON.parse(data) : null;
}

function authHeaders(): HeadersInit {
  const user = getUser();
  const headers: Record<string, string> = { "Content-Type": "application/json" };
  if (user?.token) headers["Authorization"] = `Bearer ${user.token}`;
  return headers;
}

export type OrderItemPayload = {
  meal_id: number;
  quantity: number;
};

export async function createOrder(
  user_id: number,
  items: OrderItemPayload[]
) {
  const res = await fetch(`${BASE_URL}/orders`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ user_id, items }),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Failed to create order");
  }
  return res.json();
}

export type OrderItem = {
  title: string;
  price: number;
  quantity: number;
  image: string;
};

export type Order = {
  id: number;
  date: string;
  status: string;
  items: OrderItem[];
};

export async function getUserOrders(user_id: number): Promise<Order[]> {
  const res = await fetch(`${BASE_URL}/orders/user/${user_id}/full`, {
    headers: authHeaders(),
  });
  if (!res.ok) throw new Error("Failed to fetch orders");
  return res.json();
}
