import React from 'react'
import Image from 'next/image'
import { FaApple, FaGooglePlay } from 'react-icons/fa'

const MobileApp = () => {
  return (
    <div className='pt-16 pb-16'>
      <div className='w-[80%] mx-auto grid grid-cols-1 gap-6 items-center lg:grid-cols-2 '>
        {/* Image */}
        <Image src='/images/1.png' width={800} height={800} alt='image' className='object-cover' data-aos="zoom-in" data-aos-anchor-placement="top-center" data-aos-delay="0"/>
        <div>
            {/* Heading */}
            <h1 className='text-2xl sm:text-4xl font-bold leading-8 sm:leading-12 '>
                Conneting our users with IOS & Android apps. Download from iTune & App store
            </h1>
            {/* description */}
            <p className='text-sm sm:text-base font-medium text-gray-800 dark:text-gray-400 mt-6 leading-6 sm:leading-8'>
                Pick one of our slack themes, or create your custom theme with the most advanced theme editor on any online survey building tool. We are driven beyond just finishing the project. We want to find solutions using our website & apps. 
            </p>
            {/* Download apps */}
            <div className='space-y-3 space-x-4 sm:flex sm:space-y-0 mt-6'>
                {/* apps store button */}
                <a href="#_" className='flex w-fit items-center group border border-gray-400 px-4 py-3 rounded-md bg-gray-950 transition-all duration-300'>

                    <FaApple className='text-2xl mr-2 transition-all duration-300 text-white'/>
                    <div>
                        <p className='text-xs text-white transition-all duration-300'>Download on the</p>
                        <p className='text-sm font-semibold text-white transition-all duration-300'>App Store</p>
                    </div>
                </a>
                <a href="#_" className='flex w-fit items-center group border border-gray-400 px-4 py-3 rounded-md bg-gray-950 transition-all duration-300'>

                    <FaGooglePlay className='text-2xl mr-2 transition-all duration-300 text-white'/>
                    <div>
                        <p className='text-xs text-white transition-all duration-300'>Download on the</p>
                        <p className='text-sm font-semibold text-white transition-all duration-300'>Google Play</p>
                    </div>
                </a>
            </div>
        </div>
      </div>
    </div>
  )
}

export default MobileApp
