"""Contractor Model"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Contractor(Base):
    """Contractor Model"""
    __tablename__ = "contractors"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    company_name = Column(String(255), nullable=False)
    contact_person = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True, index=True)
    phone = Column(String(20), nullable=True)
    work_type = Column(String(100), nullable=False)
    contract_start_date = Column(Date, nullable=True)
    contract_end_date = Column(Date, nullable=True)
    insurance_expiry = Column(Date, nullable=True)
    license_number = Column(String(100), nullable=True)
    license_expiry = Column(Date, nullable=True)
    registration_number = Column(String(100), nullable=True, unique=True)
    website = Column(String(500), nullable=True)
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    is_certified = Column(Boolean, default=False)
    certification_type = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="contractors")
    
    def __repr__(self):
        return f"<Contractor {self.company_name}>"
