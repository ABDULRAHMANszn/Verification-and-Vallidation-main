'use client'
import React, { useState } from "react";
import { loginUser, saveUser } from "@/constant/api";
import { useRouter } from "next/navigation";

const SignInForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

const handleLogin = async (e: React.FormEvent) => {
  e.preventDefault();
  setError("");
  setLoading(true);
  try {
    const user = await loginUser(username, password);
    saveUser(user);                    // ✅ save first
    window.location.href = '/';        // 👈 change this from router.push('/')
  } catch (err: unknown) {
    setError(err instanceof Error ? err.message : "Something went wrong");
  } finally {
    setLoading(false);
  }
};

  return (
    <form id="login-form" onSubmit={handleLogin} className="space-y-4 dark:bg-gray-900">
      {error && (
        <p id="login-error" className="text-red-500 text-sm text-center bg-red-50 p-2 rounded-lg">
          {error}
        </p>
      )}
      <input
        id="username"
        type="text" placeholder="Username"
        className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-950 dark:bg-gray-900"
        value={username} onChange={(e) => setUsername(e.target.value)} required
      />
      <input
        id="password"
        type="password" placeholder="Password"
        className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-950"
        value={password} onChange={(e) => setPassword(e.target.value)} required
      />
      <button id="login-btn" type="submit" disabled={loading}
        className="w-full bg-blue-950 text-white py-3 rounded-lg font-semibold hover:bg-blue-800 transition disabled:opacity-50">
        {loading ? "Signing in..." : "Sign In"}
      </button>
    </form>
  );
};

export default SignInForm;