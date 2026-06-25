"""Application Configuration"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SMART QHSE Platform"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/smart_qhse"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    REDIS_URL: str = "redis://localhost:6379/0"
    MINIO_URL: str = "http://localhost:9000"
    DEBUG: bool = True
    ENV: str = "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
