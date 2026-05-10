import type { Metadata } from "next";
import { Manrope,} from "next/font/google";
import "./globals.css";
import ResponsiveNav from "@/components/Home/Navbar/ResponsiveNav";
import Provider from "@/components/HOD/Provider";
import Footer from '@/components/Home/Footer/Footer'
import ScrollToTop from "@/components/Helper/ScrollToTop/ScrollToTop";

const font = Manrope({
  weight: ['200', '300', '400', '500', '600', '700', '800'],
  subsets:['latin']
})

export const metadata: Metadata = {
  title: "Food Landing Page",
  description: "A simple landing page built with next.js and tailwind CSS"
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${font.className} antialiased`}
      >
        <Provider>
        {/* <ResponsiveNav/> */}
        {children}
        {/* <Footer/> */}
        <ScrollToTop/>
        </Provider>
      </body>
    </html>
  );
}
