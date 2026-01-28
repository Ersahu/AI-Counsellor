import './globals.css'

export const metadata = {
  title: 'AI Counsellor - Guided Study Abroad Decision System',
  description: 'Plan your study-abroad journey with a guided AI counsellor',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50">
        {children}
      </body>
    </html>
  )
}