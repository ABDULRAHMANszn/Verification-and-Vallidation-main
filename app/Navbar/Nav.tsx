'use client';

import { NavLinks } from '@/constant/constant'
import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
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
  const [scrolled, setScrolled] = useState(false);
  const [username, setUsername] = useState<string | null>(null);
  const pathname = usePathname();
  const router = useRouter();

  useEffect(() => {
    const sync = () => {
      const user = getUser();
      setUsername(user ? user.username : null);
    };
    sync();
    window.addEventListener('userChanged', sync);
    return () => window.removeEventListener('userChanged', sync);
  }, []);

  useEffect(() => {
    const handler = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handler);
    return () => window.removeEventListener('scroll', handler);
  }, []);

  const handleLogout = () => {
    logoutUser();
    setUsername(null);
    router.push('/login');
  };

  return (
    <header className={`fixed top-0 left-0 right-0 z-[100] h-[72px] transition-all duration-300
      bg-white/80 dark:bg-gray-900/85 backdrop-blur-md border-b border-gray-100/80 dark:border-gray-800/80
      ${scrolled ? 'shadow-md shadow-gray-200/60 dark:shadow-gray-900/60' : 'shadow-sm'}`}>

      <div className='flex items-center h-full justify-between w-[90%] xl:w-[82%] mx-auto'>

        {/* ── Left: Logo / Cart ── */}
        <div className='flex items-center gap-3'>
          <button
            id="nav-cart-btn"
            onClick={openCart}
            aria-label='Open cart'
            className='w-10 h-10 bg-[#0d1b4b] dark:bg-white hover:bg-[#e6007a] dark:hover:bg-[#e6007a] transition-colors duration-200 rounded-full flex items-center justify-center flex-shrink-0'
          >
            <FaBagShopping className='w-5 h-5 text-white dark:text-[#0d1b4b]' />
          </button>
          <span className='hidden sm:block text-[#0d1b4b] dark:text-white font-bold text-lg tracking-tight'>
            My Cart
          </span>
        </div>

        {/* ── Center: Nav Links ── */}
        <nav className='hidden lg:flex items-center gap-8'>
          {NavLinks.map((link) => {
            const isActive =
              link.url === '/'
                ? pathname === '/'
                : !link.url.startsWith('/#') && pathname.startsWith(link.url);
            return (
              <Link
                key={link.id}
                href={link.url}
                id={link.url === '/MyOrders' ? 'my-orders-link' : undefined}
                className={`relative text-sm font-semibold pb-1 transition-colors duration-200
                  ${isActive
                    ? 'text-[#e6007a]'
                    : 'text-gray-700 dark:text-gray-200 hover:text-[#e6007a] dark:hover:text-[#e6007a]'
                  }`}
              >
                {link.label}
                {isActive && (
                  <span className='absolute bottom-0 left-0 right-0 h-[2px] rounded-full bg-[#e6007a]' />
                )}
              </Link>
            );
          })}
        </nav>

        {/* ── Right: Actions ── */}
        <div className='flex items-center gap-3'>

          <ThemeToggler />

          {username ? (
            <div className='hidden lg:flex items-center gap-3'>
              <span className='text-gray-700 dark:text-gray-200 font-semibold text-sm'>
                👤 {username}
              </span>
              <button
                id="logout-btn"
                onClick={handleLogout}
                className='bg-red-500 hover:bg-red-600 text-white text-sm font-semibold px-5 py-2 rounded-xl transition-all duration-200 hover:scale-[1.03]'
              >
                Logout
              </button>
            </div>
          ) : (
            <Link
              id="login-btn"
              href='/login'
              className='hidden lg:inline-flex items-center bg-[#0d1b4b] hover:bg-blue-900 text-white text-sm font-semibold px-6 py-2.5 rounded-xl transition-all duration-200 hover:scale-[1.03] shadow-md shadow-blue-950/20'
            >
              Sign In
            </Link>
          )}

          <button
            id="open-menu-btn"
            onClick={openNav}
            aria-label='Open menu'
            className='lg:hidden p-1'
          >
            <HiBars3BottomRight className='w-7 h-7 text-[#0d1b4b] dark:text-white' />
          </button>

        </div>

      </div>
    </header>
  );
};

export default Nav;
