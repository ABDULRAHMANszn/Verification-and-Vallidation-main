'use client'
import React, { useState } from "react";
import { registerUser, saveUser } from "@/constant/api";
import { useRouter } from "next/navigation";

const SignUpForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [phone, setPhone]       = useState("");
  const [address, setAddress]   = useState("");
  const [error, setError]       = useState("");
  const [loading, setLoading]   = useState(false);
  const router = useRouter();

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const user = await registerUser(username, password, phone, address);
      saveUser(user);       // → saves to localStorage
      router.push("/");     // → back to login
    } catch (err: unknown) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleRegister} className="space-y-4">
      {error && (
        <p className="text-red-500 text-sm text-center bg-red-50 p-2 rounded-lg">
          {error}
        </p>
      )}
      <input type="text" placeholder="Username"
        className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-950"
        value={username} onChange={(e) => setUsername(e.target.value)} required />
      <input type="password" placeholder="Password"
        className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-950"
        value={password} onChange={(e) => setPassword(e.target.value)} required />
      <input type="tel" placeholder="Phone Number"
        className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-950"
        value={phone} onChange={(e) => setPhone(e.target.value)} required />
      <textarea placeholder="Address"
        className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-950 resize-none"
        value={address} onChange={(e) => setAddress(e.target.value)} rows={3} required />
      <button type="submit" disabled={loading}
        className="w-full bg-blue-950 text-white py-3 rounded-lg font-semibold hover:bg-blue-800 transition disabled:opacity-50">
        {loading ? "Creating account..." : "Sign Up"}
      </button>
    </form>
  );
};

export default SignUpForm;