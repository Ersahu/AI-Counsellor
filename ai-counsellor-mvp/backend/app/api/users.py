from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, UserProfile
from app.schemas.user import UserProfileCreate, UserProfileUpdate, UserProfileResponse
from app.api.auth import get_current_user

router = APIRouter()

@router.post("/profile", response_model=UserProfileResponse)
def create_profile(
    profile_data: UserProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if profile already exists
    existing_profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile already exists"
        )
    
    # Convert countries list to JSON string
    profile_dict = profile_data.model_dump()
    if isinstance(profile_dict.get('countries'), list):
        import json
        profile_dict['countries'] = json.dumps(profile_dict['countries'])
    
    # Create profile
    db_profile = UserProfile(**profile_dict, user_id=current_user.id)
    db.add(db_profile)
    
    # Mark onboarding as complete
    current_user.onboarding_completed = True
    current_user.current_stage = "discovery"  # Move to next stage
    
    db.commit()
    db.refresh(db_profile)
    
    return db_profile

@router.put("/profile", response_model=UserProfileResponse)
def update_profile(
    profile_data: UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    # Update profile fields
    profile_dict = profile_data.model_dump()
    if isinstance(profile_dict.get('countries'), list):
        import json
        profile_dict['countries'] = json.dumps(profile_dict['countries'])
    
    for key, value in profile_dict.items():
        setattr(db_profile, key, value)
    
    db.commit()
    db.refresh(db_profile)
    
    return db_profile

@router.get("/me", response_model=dict)
def get_current_user_info(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    
    # Convert countries JSON string back to list for response
    if profile and profile.countries:
        import json
        try:
            if isinstance(profile.countries, str):
                profile.countries = json.loads(profile.countries)
        except (json.JSONDecodeError, TypeError):
            # If it's already a list or invalid JSON, keep as is
            pass
    
    return {
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email,
            "onboarding_completed": current_user.onboarding_completed,
            "current_stage": current_user.current_stage
        },
        "profile": profile
    }