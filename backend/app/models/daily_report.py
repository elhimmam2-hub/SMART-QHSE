"""Daily Report Model"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class DailyReport(Base):
    """Daily Report Model"""
    __tablename__ = "daily_reports"
    
    id = Column(Integer, primary_key=True, index=True)
    report_number = Column(String(100), unique=True, nullable=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    report_date = Column(Date, nullable=False, index=True)
    reported_by = Column(String(255), nullable=False)
    total_workers = Column(Integer, default=0)
    absent_workers = Column(Integer, default=0)
    incidents_today = Column(Integer, default=0)
    near_misses_today = Column(Integer, default=0)
    safety_meetings = Column(Boolean, default=False)
    environmental_issues = Column(Boolean, default=False)
    health_issues = Column(Boolean, default=False)
    comments = Column(Text, nullable=True)
    approved_by = Column(String(255), nullable=True)
    approved_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    company = relationship("Company", back_populates="daily_reports")
    
    def __repr__(self):
        return f"<DailyReport {self.report_number}>"
