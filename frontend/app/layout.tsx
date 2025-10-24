
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'GREDs AI Reference Library',
  description: 'Hybrid retrieval and citation verification system for quantum research',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="min-h-screen bg-background">
          <header className="border-b">
            <div className="container mx-auto px-4 py-4">
              <h1 className="text-2xl font-bold">GREDs AI Reference Library</h1>
              <p className="text-sm text-muted-foreground">
                Quantum Research Knowledge Management
              </p>
            </div>
          </header>
          <main>{children}</main>
          <footer className="border-t mt-auto">
            <div className="container mx-auto px-4 py-6 text-center text-sm text-muted-foreground">
              © 2025 GREDs AI Reference Library | Phase 0 - Repository Initialization
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
