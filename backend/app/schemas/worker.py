"""Worker Schemas"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum


class EmploymentTypeEnum(str, Enum):
    """Employment Types"""
    PERMANENT = "permanent"
    TEMPORARY = "temporary"
    CONTRACT = "contract"
    SEASONAL = "seasonal"


class GenderEnum(str, Enum):
    """Gender"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class WorkerBase(BaseModel):
    """Base Worker Schema"""
    employee_id: str = Field(..., max_length=100)
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    department: Optional[str] = None
    position: Optional[str] = None
    employment_date: Optional[date] = None
    contract_type: EmploymentTypeEnum = EmploymentTypeEnum.PERMANENT
    nationality: Optional[str] = None
    gender: Optional[GenderEnum] = None
    marital_status: Optional[str] = None
    emergency_contact: Optional[str] = None
    emergency_phone: Optional[str] = None
    identification_type: Optional[str] = None
    identification_number: Optional[str] = None


class WorkerCreate(WorkerBase):
    """Create Worker Schema"""
    company_id: int


class WorkerUpdate(BaseModel):
    """Update Worker Schema"""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    contract_type: Optional[EmploymentTypeEnum] = None
    gender: Optional[GenderEnum] = None
    marital_status: Optional[str] = None
    emergency_contact: Optional[str] = None
    emergency_phone: Optional[str] = None


class WorkerResponse(WorkerBase):
    """Worker Response Schema"""
    id: int
    company_id: int
    is_active: bool
    avatar_url: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class WorkerListResponse(BaseModel):
    """Worker List Response Schema"""
    id: int
    employee_id: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
