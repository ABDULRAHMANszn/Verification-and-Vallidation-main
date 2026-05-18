'use client'
import React, { useEffect, useState } from 'react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { NavLinks } from '@/constant/constant'
import { CgClose } from 'react-icons/cg'
import { getUser, logoutUser } from '@/constant/api'
import { useRouter } from 'next/navigation'

type Props = {
  showNav: boolean;
  closeNav: () => void;
}

const MobileNav = ({ closeNav, showNav }: Props) => {
  const navOpen = showNav ? 'translate-x-0' : 'translate-x-[-100%]'
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

  const handleLogout = () => {
    logoutUser();
    setUsername(null);
    closeNav();
    router.push('/login');
  };

  return (
    <div>
      {/* Backdrop */}
      <div
        onClick={closeNav}
        className={`fixed inset-0 bg-black/60 backdrop-blur-sm z-[1002] transition-opacity duration-300
          ${showNav ? 'opacity-100 pointer-events-auto' : 'opacity-0 pointer-events-none'}`}
      />

      {/* Drawer */}
      <div className={`fixed top-0 left-0 h-full w-[75%] sm:w-[60%] max-w-[320px] z-[1050]
        bg-[#0d1b4b] transform transition-transform duration-300 ${navOpen}
        flex flex-col pt-16 pb-10 px-8 gap-2`}>

        {NavLinks.map((link) => {
          const isActive =
            link.url === '/'
              ? pathname === '/'
              : !link.url.startsWith('/#') && pathname.startsWith(link.url);
          return (
            <Link
              key={link.id}
              href={link.url}
              onClick={closeNav}
              className={`text-lg font-semibold py-3 border-b border-white/10 transition-colors duration-150
                ${isActive ? 'text-[#e6007a]' : 'text-white hover:text-[#e6007a]'}`}
            >
              {link.label}
            </Link>
          );
        })}

        <div className='mt-6'>
          {username ? (
            <div className='flex flex-col gap-3'>
              <span className='text-white/80 font-medium text-sm'>
                👤 {username}
              </span>
              <button
                onClick={handleLogout}
                className='bg-red-500 hover:bg-red-600 text-white text-sm font-semibold px-5 py-2.5 rounded-xl w-fit transition-all'
              >
                Logout
              </button>
            </div>
          ) : (
            <Link
              href='/login'
              onClick={closeNav}
              className='inline-flex items-center bg-white text-[#0d1b4b] font-semibold text-sm px-6 py-2.5 rounded-xl transition-all hover:bg-gray-100'
            >
              Sign In
            </Link>
          )}
        </div>

        <button
          onClick={closeNav}
          aria-label='Close menu'
          className='absolute top-4 right-4 text-white/70 hover:text-white transition-colors'
        >
          <CgClose className='w-6 h-6' />
        </button>
      </div>
    </div>
  )
}

export default MobileNav
