'use client'
import React, { useEffect, useState } from 'react'
import Link from 'next/link'
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
  const router = useRouter();

  useEffect(() => {
    const sync = () => {
      const user = getUser();
      setUsername(user ? user.username : null);
    };

    sync();
    window.addEventListener("userChanged", sync);
    return () => window.removeEventListener("userChanged", sync);
  }, []);

  const handleLogout = () => {
    logoutUser();
    setUsername(null);
    closeNav();
    router.push('/login');
  };

  return (
    <div>
      {/* Overlay */}
      <div className={`fixed bg-black z-[1002] ${navOpen} opacity-70 transition-all transform duration-500 inset-0 w-full h-screen`} />

      {/* Nav Links */}
      <div className={`fixed ${navOpen} text-white flex flex-col transform transition-all delay-300 h-full justify-center duration-500 sm:w-[60%] w-[80%] bg-blue-950 space-y-6 z-[1050]`}>

        {NavLinks.map((link) => (
          <Link key={link.id} href={link.url} onClick={closeNav}>
            <p className='text-white text-[20px] w-fit ml-12 border-b-[1.5px] pb-1 border-white sm:text-[30px]'>
              {link.label}
            </p>
          </Link>
        ))}

        {/* ── User section ── */}
        <div className='ml-12'>
          {username ? (
            // Logged in
            <div className='flex flex-col space-y-3'>
              <span className='text-white font-semibold text-[18px]'>
                👤 {username}
              </span>
              <button
                onClick={handleLogout}
                className='bg-red-500 hover:bg-red-600 text-white text-sm px-4 py-2 rounded-lg w-fit transition-all'
              >
                Logout
              </button>
            </div>
          ) : (
            // Not logged in
            <Link href='/login' onClick={closeNav}>
              <p className='text-white text-[20px] w-fit border-b-[1.5px] pb-1 border-white sm:text-[30px]'>
                Sign In
              </p>
            </Link>
          )}
        </div>

        {/* Close Icon */}
        <CgClose
          onClick={closeNav}
          className='absolute top-[0.7rem] right-[1.4rem] sm:w-8 sm:h-8 w-6 h-6'
        />
      </div>
    </div>
  )
}

export default MobileNav