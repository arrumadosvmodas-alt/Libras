"""Course, Module, Lesson and LessonStep models"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.db.base import Base


class DifficultyLevel(str, enum.Enum):
    """Difficulty level enumeration"""

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class Course(Base):
    """Course model representing a complete LIBRAS course"""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    thumbnail_url = Column(String, nullable=True)
    difficulty = Column(Enum(DifficultyLevel), default=DifficultyLevel.BEGINNER)
    order_index = Column(Integer, default=0)
    is_published = Column(Integer, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    modules = relationship(
        "Module", back_populates="course", cascade="all, delete-orphan"
    )


class Module(Base):
    """Module model representing a section within a course"""

    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    is_published = Column(Integer, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    course = relationship("Course", back_populates="modules")
    lessons = relationship(
        "Lesson", back_populates="module", cascade="all, delete-orphan"
    )


class Lesson(Base):
    """Lesson model representing a single lesson within a module"""

    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    difficulty = Column(Enum(DifficultyLevel), default=DifficultyLevel.BEGINNER)
    duration_minutes = Column(Integer, default=10)
    order_index = Column(Integer, default=0)
    is_published = Column(Integer, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    module = relationship("Module", back_populates="lessons")
    steps = relationship(
        "LessonStep", back_populates="lesson", cascade="all, delete-orphan"
    )
    progress = relationship(
        "UserProgress", back_populates="lesson", cascade="all, delete-orphan"
    )


class LessonStep(Base):
    """LessonStep model representing content within a lesson (videos, signs, etc)"""

    __tablename__ = "lesson_steps"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    title = Column(String, nullable=False)
    content_type = Column(String, default="video")  # video, text, image, sign
    content_url = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    lesson = relationship("Lesson", back_populates="steps")
