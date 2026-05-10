'use client'
import React, { useState } from "react";
import SignInForm from "./SignInForm";
import SignUpForm from "./SignUpForm";

const LoginPage = () => {
  const [isLogin, setIsLogin] = useState(true);

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
            onClick={() => setIsLogin(!isLogin)}
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