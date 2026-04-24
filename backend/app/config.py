from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # 数据库配置 (使用 SQLite，无需安装 MySQL)
    DATABASE_URL: str = "sqlite:///./book_shop.db"
    
    # JWT 配置
    JWT_SECRET_KEY: str = "your-secret-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080
    
    # Redis 配置
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    
    # 应用配置
    APP_ENV: str = "development"
    DEBUG: bool = True
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://localhost:5174"]
    
    # 文件上传
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 10485760
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
