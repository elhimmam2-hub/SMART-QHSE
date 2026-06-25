"""Incident Schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum


class IncidentTypeEnum(str, Enum):
    """Incident Types"""
    INJURY = "injury"
    NEAR_MISS = "near_miss"
    PROPERTY_DAMAGE = "property_damage"
    ENVIRONMENTAL = "environmental"
    OTHER = "other"


class SeverityLevelEnum(str, Enum):
    """Severity Levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class IncidentStatusEnum(str, Enum):
    """Incident Status"""
    OPEN = "open"
    INVESTIGATING = "investigating"
    CLOSED = "closed"


class IncidentBase(BaseModel):
    """Base Incident Schema"""
    incident_date: date
    incident_time: Optional[str] = None
    location: Optional[str] = None
    description: str = Field(..., min_length=10, max_length=2000)
    incident_type: Optional[IncidentTypeEnum] = None
    severity_level: Optional[SeverityLevelEnum] = None
    injured_workers_count: int = Field(default=0, ge=0)
    lost_time_injuries: int = Field(default=0, ge=0)
    first_aid_cases: int = Field(default=0, ge=0)
    medical_attention_required: bool = False
    hospitalized: bool = False
    fatalities: int = Field(default=0, ge=0)
    property_damage_amount: Optional[float] = Field(None, ge=0)
    production_loss: bool = False
    production_loss_hours: Optional[float] = Field(None, ge=0)


class IncidentCreate(IncidentBase):
    """Create Incident Schema"""
    company_id: int
    reported_by: str = Field(..., min_length=2)


class IncidentUpdate(BaseModel):
    """Update Incident Schema"""
    description: Optional[str] = None
    location: Optional[str] = None
    severity_level: Optional[SeverityLevelEnum] = None
    root_cause: Optional[str] = None
    corrective_actions: Optional[str] = None
    status: Optional[IncidentStatusEnum] = None
    assigned_to: Optional[str] = None
    investigation_completed: Optional[bool] = None
    investigation_date: Optional[date] = None


class IncidentResponse(IncidentBase):
    """Incident Response Schema"""
    id: int
    incident_number: str
    company_id: int
    root_cause: Optional[str] = None
    corrective_actions: Optional[str] = None
    assigned_to: Optional[str] = None
    status: IncidentStatusEnum
    investigation_completed: bool
    investigation_date: Optional[date] = None
    reported_by: str
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    attachment_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class IncidentListResponse(BaseModel):
    """Incident List Response Schema"""
    id: int
    incident_number: str
    incident_date: date
    location: Optional[str] = None
    incident_type: Optional[str] = None
    severity_level: Optional[str] = None
    status: str
    reported_by: str
    created_at: datetime
    
    class Config:
        from_attributes = True
