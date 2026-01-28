from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.ai.counsellor import ai_counsellor
from app.api.auth import get_current_user
from app.models import User

router = APIRouter()

class ChatMessage(BaseModel):
    message: str

@router.post("/chat")
def chat_with_counsellor(
    chat_data: ChatMessage,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Validate stage progression
    if not current_user.onboarding_completed and current_user.current_stage == "onboarding":
        raise HTTPException(
            status_code=400,
            detail="Complete onboarding first"
        )
    
    # Get AI response
    response = ai_counsellor.get_response(chat_data.message, current_user, db)
    
    return response

@router.get("/dashboard-summary")
def get_dashboard_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Get profile strength assessment
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    
    if not profile:
        return {
            "profile_strength": "Incomplete",
            "stage": current_user.current_stage,
            "progress": 0
        }
    
    # Simple profile strength calculation
    completed_fields = 0
    total_fields = 12  # Adjust based on your schema
    
    if profile.gpa: completed_fields += 1
    if profile.ielts_status != "Not Started": completed_fields += 1
    if profile.gre_status != "Not Started": completed_fields += 1
    if profile.sop_status != "Not Started": completed_fields += 1
    # Add more checks...
    
    strength_percentage = (completed_fields / total_fields) * 100
    
    if strength_percentage >= 80:
        strength = "Strong"
    elif strength_percentage >= 50:
        strength = "Average"
    else:
        strength = "Needs Improvement"
    
    # Count shortlists
    shortlist_count = db.query(Shortlist).filter(Shortlist.user_id == current_user.id).count()
    locked_count = db.query(Shortlist).filter(
        Shortlist.user_id == current_user.id,
        Shortlist.locked == True
    ).count()
    
    return {
        "profile_strength": strength,
        "profile_completion": strength_percentage,
        "stage": current_user.current_stage,
        "shortlisted_universities": shortlist_count,
        "locked_universities": locked_count
    }