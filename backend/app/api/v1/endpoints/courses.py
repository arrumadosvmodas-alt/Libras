"""Courses endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.course import Course, Module, Lesson
from app.schemas.course import CourseCreate, CourseUpdate, CourseResponse, ModuleResponse, LessonResponse

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("", response_model=List[CourseResponse])
async def list_courses(db: Session = Depends(get_db)):
    """List all courses"""
    courses = db.query(Course).filter(Course.is_published == True).all()
    return courses


@router.get("/{course_slug}", response_model=CourseResponse)
async def get_course(course_slug: str, db: Session = Depends(get_db)):
    """Get a specific course by slug"""
    course = db.query(Course).filter(Course.slug == course_slug).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return course


@router.post("", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Create a new course (admin only)"""
    # Check if course slug already exists
    existing = db.query(Course).filter(Course.slug == course.slug).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course with this slug already exists"
        )

    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


@router.put("/{course_id}", response_model=CourseResponse)
async def update_course(
    course_id: int,
    course_update: CourseUpdate,
    db: Session = Depends(get_db)
):
    """Update a course (admin only)"""
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    update_data = course_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_course, field, value)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    """Delete a course (admin only)"""
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    db.delete(db_course)
    db.commit()
