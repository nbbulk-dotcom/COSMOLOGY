
"""
Database session management.
Provides database connection and session creation utilities.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Verify connections before use
    echo=settings.DEBUG,  # Log SQL in debug mode
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency for database sessions.
    Yields a database session and ensures it's closed after use.
    
    Usage:
        @app.get("/items")
        def get_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """
    Create all database tables.
    Should be called during application startup or migrations.
    """
    from app.db.models import Base
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """
    Drop all database tables.
    WARNING: This will delete all data!
    Only use in development/testing.
    """
    from app.db.models import Base
    Base.metadata.drop_all(bind=engine)
