"""Response Schemas"""
from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional
from datetime import datetime

T = TypeVar('T')


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated Response Schema"""
    total: int
    page: int
    limit: int
    pages: int
    data: List[T]


class SuccessResponse(BaseModel, Generic[T]):
    """Success Response Schema"""
    success: bool = True
    message: str
    data: Optional[T] = None
    timestamp: datetime = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class ErrorResponse(BaseModel):
    """Error Response Schema"""
    success: bool = False
    message: str
    error_code: str
    details: Optional[str] = None
    timestamp: datetime = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()
