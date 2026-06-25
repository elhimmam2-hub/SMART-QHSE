"""Audit Log Schemas"""
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class AuditLogBase(BaseModel):
    """Base Audit Log Schema"""
    action: str
    entity_type: str
    entity_id: Optional[int] = None
    old_values: Optional[Dict[str, Any]] = None
    new_values: Optional[Dict[str, Any]] = None
    details: Optional[str] = None


class AuditLogCreate(AuditLogBase):
    """Create Audit Log Schema"""
    user_id: Optional[int] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None


class AuditLogResponse(AuditLogBase):
    """Audit Log Response Schema"""
    id: int
    user_id: Optional[int] = None
    ip_address: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class AuditLogListResponse(BaseModel):
    """Audit Log List Response Schema"""
    id: int
    action: str
    entity_type: str
    user_id: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
