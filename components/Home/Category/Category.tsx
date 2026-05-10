import React from 'react'

const categories = [
    {name: 'pizaa'},
    {name: 'Brakfast'},
    {name: 'Halal'},
    {name: 'Dessert'},
    {name: 'Lebnanese'},
    {name: 'Sushi'},
    {name: 'Turkish'},
    {name: 'Burgers'},
]

const Category = () => {
  return (
    <div className='pt-16 pb-16'>
        <h1 className='text-xl sm:text-2xl font-extrabold text-center'>Popular Categories by Food</h1>
        <div className='w-[80%] mx-auto mt-10'>
            <div className='flex flex-wrap gap-4 justify-center'>
                {categories.map((category, i)=>{
                    return ( <span data-aos="zoom-in" data-aos-anchor-placement="top-center" data-aos-delay={i*100} key={i} className='px-6 py-3 rounded-full cursor-pointer text-lg bg-gray-100 hover:bg-emerald-600 hover:text-white
                    transition-all duration-300 dark:bg-gray-800 dark:text-white text-gray-900 font-semibold'>
                        {category.name}
                    </span> )
                })}
            </div>
        </div>
    </div>
  )
}

export default Category
