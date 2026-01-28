from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from app.models import StageEnum

# Auth Schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# User Profile Schemas
class UserProfileBase(BaseModel):
    education_level: str
    degree: str
    graduation_year: int
    gpa: str
    target_degree: str
    field: str
    intake_year: int
    countries: List[str]
    budget_range: str
    funding_type: str
    ielts_status: str
    gre_status: str
    toefl_status: str
    sop_status: str
    lor_status: str

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfileResponse(UserProfileBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True

# User Schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserResponse(UserBase):
    id: int
    onboarding_completed: bool
    current_stage: StageEnum
    created_at: datetime
    profile: Optional[UserProfileResponse] = None
    
    class Config:
        from_attributes = True