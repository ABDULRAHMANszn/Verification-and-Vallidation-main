import React from 'react'
import FeatureCard from './FeatureCard'

const Feature = () => {
  return (
    <div className='pb-32'>
      <h1 className='text-xl sm:text-2xl text-center font-extrabold'>Meet our Quality Features</h1>
      <div className='w-[80%] mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10'>
        <div data-aos="fade-up" data-aos-anchor-placement="top-center" data-aos-delay="0">
            <FeatureCard icon='/images/9.png' title='Analytics Business' />
        </div>
        <div data-aos="fade-up" data-aos-anchor-placement="top-center" data-aos-delay="100">
            <FeatureCard icon='/images/10.png' title='Wide Coverage Map' />
        </div>
        <div data-aos="fade-up" data-aos-anchor-placement="top-center" data-aos-delay="200">
            <FeatureCard icon='/images/11.png' title='Artificial Intellignece' />
        </div>
        <div data-aos="fade-up" data-aos-anchor-placement="top-center" data-aos-delay="300">
            <FeatureCard icon='/images/12.png' title='Trusted & Secure' />
        </div>
        <div data-aos="fade-up" data-aos-anchor-placement="top-center" data-aos-delay="400">
            <FeatureCard icon='/images/13.png' title='Mobile Apps' />
        </div>
        <div data-aos="fade-up" data-aos-anchor-placement="top-center" data-aos-delay="500">
            <FeatureCard icon='/images/14.png' title='Largest People' />
        </div>
      </div>
    </div>
  )
}

export default Feature
