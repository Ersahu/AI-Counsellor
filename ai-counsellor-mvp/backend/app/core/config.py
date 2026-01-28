from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./ai_counsellor.db"
    GEMINI_API_KEY: str = "your-gemini-api-key-here"
    
    class Config:
        env_file = ".env"

settings = Settings()