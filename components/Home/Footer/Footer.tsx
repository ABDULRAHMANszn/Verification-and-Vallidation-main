import React from 'react'
import { FaDribbble, FaFacebookF, FaInstagram, FaTwitter, FaYoutube } from 'react-icons/fa'
import { MdDeliveryDining } from 'react-icons/md'


const Footer = () => {
  return (
    <div className='pb-16 pt-16 bg-gray-800'>
        {/* top part */}
      <div className='w-[80%] mx-auto items-start grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-10'>
        {/* 1st part */}
        <div>
            <div className='flex items-center space-x-2'>
                <div className='w-10 h-10 bg-white rounded-full items-center flex justify-center flex-col'>
                    <MdDeliveryDining className='w-6 h-6 text-black'/>
                </div>
                <h1 className='text-xl hidden sm:block text-white font-bold md:text-2xl'>Foodie</h1>
            </div>
            <p className='text-gray-200 font-medium mt-4'>
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo aut fuga debitis id fugit facere nam aspernatur optio. Totam, quas! Porro ut ipsum vero aliquam nisi provident nesciunt debitis adipisci?
            </p>
            <div className='mt-6 flex items-center space-x-2'>
                <div className='flex items-center justify-center flex-col w-8 h-8 rounded-full bg-blue-600 text-white'>
                    <FaFacebookF />
                </div>
                <div className='flex items-center justify-center flex-col w-8 h-8 rounded-full bg-pink-500 text-white'>
                    <FaInstagram />
                </div>
                <div className='flex items-center justify-center flex-col w-8 h-8 rounded-full bg-sky-400 text-white'>
                    <FaTwitter />
                </div>
                <div className='flex items-center justify-center flex-col w-8 h-8 rounded-full bg-red-600 text-white'>
                    <FaYoutube />
                </div>
            </div> 
        </div>
        {/* 2nd part */}
        <div className='space-y-5'>
            <h1 className='text-lg font-bold text-white'>Company</h1>
            <p className='footer__link'>About Us</p>
            <p className='footer__link'>News & Press</p>
            <p className='footer__link'>Our Customers</p>
            <p className='footer__link'>Leadership</p>
            <p className='footer__link'>Careers</p>
        </div>
        {/* 3rd part */}
        <div className='space-y-5'>
            <h1 className='text-lg font-bold text-white'>Resources</h1>
            <p className='footer__link'>Blog</p>
            <p className='footer__link'>Webinat & Events</p>
            <p className='footer__link'>Podcast</p>
            <p className='footer__link'>E-book & Guides</p>
        </div>
        {/* 4th part */}
        <div>
            <h1 className='text-lg font-bold text-white'>Contact Us</h1>
            <div className='mt-6'>
                <h1 className='text-sm text-white'>Our Mobile Number</h1>
                <h1 className='text-base font-bold text-yellow-300 mt-1'>+1321879845</h1>
            </div>
            <div className='mt-6'>
                <h1 className='text-sm text-white'>Our Email Address</h1>
                <h1 className='text-base font-bold text-yellow-300 mt-1'>example@gmail.com</h1>
            </div>
        </div>
      </div>
      {/* bottom part */}
      <div className='mt-8 pt-8 mx-auto w-[80%] border-t flex flex-col md:flex-row justify-between items-center text-gray-600 text-sm'>
        <p className='text-center text-white md:text-left'>Copyright 2025 ------ .All rights reserved</p>
        <div className='flex items-center text-white space-x-4 mt-4 md:mt-8'>
            <span>Social : </span>
            <span className='text-white hover:text-gray-500'><FaFacebookF/></span>
            <span className='text-white hover:text-gray-500'><FaTwitter/></span>
            <span className='text-white hover:text-gray-500'><FaDribbble/></span>
        </div>
      </div>
    </div>
  )
}

export default Footer
