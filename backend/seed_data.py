"""Seed initial data for development"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from app.db.base import Base
from app.models.user import User, UserRole
from app.models.course import Course, Module, Lesson, LessonStep, DifficultyLevel
from app.models.exercise import Exercise, ExerciseOption
from app.models.progress import UserStreak
from app.core.security import get_password_hash

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://libras_user:libras_password@localhost:5432/libras_db"
)

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)


def seed_database():
    """Seed the database with initial data"""
    db = SessionLocal()

    try:
        # Check if data already exists
        existing_course = db.query(Course).filter(Course.slug == "libras-basico").first()
        if existing_course:
            print("✅ Database already seeded. Skipping...")
            return

        print("🌱 Seeding database...")

        # Create test users
        admin_user = User(
            email="admin@libras.app",
            full_name="Admin LIBRAS",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            role=UserRole.ADMIN
        )

        student_user = User(
            email="student@libras.app",
            full_name="João Silva",
            hashed_password=get_password_hash("student123"),
            is_active=True,
            role=UserRole.STUDENT
        )

        db.add(admin_user)
        db.add(student_user)
        db.flush()

        # Create main course
        course = Course(
            title="LIBRAS Básico",
            slug="libras-basico",
            description="Aprenda os fundamentos de LIBRAS com aulas curtas e exercícios práticos.",
            difficulty=DifficultyLevel.BEGINNER,
            thumbnail_url=None,
            is_published=True,
            order_index=1
        )
        db.add(course)
        db.flush()

        # Create modules
        modules_data = [
            {
                "title": "Introdução à LIBRAS",
                "slug": "introducao-libras",
                "description": "Conheça a Língua Brasileira de Sinais e sua história.",
                "order_index": 1,
            },
            {
                "title": "Alfabeto Manual",
                "slug": "alfabeto-manual",
                "description": "Aprenda as 26 letras do alfabeto em LIBRAS.",
                "order_index": 2,
            },
            {
                "title": "Cumprimentos",
                "slug": "cumprimentos",
                "description": "Conheça os principais cumprimentos em LIBRAS.",
                "order_index": 3,
            },
            {
                "title": "Números",
                "slug": "numeros",
                "description": "Aprenda a contar e usar números em LIBRAS.",
                "order_index": 4,
            },
        ]

        modules = []
        for module_data in modules_data:
            module = Module(
                course_id=course.id,
                title=module_data["title"],
                slug=module_data["slug"],
                description=module_data["description"],
                order_index=module_data["order_index"],
                is_published=True
            )
            modules.append(module)
            db.add(module)

        db.flush()

        # Create lessons for first module
        lessons_data = [
            {
                "module_idx": 0,
                "title": "O que é LIBRAS?",
                "slug": "o-que-e-libras",
                "description": "Entenda o que é a Língua Brasileira de Sinais.",
                "duration_minutes": 8,
            },
            {
                "module_idx": 0,
                "title": "História e Comunidade Surda",
                "slug": "historia-comunidade-surda",
                "description": "Conheça a história da comunidade surda no Brasil.",
                "duration_minutes": 10,
            },
        ]

        lessons = []
        for idx, lesson_data in enumerate(lessons_data):
            lesson = Lesson(
                module_id=modules[lesson_data["module_idx"]].id,
                title=lesson_data["title"],
                slug=lesson_data["slug"],
                description=lesson_data["description"],
                difficulty=DifficultyLevel.BEGINNER,
                duration_minutes=lesson_data["duration_minutes"],
                order_index=idx + 1,
                is_published=True
            )
            lessons.append(lesson)
            db.add(lesson)

        db.flush()

        # Create lesson steps
        for lesson in lessons:
            step = LessonStep(
                lesson_id=lesson.id,
                title="Vídeo Principal",
                content_type="video",
                content_url="https://example.com/videos/placeholder.mp4",
                description="Videoaula com professor surdo",
                order_index=1
            )
            db.add(step)

        # Create exercises for first lesson
        if lessons:
            exercise = Exercise(
                lesson_id=lessons[0].id,
                exercise_type="multiple_choice",
                question="Qual é a língua falada pela comunidade surda brasileira?",
                explanation="LIBRAS é a Língua Brasileira de Sinais, usada pela comunidade surda do Brasil.",
                order_index=1,
                points=10
            )
            db.add(exercise)
            db.flush()

            # Add exercise options
            options = [
                {"text": "LIBRAS", "is_correct": True},
                {"text": "Língua Portuguesa", "is_correct": False},
                {"text": "Linguagem gestual", "is_correct": False},
                {"text": "Código de sinais", "is_correct": False},
            ]

            for idx, option_data in enumerate(options):
                option = ExerciseOption(
                    exercise_id=exercise.id,
                    text=option_data["text"],
                    is_correct=option_data["is_correct"],
                    order_index=idx + 1
                )
                db.add(option)

        # Create user streak for student
        if student_user:
            streak = UserStreak(
                user_id=student_user.id,
                current_streak=0,
                longest_streak=0
            )
            db.add(streak)

        # Commit all changes
        db.commit()
        print("✅ Database seeded successfully!")
        print(f"   - Created 1 course with 4 modules and 2 lessons")
        print(f"   - Created 2 test users (admin@libras.app, student@libras.app)")
        print(f"   - Created sample exercises and options")

    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
