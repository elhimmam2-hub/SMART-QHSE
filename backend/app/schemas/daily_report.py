"""Daily Report Schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date


class DailyReportBase(BaseModel):
    """Base Daily Report Schema"""
    report_date: date
    reported_by: str = Field(..., min_length=2, max_length=255)
    total_workers: int = Field(default=0, ge=0)
    absent_workers: int = Field(default=0, ge=0)
    incidents_today: int = Field(default=0, ge=0)
    near_misses_today: int = Field(default=0, ge=0)
    safety_meetings: bool = False
    environmental_issues: bool = False
    health_issues: bool = False
    comments: Optional[str] = None


class DailyReportCreate(DailyReportBase):
    """Create Daily Report Schema"""
    company_id: int


class DailyReportUpdate(BaseModel):
    """Update Daily Report Schema"""
    total_workers: Optional[int] = None
    absent_workers: Optional[int] = None
    incidents_today: Optional[int] = None
    near_misses_today: Optional[int] = None
    safety_meetings: Optional[bool] = None
    environmental_issues: Optional[bool] = None
    health_issues: Optional[bool] = None
    comments: Optional[str] = None
    approved_by: Optional[str] = None


class DailyReportResponse(DailyReportBase):
    """Daily Report Response Schema"""
    id: int
    report_number: str
    company_id: int
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class DailyReportListResponse(BaseModel):
    """Daily Report List Response Schema"""
    id: int
    report_number: str
    report_date: date
    reported_by: str
    total_workers: int
    incidents_today: int
    near_misses_today: int
    approved_by: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
