"""Worker Model"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class EmploymentType(str, enum.Enum):
    """Employment Types"""
    PERMANENT = "permanent"
    TEMPORARY = "temporary"
    CONTRACT = "contract"
    SEASONAL = "seasonal"


class Gender(str, enum.Enum):
    """Gender"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Worker(Base):
    """Worker Model"""
    __tablename__ = "workers"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(100), nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True, index=True)
    phone = Column(String(20), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    department = Column(String(100), nullable=True)
    position = Column(String(100), nullable=True)
    employment_date = Column(Date, nullable=True)
    contract_type = Column(Enum(EmploymentType), default=EmploymentType.PERMANENT)
    nationality = Column(String(100), nullable=True)
    gender = Column(Enum(Gender), nullable=True)
    marital_status = Column(String(50), nullable=True)
    emergency_contact = Column(String(255), nullable=True)
    emergency_phone = Column(String(20), nullable=True)
    identification_type = Column(String(50), nullable=True)
    identification_number = Column(String(100), nullable=True, unique=True)
    is_active = Column(Boolean, default=True)
    avatar_url = Column(String(500), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="workers")
    
    def __repr__(self):
        return f"<Worker {self.first_name} {self.last_name}>"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
