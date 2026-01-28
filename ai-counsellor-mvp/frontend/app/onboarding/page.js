'use client'
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import axios from 'axios'

export default function Onboarding() {
  const [step, setStep] = useState(1)
  const router = useRouter()

  // Check authentication
  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) {
      router.push('/login')
    }
  }, [router])
  const [formData, setFormData] = useState({
    education_level: '',
    degree: '',
    graduation_year: 2024,
    gpa: '',
    target_degree: '',
    field: '',
    intake_year: 2025,
    countries: [],
    budget_range: '',
    funding_type: '',
    ielts_status: 'Not Started',
    gre_status: 'Not Started',
    toefl_status: 'Not Started',
    sop_status: 'Not Started',
    lor_status: 'Not Started'
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const nextStep = () => {
    if (step < 4) setStep(step + 1)
  }

  const prevStep = () => {
    if (step > 1) setStep(step - 1)
  }

  const handleChange = (field, value) => {
    setFormData({
      ...formData,
      [field]: value
    })
  }

  const handleSubmit = async () => {
    setLoading(true)
    setError('')
    
    try {
      const token = localStorage.getItem('token')
      console.log('Onboarding - Token from localStorage:', token ? token.substring(0, 20) + '...' : 'null')
      const response = await axios.post(
        'http://localhost:8000/api/users/profile',
        formData,
        {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        }
      )
      
      // Redirect to dashboard
      router.push('/dashboard')
    } catch (err) {
      console.log('Onboarding error:', err.response?.data || err.message)
      setError(err.response?.data?.detail || 'Failed to save profile')
    } finally {
      setLoading(false)
    }
  }

  const renderStep = () => {
    switch(step) {
      case 1:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900">Academic Background</h3>
            <div className="grid grid-cols-1 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Current Education Level
                </label>
                <select
                  value={formData.education_level}
                  onChange={(e) => handleChange('education_level', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="">Select level</option>
                  <option value="Bachelor's">Bachelor's</option>
                  <option value="Master's">Master's</option>
                  <option value="PhD">PhD</option>
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Current Degree/Major
                </label>
                <input
                  type="text"
                  value={formData.degree}
                  onChange={(e) => handleChange('degree', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                  placeholder="e.g., Computer Science"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Expected Graduation Year
                </label>
                <input
                  type="number"
                  value={formData.graduation_year}
                  onChange={(e) => handleChange('graduation_year', parseInt(e.target.value))}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  GPA / Percentage
                </label>
                <input
                  type="text"
                  value={formData.gpa}
                  onChange={(e) => handleChange('gpa', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                  placeholder="e.g., 3.7/4.0 or 8.5/10"
                />
              </div>
            </div>
          </div>
        )
      
      case 2:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900">Study Goals</h3>
            <div className="grid grid-cols-1 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Target Degree Level
                </label>
                <select
                  value={formData.target_degree}
                  onChange={(e) => handleChange('target_degree', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="">Select target degree</option>
                  <option value="Master's">Master's</option>
                  <option value="PhD">PhD</option>
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Field of Study
                </label>
                <input
                  type="text"
                  value={formData.field}
                  onChange={(e) => handleChange('field', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                  placeholder="e.g., Data Science, MBA, Electrical Engineering"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Intake Year
                </label>
                <select
                  value={formData.intake_year}
                  onChange={(e) => handleChange('intake_year', parseInt(e.target.value))}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value={2025}>2025</option>
                  <option value={2026}>2026</option>
                  <option value={2027}>2027</option>
                </select>
              </div>
            </div>
          </div>
        )
      
      case 3:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900">Preferences & Budget</h3>
            <div className="grid grid-cols-1 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Preferred Countries (Select all that apply)
                </label>
                <div className="grid grid-cols-2 gap-3">
                  {['USA', 'Canada', 'UK', 'Australia', 'Germany', 'Singapore'].map(country => (
                    <label key={country} className="flex items-center">
                      <input
                        type="checkbox"
                        checked={formData.countries.includes(country)}
                        onChange={(e) => {
                          const newCountries = e.target.checked
                            ? [...formData.countries, country]
                            : formData.countries.filter(c => c !== country)
                          handleChange('countries', newCountries)
                        }}
                        className="h-4 w-4 text-primary-600 border-gray-300 rounded focus:ring-primary-500"
                      />
                      <span className="ml-2 text-gray-700">{country}</span>
                    </label>
                  ))}
                </div>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Budget Range (Annual)
                </label>
                <select
                  value={formData.budget_range}
                  onChange={(e) => handleChange('budget_range', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="">Select budget range</option>
                  <option value="$10k-$20k">$10k - $20k</option>
                  <option value="$20k-$30k">$20k - $30k</option>
                  <option value="$30k-$40k">$30k - $40k</option>
                  <option value="$40k+">$40k+</option>
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Funding Type
                </label>
                <select
                  value={formData.funding_type}
                  onChange={(e) => handleChange('funding_type', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="">Select funding type</option>
                  <option value="Self-funded">Self-funded</option>
                  <option value="Scholarship">Looking for Scholarship</option>
                  <option value="Loan">Planning to take Loan</option>
                </select>
              </div>
            </div>
          </div>
        )
      
      case 4:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900">Current Readiness</h3>
            <div className="grid grid-cols-1 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  IELTS/TOEFL Status
                </label>
                <select
                  value={formData.ielts_status}
                  onChange={(e) => handleChange('ielts_status', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="Not Started">Not Started</option>
                  <option value="In Progress">In Progress</option>
                  <option value="Completed">Completed</option>
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  GRE/GMAT Status
                </label>
                <select
                  value={formData.gre_status}
                  onChange={(e) => handleChange('gre_status', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="Not Started">Not Started</option>
                  <option value="In Progress">In Progress</option>
                  <option value="Completed">Completed</option>
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Statement of Purpose Status
                </label>
                <select
                  value={formData.sop_status}
                  onChange={(e) => handleChange('sop_status', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                >
                  <option value="Not Started">Not Started</option>
                  <option value="Draft">Draft in Progress</option>
                  <option value="Ready">Ready for Submission</option>
                </select>
              </div>
            </div>
          </div>
        )
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          {/* Progress Bar */}
          <div className="px-8 pt-8">
            <div className="flex items-center justify-between mb-6">
              {[1, 2, 3, 4].map((num) => (
                <div key={num} className="flex items-center">
                  <div className={`w-10 h-10 rounded-full flex items-center justify-center ${
                    step >= num 
                      ? 'bg-primary-600 text-white' 
                      : 'bg-gray-200 text-gray-500'
                  }`}>
                    {num}
                  </div>
                  {num < 4 && (
                    <div className={`w-16 h-1 ${step > num ? 'bg-primary-600' : 'bg-gray-200'}`}></div>
                  )}
                </div>
              ))}
            </div>
          </div>
          
          {/* Form Content */}
          <div className="px-8 pb-8">
            {error && (
              <div className="mb-6 rounded-lg bg-red-50 p-4">
                <div className="text-sm text-red-700">{error}</div>
              </div>
            )}
            
            {renderStep()}
            
            {/* Navigation Buttons */}
            <div className="flex justify-between mt-10">
              <button
                onClick={prevStep}
                disabled={step === 1}
                className={`px-6 py-3 rounded-lg font-medium ${
                  step === 1
                    ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                Back
              </button>
              
              {step < 4 ? (
                <button
                  onClick={nextStep}
                  className="px-6 py-3 bg-primary-600 text-white rounded-lg font-medium hover:bg-primary-700"
                >
                  Continue
                </button>
              ) : (
                <button
                  onClick={handleSubmit}
                  disabled={loading}
                  className="px-6 py-3 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 disabled:opacity-50"
                >
                  {loading ? 'Saving...' : 'Complete Onboarding'}
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}