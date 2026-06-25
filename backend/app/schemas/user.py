"""User Schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class UserRoleEnum(str, Enum):
    """User Roles"""
    ADMIN = "admin"
    MANAGER = "manager"
    SUPERVISOR = "supervisor"
    OPERATOR = "operator"
    VIEWER = "viewer"


class UserBase(BaseModel):
    """Base User Schema"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    full_name: str = Field(..., min_length=2, max_length=255)
    role: UserRoleEnum = UserRoleEnum.VIEWER
    phone: Optional[str] = None
    language: str = Field(default="ar", regex="^(ar|en|fr)$")


class UserCreate(UserBase):
    """Create User Schema"""
    password: str = Field(..., min_length=8, max_length=100)
    company_id: Optional[int] = None


class UserUpdate(BaseModel):
    """Update User Schema"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, min_length=2, max_length=255)
    phone: Optional[str] = None
    language: Optional[str] = Field(None, regex="^(ar|en|fr)$")
    role: Optional[UserRoleEnum] = None


class UserPasswordChange(BaseModel):
    """Change Password Schema"""
    current_password: str
    new_password: str = Field(..., min_length=8)
    confirm_password: str


class UserResponse(UserBase):
    """User Response Schema"""
    id: int
    is_active: bool
    is_superuser: bool
    company_id: Optional[int] = None
    avatar_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    """User List Response Schema"""
    id: int
    username: str
    email: str
    full_name: str
    role: str
    is_active: bool
    company_id: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
