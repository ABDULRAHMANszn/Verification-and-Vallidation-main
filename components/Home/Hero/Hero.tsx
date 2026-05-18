import React from 'react'
import Image from 'next/image'
import Link from 'next/link'

const stats = [
  { value: '500+', label: 'Restaurants' },
  { value: '20K+', label: 'Deliveries' },
  { value: '4.9★', label: 'Rating' },
]

const Hero = () => {
  return (
    <section className='relative w-full min-h-screen flex items-center overflow-hidden bg-gradient-to-br from-gray-50 via-white to-orange-50/40 dark:from-gray-950 dark:via-gray-900 dark:to-gray-950'>

      {/* Background blobs */}
      <div className='absolute top-[-8%] right-[-4%] w-[520px] h-[520px] rounded-full bg-pink-100/50 dark:bg-pink-900/10 blur-3xl pointer-events-none' />
      <div className='absolute bottom-[-10%] left-[-4%] w-[420px] h-[420px] rounded-full bg-blue-100/40 dark:bg-blue-900/10 blur-3xl pointer-events-none' />
      <div className='absolute top-[40%] left-[35%] w-[300px] h-[300px] rounded-full bg-orange-100/30 dark:bg-orange-900/5 blur-3xl pointer-events-none' />

      <div className='relative z-10 w-[90%] xl:w-[82%] mx-auto grid grid-cols-1 xl:grid-cols-2 items-center gap-14 py-36'>

        {/* ── Left: Text Content ── */}
        <div data-aos="fade-up" className='flex flex-col'>

          {/* Badge */}
          <div className='inline-flex items-center gap-2 bg-pink-50 dark:bg-pink-900/20 border border-pink-200 dark:border-pink-800 text-pink-600 dark:text-pink-400 text-sm font-semibold rounded-full px-4 py-1.5 w-fit mb-7'>
            <span className='w-2 h-2 rounded-full bg-pink-500 animate-pulse' />
            Fast Delivery · No Minimum Order
          </div>

          {/* Headline */}
          <h1 className='text-4xl md:text-5xl lg:text-[3.6rem] font-extrabold leading-[1.18] tracking-tight text-gray-900 dark:text-white mb-5'>
            Your favorite food,{' '}
            <span className='text-[#e6007a]'>delivered</span>{' '}
            to your door.
          </h1>

          {/* Description */}
          <p className='text-base md:text-lg text-gray-500 dark:text-gray-400 leading-relaxed max-w-[500px] mb-10'>
            Order meals, groceries, and drinks from the best restaurants near you.
          </p>

          {/* Buttons */}
          <div className='flex flex-wrap items-center gap-4 mb-12'>
            <Link
              href='/login'
              className='bg-[#0d1b4b] hover:bg-blue-900 text-white font-semibold px-9 py-3.5 rounded-xl transition-all duration-200 hover:scale-[1.04] shadow-lg shadow-blue-950/20'
            >
              Sign In
            </Link>
            <Link
              href='/login?mode=signup'
              className='border-2 border-[#0d1b4b] dark:border-white text-[#0d1b4b] dark:text-white font-semibold px-9 py-3.5 rounded-xl transition-all duration-200 hover:bg-[#0d1b4b] hover:text-white dark:hover:bg-white dark:hover:text-gray-900'
            >
              Sign Up
            </Link>
          </div>

          {/* Stats */}
          <div className='flex items-center gap-10'>
            {stats.map((stat, i) => (
              <div key={i} className='flex flex-col'>
                <span className='text-2xl font-extrabold text-gray-900 dark:text-white leading-tight'>
                  {stat.value}
                </span>
                <span className='text-sm text-gray-500 dark:text-gray-400 font-medium mt-0.5'>
                  {stat.label}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* ── Right: Food Image ── */}
        <div data-aos="fade-left" data-aos-delay="150" className='relative mx-auto hidden xl:flex items-center justify-center'>
          {/* Soft glow behind image */}
          <div className='absolute w-[440px] h-[440px] rounded-full bg-gradient-to-br from-orange-200/60 to-pink-200/60 dark:from-orange-900/20 dark:to-pink-900/20 blur-2xl' />
          <div className='relative animate-float drop-shadow-2xl'>
            <Image
              src='/images/heroD.png'
              alt='Delicious food'
              width={520}
              height={520}
              className='drop-shadow-2xl'
              priority
            />
          </div>
        </div>

      </div>
    </section>
  )
}

export default Hero
