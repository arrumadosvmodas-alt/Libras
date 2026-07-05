"""Progress schemas"""

from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class UserProgressCreate(BaseModel):
    """Schema for creating user progress"""

    lesson_id: int
    score: float = 0.0
    is_completed: bool = False


class UserProgressResponse(BaseModel):
    """Schema for user progress response"""

    id: int
    user_id: int
    lesson_id: int
    score: float
    is_completed: bool
    completed_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserStreakResponse(BaseModel):
    """Schema for user streak response"""

    id: int
    user_id: int
    current_streak: int
    longest_streak: int
    last_activity_date: Optional[date]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
