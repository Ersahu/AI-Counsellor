from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import University, Shortlist, User
from app.schemas.university import UniversityResponse, ShortlistCreate, ShortlistResponse
from app.api.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[UniversityResponse])
def get_universities(
    country: str = None,
    min_cost: int = None,
    max_cost: int = None,
    ranking: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(University)
    
    if country:
        query = query.filter(University.country == country)
    if min_cost:
        query = query.filter(University.avg_cost >= min_cost)
    if max_cost:
        query = query.filter(University.avg_cost <= max_cost)
    if ranking:
        query = query.filter(University.ranking_band == ranking)
    
    return query.all()

@router.get("/{university_id}", response_model=UniversityResponse)
def get_university(university_id: int, db: Session = Depends(get_db)):
    university = db.query(University).filter(University.id == university_id).first()
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return university

# Shortlist endpoints
@router.get("/shortlists/mine", response_model=List[ShortlistResponse])
def get_my_shortlists(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    shortlists = db.query(Shortlist).filter(Shortlist.user_id == current_user.id).all()
    return shortlists

@router.post("/shortlists", response_model=ShortlistResponse)
def add_to_shortlist(
    shortlist_data: ShortlistCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Check if already shortlisted
    existing = db.query(Shortlist).filter(
        Shortlist.user_id == current_user.id,
        Shortlist.university_id == shortlist_data.university_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Already shortlisted")
    
    # Create shortlist
    db_shortlist = Shortlist(
        user_id=current_user.id,
        university_id=shortlist_data.university_id,
        category=shortlist_data.category,
        locked=shortlist_data.locked
    )
    db.add(db_shortlist)
    db.commit()
    db.refresh(db_shortlist)
    
    # Refresh relationships
    db.refresh(db_shortlist)
    return db_shortlist

@router.put("/shortlists/{shortlist_id}/lock", response_model=ShortlistResponse)
def lock_university(
    shortlist_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    shortlist = db.query(Shortlist).filter(
        Shortlist.id == shortlist_id,
        Shortlist.user_id == current_user.id
    ).first()
    
    if not shortlist:
        raise HTTPException(status_code=404, detail="Shortlist entry not found")
    
    shortlist.locked = True
    db.commit()
    db.refresh(shortlist)
    
    # Check if user can move to next stage
    locked_count = db.query(Shortlist).filter(
        Shortlist.user_id == current_user.id,
        Shortlist.locked == True
    ).count()
    
    if locked_count >= 1 and current_user.current_stage == "locking":
        current_user.current_stage = "application"
        db.commit()
    
    return shortlist

@router.delete("/shortlists/{shortlist_id}")
def remove_from_shortlist(
    shortlist_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    shortlist = db.query(Shortlist).filter(
        Shortlist.id == shortlist_id,
        Shortlist.user_id == current_user.id
    ).first()
    
    if not shortlist:
        raise HTTPException(status_code=404, detail="Shortlist entry not found")
    
    db.delete(shortlist)
    db.commit()
    
    return {"message": "Removed from shortlist"}