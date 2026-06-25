"""Inspection Schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum


class InspectionTypeEnum(str, Enum):
    """Inspection Types"""
    SAFETY = "safety"
    HEALTH = "health"
    ENVIRONMENT = "environment"
    QUALITY = "quality"
    COMPLIANCE = "compliance"


class InspectionStatusEnum(str, Enum):
    """Inspection Status"""
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class InspectionBase(BaseModel):
    """Base Inspection Schema"""
    inspection_date: date
    inspection_type: InspectionTypeEnum
    location: Optional[str] = None
    inspector_name: str = Field(..., min_length=2, max_length=255)
    supervisor_name: Optional[str] = None
    observations: Optional[str] = None
    findings: Optional[str] = None
    non_conformities_count: int = Field(default=0, ge=0)
    corrective_actions: Optional[str] = None
    compliance_score: Optional[float] = Field(None, ge=0, le=100)
    next_inspection_date: Optional[date] = None


class InspectionCreate(InspectionBase):
    """Create Inspection Schema"""
    company_id: int


class InspectionUpdate(BaseModel):
    """Update Inspection Schema"""
    observations: Optional[str] = None
    findings: Optional[str] = None
    non_conformities_count: Optional[int] = None
    corrective_actions: Optional[str] = None
    compliance_score: Optional[float] = None
    status: Optional[InspectionStatusEnum] = None
    next_inspection_date: Optional[date] = None


class InspectionResponse(InspectionBase):
    """Inspection Response Schema"""
    id: int
    inspection_number: str
    company_id: int
    status: InspectionStatusEnum
    attachment_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class InspectionListResponse(BaseModel):
    """Inspection List Response Schema"""
    id: int
    inspection_number: str
    inspection_date: date
    inspection_type: str
    location: Optional[str] = None
    inspector_name: str
    status: str
    compliance_score: Optional[float] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
