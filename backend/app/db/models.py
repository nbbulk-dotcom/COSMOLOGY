
"""
SQLAlchemy ORM models for the GREDs database schema.
Defines all database tables and relationships.
"""
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, JSON, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Work(Base):
    """
    Represents a research artifact (paper, README, repository, etc.)
    """
    __tablename__ = "works"
    
    id = Column(Integer, primary_key=True, index=True)
    source_slug = Column(String(255), unique=True, nullable=False, index=True)
    version = Column(String(50), nullable=False)
    canonical_url = Column(String(512), nullable=False)
    title = Column(String(512))
    authors = Column(JSON)  # List of author names
    publication_date = Column(DateTime, nullable=True)
    tags = Column(JSON)  # List of tags
    file_format = Column(String(20))  # pdf, md, html, txt
    s3_raw_path = Column(String(512))  # S3 key for original file
    ingestion_status = Column(String(20), default="pending")  # pending, processing, completed, failed
    ingestion_started_at = Column(DateTime, nullable=True)
    ingestion_completed_at = Column(DateTime, nullable=True)
    total_chunks = Column(Integer, default=0)
    metadata = Column(JSON)  # Additional metadata
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    chunks = relationship("Chunk", back_populates="work", cascade="all, delete-orphan")
    
    # Indexes
    __table_args__ = (
        Index('idx_work_slug_version', 'source_slug', 'version'),
        Index('idx_work_status', 'ingestion_status'),
    )

    def __repr__(self):
        return f"<Work(id={self.id}, slug={self.source_slug}, status={self.ingestion_status})>"


class Chunk(Base):
    """
    Text segments extracted from works during ingestion.
    """
    __tablename__ = "chunks"
    
    id = Column(Integer, primary_key=True, index=True)
    work_id = Column(Integer, ForeignKey("works.id"), nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)  # 0-based position in work
    text = Column(Text, nullable=False)
    token_count = Column(Integer)
    start_char = Column(Integer)
    end_char = Column(Integer)
    chunk_hash = Column(String(64), unique=True, index=True)  # SHA256 of text
    chunking_strategy = Column(String(50))  # "fixed_tokens_with_overlap"
    chunking_params = Column(JSON)  # {chunk_size: 1024, overlap: 0.2, seed: 42}
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    work = relationship("Work", back_populates="chunks")
    embedding = relationship("Embedding", uselist=False, back_populates="chunk", cascade="all, delete-orphan")
    summaries = relationship("Summary", back_populates="chunk", cascade="all, delete-orphan")
    citations = relationship("Citation", back_populates="chunk")
    
    # Indexes
    __table_args__ = (
        Index('idx_chunk_work_index', 'work_id', 'chunk_index'),
    )

    def __repr__(self):
        return f"<Chunk(id={self.id}, work_id={self.work_id}, index={self.chunk_index})>"


class Embedding(Base):
    """
    Vector embeddings for semantic search.
    """
    __tablename__ = "embeddings"
    
    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=False, unique=True, index=True)
    model_name = Column(String(100), nullable=False)  # "all-MiniLM-L6-v2"
    model_version = Column(String(50))
    vector_dim = Column(Integer)  # 384 for MiniLM
    embedding_hash = Column(String(64))  # Hash of vector for deduplication
    faiss_index_id = Column(Integer)  # Position in FAISS index
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    chunk = relationship("Chunk", back_populates="embedding")

    def __repr__(self):
        return f"<Embedding(id={self.id}, chunk_id={self.chunk_id}, model={self.model_name})>"


class Summary(Base):
    """
    Three-level summaries for chunks (short, medium, long).
    """
    __tablename__ = "summaries"
    
    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=False, index=True)
    summary_level = Column(String(20), nullable=False)  # short, medium, long
    summary_text = Column(Text, nullable=False)
    char_count = Column(Integer)
    llm_model = Column(String(100))  # "gpt-4-turbo"
    prompt_hash = Column(String(64))  # Hash of prompt template
    temperature = Column(Float)  # 0.2
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    chunk = relationship("Chunk", back_populates="summaries")
    
    # Indexes
    __table_args__ = (
        Index('idx_summary_chunk_level', 'chunk_id', 'summary_level'),
    )

    def __repr__(self):
        return f"<Summary(id={self.id}, chunk_id={self.chunk_id}, level={self.summary_level})>"


class Session(Base):
    """
    User interaction sessions with state management and checkpointing.
    """
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(64), unique=True, nullable=False, index=True)
    user_id = Column(String(255), nullable=True)  # Optional user identifier
    condensed_summary = Column(Text, nullable=True)  # Aggregated context
    accepted_claims = Column(JSON)  # List of verified claims
    top_citations = Column(JSON)  # Top 10-20 chunk IDs
    parent_checkpoint_id = Column(Integer, ForeignKey("sessions.id"), nullable=True)
    is_checkpoint = Column(Boolean, default=False)
    checkpoint_name = Column(String(255), nullable=True)
    state_json = Column(JSON)  # Full serialized state
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationships
    checkpoints = relationship("Session", remote_side=[id])

    def __repr__(self):
        return f"<Session(id={self.id}, session_id={self.session_id}, checkpoint={self.is_checkpoint})>"


class Citation(Base):
    """
    Links between queries/claims and supporting chunks.
    """
    __tablename__ = "citations"
    
    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=False, index=True)
    retrieval_id = Column(String(255), nullable=False, index=True)  # "slug:version:chunk_id"
    query_text = Column(Text, nullable=True)
    claim_text = Column(Text, nullable=True)
    similarity_score = Column(Float)
    verifier_decision = Column(String(20))  # pass, partial, fail
    context_window = Column(JSON)  # Adjacent chunk IDs
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    chunk = relationship("Chunk", back_populates="citations")
    
    # Indexes
    __table_args__ = (
        Index('idx_citation_retrieval', 'retrieval_id'),
    )

    def __repr__(self):
        return f"<Citation(id={self.id}, retrieval_id={self.retrieval_id}, decision={self.verifier_decision})>"


class AuditLog(Base):
    """
    Database-backed audit events (complementary to JSONL logs in S3).
    """
    __tablename__ = "audit_log"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True, nullable=False)
    event_type = Column(String(50), nullable=False, index=True)  # retrieval, ingestion, verification, etc.
    correlation_id = Column(String(64), index=True)  # Links related events
    user_id = Column(String(255), nullable=True)
    action = Column(String(255))
    resource_type = Column(String(100))
    resource_id = Column(String(255))
    metadata = Column(JSON)
    status = Column(String(20))  # success, failure
    error_message = Column(Text, nullable=True)
    duration_ms = Column(Integer)
    
    # Indexes
    __table_args__ = (
        Index('idx_audit_timestamp', 'timestamp'),
        Index('idx_audit_type', 'event_type'),
        Index('idx_audit_correlation', 'correlation_id'),
    )

    def __repr__(self):
        return f"<AuditLog(id={self.id}, type={self.event_type}, status={self.status})>"
