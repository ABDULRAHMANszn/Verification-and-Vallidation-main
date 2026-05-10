export type OrderItem = {
    title: string;
    price: number;
    quantity: number;
    image: string;
  };
  
  export type Order = {
    id: number;
    date: string;
    items: OrderItem[];
  };
  
  // This file is temproray file just to see how the page is going to be visible
  // All orders and details show be retrieved from the data base.

  export const mockOrders: Order[] = [
    {
      id: 1,
      date: "2026-04-10",
      items: [
        {
          title: "Pizza Hut Delicios Pizza",
          price: 120,
          quantity: 2,
          image: "/images/r1.png",
        },
        {
          title: "Chipotle Mexican Grill",
          price: 80,
          quantity: 1,
          image: "/images/r2.png",
        },
      ],
    },
    {
      id: 2,
      date: "2026-04-12",
      items: [
        {
          title: "McDonal's Burgers",
          price: 100,
          quantity: 3,
          image: "/images/r3.png",
        },
      ],
    },
    {
      id: 3,
      date: "2026-04-15",
      items: [
        {
          title: "Shake Sheak",
          price: 180,
          quantity: 1,
          image: "/images/r5.png",
        },
        {
          title: "The Baked Bear San Fransisco",
          price: 150,
          quantity: 2,
          image: "/images/r4.png",
        },
      ],
    },
  ];