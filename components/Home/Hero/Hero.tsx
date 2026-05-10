import React from 'react'
import { FaApple, FaGooglePlay, FaLocationArrow } from 'react-icons/fa'
import { GrMapLocation } from 'react-icons/gr'
import Image from 'next/image'

const Hero = () => {
  return (
    <div className='relative w-full h-screen sm:h-screen flex flex-col justify-center '>
      
      <div className='w-[90%] md:w-[80%] mx-auto grid items-center grid-cols-1 xl:grid-cols-2 gap-10'>
        {/* Text Content */}
        <div data-aos="fade-up">
            {/* Heading */}
            <h1 className='text-3xl md:text-4xl lg:text-6xl mb-6 mt-6 font-extrabold leading-[2.5rem] md:leading-[4rem]'>
                Your favorite food, <span className='text-pink-600'>delivered</span> your home</h1>
            {/* Sub-heading */}
            <p className='text-sm text-gray-800 dark:text-gray-400 font-medium md:text-xl'>
                Food, drinks, groceries, and more available for delivery and pickup.</p>
            {/*  */}
           
        </div>
        {/* Image Content */}
        <div data-aos="fade-left" data-aos-delay="150" className='mx-auto hidden xl:block'>
            <Image src="/images/heroD.png" alt='Hero Image' width={500} height={500}/>
        </div>
      </div>
    </div>
  )
}

export default Hero
