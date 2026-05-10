import React from 'react'
import HowItWorkCard from './HowItWorkCard'

const HowItWork = () => {
  return (
    <div className='pt-16 pb-16'>
      <h1 className='text-xl sm:text-2xl text-center font-extrabold'>Let&apos;s How it Works</h1>
        <div className='w-[80%] mx-auto grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-10'>
            <div data-aos="fade-right" data-aos-anchor-placement="top-center" data-aos-delay="0">
                <HowItWorkCard num='01' image='/images/w1.png' title="Become a Delivery Man" description="As a delivery driver, you'll make a reliable money-working anytime, anywhere." />
            </div>
            <div data-aos="fade-right" data-aos-anchor-placement="top-center" data-aos-delay="100">
                <HowItWorkCard num='02' image='/images/w2.png' title='Become a Partner' description="Grow your business and reach new customrer by partenring with us." />
            </div>
            <div data-aos="fade-right" data-aos-anchor-placement="top-center" data-aos-delay="200">
                <HowItWorkCard num='03' image='/images/w3.png' title='Try Android/IOS App' description="Get the best DoorDash with live order tracking" />
            </div>
        </div>
    </div>
  )
}

export default HowItWork
