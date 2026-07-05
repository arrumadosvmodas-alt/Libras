"""Exercise schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class ExerciseOptionResponse(BaseModel):
    """Schema for exercise option response"""

    id: int
    text: str
    image_url: Optional[str]
    video_url: Optional[str]
    is_correct: bool
    order_index: int

    class Config:
        from_attributes = True


class ExerciseCreate(BaseModel):
    """Schema for creating an exercise"""

    lesson_id: int
    exercise_type: str
    question: str
    explanation: Optional[str] = None
    points: int = 10


class ExerciseResponse(BaseModel):
    """Schema for exercise response"""

    id: int
    lesson_id: int
    exercise_type: str
    question: str
    explanation: Optional[str]
    order_index: int
    points: int
    options: List[ExerciseOptionResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
