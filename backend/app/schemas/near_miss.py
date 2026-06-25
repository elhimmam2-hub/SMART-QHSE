"""Near Miss Schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum


class RiskLevelEnum(str, Enum):
    """Risk Levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class NearMissStatusEnum(str, Enum):
    """Near Miss Status"""
    OPEN = "open"
    INVESTIGATING = "investigating"
    CLOSED = "closed"


class NearMissBase(BaseModel):
    """Base Near Miss Schema"""
    report_date: date
    location: Optional[str] = None
    description: str = Field(..., min_length=10, max_length=2000)
    potential_hazard: Optional[str] = None
    potential_consequence: Optional[str] = None
    witnesses: Optional[str] = None
    severity_level: Optional[str] = None
    likelihood: Optional[str] = None
    risk_level: Optional[RiskLevelEnum] = None


class NearMissCreate(NearMissBase):
    """Create Near Miss Schema"""
    company_id: int
    reported_by: str = Field(..., min_length=2)


class NearMissUpdate(BaseModel):
    """Update Near Miss Schema"""
    description: Optional[str] = None
    location: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_actions: Optional[str] = None
    preventive_actions: Optional[str] = None
    status: Optional[NearMissStatusEnum] = None
    assigned_to: Optional[str] = None
    estimated_completion_date: Optional[date] = None
    completion_date: Optional[date] = None


class NearMissResponse(NearMissBase):
    """Near Miss Response Schema"""
    id: int
    near_miss_number: str
    company_id: int
    root_cause: Optional[str] = None
    corrective_actions: Optional[str] = None
    preventive_actions: Optional[str] = None
    reported_by: str
    assigned_to: Optional[str] = None
    status: NearMissStatusEnum
    estimated_completion_date: Optional[date] = None
    completion_date: Optional[date] = None
    verified_by: Optional[str] = None
    attachment_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class NearMissListResponse(BaseModel):
    """Near Miss List Response Schema"""
    id: int
    near_miss_number: str
    report_date: date
    location: Optional[str] = None
    risk_level: Optional[str] = None
    status: str
    reported_by: str
    created_at: datetime
    
    class Config:
        from_attributes = True
