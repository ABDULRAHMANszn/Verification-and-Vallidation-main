
'use client';
console.log("APP/NAVBAR/NAV.TSX KULLANILIYOR");
import { NavLinks } from '@/constant/constant'
import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { HiBars3BottomRight } from 'react-icons/hi2'
import ThemeToggler from '@/components/Helper/ThemeToggler';
import { FaBagShopping } from 'react-icons/fa6';
import { getUser, logoutUser } from '@/constant/api';
import { useRouter } from 'next/navigation';

type Props = {
  openNav: () => void;
  openCart: () => void;
}

const Nav = ({ openNav, openCart }: Props) => {

  const [navBg, setNavBg] = useState(false);
  const [username, setUsername] = useState<string | null>(null);
  const router = useRouter();

  // ── Read user from localStorage + listen for changes ──
  useEffect(() => {
    console.log("Nav useEffect running ✅");

    const sync = () => {
      const raw = localStorage.getItem("user");
      console.log("raw from localStorage:", raw);
      const user = getUser();
      setUsername(user ? user.username : null);
    };

    sync(); // run immediately on mount
    window.addEventListener("userChanged", sync);
    return () => window.removeEventListener("userChanged", sync);
  }, []);

  // ── Scroll background handler ──
  useEffect(() => {
    const handler = () => {
      if (window.scrollY >= 90) setNavBg(true)
      else setNavBg(false)
    }
    window.addEventListener('scroll', handler)
    return () => window.removeEventListener('scroll', handler)
  }, [])

  const handleLogout = () => {
    logoutUser();
    setUsername(null);
    router.push('/login');
  };

  return (
    <div className={`transition-all ${navBg ? `bg-white dark:bg-gray-900 shadow-md` : `fixed`} duration-200 h-[12vh] z-[100] fixed w-full`}>
      <div className='flex items-center h-full justify-between w-[90%] xl:w-[80%] mx-auto'>

        {/* CART ICON */}
        <div className='flex items-center space-x-2'>
          <div
            onClick={openCart}
            className='w-10 h-10 bg-blue-950 dark:bg-white hover:bg-pink-600 transition-all rounded-full flex items-center justify-center cursor-pointer'
          >
            <FaBagShopping className='w-6 h-6 text-white dark:text-black' />
          </div>
          <h1 className='text-xl hidden sm:block md:text-2xl text-black dark:text-white font-bold'>
            My Cart
          </h1>
        </div>

        {/* NAV LINKS */}
        <div className='hidden lg:flex items-center space-x-10'>
          {NavLinks.map((link) => (
            <Link key={link.id} href={link.url}
              className='text-black dark:text-white hover:text-green-700 dark:hover:text-green-400 font-bold transition-all duration-200'>
              {link.label}
            </Link>
          ))}
        </div>

        {/* BUTTONS */}
        <div className='flex items-center space-x-4'>

          <ThemeToggler />

          {username ? (
            // ── Logged in: show username + logout ──
            <div className='hidden lg:flex items-center space-x-3'>
              <span className='text-black dark:text-white font-semibold'>
                👤 {username}
              </span>
              <button
                onClick={handleLogout}
                className='bg-red-500 hover:bg-red-600 text-white text-sm px-4 py-2 rounded-lg transition-all'
              >
                Logout
              </button>
            </div>
          ) : (
            // ── Not logged in: show Sign In button ──
            <Link
              href='/login'
              className='hidden lg:block bg-blue-950 hover:bg-blue-800 text-white text-sm px-6 py-2 rounded-lg font-semibold transition-all'
            >
              Sign In
            </Link>
          )}

          <HiBars3BottomRight
            onClick={openNav}
            className='w-8 h-8 text-blue-950 cursor-pointer lg:hidden dark:text-white'
          />

        </div>

      </div>
    </div>
  )
}

export default Nav