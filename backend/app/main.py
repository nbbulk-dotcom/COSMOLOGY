
"""
FastAPI application entry point.
Defines the main application, middleware, and routes.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import structlog
import sys

from app.config import settings

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info(
        "Application startup",
        version="0.1.0",
        environment=settings.ENVIRONMENT,
        debug=settings.DEBUG
    )
    
    # TODO: Initialize database connection pool
    # TODO: Initialize FAISS and Whoosh indexes
    # TODO: Initialize Redis connection
    # TODO: Verify S3 connectivity
    
    yield
    
    # Shutdown
    logger.info("Application shutdown")
    # TODO: Close database connections
    # TODO: Save indexes
    # TODO: Close Redis connection


# Create FastAPI application
app = FastAPI(
    title="GREDs AI Reference Library",
    description="Hybrid retrieval and citation verification system for quantum research",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS_LIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Returns the status of the application and connected services.
    """
    return {
        "status": "healthy",
        "version": "0.1.0",
        "environment": settings.ENVIRONMENT,
        "services": {
            "database": "not_checked",  # TODO: Add actual DB health check
            "redis": "not_checked",      # TODO: Add actual Redis health check
            "s3": "not_checked"          # TODO: Add actual S3 health check
        }
    }


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "GREDs AI Reference Library API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health"
    }


# TODO: Include API routers when implemented
# from app.api.v1 import ingest, query, session, verify, audit
# app.include_router(ingest.router, prefix="/api/v1/ingest", tags=["Ingestion"])
# app.include_router(query.router, prefix="/api/v1/query", tags=["Query"])
# app.include_router(session.router, prefix="/api/v1/session", tags=["Session"])
# app.include_router(verify.router, prefix="/api/v1/verify", tags=["Verification"])
# app.include_router(audit.router, prefix="/api/v1/audit", tags=["Audit"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level=settings.LOG_LEVEL.lower()
    )
