import React from 'react'
import Image from 'next/image'

type Props = {
    image:string;
    title:string;
    num:string;
    description:string;
}

const HowItWorkCard = ({image, title, num, description}: Props) => {
  return (
    <div>
      <div className='relative'>
        <Image alt='imag' width={250} src={image} height={250} className='object-contain mx-auto'/>
        <div className='w-14 h-14 text-xl text-white bg-pink-600 flex items-center justify-center rounded-full absolute top-0 left-0 flex-col'>
            {num}
        </div>
            <h1 className='mt-6 mx-auto text-lg sm:text-xl text-center font-bold'>{title}</h1>
            <p className='text-center sm:w-[80%] mx-auto text-gray-700 dark:text-gray-300 mt-3 font-medium'>{description}</p>
            <p className='mt-4 text-base font-bold text-blue-800 dark:text-blue-400 hover:text-blue-600 transition-all duration-150 cursor-pointer text-center'>Start Earning &rarr;</p>
      </div>
    </div>
  )
}

export default HowItWorkCard
