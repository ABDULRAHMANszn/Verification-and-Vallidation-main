import React from 'react'
import { FaStar } from 'react-icons/fa';
import Image from 'next/image';

type Props = {
    reviewTitle: string;
    userName: string;
    userImage: string;
    role: string;
}

const ReviewCard = ({reviewTitle, userName, userImage, role}: Props) => {
  return (
    <div className='bg-gray-100 dark:bg-gray-900 rounded-lg shadow-md p-6 mr-4'>
        <h1 className='text-xl font-bold'>{reviewTitle}</h1>
        <div className='mt-2 flex items-center'>
            <FaStar className='text-yellow-500 w-5 h-5'/>
            <FaStar className='text-yellow-500 w-5 h-5'/>
            <FaStar className='text-yellow-500 w-5 h-5'/>
            <FaStar className='text-yellow-500 w-5 h-5'/>
            <FaStar className='text-yellow-500 w-5 h-5'/>
        </div>
        <p className='mt-4 text-gray-800 dark:text-gray-300 font-medium text-base'>
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aliquid illum debitis adipisci inventore aliquam veritatis.
        Eaque recusandae amet, dolor, corporis minus, dolore soluta consectetur excepturi non officia laborum eum consequuntur.    
        </p>
        <p className='block w-full h-[1px] text-gray-300 dark:text-gray-700 mt-6 mb-6'></p>
        <div>
            <div className='flex items-center space-x-4'>
                <Image src={userImage} alt='image' width={60} height={60} className='rounded-full'/>
                <div>
                    <h1 className='text-lg font-bold'>{userName}</h1>
                    <p className='text-sm sm:text-base'>{role}</p>
                </div>
            </div>
        </div>
    </div>
  )
}

export default ReviewCard
