"""Course, Module and Lesson schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class LessonStepResponse(BaseModel):
    """Schema for lesson step response"""

    id: int
    title: str
    content_type: str
    content_url: Optional[str]
    description: Optional[str]
    order_index: int

    class Config:
        from_attributes = True


class LessonCreate(BaseModel):
    """Schema for creating a lesson"""

    title: str
    slug: str
    description: Optional[str] = None
    difficulty: str = "beginner"
    duration_minutes: int = 10


class LessonResponse(BaseModel):
    """Schema for lesson response"""

    id: int
    module_id: int
    title: str
    slug: str
    description: Optional[str]
    difficulty: str
    duration_minutes: int
    order_index: int
    is_published: bool
    steps: List[LessonStepResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ModuleCreate(BaseModel):
    """Schema for creating a module"""

    title: str
    slug: str
    description: Optional[str] = None
    course_id: int


class ModuleResponse(BaseModel):
    """Schema for module response"""

    id: int
    course_id: int
    title: str
    slug: str
    description: Optional[str]
    order_index: int
    is_published: bool
    lessons: List[LessonResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    """Schema for creating a course"""

    title: str
    slug: str
    description: Optional[str] = None
    difficulty: str = "beginner"
    thumbnail_url: Optional[str] = None


class CourseUpdate(BaseModel):
    """Schema for updating a course"""

    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    thumbnail_url: Optional[str] = None
    is_published: Optional[bool] = None


class CourseResponse(BaseModel):
    """Schema for course response"""

    id: int
    title: str
    slug: str
    description: Optional[str]
    difficulty: str
    thumbnail_url: Optional[str]
    order_index: int
    is_published: bool
    modules: List[ModuleResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
