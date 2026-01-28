from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UniversityBase(BaseModel):
    name: str
    country: str
    city: Optional[str] = None
    avg_cost: int
    ranking_band: str
    acceptance_difficulty: str
    description: Optional[str] = None

class UniversityCreate(UniversityBase):
    pass

class UniversityResponse(UniversityBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ShortlistBase(BaseModel):
    university_id: int
    category: str  # Dream, Target, Safe
    locked: bool = False

class ShortlistCreate(ShortlistBase):
    pass

class ShortlistResponse(ShortlistBase):
    id: int
    user_id: int
    university: UniversityResponse
    
    class Config:
        from_attributes = True