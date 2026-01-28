'use client'
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import axios from 'axios'

export default function Dashboard() {
  const [user, setUser] = useState(null)
  const [profile, setProfile] = useState(null)
  const [loading, setLoading] = useState(true)
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem('token')
    console.log('Token from localStorage:', token ? token.substring(0, 20) + '...' : 'null')
    
    if (!token) {
      router.push('/login')
      return
    }

    // Fetch user data
    axios.get('http://localhost:8000/api/users/me', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    .then(response => {
      setUser(response.data.user)
      setProfile(response.data.profile)
      setLoading(false)
    })
    .catch(error => {
      console.error('Error fetching user data:', error)
      localStorage.removeItem('token')
      router.push('/login')
    })
  }, [router])

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-xl">Loading...</div>
      </div>
    )
  }

  // If user hasn't completed onboarding, redirect to onboarding
  if (!user.onboarding_completed) {
    router.push('/onboarding')
    return null
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold text-primary-600">AI Counsellor</h1>
            <div className="flex items-center space-x-4">
              <span className="text-gray-700">Welcome, {user.name}</span>
              <button 
                onClick={() => {
                  localStorage.removeItem('token')
                  router.push('/')
                }}
                className="px-4 py-2 text-gray-600 hover:text-gray-800"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-2">Dashboard</h2>
          <p className="text-gray-600">Your study abroad journey progress</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div className="text-2xl font-bold text-primary-600">
              {profile ? 'Complete' : 'Incomplete'}
            </div>
            <div className="text-gray-600">Profile Status</div>
          </div>
          
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div className="text-2xl font-bold text-secondary-500">
              {user.current_stage.charAt(0).toUpperCase() + user.current_stage.slice(1)}
            </div>
            <div className="text-gray-600">Current Stage</div>
          </div>
          
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div className="text-2xl font-bold text-green-600">
              0
            </div>
            <div className="text-gray-600">Shortlisted Universities</div>
          </div>
        </div>

        {/* Next Steps */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
          <h3 className="text-xl font-semibold mb-4">Next Steps</h3>
          <div className="space-y-4">
            {user.current_stage === 'discovery' && (
              <div className="p-4 bg-blue-50 rounded-lg">
                <h4 className="font-medium text-blue-800">University Discovery</h4>
                <p className="text-blue-600">Start exploring universities that match your profile and preferences.</p>
                <button className="mt-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
                  Explore Universities
                </button>
              </div>
            )}
            
            {user.current_stage === 'locking' && (
              <div className="p-4 bg-yellow-50 rounded-lg">
                <h4 className="font-medium text-yellow-800">University Locking</h4>
                <p className="text-yellow-600">Lock at least one university to proceed to application preparation.</p>
                <button className="mt-2 px-4 py-2 bg-yellow-600 text-white rounded-lg hover:bg-yellow-700">
                  Lock Universities
                </button>
              </div>
            )}
            
            {user.current_stage === 'application' && (
              <div className="p-4 bg-green-50 rounded-lg">
                <h4 className="font-medium text-green-800">Application Preparation</h4>
                <p className="text-green-600">Prepare your application documents and follow the timeline.</p>
                <button className="mt-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
                  Prepare Applications
                </button>
              </div>
            )}
          </div>
        </div>

        {/* AI Counsellor Chat Button */}
        <div className="mt-8 text-center">
          <button className="px-6 py-3 bg-primary-600 text-white rounded-lg font-medium hover:bg-primary-700">
            Chat with AI Counsellor
          </button>
        </div>
      </main>
    </div>
  )
}