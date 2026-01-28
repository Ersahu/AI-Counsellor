# AI Counsellor - Guided Study Abroad Decision System

A modern, stage-based AI-powered platform that guides students through the study abroad decision process with personalized recommendations and structured progression. Built with cutting-edge technologies and a focus on user experience.

## 🚀 Live Demo

The application is currently running on your local machine:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000

## 🌟 Key Features

### 🔒 Stage-Based Decision System
Our platform enforces a structured approach to ensure comprehensive decision-making:
- **Onboarding** → Complete your profile and educational background
- **Discovery** → AI analyzes your profile and recommends universities
- **University Locking** → Select and lock your preferred universities
- **Application** → Track and manage your application progress

### 🤖 Advanced AI Integration
- **Google Gemini API**: Powers intelligent university recommendations
- **Structured JSON Responses**: Consistent, predictable AI output format
- **Profile Analysis**: AI processes your complete academic and personal profile
- **Action-Oriented**: The AI creates tasks, not just conversations

### 💅 Modern UI/UX
- **Animated Authentication**: Beautiful login/signup pages with smooth transitions
- **Responsive Design**: Works perfectly on all devices
- **Interactive Elements**: Hover effects, loading states, and micro-interactions
- **Gradient Backgrounds**: Modern aesthetic with floating bubble animations

### 🔐 Secure Authentication
- **JWT Token System**: Industry-standard secure authentication
- **Protected Routes**: Role-based access control
- **Session Management**: Automatic token expiration and refresh

## 🛠️ Technology Stack

### Frontend
- **Next.js 14** (App Router) - React framework with server components
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API communication
- **React Hooks** - useState, useEffect, useRouter for state management

### Backend
- **FastAPI** (Python 3.9+) - High-performance web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI server for production

### Database & Services
- **PostgreSQL** - Relational database (configurable)
- **Google Gemini API** - AI-powered recommendations
- **JWT** - Secure token-based authentication

## 📋 Prerequisites

- **Node.js** v18 or higher
- **Python** 3.9 or higher
- **npm** or **yarn** package manager
- **Google Gemini API Key** (for AI features)

## 🚀 Quick Start

### 1. Start Backend Server
```bash
cd ai-counsellor-mvp/backend
pip install -r requirements.txt
python main.py
```
Backend API will be available at `http://localhost:8000`

### 2. Start Frontend Development Server
```bash
cd ai-counsellor-mvp/frontend
npm install
npm run dev
```
Frontend will be available at `http://localhost:3000`

### 3. Environment Configuration

**Backend** (`.env` in backend directory):
```env
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Frontend** (`.env.local` in frontend directory):
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## 🗂️ Project Structure

```
ai-counsellor-mvp/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py          # Authentication endpoints
│   │   │   ├── users.py         # User profile management
│   │   │   └── ai_counsellor.py # AI interaction endpoints
│   │   ├── models/              # Database models
│   │   │   ├── user.py          # User and profile models
│   │   │   └── __init__.py      # Model imports
│   │   ├── schemas/             # Pydantic schemas
│   │   │   ├── user.py          # User validation schemas
│   │   │   └── __init__.py      # Schema imports
│   │   ├── database.py          # Database configuration
│   │   └── main.py              # FastAPI application
│   ├── requirements.txt         # Python dependencies
│   └── main.py                  # Application entry point
├── frontend/
│   ├── app/
│   │   ├── login/               # Login page with animations
│   │   ├── signup/              # Signup page with animations
│   │   ├── dashboard/           # User dashboard
│   │   ├── onboarding/          # 4-step onboarding flow
│   │   ├── page.js              # Landing page
│   │   ├── layout.js            # Root layout
│   │   └── globals.css          # Global styles and animations
│   ├── public/                  # Static assets
│   ├── package.json             # Frontend dependencies
│   └── next.config.js           # Next.js configuration
└── README.md                    # This file

## 🎯 Core Workflows

