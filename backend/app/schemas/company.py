"""Company Schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime, date


class CompanyBase(BaseModel):
    """Base Company Schema"""
    name: str = Field(..., min_length=2, max_length=255)
    name_ar: Optional[str] = None
    name_fr: Optional[str] = None
    registration_number: Optional[str] = Field(None, max_length=100)
    industry: Optional[str] = None
    website: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    employees_count: Optional[int] = None
    subscription_plan: str = Field(default="basic", regex="^(basic|pro|enterprise)$")


class CompanyCreate(CompanyBase):
    """Create Company Schema"""
    pass


class CompanyUpdate(BaseModel):
    """Update Company Schema"""
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    name_ar: Optional[str] = None
    name_fr: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    employees_count: Optional[int] = None
    subscription_plan: Optional[str] = None


class CompanyResponse(CompanyBase):
    """Company Response Schema"""
    id: int
    is_active: bool
    logo_url: Optional[str] = None
    subscription_expires_at: Optional[date] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class CompanyListResponse(BaseModel):
    """Company List Response Schema"""
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    industry: Optional[str] = None
    employees_count: Optional[int] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
