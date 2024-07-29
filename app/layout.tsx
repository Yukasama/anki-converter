import { Provider } from '@/components/provider'
import { cn } from '@/utils/utils'
import type { Metadata } from 'next'
import { K2D } from 'next/font/google'
import { ReactNode } from 'react'
import './globals.css'

const k2d = K2D({
  subsets: ['latin'],
  weight: ['100', '200', '300', '400', '500', '600'],
})

export const metadata: Metadata = {
  title: 'Anki Converter',
  description: 'Convert Markdown to Anki easily',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: ReactNode
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={cn('min-h-screen antialiased', k2d.className)}>
        <Provider>
          <main className="min-h-screen">{children}</main>
        </Provider>
      </body>
    </html>
  )
}