### User Journey
1. **Landing Page**: Modern hero section with animated buttons
2. **Authentication**: Animated login/signup with gradient backgrounds
3. **Onboarding**: 4-step process to collect user profile
4. **Dashboard**: Central hub for AI interactions and progress tracking

### AI Interaction Flow
1. User sends message to AI counselor
2. Backend processes message with Gemini API
3. AI responds with structured JSON format
4. Frontend renders appropriate UI based on response type



## 🔧 API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User authentication
- `POST /api/auth/logout` - User logout

### User Management
- `GET /api/users/me` - Get current user information
- `PUT /api/users/profile` - Update user profile
- `GET /api/users/profile` - Get user profile

### AI Counsellor
- `POST /api/ai/chat` - Send message to AI counselor
- `GET /api/ai/history` - Retrieve conversation history

## 🎨 UI Highlights

### Animated Authentication Pages
- **Gradient Backgrounds**: Floating animated bubbles
- **Form Design**: Icons inside input fields with proper labels
- **Loading States**: Animated spinners during API calls
- **Error Handling**: Shake animations for validation errors
- **Hover Effects**: Smooth scale transformations on interactive elements

### Landing Page Features
- **Hero Section**: Modern headline with call-to-action buttons
- **Feature Cards**: Clean, informative sections highlighting key features
- **Demo Modal**: Interactive "Watch Demo" functionality
- **Responsive Navigation**: Header with functional login/signup buttons

## 🤖 AI Capabilities

### University Recommendations
- **Profile Analysis**: Educational background, preferences, and goals
- **Data-Driven**: Uses Gemini API for intelligent matching
- **Structured Output**: Consistent JSON format for easy processing

### Progress Tracking
- **Stage Management**: Locks and unlocks based on completion
- **Task Creation**: AI generates actionable items
- **Status Updates**: Real-time progress tracking

## 🧪 Development Commands

### Backend Development
```bash
# Run development server
cd backend
python main.py

# Run with auto-reload (development)
uvicorn app.main:app --reload


### Frontend Development
```bash
# Start development server
cd frontend
npm run dev

# Build for production
npm run build

# Start production server
npm run start


## 🚀 Deployment Options

### Frontend (Vercel/Netlify)
```bash
# Build frontend for production
cd frontend
npm run build
```

### Backend (Railway/Render/Vercel)
```bash
# Production server
cd backend
uvicorn app.main:app --host 0.0.0.0 --port $PORT


## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Protected Routes**: Middleware validation for all sensitive endpoints
- **Input Validation**: Pydantic schemas for data validation
- **Password Security**: Proper hashing and storage
- **CORS Configuration**: Secure cross-origin resource sharing

## 📈 Future Enhancements

- **University Database Integration**: Real university data and requirements
- **Application Tracking**: Integration with actual application portals
- **Video/Audio Calls**: Agora SDK integration for virtual consultations
- **Multi-language Support**: Localization for international users
- **Advanced Analytics**: Progress insights and recommendations

## 🆘 Troubleshooting

### Common Issues

**1. "Login failed" or authentication errors**
- Check if backend server is running on `localhost:8000`
- Verify database connection
- Ensure valid user credentials

**2. "Failed to save profile"**
- Check console for database errors
- Ensure all required fields are filled
- Verify database migration status

**3. UI components not rendering**
- Clear browser cache
- Check for JavaScript errors in console
- Ensure all dependencies are installed

### Debugging Tips

**Backend Logs**
- Check terminal output for error messages
- Use `print()` statements for debugging
- Enable detailed logging in development

**Frontend Debugging**
- Open browser DevTools (F12)
- Check Network tab for API calls
- Use console.log() for state tracking


## 🤝 Contributions
We welcome pull requests! For major changes, please open an issue to discuss what you'd like to improve or add.

## 📧 Contact
**Developer**: Vaibhav

**Email**: sahuvaibhav064@gmail.com

**LinkedIn**: https://www.linkedin.com/in/vaibhav-chaudhary-615712272/

## 📜 License
MIT License © 2025 Vaibhav
