"""Exercise and ExerciseOption models"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Exercise(Base):
    """Exercise model representing an interactive exercise in a lesson"""

    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    exercise_type = Column(String, nullable=False)  # multiple_choice, video_match, etc
    question = Column(Text, nullable=False)
    explanation = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    points = Column(Integer, default=10)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    options = relationship(
        "ExerciseOption", back_populates="exercise", cascade="all, delete-orphan"
    )


class ExerciseOption(Base):
    """ExerciseOption model representing answer options for an exercise"""

    __tablename__ = "exercise_options"

    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    text = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    video_url = Column(String, nullable=True)
    is_correct = Column(Boolean, default=False)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    exercise = relationship("Exercise", back_populates="options")
