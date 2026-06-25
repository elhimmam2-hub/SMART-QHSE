"""Inspection Model"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Text, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class InspectionType(str, enum.Enum):
    """Inspection Types"""
    SAFETY = "safety"
    HEALTH = "health"
    ENVIRONMENT = "environment"
    QUALITY = "quality"
    COMPLIANCE = "compliance"


class InspectionStatus(str, enum.Enum):
    """Inspection Status"""
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Inspection(Base):
    """Inspection Model"""
    __tablename__ = "inspections"
    
    id = Column(Integer, primary_key=True, index=True)
    inspection_number = Column(String(100), unique=True, nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    inspection_date = Column(Date, nullable=False, index=True)
    inspection_type = Column(Enum(InspectionType), nullable=False)
    location = Column(String(255), nullable=True)
    inspector_name = Column(String(255), nullable=False)
    supervisor_name = Column(String(255), nullable=True)
    observations = Column(Text, nullable=True)
    findings = Column(Text, nullable=True)
    non_conformities_count = Column(Integer, default=0)
    corrective_actions = Column(Text, nullable=True)
    compliance_score = Column(Float, nullable=True)
    status = Column(Enum(InspectionStatus), default=InspectionStatus.PLANNED)
    attachment_url = Column(String(500), nullable=True)
    next_inspection_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="inspections")
    
    def __repr__(self):
        return f"<Inspection {self.inspection_number}>"
