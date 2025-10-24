
"""
Query API endpoints.
Handles hybrid retrieval queries.
"""
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Dict, Optional
import structlog

from app.db.session import get_db

logger = structlog.get_logger()

router = APIRouter()


class QueryRequest(BaseModel):
    """Request model for query."""
    session_id: str
    user_query: str
    constraints: Optional[Dict] = None


class Claim(BaseModel):
    """Claim with citations."""
    text: str
    citation_ids: List[str]


class QueryResponse(BaseModel):
    """Response model for query."""
    answer: str
    claims: List[Claim]
    retrieval_ids: List[str]


@router.post("/", response_model=QueryResponse)
async def query(request: QueryRequest, db: Session = Depends(get_db)):
    """
    Submit a query for hybrid retrieval.
    
    TODO: Implement in Phase 4:
    - Embed query
    - Search FAISS (semantic)
    - Search Whoosh (lexical)
    - Merge results with hybrid scoring
    - Return top-K chunks
    """
    logger.info("Query received", session_id=request.session_id, query=request.user_query)
    
    # Placeholder response
    raise HTTPException(
        status_code=501,
        detail="Query pipeline not yet implemented. Coming in Phase 4."
    )
