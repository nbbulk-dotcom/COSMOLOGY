
"""
Ingestion API endpoints.
Handles repository ingestion, chunking, embedding, and indexing.
"""
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import structlog

from app.db.session import get_db

logger = structlog.get_logger()

router = APIRouter()


class IngestWorkRequest(BaseModel):
    """Request model for ingesting a new work."""
    repo_url: str
    slug: str
    force_regenerate: bool = False


class IngestWorkResponse(BaseModel):
    """Response model for ingestion request."""
    job_id: str
    status: str


@router.post("/add-work", response_model=IngestWorkResponse)
async def ingest_work(request: IngestWorkRequest, db: Session = Depends(get_db)):
    """
    Submit a new work for ingestion.
    
    TODO: Implement ingestion pipeline in Phase 2:
    - Clone repository
    - Extract text
    - Create chunks
    - Generate embeddings
    - Build indexes
    - Store in database
    """
    logger.info("Ingestion requested", slug=request.slug, url=request.repo_url)
    
    # Placeholder response
    raise HTTPException(
        status_code=501,
        detail="Ingestion pipeline not yet implemented. Coming in Phase 2."
    )
