"""User schemas"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    """Schema for creating a new user"""

    email: EmailStr
    full_name: str
    password: str


class UserLogin(BaseModel):
    """Schema for user login"""

    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """Schema for updating user"""

    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


class UserResponse(BaseModel):
    """Schema for user response"""

    id: int
    email: str
    full_name: str
    is_active: bool
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Schema for token response"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
