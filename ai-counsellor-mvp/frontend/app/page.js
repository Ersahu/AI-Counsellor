'use client'
import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

export default function Home() {
  const [showLogin, setShowLogin] = useState(false)
  const [showDemoModal, setShowDemoModal] = useState(false)
  const router = useRouter()
  
  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold text-primary-600">AI Counsellor</h1>
            <div className="space-x-4">
              <button 
                onClick={() => router.push('/login')}
                className="px-4 py-2 text-primary-600 hover:text-primary-700 font-medium"
              >
                Login
              </button>
              <button 
                onClick={() => router.push('/signup')}
                className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 font-medium"
              >
                Sign Up
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-grow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center">
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
              Plan your{' '}
              <span className="text-primary-600">study-abroad journey</span>{' '}
              with a guided{' '}
              <span className="text-secondary-500">AI counsellor</span>
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-10">
              Make confident decisions with our stage-based system that guides you from confusion to clarity. 
              No more endless research - get personalized recommendations and actionable steps.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link 
                href={showLogin ? "/login" : "/signup"}
                className="px-8 py-4 bg-primary-600 text-white text-lg font-semibold rounded-lg hover:bg-primary-700 transition-colors"
              >
                Get Started
              </Link>
              <button 
                onClick={() => setShowDemoModal(true)}
                className="px-8 py-4 border-2 border-primary-600 text-primary-600 text-lg font-semibold rounded-lg hover:bg-primary-50 transition-colors cursor-pointer"
              >
                Watch Demo
              </button>
            </div>
          </div>

          {/* Features */}
          <div className="mt-24 grid md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-6">
                <span className="text-2xl">🔒</span>
              </div>
              <h3 className="text-xl font-semibold mb-3">Stage-Based Progression</h3>
              <p className="text-gray-600">
                Complete each stage to unlock the next. No skipping allowed - ensures thorough decision-making.
              </p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
              <div className="w-12 h-12 bg-secondary-100 rounded-lg flex items-center justify-center mb-6">
                <span className="text-2xl">🤖</span>
              </div>
              <h3 className="text-xl font-semibold mb-3">AI-Powered Guidance</h3>
              <p className="text-gray-600">
                Our AI counselor understands your profile and provides personalized university recommendations.
              </p>
            </div>
            
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-6">
                <span className="text-2xl">✅</span>
              </div>
              <h3 className="text-xl font-semibold mb-3">Action-Oriented System</h3>
              <p className="text-gray-600">
                The AI doesn't just talk - it creates tasks, shortlists universities, and tracks your progress.
              </p>
            </div>
          </div>
        </div>
      </main>

      {/* Demo Modal */}
      {showDemoModal && (
        <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden shadow-2xl">
            <div className="p-6 border-b border-gray-200 flex justify-between items-center">
              <h3 className="text-2xl font-bold text-gray-900">AI Counsellor Platform Demo</h3>
              <button 
                onClick={() => setShowDemoModal(false)}
                className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
              >
                &times;
              </button>
            </div>
            <div className="p-6">
              <div className="aspect-video bg-gray-900 rounded-lg flex items-center justify-center">
                <div className="text-center text-white">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-16 w-16 mx-auto mb-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <p className="text-lg font-medium">Demo Video Player</p>
                  <p className="text-gray-400 mt-2">Interactive demonstration of the AI Counsellor platform features</p>
                </div>
              </div>
              <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-blue-50 p-4 rounded-lg">
                  <h4 className="font-semibold text-blue-800">AI Recommendations</h4>
                  <p className="text-sm text-gray-600 mt-1">See how our AI analyzes your profile and suggests universities</p>
                </div>
                <div className="bg-green-50 p-4 rounded-lg">
                  <h4 className="font-semibold text-green-800">Stage Management</h4>
                  <p className="text-sm text-gray-600 mt-1">Track your progress through each stage of the process</p>
                </div>
                <div className="bg-purple-50 p-4 rounded-lg">
                  <h4 className="font-semibold text-purple-800">Application Tracking</h4>
                  <p className="text-sm text-gray-600 mt-1">Monitor deadlines and requirements for each university</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}


      {/* Footer */}
      <footer className="bg-gray-800 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p>&copy; 2024 AI Counsellor. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}