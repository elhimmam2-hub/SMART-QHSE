"""Contractor Schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime, date


class ContractorBase(BaseModel):
    """Base Contractor Schema"""
    company_name: str = Field(..., min_length=2, max_length=255)
    contact_person: str = Field(..., min_length=2, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    work_type: str = Field(..., min_length=2, max_length=100)
    contract_start_date: Optional[date] = None
    contract_end_date: Optional[date] = None
    insurance_expiry: Optional[date] = None
    license_number: Optional[str] = None
    license_expiry: Optional[date] = None
    registration_number: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    is_certified: bool = False
    certification_type: Optional[str] = None


class ContractorCreate(ContractorBase):
    """Create Contractor Schema"""
    company_id: int


class ContractorUpdate(BaseModel):
    """Update Contractor Schema"""
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    work_type: Optional[str] = None
    insurance_expiry: Optional[date] = None
    license_number: Optional[str] = None
    license_expiry: Optional[date] = None
    contract_end_date: Optional[date] = None
    is_certified: Optional[bool] = None
    certification_type: Optional[str] = None


class ContractorResponse(ContractorBase):
    """Contractor Response Schema"""
    id: int
    company_id: int
    is_active: bool
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ContractorListResponse(BaseModel):
    """Contractor List Response Schema"""
    id: int
    company_name: str
    contact_person: str
    work_type: str
    email: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
