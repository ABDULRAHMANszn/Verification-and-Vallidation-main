'use client'
import React from "react";
import { useSearchParams, useRouter } from "next/navigation";
import SignInForm from "./SignInForm";
import SignUpForm from "./SignUpForm";

const LoginPage = () => {
  const searchParams = useSearchParams();
  const router = useRouter();
  const isLogin = searchParams.get("mode") !== "signup";

  const toggle = () => {
    router.push(isLogin ? "/login?mode=signup" : "/login");
  };

  return (
    <div className="min-h-screen flex items-center justify-center dark:bg-gray-900  dark:text-gray-300 bg-gray-100">
      <div className="bg-white shadow-xl rounded-2xl w-[90%] max-w-md p-6  dark:text-gray-300 dark:bg-gray-900 dark:border-2">

        {/* HEADER */}
        <h1 className="text-2xl font-bold text-center text-blue-950 dark:text-gray-300 mb-6">
          {isLogin ? "Welcome Back" : "Create Account"}
        </h1>

        {/* FORM */}
        {isLogin ? <SignInForm /> : <SignUpForm />}

        {/* SWITCH */}
        <p className="text-center mt-5 text-sm">
          {isLogin ? "Don't have an account?" : "Already have an account?"}
          <button
            id="toggle-login-btn"
            onClick={toggle}
            className="ml-2 text-blue-950 font-semibold hover:underline dark:text-gray-300"
          >
            {isLogin ? "Sign Up" : "Sign In"}
          </button>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;