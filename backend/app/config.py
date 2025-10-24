
"""
Application configuration using Pydantic Settings.
Loads environment variables from .env file.
"""
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database
    POSTGRES_USER: str = Field("cosmology", description="PostgreSQL username")
    POSTGRES_PASSWORD: str = Field("changeme", description="PostgreSQL password")
    POSTGRES_DB: str = Field("greds_library", description="PostgreSQL database name")
    POSTGRES_HOST: str = Field("postgres", description="PostgreSQL host")
    POSTGRES_PORT: int = Field(5432, description="PostgreSQL port")
    
    @property
    def DATABASE_URL(self) -> str:
        """Construct database URL from components."""
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    # Redis
    REDIS_HOST: str = Field("redis", description="Redis host")
    REDIS_PORT: int = Field(6379, description="Redis port")
    REDIS_PASSWORD: str = Field("", description="Redis password")
    
    @property
    def REDIS_URL(self) -> str:
        """Construct Redis URL from components."""
        auth = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"redis://{auth}{self.REDIS_HOST}:{self.REDIS_PORT}/0"
    
    # S3 Storage
    S3_ENDPOINT_URL: str = Field("http://minio:9000", description="S3 endpoint URL")
    S3_ACCESS_KEY_ID: str = Field("minioadmin", description="S3 access key")
    S3_SECRET_ACCESS_KEY: str = Field("minioadmin", description="S3 secret key")
    S3_BUCKET_NAME: str = Field("greds-audit-logs", description="S3 bucket name")
    S3_REGION: str = Field("us-east-1", description="S3 region")
    
    # Abacus.AI
    ABACUSAI_API_KEY: str = Field(..., description="Abacus.AI API key (required)")
    ABACUSAI_MODEL_ID: str = Field("gpt-4-turbo", description="Abacus.AI model ID")
    
    # Application
    BACKEND_CORS_ORIGINS: str = Field(
        "http://localhost:3000",
        description="Comma-separated list of allowed CORS origins"
    )
    LOG_LEVEL: str = Field("INFO", description="Logging level")
    DEBUG: bool = Field(False, description="Debug mode")
    RANDOM_SEED: int = Field(42, description="Random seed for reproducibility")
    ENVIRONMENT: str = Field("development", description="Environment name")
    
    @property
    def CORS_ORIGINS_LIST(self) -> List[str]:
        """Parse CORS origins into list."""
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",")]
    
    # Embeddings
    EMBEDDING_MODEL: str = Field(
        "sentence-transformers/all-MiniLM-L6-v2",
        description="Embedding model name"
    )
    EMBEDDING_DIM: int = Field(384, description="Embedding dimension")
    
    # Chunking
    CHUNK_SIZE: int = Field(1024, description="Chunk size in tokens")
    CHUNK_OVERLAP: float = Field(0.2, description="Chunk overlap ratio")
    
    # Retrieval
    SEMANTIC_WEIGHT: float = Field(0.7, description="Semantic search weight")
    LEXICAL_WEIGHT: float = Field(0.3, description="Lexical search weight")
    TOP_K: int = Field(20, description="Number of top results to return")
    
    # Verification
    VERIFIER_PASS_THRESHOLD: float = Field(
        0.80,
        description="Similarity threshold for pass"
    )
    VERIFIER_PARTIAL_THRESHOLD: float = Field(
        0.75,
        description="Similarity threshold for partial pass"
    )
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
