"""Incident Model"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Text, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class IncidentType(str, enum.Enum):
    """Incident Types"""
    INJURY = "injury"
    NEAR_MISS = "near_miss"
    PROPERTY_DAMAGE = "property_damage"
    ENVIRONMENTAL = "environmental"
    OTHER = "other"


class SeverityLevel(str, enum.Enum):
    """Severity Levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class IncidentStatus(str, enum.Enum):
    """Incident Status"""
    OPEN = "open"
    INVESTIGATING = "investigating"
    CLOSED = "closed"


class Incident(Base):
    """Incident Model"""
    __tablename__ = "incidents"
    
    id = Column(Integer, primary_key=True, index=True)
    incident_number = Column(String(100), unique=True, nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    incident_date = Column(Date, nullable=False, index=True)
    incident_time = Column(String(10), nullable=True)
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=False)
    incident_type = Column(Enum(IncidentType), nullable=True)
    severity_level = Column(Enum(SeverityLevel), nullable=True)
    injured_workers_count = Column(Integer, default=0)
    lost_time_injuries = Column(Integer, default=0)
    first_aid_cases = Column(Integer, default=0)
    medical_attention_required = Column(Boolean, default=False)
    hospitalized = Column(Boolean, default=False)
    fatalities = Column(Integer, default=0)
    property_damage_amount = Column(Float, nullable=True)
    production_loss = Column(Boolean, default=False)
    production_loss_hours = Column(Float, nullable=True)
    root_cause = Column(Text, nullable=True)
    corrective_actions = Column(Text, nullable=True)
    assigned_to = Column(String(255), nullable=True)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.OPEN)
    investigation_completed = Column(Boolean, default=False)
    investigation_date = Column(Date, nullable=True)
    reported_by = Column(String(255), nullable=True)
    approved_by = Column(String(255), nullable=True)
    approved_date = Column(Date, nullable=True)
    attachment_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="incidents")
    
    def __repr__(self):
        return f"<Incident {self.incident_number}>"
