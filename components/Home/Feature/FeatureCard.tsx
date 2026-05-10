import React from 'react'
import Image from 'next/image'

type Props={
    icon:string;
    title:string;
}

const FeatureCard = ({icon,title}:Props) => {
  return (
    <div className='mt-16'>
      <Image src={icon} alt='image' width={100} height={100} className='mx-auto object-contain'/>
      <h1 className='mt-8 text-lg font-black text-center'>{title}</h1>
      <p className='text-center sm:w-[80%] mx-auto text-gray-700 dark:text-gray-300 mt-3'>
        we&apos;re driven beyond just finishing the project. We want to find solutions.
      </p>
    </div>
  )
}

export default FeatureCard
