"""Company Model"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Company(Base):
    """Company Model"""
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    name_ar = Column(String(255), nullable=True)
    name_fr = Column(String(255), nullable=True)
    registration_number = Column(String(100), unique=True, nullable=True, index=True)
    industry = Column(String(100), nullable=True)
    website = Column(String(500), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    employees_count = Column(Integer, nullable=True)
    subscription_plan = Column(String(50), default="basic")
    subscription_expires_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    logo_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    users = relationship("User", back_populates="company", cascade="all, delete-orphan")
    workers = relationship("Worker", back_populates="company", cascade="all, delete-orphan")
    contractors = relationship("Contractor", back_populates="company", cascade="all, delete-orphan")
    incidents = relationship("Incident", back_populates="company", cascade="all, delete-orphan")
    near_misses = relationship("NearMiss", back_populates="company", cascade="all, delete-orphan")
    inspections = relationship("Inspection", back_populates="company", cascade="all, delete-orphan")
    daily_reports = relationship("DailyReport", back_populates="company", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Company {self.name}>"
