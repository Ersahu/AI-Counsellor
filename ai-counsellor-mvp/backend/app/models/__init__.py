from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class StageEnum(str, enum.Enum):
    ONBOARDING = "onboarding"
    DISCOVERY = "discovery"
    LOCKING = "locking"
    APPLICATION = "application"

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Academic Background
    education_level = Column(String)  # Bachelor's, Master's, PhD
    degree = Column(String)           # Computer Science, etc.
    graduation_year = Column(Integer)
    gpa = Column(String)              # 3.5/4.0, 8.2/10, etc.
    
    # Study Goals
    target_degree = Column(String)    # Master's, PhD
    field = Column(String)            # Engineering, Business, etc.
    intake_year = Column(Integer)     # 2025, 2026
    
    # Location & Budget
    countries = Column(Text)          # JSON array: ["USA", "Canada"]
    budget_range = Column(String)     # "$20k-$30k", "$30k-$40k"
    funding_type = Column(String)     # Self-funded, Scholarship, Loan
    
    # Exam Status
    ielts_status = Column(String)     # Not Started, In Progress, Completed
    gre_status = Column(String)       # Not Started, In Progress, Completed
    toefl_status = Column(String)     # Not Started, In Progress, Completed
    
    # Documents
    sop_status = Column(String)       # Not Started, Draft, Ready
    lor_status = Column(String)       # Not Started, Partial, Ready
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship
    user = relationship("User", back_populates="profile")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    onboarding_completed = Column(Boolean, default=False)
    current_stage = Column(Enum(StageEnum), default=StageEnum.ONBOARDING)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    shortlists = relationship("Shortlist", back_populates="user")

class University(Base):
    __tablename__ = "universities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String)
    avg_cost = Column(Integer)        # Annual cost in USD
    ranking_band = Column(String)     # Top 10, Top 50, Top 100
    acceptance_difficulty = Column(String)  # Low, Medium, High
    description = Column(Text)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Shortlist(Base):
    __tablename__ = "shortlists"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    university_id = Column(Integer, ForeignKey("universities.id"))
    category = Column(String)         # Dream, Target, Safe
    locked = Column(Boolean, default=False)  # Critical for stage progression
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="shortlists")
    university = relationship("University")