"""Authentication Schemas"""
from pydantic import BaseModel, EmailStr
from typing import Optional


class LoginRequest(BaseModel):
    """Login Request Schema"""
    username: str
    password: str


class TokenResponse(BaseModel):
    """Token Response Schema"""
    access_token: str
    token_type: str = "bearer"
    user_id: int
    username: str
    email: str
    full_name: str
    role: str
    language: str


class RefreshTokenRequest(BaseModel):
    """Refresh Token Request Schema"""
    refresh_token: str


class PasswordResetRequest(BaseModel):
    """Password Reset Request Schema"""
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    """Password Reset Confirm Schema"""
    token: str
    new_password: str
    confirm_password: str
