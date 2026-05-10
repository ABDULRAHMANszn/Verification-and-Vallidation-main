import React from 'react'
import Image from 'next/image'

const About = () => {
  return (
    <div className='pt-16 pb-16'>
      <div className='w-[80%] mx-auto grid grid-cols-1 lg:grid-cols-2 gap-10 items-center'>
        {/* Image content */}
        <div data-aos="fade-right" data-aos-anchor-placement="top-center">
            <Image src='/images/a.png' width={800} height={800} alt="image" />
        </div>
        {/* Text content */}
        <div>
            <h1 className='text-xl sm:text-2xl md:text-3xl lg:text-4xl leading-8 md:leading-12 font-extrabold '>
                We deliver our products as fast as superman can do.
            </h1>
            <p className='mt-4 leading-6 md:leading-8 text-gray-800 dark:text-gray-300 font-medium text-sm sm:text-base'>
                Wherever you are in, the delivery finds you well.
            </p>
            <div className='mt-8'>
              <div className='mt-8 flex items-center space-x-6'>
                <p className='text-3xl md:text-5xl opacity-60 font-bold'>01</p>
                  <div>
                    <h1 className='text-base sm:text-lg font-extrabold'>Easy to use application</h1>
                    <p className='mt-2 text-gray-800 dark:text-gray-300 font-medium text-sm sm:text-base'>
                        we&apos;re driven beyond just finishing the project. We want to find solutions using our website & apps
                    </p>
                  </div>
              </div>
              <div className='mt-8 flex items-center space-x-6'>
                <p className='text-3xl md:text-5xl opacity-60 font-bold'>02</p>
                  <div>
                    <h1 className='text-base sm:text-lg font-extrabold'>Deliver food within 30 min.</h1>
                    <p className='mt-2 text-gray-800 dark:text-gray-300 font-medium text-sm sm:text-base'>
                        we&apos;re driven beyond just finishing the project. We want to find solutions using our website & apps
                    </p>
                  </div>
              </div>
              <div className='mt-8 flex items-center space-x-6'>
                <p className='text-3xl md:text-5xl opacity-60 font-bold'>03</p>
                  <div>
                    <h1 className='text-base sm:text-lg font-extrabold'>100% Reliable with privacy</h1>
                    <p className='mt-2 text-gray-800 dark:text-gray-300 font-medium text-sm sm:text-base'>
                        we&apos;re driven beyond just finishing the project. We want to find solutions using our website & apps
                    </p>
                  </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  )
}

export default About
