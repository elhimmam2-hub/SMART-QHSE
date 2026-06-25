"""Near Miss Model"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class NearMissStatus(str, enum.Enum):
    """Near Miss Status"""
    OPEN = "open"
    INVESTIGATING = "investigating"
    CLOSED = "closed"


class RiskLevel(str, enum.Enum):
    """Risk Levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class NearMiss(Base):
    """Near Miss Model"""
    __tablename__ = "near_misses"
    
    id = Column(Integer, primary_key=True, index=True)
    near_miss_number = Column(String(100), unique=True, nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    report_date = Column(Date, nullable=False, index=True)
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=False)
    potential_hazard = Column(String(255), nullable=True)
    potential_consequence = Column(Text, nullable=True)
    reported_by = Column(String(255), nullable=False)
    witnesses = Column(Text, nullable=True)
    severity_level = Column(String(50), nullable=True)
    likelihood = Column(String(50), nullable=True)
    risk_level = Column(Enum(RiskLevel), nullable=True)
    root_cause = Column(Text, nullable=True)
    corrective_actions = Column(Text, nullable=True)
    preventive_actions = Column(Text, nullable=True)
    assigned_to = Column(String(255), nullable=True)
    status = Column(Enum(NearMissStatus), default=NearMissStatus.OPEN)
    estimated_completion_date = Column(Date, nullable=True)
    completion_date = Column(Date, nullable=True)
    verified_by = Column(String(255), nullable=True)
    attachment_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="near_misses")
    
    def __repr__(self):
        return f"<NearMiss {self.near_miss_number}>"
