'use client'
import React, { useEffect, useState } from 'react'
import { FaArrowUp } from 'react-icons/fa'

const ScrollToTop = () => {

    const [isVisible, setIsVisible] = useState(false)


    //show and hide
    useEffect(()=>{
        const toggleVisibility = ()=>{
            if(window.scrollY > 300) setIsVisible(true)
            else setIsVisible(false)
        }

        window.addEventListener('scroll', toggleVisibility)

        return () => window.removeEventListener('scroll',toggleVisibility)
    }, [])


    const scrollToTop = ()=>{
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    }
  return (
    <div className='fixed animate-pulse bottom-4 right-4'>
      {isVisible && (
        <button onClick={scrollToTop} className='bg-cyan-500 text-white cursor-pointer rounded-full w-12 h-12 flex items-center justify-center focus:outline-none'>
            <FaArrowUp />
        </button>
      )}
    </div>
  )
}

export default ScrollToTop
