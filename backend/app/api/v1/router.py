"""API v1 router"""

from fastapi import APIRouter
from .endpoints import health, courses, auth

api_router = APIRouter()

# Include routers
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(courses.router)
