# GREDs AI Reference Library - Project Plan

**Version:** 1.0  
**Last Updated:** October 24, 2025  
**Project Status:** Planning Phase  
**Estimated Total Duration:** 10-12 weeks  

---

## Executive Summary

### Project Overview

The **GREDs AI Reference Library** (COSMOLOGY) is an enterprise-grade knowledge management system designed to ingest, index, retrieve, and verify scientific research documents with deterministic, auditable operations. The system implements a hybrid retrieval architecture combining semantic (FAISS) and lexical (BM25) search, backed by a three-level summarization hierarchy and citation verification system.

**Core Capabilities:**
- **Deterministic Ingestion**: Text chunking with fixed seeds for reproducibility
- **Hybrid Retrieval**: 0.7 semantic + 0.3 lexical scoring for optimal accuracy
- **Citation Verification**: Automated fact-checking with cosine similarity thresholds
- **Session Management**: Stateful context preservation with checkpoint/rehydration
- **Immutable Audit Trail**: SHA256-chained JSONL logs for compliance
- **Knowledge Graphs**: Visual dependency mapping between research artifacts

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend API** | FastAPI + Uvicorn | High-performance async Python framework |
| **Frontend** | Next.js 14 (App Router) | React-based SSR/SSG framework |
| **Database** | PostgreSQL 15+ | Relational data storage (metadata, chunks, sessions) |
| **Vector Store** | FAISS | High-speed semantic similarity search |
| **Lexical Search** | Whoosh | BM25 ranking for keyword matching |
| **Embeddings** | sentence-transformers | all-MiniLM-L6-v2 (384-dim vectors) |
| **LLM Provider** | Abacus.AI APIs | Summary generation (low temperature=0.2) |
| **Object Storage** | S3-compatible | MinIO (dev) / AWS S3 (prod) for audit logs & artifacts |
| **Task Queue** | Redis + RQ | Background job processing |
| **Containerization** | Docker + Compose | Unified deployment environment |
| **UI Components** | shadcn/ui + Tailwind CSS | Consistent design system |
| **Visualization** | D3.js / React Flow | Knowledge graph rendering |
| **CI/CD** | GitHub Actions | Automated testing and deployment |

### Timeline Estimate

| Phase | Duration | Cumulative |
|-------|----------|-----------|
| Phase 0: Repository Initialization | 3 days | Week 1 |
| Phase 1: Core Backend Infrastructure | 5 days | Week 1-2 |
| Phase 2: Ingestion Pipeline | 7 days | Week 2-3 |
| Phase 3: Summarization System | 5 days | Week 3-4 |
| Phase 4: Hybrid Retrieval | 7 days | Week 4-5 |
| Phase 5: Citation Verification | 7 days | Week 5-6 |
| Phase 6: Session Management | 5 days | Week 6-7 |
| Phase 7: Immutable Audit Trail | 4 days | Week 7 |
| Phase 8: Frontend Development | 14 days | Week 8-10 |
| Phase 9: Docker Deployment | 5 days | Week 10-11 |
| Phase 10: Pilot Validation | 5 days | Week 11-12 |
| **Total** | **67 days** | **~12 weeks** |

*Note: Timeline assumes 1 full-time developer. Parallel workstreams can reduce duration.*

### Success Criteria

**Functional Requirements:**
- ✅ All 10 phases completed with acceptance criteria validated
- ✅ COSMOLOGY repository fully indexed (README.md → embeddings → summaries)
- ✅ Hybrid retrieval returns contextually relevant results for 5 predefined queries
- ✅ Citation verifier achieves ≥90% pass rate on ground truth dataset
- ✅ Session rehydration reconstructs context with ≥95% semantic overlap
- ✅ All API endpoints respond with correct status codes and schemas

**Performance Benchmarks:**
- ✅ Ingestion throughput: ≥50 chunks/minute (including embeddings)
- ✅ Query latency: median ≤300ms, p95 ≤800ms, p99 ≤1.5s
- ✅ Rehydration speed: ≤2s for 20-chunk context window
- ✅ Verifier execution: ≤500ms per claim

**Operational Requirements:**
- ✅ Docker Compose deployment successful on clean Ubuntu 22.04 host
- ✅ Frontend accessible at http://localhost:3000 with all pages functional
- ✅ Health checks passing for all services (Postgres, Redis, MinIO, Backend, Frontend)
- ✅ Unit test coverage ≥80% for core modules (chunker, retrieval, verifier)
- ✅ Integration tests passing for end-to-end workflows
- ✅ Documentation complete (API reference, deployment guide, user manual)

---

## Phase Breakdown

---

## PHASE 0: Repository Initialization & Project Scaffolding

**Duration:** 3 days  
**Dependencies:** None  
**Risk Level:** Low  

### Objectives

1. Establish repository structure following best practices (monorepo with backend/frontend separation)
2. Configure development environment with reproducible tooling
3. Set up CI/CD pipeline for automated testing
4. Initialize version control with appropriate .gitignore patterns
5. Create baseline documentation and contribution guidelines

### Deliverables

**Repository Structure:**
```
COSMOLOGY/
├── README.md                          # Project overview, setup instructions
├── PROJECT_PLAN.md                    # This document
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
├── .gitignore                         # Exclude .env, __pycache__, node_modules, etc.
├── .env.example                       # Template for environment variables
├── docker-compose.yml                 # Multi-service orchestration
├── docker-compose.dev.yml             # Dev overrides (hot reload, debug ports)
├── .github/
│   └── workflows/
│       ├── ci.yml                     # Run tests on push/PR
│       └── deploy.yml                 # CD pipeline (future)
├── backend/
│   ├── Dockerfile                     # Python 3.12 slim image
│   ├── Dockerfile.dev                 # Dev image with debugpy
│   ├── requirements.txt               # Pinned dependencies
│   ├── requirements-dev.txt           # Testing/linting tools
│   ├── alembic.ini                    # Database migration config
│   ├── pytest.ini                     # Test configuration
│   ├── .coveragerc                    # Coverage settings
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI application entry point
│   │   ├── config.py                  # Pydantic settings
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── ingest.py          # Ingestion endpoints
│   │   │       ├── query.py           # Search endpoints
│   │   │       ├── session.py         # Session management
│   │   │       ├── verify.py          # Citation verification
│   │   │       └── audit.py           # Audit log queries
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── chunker.py             # Text segmentation
│   │   │   ├── embeddings.py          # Vector generation
│   │   │   ├── indexer.py             # FAISS + Whoosh
│   │   │   ├── retrieval.py           # Hybrid search
│   │   │   ├── summarizer.py          # LLM summarization
│   │   │   ├── verifier.py            # Citation validation
│   │   │   └── checkpoint.py          # Session state
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── models.py              # SQLAlchemy ORM models
│   │   │   ├── session.py             # Database connection
│   │   │   └── migrations/            # Alembic versions
│   │   ├── storage/
│   │   │   ├── __init__.py
│   │   │   └── s3_client.py           # Boto3 wrapper
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── audit_log.py           # JSONL logger
│   │       └── helpers.py             # Shared utilities
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py                # Pytest fixtures
│       ├── test_ingest.py
│       ├── test_retrieval.py
│       ├── test_verifier.py
│       └── test_session.py
├── frontend/
│   ├── Dockerfile                     # Node.js Alpine image
│   ├── Dockerfile.dev                 # Dev mode with hot reload
│   ├── package.json                   # NPM dependencies
│   ├── package-lock.json
│   ├── next.config.js                 # Next.js configuration
│   ├── tailwind.config.js             # Tailwind customization
│   ├── postcss.config.js              # PostCSS setup
│   ├── tsconfig.json                  # TypeScript config
│   ├── .eslintrc.json                 # Linting rules
│   ├── app/
│   │   ├── layout.tsx                 # Root layout
│   │   ├── page.tsx                   # Homepage
│   │   ├── globals.css                # Tailwind imports
│   │   ├── dashboard/
│   │   │   └── page.tsx               # Metrics dashboard
│   │   ├── repositories/
│   │   │   └── page.tsx               # Repo manager
│   │   ├── query/
│   │   │   └── page.tsx               # Search interface
│   │   ├── graph/
│   │   │   └── page.tsx               # Knowledge graph
│   │   ├── sessions/
│   │   │   └── page.tsx               # Session manager
│   │   ├── audit/
│   │   │   └── page.tsx               # Audit log viewer
│   │   └── verifier/
│   │       └── page.tsx               # Verifier dashboard
│   ├── components/
│   │   ├── ui/                        # shadcn components
│   │   ├── CitationBadge.tsx
│   │   ├── ChunkViewer.tsx
│   │   ├── VerifierReport.tsx
│   │   ├── MetricsCard.tsx
│   │   └── KnowledgeGraph.tsx
│   ├── lib/
│   │   ├── api-client.ts              # Fetch wrapper
│   │   └── utils.ts                   # Shared helpers
│   └── public/
│       ├── favicon.ico
│       └── logo.svg
└── docs/
    ├── mkdocs.yml                     # Documentation site config
    ├── index.md                       # Landing page
    ├── api-reference.md               # OpenAPI spec
    ├── deployment.md                  # Deployment guide
    ├── architecture.md                # System design
    └── user-guide.md                  # End-user documentation
```

**Configuration Files:**

1. **`.env.example`** (Environment template):
```env
# Database
POSTGRES_USER=cosmology
POSTGRES_PASSWORD=changeme
POSTGRES_DB=greds_library
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=

# S3 Storage
S3_ENDPOINT_URL=http://minio:9000
S3_ACCESS_KEY_ID=minioadmin
S3_SECRET_ACCESS_KEY=minioadmin
S3_BUCKET_NAME=greds-audit-logs
S3_REGION=us-east-1

# Abacus.AI
ABACUSAI_API_KEY=your_api_key_here
ABACUSAI_MODEL_ID=gpt-4-turbo

# Application
BACKEND_CORS_ORIGINS=http://localhost:3000
LOG_LEVEL=INFO
RANDOM_SEED=42

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

2. **`docker-compose.yml`** (Base configuration):
```yaml
version: '3.9'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: ${S3_ACCESS_KEY_ID}
      MINIO_ROOT_PASSWORD: ${S3_SECRET_ACCESS_KEY}
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - minio_data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      POSTGRES_HOST: postgres
      REDIS_HOST: redis
      S3_ENDPOINT_URL: http://minio:9000
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      minio:
        condition: service_healthy
    volumes:
      - ./backend:/app
      - faiss_indexes:/app/data/faiss
      - whoosh_indexes:/app/data/whoosh
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: http://backend:8000/api/v1
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - /app/.next
    command: npm run dev

volumes:
  postgres_data:
  redis_data:
  minio_data:
  faiss_indexes:
  whoosh_indexes:
```

3. **`.github/workflows/ci.yml`** (CI Pipeline):
```yaml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python 3.12
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt -r requirements-dev.txt
      - name: Run linting
        run: |
          cd backend
          flake8 app/ --max-line-length=120
          black --check app/
      - name: Run tests with coverage
        env:
          POSTGRES_HOST: localhost
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        run: |
          cd backend
          pytest --cov=app --cov-report=xml --cov-report=term
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: |
          cd frontend
          npm ci
      - name: Run linting
        run: |
          cd frontend
          npm run lint
      - name: Run type checking
        run: |
          cd frontend
          npm run type-check
      - name: Build
        run: |
          cd frontend
          npm run build
```

4. **`backend/requirements.txt`** (Python dependencies):
```txt
# Core Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0

# Database
sqlalchemy==2.0.23
alembic==1.12.1
psycopg2-binary==2.9.9

# Vector & Search
faiss-cpu==1.7.4
whoosh==2.7.4
sentence-transformers==2.2.2

# Storage & Queue
boto3==1.29.7
redis==5.0.1
rq==1.15.1

# HTTP & Utilities
httpx==0.25.2
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4

# Logging & Monitoring
structlog==23.2.0
```

5. **`frontend/package.json`** (Node dependencies):
```json
{
  "name": "greds-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit"
  },
  "dependencies": {
    "next": "14.0.4",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "tailwindcss": "3.3.6",
    "autoprefixer": "10.4.16",
    "postcss": "8.4.32",
    "@radix-ui/react-dialog": "^1.0.5",
    "@radix-ui/react-dropdown-menu": "^2.0.6",
    "@radix-ui/react-label": "^2.0.2",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-tabs": "^1.0.4",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "d3": "^7.8.5",
    "lucide-react": "^0.294.0",
    "react-flow-renderer": "^10.3.17",
    "tailwind-merge": "^2.1.0"
  },
  "devDependencies": {
    "@types/node": "20.10.4",
    "@types/react": "18.2.42",
    "@types/react-dom": "18.2.17",
    "@types/d3": "^7.4.3",
    "eslint": "8.55.0",
    "eslint-config-next": "14.0.4",
    "typescript": "5.3.3"
  }
}
```

### Acceptance Criteria

**✅ Repository Structure:**
- [ ] All directories and base files created as specified
- [ ] `.gitignore` excludes sensitive files (.env, __pycache__, node_modules, .next)
- [ ] `.env.example` contains all required variables with descriptions

**✅ Backend Scaffolding:**
- [ ] `backend/requirements.txt` lists all core dependencies
- [ ] Empty module files created with proper `__init__.py`
- [ ] `backend/Dockerfile` builds successfully
- [ ] Alembic initialized: `alembic init migrations` executed

**✅ Frontend Scaffolding:**
- [ ] Next.js 14 project initialized with App Router
- [ ] Tailwind CSS and PostCSS configured
- [ ] shadcn/ui CLI installed: `npx shadcn-ui@latest init`
- [ ] `frontend/Dockerfile` builds successfully

**✅ Docker Orchestration:**
- [ ] `docker-compose.yml` defines all 5 services (postgres, redis, minio, backend, frontend)
- [ ] All services start successfully: `docker-compose up -d`
- [ ] Health checks pass for postgres, redis, minio within 60 seconds
- [ ] Backend accessible at http://localhost:8000
- [ ] Frontend accessible at http://localhost:3000

**✅ CI/CD Pipeline:**
- [ ] GitHub Actions workflow file created
- [ ] Workflow triggers on push to main/develop branches
- [ ] Linting and type checking steps defined (will pass with empty codebase)

**✅ Documentation:**
- [ ] `README.md` includes project description, setup instructions, architecture diagram
- [ ] `CONTRIBUTING.md` outlines code style, PR process, testing requirements

### Technical Specifications

**Python Version:** 3.12+  
**Node.js Version:** 18 LTS  
**PostgreSQL Version:** 15+  
**Docker Compose Version:** 3.9  

**Directory Permissions:**
- Backend source: 755 for directories, 644 for files
- Frontend source: 755 for directories, 644 for files
- Docker volumes: Managed by Docker daemon

**Naming Conventions:**
- Python: `snake_case` for files, functions, variables; `PascalCase` for classes
- TypeScript: `camelCase` for variables/functions; `PascalCase` for components/types; `kebab-case` for files
- SQL: `snake_case` for tables and columns

### Testing Requirements

**Manual Tests:**
1. Clone repository to fresh environment
2. Copy `.env.example` to `.env` and fill credentials
3. Run `docker-compose up -d`
4. Verify all services healthy: `docker-compose ps`
5. Access backend health endpoint: `curl http://localhost:8000/health`
6. Access frontend: Open http://localhost:3000 in browser
7. Stop services: `docker-compose down`

**Automated Tests:**
- CI pipeline should run successfully on empty codebase (linting passes with no files)

### Dependencies & Prerequisites

**Development Machine Requirements:**
- Docker 20.10+ with Compose plugin
- Git 2.30+
- Text editor (VSCode recommended with extensions: Python, ESLint, Prettier)
- 8GB RAM minimum (16GB recommended for running all services)
- 20GB free disk space

**External Services:**
- GitHub account for version control
- Abacus.AI account with API key (for Phase 3)

### Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Docker networking issues on Windows/Mac | High | Medium | Provide platform-specific docker-compose overrides |
| Port conflicts (3000, 8000, 5432 already in use) | Medium | High | Document how to change ports in .env |
| Large dependency download time | Low | High | Pre-build Docker images, use layer caching |

---

## PHASE 1: Core Backend Infrastructure

**Duration:** 5 days  
**Dependencies:** Phase 0 complete  
**Risk Level:** Low  

### Objectives

1. Define PostgreSQL database schema for all data models
2. Implement SQLAlchemy ORM models with relationships
3. Create database migration system with Alembic
4. Build S3 storage client for artifact management
5. Set up FastAPI application with CORS, middleware, health checks
6. Implement Pydantic settings for configuration management

### Deliverables

#### 1. Database Models (`backend/app/db/models.py`)

**Schema Design:**

```python
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, JSON, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Work(Base):
    """Represents a research artifact (paper, README, etc.)"""
    __tablename__ = "works"
    
    id = Column(Integer, primary_key=True)
    source_slug = Column(String(255), unique=True, nullable=False, index=True)
    version = Column(String(50), nullable=False)
    canonical_url = Column(String(512), nullable=False)
    title = Column(String(512))
    authors = Column(JSON)  # List of author names
    publication_date = Column(DateTime)
    tags = Column(JSON)  # List of tags
    file_format = Column(String(20))  # pdf, md, html
    s3_raw_path = Column(String(512))  # S3 key for original file
    ingestion_status = Column(String(20), default="pending")  # pending, processing, completed, failed
    ingestion_started_at = Column(DateTime)
    ingestion_completed_at = Column(DateTime)
    total_chunks = Column(Integer, default=0)
    metadata = Column(JSON)  # Additional metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    chunks = relationship("Chunk", back_populates="work", cascade="all, delete-orphan")
    
    __table_args__ = (
        Index('idx_work_slug_version', 'source_slug', 'version'),
    )

class Chunk(Base):
    """Text segments from works"""
    __tablename__ = "chunks"
    
    id = Column(Integer, primary_key=True)
    work_id = Column(Integer, ForeignKey("works.id"), nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)  # 0-based position in work
    text = Column(Text, nullable=False)
    token_count = Column(Integer)
    start_char = Column(Integer)
    end_char = Column(Integer)
    chunk_hash = Column(String(64), unique=True, index=True)  # SHA256 of text
    chunking_strategy = Column(String(50))  # "fixed_tokens_with_overlap"
    chunking_params = Column(JSON)  # {chunk_size: 1024, overlap: 0.2, seed: 42}
    created_at = Column(DateTime, default=datetime.utcnow)
    
    work = relationship("Work", back_populates="chunks")
    embedding = relationship("Embedding", uselist=False, back_populates="chunk", cascade="all, delete-orphan")
    summaries = relationship("Summary", back_populates="chunk", cascade="all, delete-orphan")
    citations = relationship("Citation", back_populates="chunk")
    
    __table_args__ = (
        Index('idx_chunk_work_index', 'work_id', 'chunk_index'),
    )

class Embedding(Base):
    """Vector embeddings for semantic search"""
    __tablename__ = "embeddings"
    
    id = Column(Integer, primary_key=True)
    chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=False, unique=True, index=True)
    model_name = Column(String(100), nullable=False)  # "all-MiniLM-L6-v2"
    model_version = Column(String(50))
    vector_dim = Column(Integer)  # 384 for MiniLM
    embedding_hash = Column(String(64))  # Hash of vector for deduplication
    faiss_index_id = Column(Integer)  # Position in FAISS index
    created_at = Column(DateTime, default=datetime.utcnow)
    
    chunk = relationship("Chunk", back_populates="embedding")

class Summary(Base):
    """Three-level summaries for chunks"""
    __tablename__ = "summaries"
    
    id = Column(Integer, primary_key=True)
    chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=False, index=True)
    summary_level = Column(String(20), nullable=False)  # short, medium, long
    summary_text = Column(Text, nullable=False)
    char_count = Column(Integer)
    llm_model = Column(String(100))  # "gpt-4-turbo"
    prompt_hash = Column(String(64))  # Hash of prompt template
    temperature = Column(Float)  # 0.2
    created_at = Column(DateTime, default=datetime.utcnow)
    
    chunk = relationship("Chunk", back_populates="summaries")
    
    __table_args__ = (
        Index('idx_summary_chunk_level', 'chunk_id', 'summary_level'),
    )

class Session(Base):
    """User interaction sessions with state management"""
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String(64), unique=True, nullable=False, index=True)
    user_id = Column(String(255))  # Optional user identifier
    condensed_summary = Column(Text)  # Aggregated context
    accepted_claims = Column(JSON)  # List of verified claims
    top_citations = Column(JSON)  # Top 10-20 chunk IDs
    parent_checkpoint_id = Column(Integer, ForeignKey("sessions.id"), nullable=True)
    is_checkpoint = Column(Boolean, default=False)
    checkpoint_name = Column(String(255))
    state_json = Column(JSON)  # Full serialized state
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    checkpoints = relationship("Session", remote_side=[id])

class Citation(Base):
    """Links between queries/claims and chunks"""
    __tablename__ = "citations"
    
    id = Column(Integer, primary_key=True)
    chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=False, index=True)
    retrieval_id = Column(String(255), nullable=False)  # "slug:version:chunk_id"
    query_text = Column(Text)
    claim_text = Column(Text)
    similarity_score = Column(Float)
    verifier_decision = Column(String(20))  # pass, partial, fail
    context_window = Column(JSON)  # Adjacent chunk IDs
    created_at = Column(DateTime, default=datetime.utcnow)
    
    chunk = relationship("Chunk", back_populates="citations")
    
    __table_args__ = (
        Index('idx_citation_retrieval', 'retrieval_id'),
    )

class AuditLog(Base):
    """Database-backed audit events (complementary to JSONL logs)"""
    __tablename__ = "audit_log"
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    event_type = Column(String(50), nullable=False, index=True)  # retrieval, ingestion, verification, etc.
    correlation_id = Column(String(64), index=True)  # Links related events
    user_id = Column(String(255))
    action = Column(String(255))
    resource_type = Column(String(100))
    resource_id = Column(String(255))
    metadata = Column(JSON)
    status = Column(String(20))  # success, failure
    error_message = Column(Text)
    duration_ms = Column(Integer)
```

**Indexes:**
- `works`: `source_slug`, `(source_slug, version)`, `ingestion_status`
- `chunks`: `work_id`, `(work_id, chunk_index)`, `chunk_hash`
- `embeddings`: `chunk_id`, `faiss_index_id`
- `summaries`: `chunk_id`, `(chunk_id, summary_level)`
- `citations`: `chunk_id`, `retrieval_id`
- `sessions`: `session_id`
- `audit_log`: `timestamp`, `event_type`, `correlation_id`

#### 2. Database Session Management (`backend/app/db/session.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Verify connections before use
    echo=settings.DEBUG,  # Log SQL in debug mode
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """Dependency for FastAPI routes"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### 3. Alembic Migrations (`backend/alembic/versions/001_initial_schema.py`)

```python
"""Initial schema

Revision ID: 001
Create Date: 2025-10-24
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create works table
    op.create_table(
        'works',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('source_slug', sa.String(255), nullable=False),
        sa.Column('version', sa.String(50), nullable=False),
        # ... (full schema as per models.py)
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('source_slug', name='uq_work_slug')
    )
    op.create_index('idx_work_slug_version', 'works', ['source_slug', 'version'])
    
    # Create chunks, embeddings, summaries, sessions, citations, audit_log
    # ... (repeat for all tables)

def downgrade():
    op.drop_table('audit_log')
    op.drop_table('citations')
    op.drop_table('sessions')
    op.drop_table('summaries')
    op.drop_table('embeddings')
    op.drop_table('chunks')
    op.drop_table('works')
```

#### 4. S3 Storage Client (`backend/app/storage/s3_client.py`)

```python
import boto3
from botocore.client import Config
from typing import BinaryIO, Optional
from app.config import settings
import structlog

logger = structlog.get_logger()

class S3Client:
    def __init__(self):
        self.client = boto3.client(
            's3',
            endpoint_url=settings.S3_ENDPOINT_URL,
            aws_access_key_id=settings.S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.S3_SECRET_ACCESS_KEY,
            region_name=settings.S3_REGION,
            config=Config(signature_version='s3v4')
        )
        self.bucket = settings.S3_BUCKET_NAME
        self._ensure_bucket()
    
    def _ensure_bucket(self):
        """Create bucket if it doesn't exist"""
        try:
            self.client.head_bucket(Bucket=self.bucket)
        except:
            self.client.create_bucket(Bucket=self.bucket)
            logger.info("Created S3 bucket", bucket=self.bucket)
    
    def upload_file(self, file_obj: BinaryIO, key: str, metadata: Optional[dict] = None):
        """Upload file object to S3"""
        extra_args = {'Metadata': metadata} if metadata else {}
        self.client.upload_fileobj(file_obj, self.bucket, key, ExtraArgs=extra_args)
        logger.info("Uploaded file to S3", key=key)
    
    def download_file(self, key: str) -> bytes:
        """Download file from S3"""
        response = self.client.get_object(Bucket=self.bucket, Key=key)
        return response['Body'].read()
    
    def upload_json(self, data: dict, key: str):
        """Upload JSON data"""
        import json
        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=json.dumps(data).encode('utf-8'),
            ContentType='application/json'
        )
    
    def append_jsonl(self, data: dict, key: str):
        """Append JSONL entry (for audit logs)"""
        import json
        entry = json.dumps(data) + '\n'
        
        # Try to append to existing file
        try:
            existing = self.download_file(key).decode('utf-8')
            content = existing + entry
        except self.client.exceptions.NoSuchKey:
            content = entry
        
        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=content.encode('utf-8'),
            ContentType='application/x-ndjson'
        )

s3_client = S3Client()
```

#### 5. Pydantic Settings (`backend/app/config.py`)

```python
from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn
from typing import List

class Settings(BaseSettings):
    # Database
    POSTGRES_USER: str = Field("cosmology")
    POSTGRES_PASSWORD: str = Field("changeme")
    POSTGRES_DB: str = Field("greds_library")
    POSTGRES_HOST: str = Field("postgres")
    POSTGRES_PORT: int = Field(5432)
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # Redis
    REDIS_HOST: str = Field("redis")
    REDIS_PORT: int = Field(6379)
    REDIS_PASSWORD: str = Field("")
    
    @property
    def REDIS_URL(self) -> str:
        auth = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"redis://{auth}{self.REDIS_HOST}:{self.REDIS_PORT}/0"
    
    # S3
    S3_ENDPOINT_URL: str = Field("http://minio:9000")
    S3_ACCESS_KEY_ID: str = Field("minioadmin")
    S3_SECRET_ACCESS_KEY: str = Field("minioadmin")
    S3_BUCKET_NAME: str = Field("greds-audit-logs")
    S3_REGION: str = Field("us-east-1")
    
    # Abacus.AI
    ABACUSAI_API_KEY: str = Field(..., description="Required API key")
    ABACUSAI_MODEL_ID: str = Field("gpt-4-turbo")
    
    # Application
    BACKEND_CORS_ORIGINS: List[str] = Field(["http://localhost:3000"])
    LOG_LEVEL: str = Field("INFO")
    DEBUG: bool = Field(False)
    RANDOM_SEED: int = Field(42)
    
    # Embeddings
    EMBEDDING_MODEL: str = Field("sentence-transformers/all-MiniLM-L6-v2")
    EMBEDDING_DIM: int = Field(384)
    
    # Chunking
    CHUNK_SIZE: int = Field(1024)
    CHUNK_OVERLAP: float = Field(0.2)
    
    # Retrieval
    SEMANTIC_WEIGHT: float = Field(0.7)
    LEXICAL_WEIGHT: float = Field(0.3)
    TOP_K: int = Field(20)
    
    # Verification
    VERIFIER_PASS_THRESHOLD: float = Field(0.80)
    VERIFIER_PARTIAL_THRESHOLD: float = Field(0.75)
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

#### 6. FastAPI Application (`backend/app/main.py`)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import structlog

from app.config import settings
from app.db.session import engine
from app.db.models import Base
from app.api.v1 import ingest, query, session, verify, audit

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
)

logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    logger.info("Application startup", version="0.1.0")
    
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    yield
    
    logger.info("Application shutdown")

app = FastAPI(
    title="GREDs AI Reference Library",
    description="Hybrid retrieval and citation verification system",
    version="0.1.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "0.1.0",
        "database": "connected",  # TODO: Add actual DB health check
        "redis": "connected",      # TODO: Add actual Redis health check
        "s3": "connected"          # TODO: Add actual S3 health check
    }

# API Routers
app.include_router(ingest.router, prefix="/api/v1/ingest", tags=["Ingestion"])
app.include_router(query.router, prefix="/api/v1/query", tags=["Query"])
app.include_router(session.router, prefix="/api/v1/session", tags=["Session"])
app.include_router(verify.router, prefix="/api/v1/verify", tags=["Verification"])
app.include_router(audit.router, prefix="/api/v1/audit", tags=["Audit"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Acceptance Criteria

**✅ Database Models:**
- [ ] All 7 tables defined (works, chunks, embeddings, summaries, sessions, citations, audit_log)
- [ ] Foreign key relationships correctly specified
- [ ] Indexes created for frequently queried columns
- [ ] JSON columns used for flexible metadata storage

**✅ Database Connectivity:**
- [ ] Alembic migrations run successfully: `alembic upgrade head`
- [ ] Tables visible in PostgreSQL: `psql -U cosmology -d greds_library -c '\dt'`
- [ ] Can insert and query test records

**✅ S3 Client:**
- [ ] MinIO bucket created automatically on first run
- [ ] File upload succeeds: `s3_client.upload_json({"test": "data"}, "test.json")`
- [ ] File download succeeds: `s3_client.download_file("test.json")`
- [ ] JSONL append works for audit logs

**✅ FastAPI Application:**
- [ ] Server starts without errors: `uvicorn app.main:app --reload`
- [ ] Health endpoint returns 200: `curl http://localhost:8000/health`
- [ ] OpenAPI docs accessible: http://localhost:8000/docs
- [ ] CORS headers present in responses

**✅ Configuration Management:**
- [ ] Environment variables loaded from .env
- [ ] Settings accessible: `from app.config import settings; print(settings.DATABASE_URL)`
- [ ] Validation fails for missing required fields (e.g., ABACUSAI_API_KEY)

### Technical Specifications

**SQLAlchemy ORM:**
- Relationships use `back_populates` for bidirectional navigation
- Cascade delete enabled for dependent entities (chunks → embeddings, summaries)
- `pool_pre_ping=True` to handle stale connections

**Alembic Configuration:**
- `sqlalchemy.url` in `alembic.ini` reads from environment
- Migration scripts auto-generated: `alembic revision --autogenerate -m "message"`
- Target metadata: `from app.db.models import Base; target_metadata = Base.metadata`

**S3 Compatibility:**
- Works with both MinIO (local) and AWS S3 (production)
- Uses path-style addressing for MinIO compatibility
- Object locking enabled for immutable audit logs (production only)

### Testing Requirements

**Unit Tests (`backend/tests/test_db_models.py`):**
```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base, Work, Chunk

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_work_creation(db_session):
    work = Work(
        source_slug="test-paper",
        version="v1",
        canonical_url="https://example.com/paper.pdf"
    )
    db_session.add(work)
    db_session.commit()
    
    assert work.id is not None
    assert work.source_slug == "test-paper"

def test_chunk_relationship(db_session):
    work = Work(source_slug="test", version="v1", canonical_url="http://test")
    chunk = Chunk(work=work, chunk_index=0, text="Sample text", token_count=2)
    
    db_session.add(work)
    db_session.commit()
    
    assert len(work.chunks) == 1
    assert chunk.work_id == work.id
```

**Integration Tests:**
```python
def test_s3_upload_download():
    from app.storage.s3_client import s3_client
    
    test_data = {"message": "Hello S3"}
    s3_client.upload_json(test_data, "test/data.json")
    
    downloaded = s3_client.download_file("test/data.json")
    assert json.loads(downloaded) == test_data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

### Dependencies

**Python Packages:**
- SQLAlchemy 2.0+ (async support)
- Alembic for migrations
- psycopg2-binary for PostgreSQL driver
- boto3 for S3 operations
- FastAPI + Uvicorn for web framework
- Pydantic for data validation
- structlog for JSON logging

**External Services:**
- PostgreSQL 15+ running and accessible
- Redis running (for Phase 2 job queue)
- MinIO/S3 accessible
- Network connectivity between services

### Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Database schema changes requiring backfill | Use Alembic's batch operations; test migrations on staging data |
| S3 connectivity issues | Implement retry logic with exponential backoff; cache frequently accessed objects |
| Large JSONB columns causing slow queries | Add GIN indexes on JSONB columns; consider separate table for very large metadata |

---

## PHASE 2: Ingestion Pipeline

**Duration:** 7 days  
**Dependencies:** Phase 1 complete  
**Risk Level:** Medium  

### Objectives

1. Implement deterministic text chunking with fixed token sizes and overlap
2. Integrate sentence-transformers for embedding generation
3. Create FAISS vector index for semantic search
4. Build Whoosh BM25 index for lexical search
5. Develop repository cloning and text extraction logic
6. Create background job queue for async ingestion
7. Build API endpoints for initiating and monitoring ingestion

### Deliverables

#### 1. Text Chunker (`backend/app/core/chunker.py`)

```python
import hashlib
import tiktoken
from typing import List, Dict
from dataclasses import dataclass
import random

@dataclass
class TextChunk:
    text: str
    chunk_index: int
    start_char: int
    end_char: int
    token_count: int
    chunk_hash: str

class DeterministicChunker:
    """
    Chunks text into fixed-size segments with overlap.
    Reproducible with seed for consistent hashing.
    """
    
    def __init__(self, chunk_size: int = 1024, overlap: float = 0.2, seed: int = 42):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.seed = seed
        self.encoder = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer
        random.seed(seed)
    
    def chunk_text(self, text: str) -> List[TextChunk]:
        """
        Split text into overlapping chunks of fixed token size.
        
        Algorithm:
        1. Tokenize entire text
        2. Create sliding windows of chunk_size tokens
        3. Step size = chunk_size * (1 - overlap)
        4. Convert tokens back to text for each chunk
        5. Calculate character positions
        """
        tokens = self.encoder.encode(text)
        step_size = int(self.chunk_size * (1 - self.overlap))
        
        chunks = []
        char_offset = 0
        
        for i in range(0, len(tokens), step_size):
            chunk_tokens = tokens[i:i + self.chunk_size]
            chunk_text = self.encoder.decode(chunk_tokens)
            
            # Calculate character positions
            start_char = char_offset
            end_char = start_char + len(chunk_text)
            char_offset = end_char - int(len(chunk_text) * self.overlap)  # Approximate overlap
            
            # Deterministic hash
            chunk_hash = hashlib.sha256(
                f"{chunk_text}{self.seed}".encode('utf-8')
            ).hexdigest()
            
            chunks.append(TextChunk(
                text=chunk_text,
                chunk_index=len(chunks),
                start_char=start_char,
                end_char=end_char,
                token_count=len(chunk_tokens),
                chunk_hash=chunk_hash
            ))
            
            if i + self.chunk_size >= len(tokens):
                break
        
        return chunks
    
    def get_metadata(self) -> Dict:
        """Return chunking configuration for storage"""
        return {
            "chunk_size": self.chunk_size,
            "overlap": self.overlap,
            "seed": self.seed,
            "strategy": "fixed_tokens_with_overlap",
            "tokenizer": "cl100k_base"
        }
```

#### 2. Embedding Generator (`backend/app/core/embeddings.py`)

```python
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List
import hashlib
import structlog

logger = structlog.get_logger()

class EmbeddingGenerator:
    """
    Generates vector embeddings using sentence-transformers.
    Model: all-MiniLM-L6-v2 (384 dimensions)
    """
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.vector_dim = self.model.get_sentence_embedding_dimension()
        logger.info("Loaded embedding model", model=model_name, dim=self.vector_dim)
    
    def embed_text(self, text: str) -> np.ndarray:
        """Generate embedding for single text"""
        return self.model.encode(text, convert_to_numpy=True)
    
    def embed_batch(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        """Generate embeddings for multiple texts efficiently"""
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        return embeddings
    
    def hash_embedding(self, embedding: np.ndarray) -> str:
        """Create deterministic hash of embedding vector"""
        # Round to 6 decimals for consistency
        rounded = np.round(embedding, decimals=6)
        return hashlib.sha256(rounded.tobytes()).hexdigest()
    
    def get_metadata(self) -> Dict:
        """Return model configuration"""
        return {
            "model_name": self.model_name,
            "vector_dim": self.vector_dim,
            "model_version": self.model.model_card_data.model_id if hasattr(self.model, 'model_card_data') else "unknown"
        }
```

#### 3. FAISS Indexer (`backend/app/core/indexer.py`)

```python
import faiss
import numpy as np
from pathlib import Path
import pickle
from typing import List, Dict, Optional
import structlog

logger = structlog.get_logger()

class FAISSIndexer:
    """
    Manages FAISS index for semantic similarity search.
    Uses IndexFlatIP (inner product) for cosine similarity after L2 normalization.
    """
    
    def __init__(self, vector_dim: int = 384, index_path: str = "/app/data/faiss"):
        self.vector_dim = vector_dim
        self.index_path = Path(index_path)
        self.index_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize FAISS index
        self.index = faiss.IndexFlatIP(vector_dim)  # Inner product for cosine similarity
        self.id_mapping = {}  # faiss_index_id -> chunk_id
        self.next_id = 0
        
        logger.info("Initialized FAISS index", dim=vector_dim)
    
    def add_embedding(self, chunk_id: int, embedding: np.ndarray) -> int:
        """
        Add single embedding to index.
        Returns FAISS index ID.
        """
        # Normalize for cosine similarity
        normalized = embedding / np.linalg.norm(embedding)
        normalized = normalized.reshape(1, -1).astype('float32')
        
        faiss_id = self.next_id
        self.index.add(normalized)
        self.id_mapping[faiss_id] = chunk_id
        self.next_id += 1
        
        return faiss_id
    
    def add_batch(self, chunk_ids: List[int], embeddings: np.ndarray) -> List[int]:
        """
        Add multiple embeddings efficiently.
        Returns list of FAISS index IDs.
        """
        # Normalize all embeddings
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        normalized = (embeddings / norms).astype('float32')
        
        start_id = self.next_id
        self.index.add(normalized)
        
        faiss_ids = list(range(start_id, start_id + len(chunk_ids)))
        for faiss_id, chunk_id in zip(faiss_ids, chunk_ids):
            self.id_mapping[faiss_id] = chunk_id
        
        self.next_id += len(chunk_ids)
        
        logger.info("Added batch to FAISS", count=len(chunk_ids), total=self.next_id)
        return faiss_ids
    
    def search(self, query_embedding: np.ndarray, k: int = 20) -> List[Dict]:
        """
        Find k nearest neighbors.
        Returns list of {chunk_id, score}.
        """
        # Normalize query
        normalized = query_embedding / np.linalg.norm(query_embedding)
        normalized = normalized.reshape(1, -1).astype('float32')
        
        distances, indices = self.index.search(normalized, k)
        
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx != -1:  # FAISS returns -1 for empty slots
                results.append({
                    "chunk_id": self.id_mapping[idx],
                    "score": float(dist)  # Cosine similarity (0-1)
                })
        
        return results
    
    def save(self, name: str = "index"):
        """Persist index and mappings to disk"""
        index_file = self.index_path / f"{name}.faiss"
        mapping_file = self.index_path / f"{name}_mapping.pkl"
        
        faiss.write_index(self.index, str(index_file))
        with open(mapping_file, 'wb') as f:
            pickle.dump({
                'id_mapping': self.id_mapping,
                'next_id': self.next_id
            }, f)
        
        logger.info("Saved FAISS index", path=str(index_file), vectors=self.next_id)
    
    def load(self, name: str = "index"):
        """Load index from disk"""
        index_file = self.index_path / f"{name}.faiss"
        mapping_file = self.index_path / f"{name}_mapping.pkl"
        
        if not index_file.exists():
            logger.warning("Index file not found", path=str(index_file))
            return False
        
        self.index = faiss.read_index(str(index_file))
        with open(mapping_file, 'rb') as f:
            data = pickle.load(f)
            self.id_mapping = data['id_mapping']
            self.next_id = data['next_id']
        
        logger.info("Loaded FAISS index", path=str(index_file), vectors=self.next_id)
        return True
```

#### 4. Whoosh BM25 Indexer (`backend/app/core/indexer.py` - continued)

```python
from whoosh import index
from whoosh.fields import Schema, TEXT, ID, NUMERIC
from whoosh.qparser import QueryParser
from whoosh.scoring import BM25F
import os

class WhooshIndexer:
    """
    Manages Whoosh index for BM25 lexical search.
    """
    
    def __init__(self, index_path: str = "/app/data/whoosh"):
        self.index_path = Path(index_path)
        self.index_path.mkdir(parents=True, exist_ok=True)
        
        # Define schema
        self.schema = Schema(
            chunk_id=ID(stored=True, unique=True),
            text=TEXT(stored=False),  # Don't store text, retrieve from DB
            work_slug=ID(stored=True),
            version=ID(stored=True),
            chunk_index=NUMERIC(stored=True)
        )
        
        # Create or open index
        if not index.exists_in(str(self.index_path)):
            self.ix = index.create_in(str(self.index_path), self.schema)
            logger.info("Created Whoosh index", path=str(self.index_path))
        else:
            self.ix = index.open_dir(str(self.index_path))
            logger.info("Opened existing Whoosh index", path=str(self.index_path))
    
    def add_document(self, chunk_id: int, text: str, work_slug: str, version: str, chunk_index: int):
        """Add single document to index"""
        writer = self.ix.writer()
        writer.add_document(
            chunk_id=str(chunk_id),
            text=text,
            work_slug=work_slug,
            version=version,
            chunk_index=chunk_index
        )
        writer.commit()
    
    def add_batch(self, documents: List[Dict]):
        """
        Add multiple documents efficiently.
        documents: [{chunk_id, text, work_slug, version, chunk_index}, ...]
        """
        writer = self.ix.writer()
        for doc in documents:
            writer.add_document(
                chunk_id=str(doc['chunk_id']),
                text=doc['text'],
                work_slug=doc['work_slug'],
                version=doc['version'],
                chunk_index=doc['chunk_index']
            )
        writer.commit()
        logger.info("Added batch to Whoosh", count=len(documents))
    
    def search(self, query_text: str, k: int = 20, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Search using BM25 ranking.
        filters: {work_slug: str, version: str}
        """
        with self.ix.searcher(weighting=BM25F()) as searcher:
            query_parser = QueryParser("text", self.ix.schema)
            query = query_parser.parse(query_text)
            
            # Apply filters if provided
            if filters:
                from whoosh.query import And, Term
                filter_queries = []
                if 'work_slug' in filters:
                    filter_queries.append(Term("work_slug", filters['work_slug']))
                if 'version' in filters:
                    filter_queries.append(Term("version", filters['version']))
                
                if filter_queries:
                    query = And([query] + filter_queries)
            
            results = searcher.search(query, limit=k)
            
            return [
                {
                    "chunk_id": int(hit['chunk_id']),
                    "score": hit.score,
                    "work_slug": hit['work_slug'],
                    "version": hit['version'],
                    "chunk_index": hit['chunk_index']
                }
                for hit in results
            ]
```

#### 5. Repository Extractor (`backend/app/core/extractor.py`)

```python
import git
import tempfile
import shutil
from pathlib import Path
from typing import Optional, Dict
import yaml
import PyPDF2
import markdown
import structlog

logger = structlog.get_logger()

class RepositoryExtractor:
    """
    Clones repositories and extracts text from various file formats.
    """
    
    def __init__(self, temp_dir: str = "/tmp/greds_repos"):
        self.temp_dir = Path(temp_dir)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def clone_repo(self, repo_url: str, branch: str = "main") -> Path:
        """Clone repository to temporary directory"""
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        clone_path = self.temp_dir / repo_name
        
        if clone_path.exists():
            shutil.rmtree(clone_path)
        
        logger.info("Cloning repository", url=repo_url, branch=branch)
        git.Repo.clone_from(repo_url, clone_path, branch=branch, depth=1)
        
        return clone_path
    
    def extract_text_from_pdf(self, pdf_path: Path) -> str:
        """Extract text from PDF file"""
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
        return text
    
    def extract_text_from_markdown(self, md_path: Path) -> str:
        """Extract text from Markdown (convert to plain text)"""
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        
        # Convert markdown to HTML then strip tags for plain text
        html = markdown.markdown(md_text)
        from html.parser import HTMLParser
        
        class MLStripper(HTMLParser):
            def __init__(self):
                super().__init__()
                self.strict = False
                self.convert_charrefs = True
                self.text = []
            def handle_data(self, d):
                self.text.append(d)
            def get_data(self):
                return ''.join(self.text)
        
        stripper = MLStripper()
        stripper.feed(html)
        return stripper.get_data()
    
    def load_metadata(self, repo_path: Path) -> Dict:
        """Load metadata.yaml if exists"""
        metadata_path = repo_path / "metadata.yaml"
        if metadata_path.exists():
            with open(metadata_path, 'r') as f:
                return yaml.safe_load(f)
        return {}
    
    def extract_work(self, repo_path: Path, target_file: str) -> Dict:
        """
        Extract text and metadata from a specific file in the repository.
        Returns: {text: str, metadata: dict}
        """
        file_path = repo_path / target_file
        
        if not file_path.exists():
            raise FileNotFoundError(f"Target file not found: {target_file}")
        
        # Determine file type and extract text
        if file_path.suffix == '.pdf':
            text = self.extract_text_from_pdf(file_path)
        elif file_path.suffix in ['.md', '.markdown']:
            text = self.extract_text_from_markdown(file_path)
        elif file_path.suffix in ['.txt', '.rst']:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")
        
        # Load metadata
        metadata = self.load_metadata(repo_path)
        
        logger.info("Extracted text", file=target_file, length=len(text))
        
        return {
            "text": text,
            "metadata": metadata,
            "file_format": file_path.suffix.lstrip('.')
        }
    
    def cleanup(self, repo_path: Path):
        """Remove cloned repository"""
        if repo_path.exists():
            shutil.rmtree(repo_path)
            logger.info("Cleaned up repository", path=str(repo_path))
```

#### 6. Ingestion Orchestrator (`backend/app/core/ingestion.py`)

```python
from sqlalchemy.orm import Session
from app.db.models import Work, Chunk, Embedding
from app.core.chunker import DeterministicChunker
from app.core.embeddings import EmbeddingGenerator
from app.core.indexer import FAISSIndexer, WhooshIndexer
from app.core.extractor import RepositoryExtractor
from app.storage.s3_client import s3_client
from datetime import datetime
import structlog

logger = structlog.get_logger()

class IngestionPipeline:
    """
    Orchestrates the full ingestion workflow:
    1. Clone repository
    2. Extract text from target file
    3. Chunk text deterministically
    4. Generate embeddings
    5. Build FAISS and Whoosh indexes
    6. Store in database and S3
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.chunker = DeterministicChunker()
        self.embedder = EmbeddingGenerator()
        self.faiss_indexer = FAISSIndexer()
        self.whoosh_indexer = WhooshIndexer()
        self.extractor = RepositoryExtractor()
    
    def ingest_work(
        self,
        repo_url: str,
        target_file: str,
        source_slug: str,
        version: str,
        branch: str = "main"
    ) -> int:
        """
        Full ingestion pipeline for a single work.
        Returns work_id.
        """
        logger.info("Starting ingestion", slug=source_slug, version=version)
        
        # Create work record
        work = Work(
            source_slug=source_slug,
            version=version,
            canonical_url=repo_url,
            ingestion_status="processing",
            ingestion_started_at=datetime.utcnow()
        )
        self.db.add(work)
        self.db.commit()
        
        try:
            # Step 1: Clone and extract
            repo_path = self.extractor.clone_repo(repo_url, branch)
            extracted = self.extractor.extract_work(repo_path, target_file)
            
            # Update work metadata
            work.title = extracted['metadata'].get('title')
            work.authors = extracted['metadata'].get('authors')
            work.tags = extracted['metadata'].get('tags')
            work.file_format = extracted['file_format']
            work.metadata = extracted['metadata']
            
            # Store raw file in S3
            with open(repo_path / target_file, 'rb') as f:
                s3_key = f"works/{source_slug}/{version}/original.{extracted['file_format']}"
                s3_client.upload_file(f, s3_key)
                work.s3_raw_path = s3_key
            
            # Step 2: Chunk text
            chunks = self.chunker.chunk_text(extracted['text'])
            logger.info("Chunked text", count=len(chunks))
            
            # Step 3: Generate embeddings (batch)
            chunk_texts = [c.text for c in chunks]
            embeddings = self.embedder.embed_batch(chunk_texts)
            
            # Step 4: Store chunks and embeddings in DB
            chunk_records = []
            embedding_records = []
            whoosh_docs = []
            
            for chunk_data, embedding_vector in zip(chunks, embeddings):
                # Create chunk record
                chunk_record = Chunk(
                    work_id=work.id,
                    chunk_index=chunk_data.chunk_index,
                    text=chunk_data.text,
                    token_count=chunk_data.token_count,
                    start_char=chunk_data.start_char,
                    end_char=chunk_data.end_char,
                    chunk_hash=chunk_data.chunk_hash,
                    chunking_strategy="fixed_tokens_with_overlap",
                    chunking_params=self.chunker.get_metadata()
                )
                self.db.add(chunk_record)
                self.db.flush()  # Get chunk.id
                
                chunk_records.append(chunk_record)
                
                # Add to FAISS
                faiss_id = self.faiss_indexer.add_embedding(chunk_record.id, embedding_vector)
                
                # Create embedding record
                embedding_record = Embedding(
                    chunk_id=chunk_record.id,
                    model_name=self.embedder.model_name,
                    vector_dim=self.embedder.vector_dim,
                    embedding_hash=self.embedder.hash_embedding(embedding_vector),
                    faiss_index_id=faiss_id
                )
                self.db.add(embedding_record)
                embedding_records.append(embedding_record)
                
                # Prepare for Whoosh
                whoosh_docs.append({
                    'chunk_id': chunk_record.id,
                    'text': chunk_data.text,
                    'work_slug': source_slug,
                    'version': version,
                    'chunk_index': chunk_data.chunk_index
                })
            
            # Step 5: Add to Whoosh index
            self.whoosh_indexer.add_batch(whoosh_docs)
            
            # Update work record
            work.total_chunks = len(chunks)
            work.ingestion_status = "completed"
            work.ingestion_completed_at = datetime.utcnow()
            
            self.db.commit()
            
            # Save indexes
            self.faiss_indexer.save()
            
            # Cleanup
            self.extractor.cleanup(repo_path)
            
            logger.info(
                "Ingestion complete",
                work_id=work.id,
                chunks=len(chunks),
                embeddings=len(embeddings)
            )
            
            return work.id
            
        except Exception as e:
            work.ingestion_status = "failed"
            work.metadata = {"error": str(e)}
            self.db.commit()
            logger.error("Ingestion failed", error=str(e), slug=source_slug)
            raise
```

#### 7. Ingestion API Endpoints (`backend/app/api/v1/ingest.py`)

```python
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, HttpUrl
from app.db.session import get_db
from app.db.models import Work
from app.core.ingestion import IngestionPipeline
import uuid

router = APIRouter()

class IngestWorkRequest(BaseModel):
    repo_url: HttpUrl
    target_file: str
    source_slug: str
    version: str
    branch: str = "main"

class IngestWorkResponse(BaseModel):
    job_id: str
    message: str

class JobStatusResponse(BaseModel):
    job_id: str
    status: str  # pending, processing, completed, failed
    work_id: int = None
    total_chunks: int = None
    error: str = None

# In-memory job tracking (use Redis in production)
jobs = {}

def run_ingestion(job_id: str, request: IngestWorkRequest, db: Session):
    """Background task for ingestion"""
    try:
        jobs[job_id]['status'] = 'processing'
        
        pipeline = IngestionPipeline(db)
        work_id = pipeline.ingest_work(
            repo_url=str(request.repo_url),
            target_file=request.target_file,
            source_slug=request.source_slug,
            version=request.version,
            branch=request.branch
        )
        
        work = db.query(Work).filter(Work.id == work_id).first()
        jobs[job_id].update({
            'status': 'completed',
            'work_id': work_id,
            'total_chunks': work.total_chunks
        })
        
    except Exception as e:
        jobs[job_id].update({
            'status': 'failed',
            'error': str(e)
        })

@router.post("/add-work", response_model=IngestWorkResponse)
async def add_work(
    request: IngestWorkRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Initiate ingestion of a new work.
    Returns job ID for status tracking.
    """
    # Check for duplicate
    existing = db.query(Work).filter(
        Work.source_slug == request.source_slug,
        Work.version == request.version
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Work {request.source_slug}:{request.version} already exists"
        )
    
    # Create job
    job_id = str(uuid.uuid4())
    jobs[job_id] = {'status': 'pending'}
    
    # Start background ingestion
    background_tasks.add_task(run_ingestion, job_id, request, db)
    
    return IngestWorkResponse(
        job_id=job_id,
        message="Ingestion job started"
    )

@router.get("/job/{job_id}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """Check ingestion job status"""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs[job_id]
    return JobStatusResponse(job_id=job_id, **job)
```

### Acceptance Criteria

**✅ Text Chunking:**
- [ ] Deterministic chunking produces identical hashes for same input
- [ ] Chunk size ~1024 tokens (±5% variance acceptable)
- [ ] 20% overlap between adjacent chunks
- [ ] Token count accurate using tiktoken

**✅ Embeddings:**
- [ ] sentence-transformers model loads successfully
- [ ] Embeddings are 384-dimensional numpy arrays
- [ ] Batch processing ≥10x faster than sequential
- [ ] Embedding hashes are deterministic

**✅ FAISS Index:**
- [ ] Index initialized with correct dimensionality
- [ ] Vectors normalized before adding (L2 norm = 1)
- [ ] Search returns top-k results ranked by cosine similarity
- [ ] Index persists to disk and reloads correctly
- [ ] ID mapping correctly links FAISS IDs to chunk IDs

**✅ Whoosh Index:**
- [ ] Schema created with all required fields
- [ ] BM25F scoring enabled
- [ ] Search returns ranked results
- [ ] Filters work correctly (work_slug, version)

**✅ Repository Extraction:**
- [ ] Git clone succeeds for public repositories
- [ ] PDF text extraction works (tested with sample PDF)
- [ ] Markdown extraction preserves text structure
- [ ] metadata.yaml parsing succeeds

**✅ Ingestion Pipeline:**
- [ ] Full pipeline completes without errors
- [ ] Work record created with correct status transitions
- [ ] All chunks stored in database
- [ ] All embeddings stored and indexed
- [ ] Whoosh documents added
- [ ] S3 raw file uploaded
- [ ] Cleanup removes temporary files

**✅ API Endpoints:**
- [ ] POST /api/v1/ingest/add-work returns job_id
- [ ] GET /api/v1/ingest/job/{job_id} returns status
- [ ] Duplicate ingestion prevented
- [ ] Background task executes asynchronously

### Technical Specifications

**Chunking Parameters:**
- Token size: 1024 ± 5% (depending on text structure)
- Overlap: 20% (204-205 tokens)
- Seed: 42 (fixed for reproducibility)
- Tokenizer: cl100k_base (GPT-4 compatible)

**Embedding Model:**
- Name: sentence-transformers/all-MiniLM-L6-v2
- Dimensions: 384
- Context window: 256 tokens
- Normalization: L2 (for cosine similarity)

**FAISS Configuration:**
- Index type: IndexFlatIP (inner product after normalization = cosine)
- Precision: float32
- No dimensionality reduction (exact search)

**Whoosh Configuration:**
- Analyzer: StandardAnalyzer
- Scoring: BM25F (k1=1.2, b=0.75)
- Index location: /app/data/whoosh

### Testing Requirements

**Unit Tests:**
```python
def test_chunker_deterministic():
    chunker = DeterministicChunker(seed=42)
    text = "Sample text " * 1000
    
    chunks1 = chunker.chunk_text(text)
    chunks2 = chunker.chunk_text(text)
    
    assert len(chunks1) == len(chunks2)
    assert all(c1.chunk_hash == c2.chunk_hash for c1, c2 in zip(chunks1, chunks2))

def test_embedder_dimensionality():
    embedder = EmbeddingGenerator()
    embedding = embedder.embed_text("Test text")
    
    assert embedding.shape == (384,)
    assert np.isfinite(embedding).all()

def test_faiss_search():
    indexer = FAISSIndexer()
    
    # Add dummy embeddings
    embeddings = np.random.rand(100, 384).astype('float32')
    chunk_ids = list(range(100))
    indexer.add_batch(chunk_ids, embeddings)
    
    # Search
    query = np.random.rand(384).astype('float32')
    results = indexer.search(query, k=10)
    
    assert len(results) == 10
    assert all('chunk_id' in r and 'score' in r for r in results)
```

**Integration Tests:**
```python
@pytest.mark.integration
def test_full_ingestion_pipeline(db_session):
    pipeline = IngestionPipeline(db_session)
    
    work_id = pipeline.ingest_work(
        repo_url="https://github.com/test/sample-repo",
        target_file="README.md",
        source_slug="sample-work",
        version="v1.0"
    )
    
    work = db_session.query(Work).filter(Work.id == work_id).first()
    assert work.ingestion_status == "completed"
    assert work.total_chunks > 0
    
    chunks = db_session.query(Chunk).filter(Chunk.work_id == work_id).all()
    assert len(chunks) == work.total_chunks
```

### Dependencies

**New Python Packages:**
- tiktoken (OpenAI tokenizer)
- sentence-transformers
- faiss-cpu (or faiss-gpu for production)
- whoosh
- GitPython
- PyPDF2
- python-markdown
- PyYAML

**System Requirements:**
- Git installed
- 4GB RAM for embedding model
- 500MB disk space for indexes

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Large PDFs cause memory overflow | High | Stream processing; chunk PDFs before full extraction |
| Embedding generation is slow | Medium | Use GPU acceleration (faiss-gpu); batch processing |
| FAISS index grows too large | High | Use IVF indexes for >1M vectors; consider quantization |
| Repository clone fails (private repos) | Medium | Support SSH keys and tokens; add authentication layer |

---

## PHASE 3: Three-Level Summarization System

**Duration:** 5 days  
**Dependencies:** Phase 2 complete  
**Risk Level:** Medium  

### Objectives

1. Integrate Abacus.AI LLM APIs for text generation
2. Design prompt templates for three summarization levels (short, medium, long)
3. Implement low-temperature (0.2) generation for consistency
4. Create summary generation service with batch processing
5. Store summaries with prompt hashing for reproducibility
6. Build API endpoints for on-demand summarization

### Deliverables

#### 1. LLM Client (`backend/app/core/llm_client.py`)

```python
import httpx
from typing import Dict, List, Optional
from app.config import settings
import structlog
import hashlib

logger = structlog.get_logger()

class AbacusAIClient:
    """
    Client for Abacus.AI LLM APIs.
    Supports text generation with configurable temperature.
    """
    
    def __init__(self):
        self.api_key = settings.ABACUSAI_API_KEY
        self.model_id = settings.ABACUSAI_MODEL_ID
        self.base_url = "https://api.abacus.ai/v1"
        self.temperature = 0.2  # Low temperature for consistency
        
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            timeout=60.0
        )
    
    async def generate(
        self,
        prompt: str,
        max_tokens: int = 500,
        temperature: float = None
    ) -> str:
        """
        Generate text completion.
        
        Args:
            prompt: Input text
            max_tokens: Maximum response length
            temperature: Override default temperature
        
        Returns:
            Generated text
        """
        temp = temperature if temperature is not None else self.temperature
        
        payload = {
            "model": self.model_id,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temp,
            "top_p": 1.0,
            "n": 1
        }
        
        logger.info("Calling LLM API", model=self.model_id, prompt_len=len(prompt))
        
        try:
            response = await self.client.post("/completions", json=payload)
            response.raise_for_status()
            
            data = response.json()
            generated_text = data['choices'][0]['text'].strip()
            
            logger.info("LLM response received", response_len=len(generated_text))
            return generated_text
            
        except httpx.HTTPError as e:
            logger.error("LLM API error", error=str(e))
            raise
    
    async def batch_generate(
        self,
        prompts: List[str],
        max_tokens: int = 500,
        temperature: float = None
    ) -> List[str]:
        """
        Generate completions for multiple prompts.
        Sequential execution (Abacus.AI may not support batch endpoints).
        """
        results = []
        for prompt in prompts:
            result = await self.generate(prompt, max_tokens, temperature)
            results.append(result)
        return results
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()
```

#### 2. Prompt Templates (`backend/app/core/prompts.py`)

```python
from typing import Dict
import hashlib

class SummaryPrompts:
    """
    Prompt templates for three-level summarization.
    Prompts are deterministic and versioned via hashing.
    """
    
    SHORT_TEMPLATE = """Summarize the following text in 50-100 characters. Be concise and capture the main idea.

Text:
{text}

Summary (50-100 chars):"""
    
    MEDIUM_TEMPLATE = """Provide a medium-length summary of the following text in 150-300 words. Include key points and main arguments.

Text:
{text}

Summary (150-300 words):"""
    
    LONG_TEMPLATE = """Create a comprehensive summary of the following text in 400-800 words. Include:
- Main thesis and key arguments
- Supporting evidence and examples
- Conclusions or implications
- Any important technical details

Text:
{text}

Comprehensive Summary (400-800 words):"""
    
    @classmethod
    def get_prompt(cls, level: str, text: str) -> str:
        """
        Generate prompt for given summarization level.
        
        Args:
            level: "short", "medium", or "long"
            text: Text to summarize
        
        Returns:
            Formatted prompt
        """
        templates = {
            "short": cls.SHORT_TEMPLATE,
            "medium": cls.MEDIUM_TEMPLATE,
            "long": cls.LONG_TEMPLATE
        }
        
        if level not in templates:
            raise ValueError(f"Invalid summary level: {level}")
        
        return templates[level].format(text=text)
    
    @classmethod
    def hash_prompt(cls, level: str, text: str) -> str:
        """
        Create deterministic hash of prompt for tracking.
        Hashes template + text to detect changes.
        """
        prompt = cls.get_prompt(level, text)
        return hashlib.sha256(prompt.encode('utf-8')).hexdigest()
    
    @classmethod
    def get_template_version(cls) -> Dict[str, str]:
        """
        Return hashes of each template (without text substitution).
        Useful for tracking prompt version changes.
        """
        return {
            "short": hashlib.sha256(cls.SHORT_TEMPLATE.encode()).hexdigest()[:8],
            "medium": hashlib.sha256(cls.MEDIUM_TEMPLATE.encode()).hexdigest()[:8],
            "long": hashlib.sha256(cls.LONG_TEMPLATE.encode()).hexdigest()[:8]
        }
```

#### 3. Summarization Service (`backend/app/core/summarizer.py`)

```python
from sqlalchemy.orm import Session
from app.db.models import Chunk, Summary
from app.core.llm_client import AbacusAIClient
from app.core.prompts import SummaryPrompts
from typing import List, Dict
import structlog
from datetime import datetime

logger = structlog.get_logger()

class SummarizationService:
    """
    Generates three-level summaries for text chunks using LLMs.
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.llm_client = AbacusAIClient()
        self.prompts = SummaryPrompts()
    
    async def summarize_chunk(
        self,
        chunk: Chunk,
        levels: List[str] = ["short", "medium", "long"]
    ) -> Dict[str, Summary]:
        """
        Generate summaries at specified levels for a single chunk.
        
        Returns:
            Dictionary mapping level -> Summary object
        """
        summaries = {}
        
        for level in levels:
            # Check if summary already exists
            existing = self.db.query(Summary).filter(
                Summary.chunk_id == chunk.id,
                Summary.summary_level == level
            ).first()
            
            if existing:
                logger.info("Summary exists", chunk_id=chunk.id, level=level)
                summaries[level] = existing
                continue
            
            # Generate prompt
            prompt = self.prompts.get_prompt(level, chunk.text)
            prompt_hash = self.prompts.hash_prompt(level, chunk.text)
            
            # Generate summary
            max_tokens = {"short": 50, "medium": 400, "long": 1000}[level]
            
            logger.info("Generating summary", chunk_id=chunk.id, level=level)
            summary_text = await self.llm_client.generate(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.2
            )
            
            # Create summary record
            summary = Summary(
                chunk_id=chunk.id,
                summary_level=level,
                summary_text=summary_text,
                char_count=len(summary_text),
                llm_model=self.llm_client.model_id,
                prompt_hash=prompt_hash,
                temperature=0.2,
                created_at=datetime.utcnow()
            )
            
            self.db.add(summary)
            self.db.commit()
            
            summaries[level] = summary
            
            logger.info(
                "Summary created",
                chunk_id=chunk.id,
                level=level,
                char_count=len(summary_text)
            )
        
        return summaries
    
    async def summarize_work(
        self,
        work_id: int,
        levels: List[str] = ["short", "medium", "long"],
        batch_size: int = 10
    ) -> Dict[str, int]:
        """
        Generate summaries for all chunks in a work.
        Processes in batches for efficiency.
        
        Returns:
            Statistics: {level: count_generated}
        """
        chunks = self.db.query(Chunk).filter(Chunk.work_id == work_id).all()
        
        stats = {level: 0 for level in levels}
        
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            
            for chunk in batch:
                summaries = await self.summarize_chunk(chunk, levels)
                
                for level in levels:
                    if summaries[level].created_at >= datetime.utcnow().replace(microsecond=0):
                        stats[level] += 1
        
        logger.info("Work summarization complete", work_id=work_id, stats=stats)
        return stats
    
    async def get_summary_by_level(self, chunk_id: int, level: str) -> Summary:
        """Retrieve specific summary level for a chunk"""
        summary = self.db.query(Summary).filter(
            Summary.chunk_id == chunk_id,
            Summary.summary_level == level
        ).first()
        
        if not summary:
            # Generate on-demand
            chunk = self.db.query(Chunk).filter(Chunk.id == chunk_id).first()
            if not chunk:
                raise ValueError(f"Chunk {chunk_id} not found")
            
            summaries = await self.summarize_chunk(chunk, [level])
            summary = summaries[level]
        
        return summary
    
    async def close(self):
        """Cleanup"""
        await self.llm_client.close()
```

#### 4. Batch Summarization Worker (Optional - for RQ/Celery)

```python
# backend/app/workers/summarize_worker.py
from rq import Worker, Queue
from app.db.session import SessionLocal
from app.core.summarizer import SummarizationService
import asyncio

def summarize_work_task(work_id: int):
    """
    Background task to summarize all chunks in a work.
    Designed for RQ/Celery job queue.
    """
    db = SessionLocal()
    
    try:
        service = SummarizationService(db)
        
        # Run async summarization
        stats = asyncio.run(service.summarize_work(work_id))
        
        return {
            "work_id": work_id,
            "status": "completed",
            "summaries_generated": stats
        }
    
    except Exception as e:
        return {
            "work_id": work_id,
            "status": "failed",
            "error": str(e)
        }
    
    finally:
        asyncio.run(service.close())
        db.close()
```

#### 5. Summarization API Endpoints (`backend/app/api/v1/summarize.py`)

```python
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.db.models import Work, Summary
from app.core.summarizer import SummarizationService
from typing import List

router = APIRouter()

class SummarizeWorkRequest(BaseModel):
    work_id: int
    levels: List[str] = ["short", "medium", "long"]

class SummarizeWorkResponse(BaseModel):
    message: str
    work_id: int

class GetSummaryRequest(BaseModel):
    chunk_id: int
    level: str  # short, medium, long

class GetSummaryResponse(BaseModel):
    chunk_id: int
    level: str
    summary_text: str
    char_count: int
    llm_model: str
    created_at: str

@router.post("/work", response_model=SummarizeWorkResponse)
async def summarize_work(
    request: SummarizeWorkRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Generate summaries for all chunks in a work.
    Runs in background.
    """
    work = db.query(Work).filter(Work.id == request.work_id).first()
    if not work:
        raise HTTPException(status_code=404, detail="Work not found")
    
    # Start background task
    async def run_summarization():
        service = SummarizationService(db)
        await service.summarize_work(request.work_id, request.levels)
        await service.close()
    
    background_tasks.add_task(run_summarization)
    
    return SummarizeWorkResponse(
        message="Summarization started",
        work_id=request.work_id
    )

@router.post("/chunk", response_model=GetSummaryResponse)
async def get_chunk_summary(
    request: GetSummaryRequest,
    db: Session = Depends(get_db)
):
    """
    Get or generate summary for a specific chunk.
    """
    service = SummarizationService(db)
    
    try:
        summary = await service.get_summary_by_level(request.chunk_id, request.level)
        
        return GetSummaryResponse(
            chunk_id=summary.chunk_id,
            level=summary.summary_level,
            summary_text=summary.summary_text,
            char_count=summary.char_count,
            llm_model=summary.llm_model,
            created_at=summary.created_at.isoformat()
        )
    
    finally:
        await service.close()
```

### Acceptance Criteria

**✅ LLM Integration:**
- [ ] Abacus.AI client successfully authenticates
- [ ] Text generation works with sample prompt
- [ ] Temperature setting honored (0.2 produces consistent outputs)
- [ ] Error handling for API failures (rate limits, timeouts)

**✅ Prompt Templates:**
- [ ] Three templates defined (short, medium, long)
- [ ] Template hashing is deterministic
- [ ] Prompts produce outputs within specified length ranges (±20%)

**✅ Summary Generation:**
- [ ] Short summaries: 50-100 characters
- [ ] Medium summaries: 150-300 words
- [ ] Long summaries: 400-800 words
- [ ] Summaries capture main ideas accurately (manual review of 10 samples)

**✅ Database Storage:**
- [ ] Summaries stored with correct metadata (prompt_hash, model, temperature)
- [ ] Query by chunk_id and level works
- [ ] Duplicate prevention (same chunk + level not regenerated)

**✅ Batch Processing:**
- [ ] Work-level summarization completes for 10+ chunks
- [ ] Processing time: ≤60 seconds for 10 chunks
- [ ] Error in one chunk doesn't fail entire batch

**✅ API Endpoints:**
- [ ] POST /api/v1/summarize/work initiates background task
- [ ] POST /api/v1/summarize/chunk returns summary (generates if needed)
- [ ] Proper error codes for invalid requests

### Technical Specifications

**LLM Configuration:**
- Model: gpt-4-turbo (or equivalent Abacus.AI model)
- Temperature: 0.2 (low for consistency)
- Top-p: 1.0
- Max tokens: Variable by level (50/400/1000)

**Prompt Engineering:**
- Clear instructions with character/word count targets
- Structured output format
- Context window: Full chunk text (up to ~2048 tokens)

**Performance Targets:**
- Generation latency: ≤5 seconds per summary
- Batch throughput: ≥10 summaries/minute
- API uptime: 99.5% (dependent on Abacus.AI SLA)

### Testing Requirements

**Unit Tests:**
```python
@pytest.mark.asyncio
async def test_llm_generation():
    client = AbacusAIClient()
    result = await client.generate("Summarize: The sky is blue.", max_tokens=50)
    
    assert len(result) > 0
    assert len(result) <= 250  # Rough check for max_tokens
    
    await client.close()

def test_prompt_templates():
    text = "Sample text " * 100
    
    short_prompt = SummaryPrompts.get_prompt("short", text)
    assert "50-100 characters" in short_prompt
    assert text in short_prompt
    
    hash1 = SummaryPrompts.hash_prompt("short", text)
    hash2 = SummaryPrompts.hash_prompt("short", text)
    assert hash1 == hash2  # Deterministic

@pytest.mark.asyncio
async def test_summarization_service(db_session):
    # Create test chunk
    chunk = Chunk(
        work_id=1,
        chunk_index=0,
        text="This is a test chunk. " * 50,
        token_count=100
    )
    db_session.add(chunk)
    db_session.commit()
    
    service = SummarizationService(db_session)
    summaries = await service.summarize_chunk(chunk, ["short"])
    
    assert "short" in summaries
    assert summaries["short"].char_count >= 50
    assert summaries["short"].char_count <= 150
    
    await service.close()
```

**Integration Tests:**
```python
@pytest.mark.integration
async def test_full_summarization_pipeline(db_session):
    # Assume work with chunks already exists
    work_id = 1
    
    service = SummarizationService(db_session)
    stats = await service.summarize_work(work_id, ["short", "medium"])
    
    assert stats["short"] > 0
    assert stats["medium"] > 0
    
    # Verify summaries in DB
    summaries = db_session.query(Summary).filter(Summary.chunk.work_id == work_id).all()
    assert len(summaries) >= stats["short"] + stats["medium"]
```

### Dependencies

**New Python Packages:**
- httpx (async HTTP client)
- No additional packages (uses existing structlog, sqlalchemy)

**External Services:**
- Abacus.AI account with API key
- Sufficient API quota/credits for testing

**Environment Variables:**
- ABACUSAI_API_KEY (required)
- ABACUSAI_MODEL_ID (optional, defaults to gpt-4-turbo)

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| LLM API rate limits | High | Implement exponential backoff; use job queue for throttling |
| Inconsistent summary quality | Medium | Use low temperature; add quality validation prompts |
| High API costs | Medium | Cache summaries aggressively; use cheaper models for short summaries |
| API downtime | High | Implement retry logic; queue failed jobs for later processing |

---

## PHASE 4: Hybrid Retrieval System

**Duration:** 7 days  
**Dependencies:** Phases 2 & 3 complete  
**Risk Level:** Medium  

### Objectives

1. Implement FAISS vector search for semantic retrieval
2. Implement Whoosh BM25 search for lexical retrieval
3. Design hybrid scoring algorithm (0.7 semantic + 0.3 lexical)
4. Add deterministic ranking with seed for reproducibility
5. Support query constraint filtering (tags, canonical, version)
6. Build query API with citation formatting
7. Optimize for top-K performance (≤300ms median latency)

### Deliverables

#### 1. Hybrid Retrieval Engine (`backend/app/core/retrieval.py`)

```python
from typing import List, Dict, Optional, Tuple
from sqlalchemy.orm import Session
from app.db.models import Chunk, Work, Embedding, Summary
from app.core.embeddings import EmbeddingGenerator
from app.core.indexer import FAISSIndexer, WhooshIndexer
from app.config import settings
import numpy as np
import random
import structlog

logger = structlog.get_logger()

class HybridRetriever:
    """
    Combines semantic (FAISS) and lexical (Whoosh BM25) search.
    Implements weighted scoring: 0.7 semantic + 0.3 lexical.
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.embedder = EmbeddingGenerator()
        self.faiss_indexer = FAISSIndexer()
        self.whoosh_indexer = WhooshIndexer()
        
        # Load existing indexes
        self.faiss_indexer.load()
        
        # Scoring weights
        self.semantic_weight = settings.SEMANTIC_WEIGHT  # 0.7
        self.lexical_weight = settings.LEXICAL_WEIGHT    # 0.3
        
        # Deterministic ranking
        self.seed = settings.RANDOM_SEED  # 42
        random.seed(self.seed)
    
    def retrieve(
        self,
        query: str,
        top_k: int = 20,
        filters: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Hybrid retrieval combining semantic and lexical search.
        
        Args:
            query: Search query string
            top_k: Number of results to return
            filters: Optional constraints {work_slug, version, tags}
        
        Returns:
            List of results with metadata and citations
        """
        logger.info("Starting hybrid retrieval", query_len=len(query), top_k=top_k)
        
        # Step 1: Semantic Search (FAISS)
        query_embedding = self.embedder.embed_text(query)
        semantic_results = self.faiss_indexer.search(query_embedding, k=top_k * 2)
        
        # Step 2: Lexical Search (Whoosh BM25)
        whoosh_filters = {}
        if filters:
            if 'work_slug' in filters:
                whoosh_filters['work_slug'] = filters['work_slug']
            if 'version' in filters:
                whoosh_filters['version'] = filters['version']
        
        lexical_results = self.whoosh_indexer.search(query, k=top_k * 2, filters=whoosh_filters)
        
        # Step 3: Normalize scores
        semantic_scores = self._normalize_scores([r['score'] for r in semantic_results])
        lexical_scores = self._normalize_scores([r['score'] for r in lexical_results])
        
        # Step 4: Merge results with hybrid scoring
        chunk_scores = {}
        
        for i, result in enumerate(semantic_results):
            chunk_id = result['chunk_id']
            chunk_scores[chunk_id] = {
                'semantic_score': semantic_scores[i],
                'lexical_score': 0.0,
                'chunk_id': chunk_id
            }
        
        for i, result in enumerate(lexical_results):
            chunk_id = result['chunk_id']
            if chunk_id in chunk_scores:
                chunk_scores[chunk_id]['lexical_score'] = lexical_scores[i]
            else:
                chunk_scores[chunk_id] = {
                    'semantic_score': 0.0,
                    'lexical_score': lexical_scores[i],
                    'chunk_id': chunk_id
                }
        
        # Step 5: Calculate hybrid scores
        for chunk_id, scores in chunk_scores.items():
            hybrid_score = (
                self.semantic_weight * scores['semantic_score'] +
                self.lexical_weight * scores['lexical_score']
            )
            scores['hybrid_score'] = hybrid_score
        
        # Step 6: Rank by hybrid score (deterministic tie-breaking)
        ranked_chunks = sorted(
            chunk_scores.values(),
            key=lambda x: (x['hybrid_score'], x['chunk_id']),  # Deterministic secondary sort
            reverse=True
        )[:top_k]
        
        # Step 7: Fetch chunk details from database
        chunk_ids = [c['chunk_id'] for c in ranked_chunks]
        chunks = self.db.query(Chunk, Work).join(Work).filter(Chunk.id.in_(chunk_ids)).all()
        
        chunk_map = {chunk.id: (chunk, work) for chunk, work in chunks}
        
        # Step 8: Apply additional filters (tags, etc.)
        if filters and 'tags' in filters:
            required_tags = set(filters['tags'])
            filtered_chunk_ids = [
                chunk_id for chunk_id in chunk_ids
                if chunk_id in chunk_map and 
                set(chunk_map[chunk_id][1].tags or []) & required_tags
            ]
            chunk_ids = filtered_chunk_ids[:top_k]
        
        # Step 9: Format results with citations
        results = []
        for ranked_chunk in ranked_chunks:
            chunk_id = ranked_chunk['chunk_id']
            if chunk_id not in chunk_map:
                continue
            
            chunk, work = chunk_map[chunk_id]
            
            # Generate retrieval_id (citation format)
            retrieval_id = f"{work.source_slug}:{work.version}:{chunk.id}"
            
            results.append({
                'retrieval_id': retrieval_id,
                'chunk_id': chunk.id,
                'work_slug': work.source_slug,
                'version': work.version,
                'chunk_index': chunk.chunk_index,
                'text': chunk.text,
                'semantic_score': ranked_chunk['semantic_score'],
                'lexical_score': ranked_chunk['lexical_score'],
                'hybrid_score': ranked_chunk['hybrid_score'],
                'work_title': work.title,
                'work_url': work.canonical_url
            })
        
        logger.info("Retrieval complete", results_count=len(results))
        return results
    
    def _normalize_scores(self, scores: List[float]) -> List[float]:
        """
        Min-max normalization to [0, 1] range.
        Handles edge cases (all same scores, empty list).
        """
        if not scores:
            return []
        
        min_score = min(scores)
        max_score = max(scores)
        
        if max_score == min_score:
            return [1.0] * len(scores)  # All equal = max score
        
        return [(s - min_score) / (max_score - min_score) for s in scores]
    
    def get_context_window(
        self,
        chunk_id: int,
        window_size: int = 2
    ) -> List[Chunk]:
        """
        Retrieve adjacent chunks for context.
        
        Args:
            chunk_id: Central chunk ID
            window_size: Number of chunks before/after
        
        Returns:
            List of chunks in order [chunk_id-2, chunk_id-1, chunk_id, chunk_id+1, chunk_id+2]
        """
        chunk = self.db.query(Chunk).filter(Chunk.id == chunk_id).first()
        if not chunk:
            return []
        
        # Get adjacent chunks by index
        adjacent_chunks = self.db.query(Chunk).filter(
            Chunk.work_id == chunk.work_id,
            Chunk.chunk_index >= chunk.chunk_index - window_size,
            Chunk.chunk_index <= chunk.chunk_index + window_size
        ).order_by(Chunk.chunk_index).all()
        
        return adjacent_chunks
```

#### 2. Query API Endpoints (`backend/app/api/v1/query.py`)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.core.retrieval import HybridRetriever
from typing import List, Optional, Dict

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 20
    filters: Optional[Dict] = None  # {work_slug, version, tags}
    include_context: bool = False   # Include adjacent chunks
    include_summaries: bool = False  # Include short summaries

class QueryResult(BaseModel):
    retrieval_id: str
    chunk_id: int
    work_slug: str
    version: str
    chunk_index: int
    text: str
    semantic_score: float
    lexical_score: float
    hybrid_score: float
    work_title: Optional[str]
    work_url: str
    context_window: Optional[List[str]] = None  # Adjacent chunk texts
    short_summary: Optional[str] = None

class QueryResponse(BaseModel):
    query: str
    results_count: int
    results: List[QueryResult]
    execution_time_ms: int

@router.post("/", response_model=QueryResponse)
async def query(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    """
    Hybrid retrieval endpoint.
    Returns ranked results with citations.
    """
    import time
    start_time = time.time()
    
    # Validate inputs
    if not request.query or len(request.query) < 3:
        raise HTTPException(status_code=400, detail="Query too short (min 3 chars)")
    
    if request.top_k > 100:
        raise HTTPException(status_code=400, detail="top_k cannot exceed 100")
    
    # Perform retrieval
    retriever = HybridRetriever(db)
    results = retriever.retrieve(
        query=request.query,
        top_k=request.top_k,
        filters=request.filters
    )
    
    # Enrich results if requested
    enriched_results = []
    for result in results:
        query_result = QueryResult(**result)
        
        # Add context window
        if request.include_context:
            context_chunks = retriever.get_context_window(result['chunk_id'], window_size=2)
            query_result.context_window = [c.text for c in context_chunks]
        
        # Add short summary
        if request.include_summaries:
            from app.db.models import Summary
            summary = db.query(Summary).filter(
                Summary.chunk_id == result['chunk_id'],
                Summary.summary_level == "short"
            ).first()
            if summary:
                query_result.short_summary = summary.summary_text
        
        enriched_results.append(query_result)
    
    execution_time = int((time.time() - start_time) * 1000)
    
    return QueryResponse(
        query=request.query,
        results_count=len(enriched_results),
        results=enriched_results,
        execution_time_ms=execution_time
    )

@router.get("/chunk/{chunk_id}", response_model=QueryResult)
async def get_chunk_by_id(
    chunk_id: int,
    include_context: bool = False,
    include_summaries: bool = False,
    db: Session = Depends(get_db)
):
    """
    Retrieve specific chunk by ID with optional enrichment.
    """
    from app.db.models import Chunk, Work, Summary
    
    chunk_work = db.query(Chunk, Work).join(Work).filter(Chunk.id == chunk_id).first()
    
    if not chunk_work:
        raise HTTPException(status_code=404, detail="Chunk not found")
    
    chunk, work = chunk_work
    
    result = QueryResult(
        retrieval_id=f"{work.source_slug}:{work.version}:{chunk.id}",
        chunk_id=chunk.id,
        work_slug=work.source_slug,
        version=work.version,
        chunk_index=chunk.chunk_index,
        text=chunk.text,
        semantic_score=0.0,  # Not applicable for direct lookup
        lexical_score=0.0,
        hybrid_score=0.0,
        work_title=work.title,
        work_url=work.canonical_url
    )
    
    # Add context
    if include_context:
        retriever = HybridRetriever(db)
        context_chunks = retriever.get_context_window(chunk_id, window_size=2)
        result.context_window = [c.text for c in context_chunks]
    
    # Add summary
    if include_summaries:
        summary = db.query(Summary).filter(
            Summary.chunk_id == chunk_id,
            Summary.summary_level == "short"
        ).first()
        if summary:
            result.short_summary = summary.summary_text
    
    return result
```

### Acceptance Criteria

**✅ Semantic Search:**
- [ ] FAISS index loaded successfully on startup
- [ ] Query embedding generated correctly
- [ ] Top-K semantic results returned
- [ ] Cosine similarity scores in [0, 1] range

**✅ Lexical Search:**
- [ ] Whoosh BM25 search returns ranked results
- [ ] Query parsing handles special characters
- [ ] Filters (work_slug, version) applied correctly

**✅ Hybrid Scoring:**
- [ ] Scores normalized to [0, 1] before weighting
- [ ] Hybrid score = 0.7 * semantic + 0.3 * lexical
- [ ] Results ranked by hybrid score (highest first)
- [ ] Deterministic ranking (same query → same results)

**✅ Filtering:**
- [ ] work_slug filter excludes non-matching works
- [ ] version filter works correctly
- [ ] tags filter (if provided) returns only matching works
- [ ] Empty results when no matches

**✅ Citation Format:**
- [ ] retrieval_id follows pattern: `slug:version:chunk_id`
- [ ] All results include complete metadata (title, URL, etc.)

**✅ Performance:**
- [ ] Query latency: median ≤300ms, p95 ≤800ms (measured over 100 queries)
- [ ] No timeout errors for top_k ≤ 100
- [ ] Memory usage stable (no leaks during 1000 queries)

**✅ API Endpoints:**
- [ ] POST /api/v1/query returns correct schema
- [ ] GET /api/v1/query/chunk/{id} works
- [ ] Optional enrichment (context, summaries) works
- [ ] Proper error codes for invalid inputs

### Technical Specifications

**Hybrid Scoring Formula:**
```
hybrid_score = 0.7 * normalized_semantic_score + 0.3 * normalized_lexical_score
```

**Normalization:**
- Min-max scaling: `(score - min) / (max - min)`
- Edge case: If all scores equal, assign 1.0

**Deterministic Ranking:**
- Primary sort: hybrid_score (descending)
- Secondary sort: chunk_id (ascending, for ties)
- Seed: 42 (for any randomness in retrieval)

**Context Window:**
- Default: ±2 chunks around target
- Maximum: ±5 chunks (configurable)
- Ordered by chunk_index

### Testing Requirements

**Unit Tests:**
```python
def test_score_normalization():
    retriever = HybridRetriever(None)
    
    scores = [0.5, 0.8, 0.2, 0.9]
    normalized = retriever._normalize_scores(scores)
    
    assert min(normalized) == pytest.approx(0.0)
    assert max(normalized) == pytest.approx(1.0)
    assert len(normalized) == len(scores)

def test_hybrid_scoring():
    # Mock semantic and lexical results
    semantic = [{'chunk_id': 1, 'score': 0.9}, {'chunk_id': 2, 'score': 0.6}]
    lexical = [{'chunk_id': 1, 'score': 0.5}, {'chunk_id': 2, 'score': 0.8}]
    
    # Expected hybrid scores:
    # chunk_1: 0.7 * 1.0 + 0.3 * 0.0 = 0.7
    # chunk_2: 0.7 * 0.0 + 0.3 * 1.0 = 0.3
    
    # Test implementation...

def test_deterministic_ranking():
    retriever = HybridRetriever(db_session)
    
    results1 = retriever.retrieve("test query", top_k=10)
    results2 = retriever.retrieve("test query", top_k=10)
    
    # Same query should produce identical results
    assert [r['retrieval_id'] for r in results1] == [r['retrieval_id'] for r in results2]
```

**Performance Tests:**
```python
import pytest
import time

@pytest.mark.performance
def test_query_latency(db_session):
    retriever = HybridRetriever(db_session)
    
    queries = ["quantum computing", "machine learning", "data science"] * 33  # 99 queries
    
    latencies = []
    for query in queries:
        start = time.time()
        results = retriever.retrieve(query, top_k=20)
        latency = (time.time() - start) * 1000  # ms
        latencies.append(latency)
    
    median = sorted(latencies)[len(latencies) // 2]
    p95 = sorted(latencies)[int(len(latencies) * 0.95)]
    
    assert median <= 300, f"Median latency {median}ms exceeds 300ms"
    assert p95 <= 800, f"P95 latency {p95}ms exceeds 800ms"
```

### Dependencies

**No new packages required** - uses existing:
- sentence-transformers (embeddings)
- faiss-cpu (vector search)
- whoosh (BM25 search)
- sqlalchemy (database queries)

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| FAISS index not loaded on startup | High | Add health check; load index in lifespan event |
| Slow queries with large indexes | High | Use FAISS IVF indexes for >100k vectors; add caching |
| Inconsistent ranking across restarts | Medium | Ensure deterministic seed propagation; version indexes |
| Context window retrieval is slow | Low | Index chunk_index for fast range queries; limit window size |

---

## PHASE 5: Citation Verification System

**Duration:** 7 days  
**Dependencies:** Phase 4 complete  
**Risk Level:** High  

### Objectives

1. Implement cosine similarity calculation between claims and chunks
2. Define threshold-based validation (pass ≥0.80, partial 0.75-0.80, fail <0.75)
3. Build claim extraction from model outputs
4. Parse citation IDs (source_slug:version:chunk_id format)
5. Create verifier decision logic with confidence scoring
6. Implement audit logging for all verifications
7. Build API endpoint for verification runs
8. Generate annotated claims response

### Deliverables

#### 1. Citation Parser (`backend/app/core/citation_parser.py`)

```python
from typing import List, Dict, Optional, Tuple
import re
import structlog

logger = structlog.get_logger()

class CitationParser:
    """
    Parses citation IDs from text.
    Format: source_slug:version:chunk_id
    Example: quantum-paper:v1.0:42
    """
    
    # Regex pattern for citation format
    CITATION_PATTERN = r'\[([a-zA-Z0-9\-\_]+):([a-zA-Z0-9\.\-]+):(\d+)\]'
    
    @classmethod
    def extract_citations(cls, text: str) -> List[Dict]:
        """
        Extract all citations from text.
        
        Returns:
            List of {citation_id, source_slug, version, chunk_id, position}
        """
        citations = []
        
        for match in re.finditer(cls.CITATION_PATTERN, text):
            source_slug = match.group(1)
            version = match.group(2)
            chunk_id = int(match.group(3))
            
            citations.append({
                'citation_id': match.group(0),  # Full citation with brackets
                'retrieval_id': f"{source_slug}:{version}:{chunk_id}",
                'source_slug': source_slug,
                'version': version,
                'chunk_id': chunk_id,
                'start_pos': match.start(),
                'end_pos': match.end()
            })
        
        logger.info("Extracted citations", count=len(citations))
        return citations
    
    @classmethod
    def extract_claims(cls, text: str) -> List[Dict]:
        """
        Extract individual claims from text.
        A claim is defined as a sentence or statement that may contain citations.
        
        Returns:
            List of {claim_text, citations, claim_index}
        """
        # Split text into sentences (simple approach)
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        claims = []
        for i, sentence in enumerate(sentences):
            # Extract citations in this sentence
            sentence_citations = cls.extract_citations(sentence)
            
            if sentence_citations or len(sentence.strip()) > 10:  # Include non-trivial sentences
                # Remove citation markers for clean claim text
                clean_claim = re.sub(cls.CITATION_PATTERN, '', sentence).strip()
                
                claims.append({
                    'claim_text': clean_claim,
                    'original_text': sentence,
                    'citations': sentence_citations,
                    'claim_index': i
                })
        
        logger.info("Extracted claims", count=len(claims))
        return claims
    
    @classmethod
    def validate_citation_format(cls, citation_id: str) -> bool:
        """Check if citation ID follows the expected format"""
        match = re.fullmatch(cls.CITATION_PATTERN.strip('[]'), citation_id)
        return match is not None
```

#### 2. Verifier Engine (`backend/app/core/verifier.py`)

```python
from typing import List, Dict, Optional
from sqlalchemy.orm import Session
from app.db.models import Chunk, Citation
from app.core.embeddings import EmbeddingGenerator
from app.core.citation_parser import CitationParser
from app.config import settings
import numpy as np
import structlog
from datetime import datetime

logger = structlog.get_logger()

class VerifierDecision:
    PASS = "pass"
    PARTIAL = "partial"
    FAIL = "fail"

class CitationVerifier:
    """
    Verifies citations by calculating cosine similarity between claims and cited chunks.
    
    Thresholds:
    - Pass: ≥0.80
    - Partial: 0.75-0.80
    - Fail: <0.75
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.embedder = EmbeddingGenerator()
        self.parser = CitationParser()
        
        # Verification thresholds
        self.pass_threshold = settings.VERIFIER_PASS_THRESHOLD  # 0.80
        self.partial_threshold = settings.VERIFIER_PARTIAL_THRESHOLD  # 0.75
    
    def cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors"""
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        similarity = dot_product / (norm1 * norm2)
        return float(similarity)
    
    def verify_single_citation(
        self,
        claim_text: str,
        chunk_id: int,
        query_text: Optional[str] = None
    ) -> Dict:
        """
        Verify a single claim-citation pair.
        
        Args:
            claim_text: The claim being made
            chunk_id: ID of the cited chunk
            query_text: Original query (optional)
        
        Returns:
            {
                'chunk_id': int,
                'similarity_score': float,
                'decision': str (pass/partial/fail),
                'chunk_text': str,
                'confidence': float
            }
        """
        # Retrieve chunk
        chunk = self.db.query(Chunk).filter(Chunk.id == chunk_id).first()
        
        if not chunk:
            return {
                'chunk_id': chunk_id,
                'similarity_score': 0.0,
                'decision': VerifierDecision.FAIL,
                'error': 'Chunk not found',
                'confidence': 0.0
            }
        
        # Generate embeddings
        claim_embedding = self.embedder.embed_text(claim_text)
        chunk_embedding = self.embedder.embed_text(chunk.text)
        
        # Calculate similarity
        similarity = self.cosine_similarity(claim_embedding, chunk_embedding)
        
        # Make decision
        if similarity >= self.pass_threshold:
            decision = VerifierDecision.PASS
            confidence = similarity
        elif similarity >= self.partial_threshold:
            decision = VerifierDecision.PARTIAL
            confidence = similarity
        else:
            decision = VerifierDecision.FAIL
            confidence = 1.0 - similarity  # Confidence in failure
        
        result = {
            'chunk_id': chunk_id,
            'similarity_score': similarity,
            'decision': decision,
            'chunk_text': chunk.text[:200] + "..." if len(chunk.text) > 200 else chunk.text,
            'confidence': confidence
        }
        
        logger.info(
            "Citation verified",
            chunk_id=chunk_id,
            similarity=f"{similarity:.3f}",
            decision=decision
        )
        
        # Store in database
        citation = Citation(
            chunk_id=chunk_id,
            retrieval_id=f"unknown:unknown:{chunk_id}",  # Will be updated with proper ID
            query_text=query_text,
            claim_text=claim_text,
            similarity_score=similarity,
            verifier_decision=decision,
            context_window=[],
            created_at=datetime.utcnow()
        )
        self.db.add(citation)
        self.db.commit()
        
        return result
    
    def verify_claims(
        self,
        text: str,
        query_text: Optional[str] = None
    ) -> Dict:
        """
        Extract and verify all claims with citations from text.
        
        Args:
            text: Generated text containing claims and citations
            query_text: Original query
        
        Returns:
            {
                'claims': List of claim verification results,
                'overall_stats': {pass_count, partial_count, fail_count, accuracy},
                'annotated_text': Text with verification markers
            }
        """
        logger.info("Starting claims verification", text_length=len(text))
        
        # Extract claims
        claims = self.parser.extract_claims(text)
        
        verified_claims = []
        pass_count = 0
        partial_count = 0
        fail_count = 0
        
        for claim in claims:
            claim_result = {
                'claim_index': claim['claim_index'],
                'claim_text': claim['claim_text'],
                'original_text': claim['original_text'],
                'citations': []
            }
            
            # Verify each citation in the claim
            for citation in claim['citations']:
                chunk_id = citation['chunk_id']
                
                verification = self.verify_single_citation(
                    claim_text=claim['claim_text'],
                    chunk_id=chunk_id,
                    query_text=query_text
                )
                
                verification['citation_id'] = citation['citation_id']
                verification['retrieval_id'] = citation['retrieval_id']
                
                claim_result['citations'].append(verification)
                
                # Update counts
                if verification['decision'] == VerifierDecision.PASS:
                    pass_count += 1
                elif verification['decision'] == VerifierDecision.PARTIAL:
                    partial_count += 1
                else:
                    fail_count += 1
            
            # Overall claim decision (worst of all citations)
            if claim_result['citations']:
                decisions = [c['decision'] for c in claim_result['citations']]
                if VerifierDecision.FAIL in decisions:
                    claim_result['overall_decision'] = VerifierDecision.FAIL
                elif VerifierDecision.PARTIAL in decisions:
                    claim_result['overall_decision'] = VerifierDecision.PARTIAL
                else:
                    claim_result['overall_decision'] = VerifierDecision.PASS
            else:
                claim_result['overall_decision'] = None  # No citations
            
            verified_claims.append(claim_result)
        
        # Calculate statistics
        total_citations = pass_count + partial_count + fail_count
        accuracy = (pass_count / total_citations * 100) if total_citations > 0 else 0.0
        
        overall_stats = {
            'total_claims': len(claims),
            'total_citations': total_citations,
            'pass_count': pass_count,
            'partial_count': partial_count,
            'fail_count': fail_count,
            'accuracy': accuracy
        }
        
        # Annotate text with verification results
        annotated_text = self._annotate_text(text, verified_claims)
        
        logger.info(
            "Verification complete",
            claims=len(claims),
            citations=total_citations,
            accuracy=f"{accuracy:.1f}%"
        )
        
        return {
            'claims': verified_claims,
            'overall_stats': overall_stats,
            'annotated_text': annotated_text
        }
    
    def _annotate_text(self, text: str, verified_claims: List[Dict]) -> str:
        """
        Add verification markers to text.
        Format: [citation]✓ for pass, [citation]⚠ for partial, [citation]✗ for fail
        """
        annotated = text
        
        for claim in verified_claims:
            for citation in claim['citations']:
                decision = citation['decision']
                citation_id = citation['citation_id']
                
                if decision == VerifierDecision.PASS:
                    marker = "✓"
                elif decision == VerifierDecision.PARTIAL:
                    marker = "⚠"
                else:
                    marker = "✗"
                
                # Replace citation with annotated version
                annotated = annotated.replace(
                    citation_id,
                    f"{citation_id}{marker}"
                )
        
        return annotated
```

#### 3. Verification API Endpoints (`backend/app/api/v1/verify.py`)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.core.verifier import CitationVerifier
from typing import List, Optional, Dict

router = APIRouter()

class VerifyRequest(BaseModel):
    text: str
    query_text: Optional[str] = None

class CitationResult(BaseModel):
    citation_id: str
    retrieval_id: str
    chunk_id: int
    similarity_score: float
    decision: str  # pass, partial, fail
    confidence: float
    chunk_text: str

class ClaimResult(BaseModel):
    claim_index: int
    claim_text: str
    original_text: str
    citations: List[CitationResult]
    overall_decision: Optional[str]

class VerifyResponse(BaseModel):
    claims: List[ClaimResult]
    overall_stats: Dict
    annotated_text: str

class SingleCitationRequest(BaseModel):
    claim_text: str
    chunk_id: int
    query_text: Optional[str] = None

class SingleCitationResponse(BaseModel):
    chunk_id: int
    similarity_score: float
    decision: str
    confidence: float
    chunk_text: str

@router.post("/run", response_model=VerifyResponse)
async def verify_claims(
    request: VerifyRequest,
    db: Session = Depends(get_db)
):
    """
    Verify all claims and citations in provided text.
    Returns annotated results with verification decisions.
    """
    if not request.text or len(request.text) < 10:
        raise HTTPException(status_code=400, detail="Text too short")
    
    verifier = CitationVerifier(db)
    results = verifier.verify_claims(request.text, request.query_text)
    
    return VerifyResponse(**results)

@router.post("/single", response_model=SingleCitationResponse)
async def verify_single_citation(
    request: SingleCitationRequest,
    db: Session = Depends(get_db)
):
    """
    Verify a single claim-citation pair.
    Useful for on-demand validation.
    """
    if not request.claim_text:
        raise HTTPException(status_code=400, detail="claim_text is required")
    
    verifier = CitationVerifier(db)
    result = verifier.verify_single_citation(
        claim_text=request.claim_text,
        chunk_id=request.chunk_id,
        query_text=request.query_text
    )
    
    if 'error' in result:
        raise HTTPException(status_code=404, detail=result['error'])
    
    return SingleCitationResponse(**result)

@router.get("/stats")
async def get_verification_stats(db: Session = Depends(get_db)):
    """
    Get overall verification statistics.
    """
    from app.db.models import Citation
    from sqlalchemy import func
    
    total = db.query(func.count(Citation.id)).scalar()
    
    pass_count = db.query(func.count(Citation.id)).filter(
        Citation.verifier_decision == "pass"
    ).scalar()
    
    partial_count = db.query(func.count(Citation.id)).filter(
        Citation.verifier_decision == "partial"
    ).scalar()
    
    fail_count = db.query(func.count(Citation.id)).filter(
        Citation.verifier_decision == "fail"
    ).scalar()
    
    accuracy = (pass_count / total * 100) if total > 0 else 0.0
    
    return {
        'total_verifications': total,
        'pass_count': pass_count,
        'partial_count': partial_count,
        'fail_count': fail_count,
        'accuracy': accuracy
    }
```

### Acceptance Criteria

**✅ Citation Parsing:**
- [ ] Regex correctly extracts citations in format `[slug:version:chunk_id]`
- [ ] Handles multiple citations in single sentence
- [ ] Ignores malformed citations
- [ ] Claim extraction splits text into logical units

**✅ Similarity Calculation:**
- [ ] Cosine similarity returns values in [-1, 1] range
- [ ] Normalized properly (L2 norm)
- [ ] Deterministic (same inputs → same outputs)
- [ ] Handles edge cases (zero vectors, identical texts)

**✅ Threshold-Based Decisions:**
- [ ] ≥0.80 → PASS
- [ ] 0.75-0.79 → PARTIAL
- [ ] <0.75 → FAIL
- [ ] Confidence scores calculated correctly

**✅ Verification Results:**
- [ ] All claims annotated with verification markers (✓⚠✗)
- [ ] Statistics accurate (counts, accuracy percentage)
- [ ] Results stored in citations table
- [ ] Audit log entries created

**✅ Performance:**
- [ ] Single verification: ≤500ms
- [ ] Batch verification (10 claims): ≤5 seconds
- [ ] No memory leaks during 1000 verifications

**✅ API Endpoints:**
- [ ] POST /api/v1/verify/run returns correct schema
- [ ] POST /api/v1/verify/single works for individual claims
- [ ] GET /api/v1/verify/stats returns accurate statistics
- [ ] Proper error handling for invalid inputs

**✅ Accuracy Target:**
- [ ] ≥90% pass rate on manually curated test set (20 claim-citation pairs)

### Technical Specifications

**Similarity Metric:**
- Cosine similarity: `dot(v1, v2) / (||v1|| * ||v2||)`
- Range: [-1, 1], but typically [0, 1] for text embeddings
- Threshold calibration based on all-MiniLM-L6-v2 characteristics

**Thresholds Rationale:**
- **0.80 (Pass)**: High semantic overlap, claim directly supported by chunk
- **0.75-0.80 (Partial)**: Related content, but claim may be extrapolated or partially unsupported
- **<0.75 (Fail)**: Low semantic similarity, citation likely incorrect or misleading

**Citation Format:**
- Pattern: `[source_slug:version:chunk_id]`
- Example: `[quantum-paper:v1.0:42]`
- Validation: Alphanumeric with hyphens/underscores for slug, semantic versioning for version, integer for chunk_id

### Testing Requirements

**Unit Tests:**
```python
def test_citation_extraction():
    text = "Quantum entanglement is proven [quantum-paper:v1.0:42]. Another claim [another-work:v2:15]."
    
    citations = CitationParser.extract_citations(text)
    
    assert len(citations) == 2
    assert citations[0]['chunk_id'] == 42
    assert citations[1]['source_slug'] == 'another-work'

def test_cosine_similarity():
    verifier = CitationVerifier(None)
    
    vec1 = np.array([1.0, 0.0, 0.0])
    vec2 = np.array([1.0, 0.0, 0.0])
    
    sim = verifier.cosine_similarity(vec1, vec2)
    assert sim == pytest.approx(1.0)
    
    vec3 = np.array([0.0, 1.0, 0.0])
    sim2 = verifier.cosine_similarity(vec1, vec3)
    assert sim2 == pytest.approx(0.0)

def test_threshold_decisions():
    verifier = CitationVerifier(db_session)
    
    # Mock high similarity → PASS
    high_sim_result = verifier.verify_single_citation("Test claim", chunk_id=1)
    # (Requires mocking embedder or using real data)
    
    assert high_sim_result['decision'] == VerifierDecision.PASS
```

**Integration Tests:**
```python
@pytest.mark.integration
def test_full_verification_pipeline(db_session):
    # Create test chunk
    chunk = Chunk(work_id=1, chunk_index=0, text="Quantum mechanics describes behavior of particles.")
    db_session.add(chunk)
    db_session.commit()
    
    # Verify claim
    verifier = CitationVerifier(db_session)
    text = "Particles behave according to quantum mechanics [test-work:v1:{}].".format(chunk.id)
    
    results = verifier.verify_claims(text)
    
    assert results['overall_stats']['total_citations'] == 1
    assert results['overall_stats']['pass_count'] >= 1  # Should pass due to high similarity
```

**Accuracy Validation:**
```python
# Create ground truth test set (manual curation)
TEST_CASES = [
    {
        'claim': "Water freezes at 0°C at sea level.",
        'chunk_text': "The freezing point of water is 0 degrees Celsius at standard atmospheric pressure.",
        'expected_decision': VerifierDecision.PASS
    },
    {
        'claim': "All birds can fly.",
        'chunk_text': "Most birds have the ability to fly using their wings.",
        'expected_decision': VerifierDecision.PARTIAL  # "All" is too strong
    },
    {
        'claim': "The Earth is flat.",
        'chunk_text': "Earth is an oblate spheroid with equatorial radius of 6378 km.",
        'expected_decision': VerifierDecision.FAIL
    },
    # ... (add 17 more cases)
]

@pytest.mark.accuracy
def test_verifier_accuracy(db_session):
    verifier = CitationVerifier(db_session)
    
    correct = 0
    for case in TEST_CASES:
        # Create temporary chunk
        chunk = Chunk(work_id=1, chunk_index=0, text=case['chunk_text'])
        db_session.add(chunk)
        db_session.commit()
        
        result = verifier.verify_single_citation(case['claim'], chunk.id)
        
        if result['decision'] == case['expected_decision']:
            correct += 1
    
    accuracy = correct / len(TEST_CASES) * 100
    assert accuracy >= 90.0, f"Verifier accuracy {accuracy}% below 90% threshold"
```

### Dependencies

**No new packages required** - uses existing:
- sentence-transformers (embeddings)
- numpy (cosine similarity)
- sqlalchemy (database operations)

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Threshold calibration incorrect | High | Validate with diverse test set; allow threshold configuration |
| Embedding quality affects similarity | High | Use high-quality models (all-MiniLM-L6-v2 proven); consider model upgrades |
| Claim extraction misses nuanced statements | Medium | Use advanced NLP (spaCy) for sentence segmentation |
| High false positive rate | Medium | Lower pass threshold to 0.85; add human review for critical applications |

---

Due to character limits, I'll continue with the remaining phases in my next message. The document continues with:

- Phase 6: Session Management System
- Phase 7: Immutable Audit Trail
- Phase 8: Frontend Development  
- Phase 9: Docker Deployment
- Phase 10: Pilot Validation

---

## PHASE 6: Session Management System

**Duration:** 5 days  
**Dependencies:** Phases 4 & 5 complete  
**Risk Level:** Medium  

### Objectives

1. Implement session state model (condensed_summary, accepted_claims, top_citations)
2. Create checkpoint creation logic with parent linkage
3. Build state serialization to JSON format
4. Develop rehydration algorithm to reconstruct context from checkpoints
5. Implement top 10-20 chunk retrieval for context restoration
6. Build API endpoints for checkpoint/rehydrate operations
7. Track session history and enable session restoration

### Deliverables

#### 1. Session State Manager (`backend/app/core/checkpoint.py`)

```python
from typing import List, Dict, Optional
from sqlalchemy.orm import Session
from app.db.models import Session as SessionModel, Chunk, Citation
from app.core.retrieval import HybridRetriever
import json
from datetime import datetime
import hashlib
import structlog

logger = structlog.get_logger()

class SessionStateManager:
    """
    Manages session state including checkpoints and rehydration.
    Enables context preservation across interactions.
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.retriever = HybridRetriever(db)
    
    def create_checkpoint(
        self,
        session_id: str,
        condensed_summary: str,
        accepted_claims: List[Dict],
        top_citations: List[str],
        checkpoint_name: Optional[str] = None,
        parent_checkpoint_id: Optional[int] = None
    ) -> SessionModel:
        """
        Create a session checkpoint with current state.
        
        Args:
            session_id: Unique session identifier
            condensed_summary: Aggregated context summary
            accepted_claims: List of verified claims with metadata
            top_citations: Top 10-20 retrieval_ids for context
            checkpoint_name: Optional human-readable name
            parent_checkpoint_id: Link to previous checkpoint
        
        Returns:
            SessionModel object
        """
        logger.info(
            "Creating checkpoint",
            session_id=session_id,
            claims_count=len(accepted_claims),
            citations_count=len(top_citations)
        )
        
        # Build full state JSON
        state_json = {
            'condensed_summary': condensed_summary,
            'accepted_claims': accepted_claims,
            'top_citations': top_citations,
            'timestamp': datetime.utcnow().isoformat(),
            'parent_checkpoint_id': parent_checkpoint_id,
            'metadata': {
                'total_claims': len(accepted_claims),
                'total_citations': len(top_citations),
                'summary_length': len(condensed_summary)
            }
        }
        
        # Create session record
        checkpoint = SessionModel(
            session_id=session_id,
            condensed_summary=condensed_summary,
            accepted_claims=accepted_claims,
            top_citations=top_citations,
            parent_checkpoint_id=parent_checkpoint_id,
            is_checkpoint=True,
            checkpoint_name=checkpoint_name or f"Checkpoint {datetime.utcnow().isoformat()}",
            state_json=state_json,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        self.db.add(checkpoint)
        self.db.commit()
        
        logger.info("Checkpoint created", checkpoint_id=checkpoint.id)
        return checkpoint
    
    def rehydrate_session(
        self,
        checkpoint_id: int,
        include_full_chunks: bool = True
    ) -> Dict:
        """
        Reconstruct session context from checkpoint.
        
        Args:
            checkpoint_id: ID of checkpoint to restore
            include_full_chunks: Whether to retrieve full chunk texts
        
        Returns:
            {
                'session_id': str,
                'checkpoint_name': str,
                'condensed_summary': str,
                'accepted_claims': List[Dict],
                'top_citations': List[str],
                'chunks': List[Dict] (if include_full_chunks),
                'context_overlap': float (percentage of retrieved chunks)
            }
        """
        logger.info("Rehydrating session", checkpoint_id=checkpoint_id)
        
        # Retrieve checkpoint
        checkpoint = self.db.query(SessionModel).filter(
            SessionModel.id == checkpoint_id
        ).first()
        
        if not checkpoint:
            raise ValueError(f"Checkpoint {checkpoint_id} not found")
        
        # Base rehydration data
        rehydrated = {
            'session_id': checkpoint.session_id,
            'checkpoint_id': checkpoint.id,
            'checkpoint_name': checkpoint.checkpoint_name,
            'condensed_summary': checkpoint.condensed_summary,
            'accepted_claims': checkpoint.accepted_claims,
            'top_citations': checkpoint.top_citations,
            'created_at': checkpoint.created_at.isoformat()
        }
        
        # Retrieve full chunks if requested
        if include_full_chunks:
            chunks_data = self._retrieve_chunks_from_citations(checkpoint.top_citations)
            rehydrated['chunks'] = chunks_data
            
            # Calculate context overlap (chunks successfully retrieved)
            overlap = len(chunks_data) / len(checkpoint.top_citations) * 100 if checkpoint.top_citations else 0
            rehydrated['context_overlap'] = overlap
            
            logger.info("Context rehydrated", overlap=f"{overlap:.1f}%")
        
        return rehydrated
    
    def _retrieve_chunks_from_citations(self, citation_ids: List[str]) -> List[Dict]:
        """
        Retrieve full chunk data from retrieval_ids.
        
        Args:
            citation_ids: List of retrieval_ids (slug:version:chunk_id)
        
        Returns:
            List of chunk dictionaries with text and metadata
        """
        chunks = []
        
        for citation_id in citation_ids:
            try:
                # Parse citation_id
                parts = citation_id.split(':')
                if len(parts) != 3:
                    logger.warning("Invalid citation format", citation_id=citation_id)
                    continue
                
                source_slug, version, chunk_id_str = parts
                chunk_id = int(chunk_id_str)
                
                # Retrieve chunk
                chunk = self.db.query(Chunk).filter(Chunk.id == chunk_id).first()
                
                if chunk:
                    chunks.append({
                        'retrieval_id': citation_id,
                        'chunk_id': chunk.id,
                        'text': chunk.text,
                        'chunk_index': chunk.chunk_index,
                        'token_count': chunk.token_count
                    })
                else:
                    logger.warning("Chunk not found", chunk_id=chunk_id)
            
            except Exception as e:
                logger.error("Error retrieving chunk", error=str(e), citation_id=citation_id)
        
        return chunks
    
    def get_session_history(self, session_id: str) -> List[SessionModel]:
        """
        Retrieve all checkpoints for a session in chronological order.
        """
        checkpoints = self.db.query(SessionModel).filter(
            SessionModel.session_id == session_id,
            SessionModel.is_checkpoint == True
        ).order_by(SessionModel.created_at).all()
        
        return checkpoints
    
    def update_session_state(
        self,
        session_id: str,
        condensed_summary: Optional[str] = None,
        new_claims: Optional[List[Dict]] = None,
        new_citations: Optional[List[str]] = None
    ):
        """
        Update active session state (non-checkpoint).
        Used for incremental updates during conversation.
        """
        session = self.db.query(SessionModel).filter(
            SessionModel.session_id == session_id,
            SessionModel.is_checkpoint == False
        ).order_by(SessionModel.updated_at.desc()).first()
        
        if not session:
            # Create new active session
            session = SessionModel(
                session_id=session_id,
                is_checkpoint=False,
                condensed_summary=condensed_summary or "",
                accepted_claims=new_claims or [],
                top_citations=new_citations or [],
                state_json={}
            )
            self.db.add(session)
        else:
            # Update existing session
            if condensed_summary:
                session.condensed_summary = condensed_summary
            
            if new_claims:
                session.accepted_claims = (session.accepted_claims or []) + new_claims
            
            if new_citations:
                # Keep only top 20 most recent
                all_citations = (session.top_citations or []) + new_citations
                session.top_citations = list(dict.fromkeys(all_citations))[:20]  # Deduplicate and limit
            
            session.updated_at = datetime.utcnow()
        
        self.db.commit()
        logger.info("Session state updated", session_id=session_id)
```

#### 2. Session API Endpoints (`backend/app/api/v1/session.py`)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from pydantic import BaseModel
from app.db.session import get_db
from app.core.checkpoint import SessionStateManager
from typing import List, Optional, Dict
from datetime import datetime

router = APIRouter()

class CreateCheckpointRequest(BaseModel):
    session_id: str
    condensed_summary: str
    accepted_claims: List[Dict]
    top_citations: List[str]
    checkpoint_name: Optional[str] = None
    parent_checkpoint_id: Optional[int] = None

class CreateCheckpointResponse(BaseModel):
    checkpoint_id: int
    session_id: str
    checkpoint_name: str
    created_at: str
    message: str

class RehydrateRequest(BaseModel):
    checkpoint_id: int
    include_full_chunks: bool = True

class RehydrateResponse(BaseModel):
    session_id: str
    checkpoint_id: int
    checkpoint_name: str
    condensed_summary: str
    accepted_claims: List[Dict]
    top_citations: List[str]
    chunks: Optional[List[Dict]] = None
    context_overlap: Optional[float] = None
    created_at: str

class SessionHistoryItem(BaseModel):
    checkpoint_id: int
    checkpoint_name: str
    created_at: str
    claims_count: int
    citations_count: int

class SessionHistoryResponse(BaseModel):
    session_id: str
    checkpoints: List[SessionHistoryItem]
    total_checkpoints: int

@router.post("/checkpoint", response_model=CreateCheckpointResponse)
async def create_checkpoint(
    request: CreateCheckpointRequest,
    db: DBSession = Depends(get_db)
):
    """
    Create a session checkpoint.
    Preserves current state for later restoration.
    """
    if not request.session_id:
        raise HTTPException(status_code=400, detail="session_id is required")
    
    if not request.top_citations:
        raise HTTPException(status_code=400, detail="top_citations cannot be empty")
    
    manager = SessionStateManager(db)
    
    checkpoint = manager.create_checkpoint(
        session_id=request.session_id,
        condensed_summary=request.condensed_summary,
        accepted_claims=request.accepted_claims,
        top_citations=request.top_citations,
        checkpoint_name=request.checkpoint_name,
        parent_checkpoint_id=request.parent_checkpoint_id
    )
    
    return CreateCheckpointResponse(
        checkpoint_id=checkpoint.id,
        session_id=checkpoint.session_id,
        checkpoint_name=checkpoint.checkpoint_name,
        created_at=checkpoint.created_at.isoformat(),
        message="Checkpoint created successfully"
    )

@router.post("/rehydrate", response_model=RehydrateResponse)
async def rehydrate_session(
    request: RehydrateRequest,
    db: DBSession = Depends(get_db)
):
    """
    Restore session context from checkpoint.
    Reconstructs conversation state and retrieves chunks.
    """
    manager = SessionStateManager(db)
    
    try:
        rehydrated = manager.rehydrate_session(
            checkpoint_id=request.checkpoint_id,
            include_full_chunks=request.include_full_chunks
        )
        
        return RehydrateResponse(**rehydrated)
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/history/{session_id}", response_model=SessionHistoryResponse)
async def get_session_history(
    session_id: str,
    db: DBSession = Depends(get_db)
):
    """
    Retrieve all checkpoints for a session.
    Shows chronological history of saved states.
    """
    manager = SessionStateManager(db)
    checkpoints = manager.get_session_history(session_id)
    
    history_items = [
        SessionHistoryItem(
            checkpoint_id=cp.id,
            checkpoint_name=cp.checkpoint_name,
            created_at=cp.created_at.isoformat(),
            claims_count=len(cp.accepted_claims or []),
            citations_count=len(cp.top_citations or [])
        )
        for cp in checkpoints
    ]
    
    return SessionHistoryResponse(
        session_id=session_id,
        checkpoints=history_items,
        total_checkpoints=len(checkpoints)
    )

@router.put("/update")
async def update_session_state(
    session_id: str,
    condensed_summary: Optional[str] = None,
    new_claims: Optional[List[Dict]] = None,
    new_citations: Optional[List[str]] = None,
    db: DBSession = Depends(get_db)
):
    """
    Update active session state incrementally.
    """
    if not any([condensed_summary, new_claims, new_citations]):
        raise HTTPException(status_code=400, detail="At least one update field required")
    
    manager = SessionStateManager(db)
    manager.update_session_state(
        session_id=session_id,
        condensed_summary=condensed_summary,
        new_claims=new_claims,
        new_citations=new_citations
    )
    
    return {"message": "Session state updated", "session_id": session_id}
```

### Acceptance Criteria

**✅ Checkpoint Creation:**
- [ ] Checkpoint stored with all required fields
- [ ] Parent-child relationship preserved
- [ ] State JSON serializable and valid
- [ ] Timestamp recorded accurately

**✅ Rehydration:**
- [ ] Checkpoint data retrieved correctly
- [ ] Chunks fetched from retrieval_ids
- [ ] Context overlap ≥95% for valid checkpoints
- [ ] Missing chunks handled gracefully

**✅ Session History:**
- [ ] All checkpoints for session retrieved in order
- [ ] Chronological sorting works
- [ ] Metadata accurate (counts, timestamps)

**✅ State Updates:**
- [ ] Incremental updates don't overwrite existing data
- [ ] Top citations limited to 20 (most recent)
- [ ] Deduplication works for citations

**✅ Performance:**
- [ ] Checkpoint creation: ≤100ms
- [ ] Rehydration (20 chunks): ≤2 seconds
- [ ] History retrieval: ≤50ms

**✅ API Endpoints:**
- [ ] POST /api/v1/session/checkpoint works
- [ ] POST /api/v1/session/rehydrate works
- [ ] GET /api/v1/session/history/{id} works
- [ ] PUT /api/v1/session/update works

### Technical Specifications

**Checkpoint State Schema:**
```json
{
  "condensed_summary": "string (aggregated context)",
  "accepted_claims": [
    {
      "claim_text": "string",
      "verification_status": "pass|partial|fail",
      "citations": ["retrieval_id1", "retrieval_id2"]
    }
  ],
  "top_citations": ["slug:version:chunk_id", ...],
  "timestamp": "ISO 8601",
  "parent_checkpoint_id": "integer or null",
  "metadata": {
    "total_claims": "integer",
    "total_citations": "integer",
    "summary_length": "integer"
  }
}
```

**Rehydration Algorithm:**
1. Retrieve checkpoint record from database
2. Parse top_citations list
3. Query chunks table for each citation
4. Assemble full context with chunk texts
5. Calculate overlap percentage
6. Return structured response

**Context Overlap Calculation:**
```
overlap = (successfully_retrieved_chunks / total_citations) * 100
```
- Target: ≥95% overlap
- Acceptable: ≥90% overlap
- Warning: <90% overlap (some chunks missing)

### Testing Requirements

**Unit Tests:**
```python
def test_checkpoint_creation(db_session):
    manager = SessionStateManager(db_session)
    
    checkpoint = manager.create_checkpoint(
        session_id="test-session-1",
        condensed_summary="Summary of conversation",
        accepted_claims=[{"claim": "Test claim", "status": "pass"}],
        top_citations=["work1:v1:1", "work1:v1:2"]
    )
    
    assert checkpoint.id is not None
    assert checkpoint.session_id == "test-session-1"
    assert len(checkpoint.top_citations) == 2

def test_rehydration_with_valid_chunks(db_session):
    # Create test chunks
    chunk1 = Chunk(work_id=1, chunk_index=0, text="Chunk 1 text")
    chunk2 = Chunk(work_id=1, chunk_index=1, text="Chunk 2 text")
    db_session.add_all([chunk1, chunk2])
    db_session.commit()
    
    # Create checkpoint
    manager = SessionStateManager(db_session)
    checkpoint = manager.create_checkpoint(
        session_id="test",
        condensed_summary="Test",
        accepted_claims=[],
        top_citations=[f"work1:v1:{chunk1.id}", f"work1:v1:{chunk2.id}"]
    )
    
    # Rehydrate
    rehydrated = manager.rehydrate_session(checkpoint.id)
    
    assert rehydrated['context_overlap'] >= 95.0
    assert len(rehydrated['chunks']) == 2

def test_session_history(db_session):
    manager = SessionStateManager(db_session)
    
    # Create multiple checkpoints
    for i in range(3):
        manager.create_checkpoint(
            session_id="multi-checkpoint",
            condensed_summary=f"Summary {i}",
            accepted_claims=[],
            top_citations=[]
        )
    
    history = manager.get_session_history("multi-checkpoint")
    
    assert len(history) == 3
    assert history[0].created_at < history[1].created_at < history[2].created_at
```

### Dependencies

**No new packages required** - uses existing SQLAlchemy, JSON serialization

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Large state JSON causes storage issues | Medium | Limit top_citations to 20; compress summaries |
| Chunks deleted before rehydration | High | Add soft delete; validate chunk existence during rehydration |
| Session history grows unbounded | Low | Implement checkpoint expiration policy (30 days) |

---

## PHASE 7: Immutable Audit Trail

**Duration:** 4 days  
**Dependencies:** All previous phases  
**Risk Level:** Low  

### Objectives

1. Design append-only JSONL log format for audit events
2. Implement SHA256 chain linking for tamper detection
3. Define event types (retrieval, ingestion, verification, checkpoint, query)
4. Build S3 storage with object immutability (production)
5. Create correlation ID system for request tracking
6. Add timestamp and metadata to all events
7. Build query API for audit logs with filtering
8. Implement log rotation and archival strategy

### Deliverables

#### 1. Audit Logger (`backend/app/utils/audit_log.py`)

```python
from typing import Dict, Optional, List
from datetime import datetime
import hashlib
import json
import uuid
from app.storage.s3_client import s3_client
from app.config import settings
import structlog

logger = structlog.get_logger()

class AuditLogger:
    """
    Immutable audit trail with SHA256 chain linking.
    Events stored as append-only JSONL in S3.
    """
    
    def __init__(self):
        self.s3_client = s3_client
        self.log_prefix = "audit-logs"
        self.last_hash = None  # In-memory cache of last event hash
    
    def _generate_event_hash(self, event: Dict) -> str:
        """
        Generate SHA256 hash of event.
        Includes previous hash for chain linking.
        """
        # Serialize event deterministically
        event_string = json.dumps(event, sort_keys=True)
        
        # Include previous hash in chain
        if self.last_hash:
            event_string = f"{self.last_hash}{event_string}"
        
        hash_value = hashlib.sha256(event_string.encode('utf-8')).hexdigest()
        return hash_value
    
    def log_event(
        self,
        event_type: str,
        action: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
        user_id: Optional[str] = None,
        correlation_id: Optional[str] = None,
        status: str = "success",
        error_message: Optional[str] = None,
        duration_ms: Optional[int] = None
    ) -> str:
        """
        Log an audit event.
        
        Args:
            event_type: Type of event (retrieval, ingestion, verification, etc.)
            action: Specific action taken
            resource_type: Type of resource affected
            resource_id: ID of resource
            metadata: Additional event data
            user_id: User identifier (if applicable)
            correlation_id: Request correlation ID
            status: success or failure
            error_message: Error details if status=failure
            duration_ms: Execution time in milliseconds
        
        Returns:
            Event hash (for verification)
        """
        # Generate correlation ID if not provided
        if not correlation_id:
            correlation_id = str(uuid.uuid4())
        
        # Build event structure
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "action": action,
            "resource_type": resource_type,
            "resource_id": resource_id,
            "user_id": user_id,
            "correlation_id": correlation_id,
            "status": status,
            "error_message": error_message,
            "duration_ms": duration_ms,
            "metadata": metadata or {},
            "previous_hash": self.last_hash
        }
        
        # Generate hash
        event_hash = self._generate_event_hash(event)
        event["event_hash"] = event_hash
        
        # Update last hash
        self.last_hash = event_hash
        
        # Write to S3 (append to daily log file)
        log_key = self._get_log_key()
        try:
            self.s3_client.append_jsonl(event, log_key)
            logger.info(
                "Audit event logged",
                event_type=event_type,
                correlation_id=correlation_id,
                event_hash=event_hash[:8]
            )
        except Exception as e:
            logger.error("Failed to write audit log", error=str(e))
            # Don't fail the main operation, but log the error
        
        return event_hash
    
    def _get_log_key(self) -> str:
        """
        Generate S3 key for current day's log file.
        Format: audit-logs/YYYY/MM/DD/audit.jsonl
        """
        now = datetime.utcnow()
        return f"{self.log_prefix}/{now.year}/{now.month:02d}/{now.day:02d}/audit.jsonl"
    
    def verify_chain(self, events: List[Dict]) -> bool:
        """
        Verify integrity of event chain.
        Recalculates hashes and checks consistency.
        
        Returns:
            True if chain is valid, False if tampered
        """
        prev_hash = None
        
        for event in events:
            # Store and remove hash from event
            stored_hash = event.pop("event_hash")
            stored_prev_hash = event.get("previous_hash")
            
            # Verify previous hash matches
            if stored_prev_hash != prev_hash:
                logger.warning("Chain broken: previous hash mismatch")
                return False
            
            # Recalculate hash
            event_string = json.dumps(event, sort_keys=True)
            if prev_hash:
                event_string = f"{prev_hash}{event_string}"
            
            calculated_hash = hashlib.sha256(event_string.encode('utf-8')).hexdigest()
            
            # Verify hash matches
            if calculated_hash != stored_hash:
                logger.warning("Chain broken: hash mismatch", event_id=event.get("event_id"))
                return False
            
            # Update for next iteration
            prev_hash = stored_hash
            event["event_hash"] = stored_hash  # Restore hash
        
        logger.info("Chain verified", events_count=len(events))
        return True
    
    def query_logs(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        event_type: Optional[str] = None,
        correlation_id: Optional[str] = None,
        user_id: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict]:
        """
        Query audit logs with filters.
        
        Returns:
            List of matching events
        """
        # Determine date range for S3 keys
        if not start_date:
            start_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        
        if not end_date:
            end_date = datetime.utcnow()
        
        # Iterate through days in range
        events = []
        current_date = start_date
        
        while current_date <= end_date and len(events) < limit:
            log_key = f"{self.log_prefix}/{current_date.year}/{current_date.month:02d}/{current_date.day:02d}/audit.jsonl"
            
            try:
                # Download log file
                log_data = self.s3_client.download_file(log_key).decode('utf-8')
                
                # Parse JSONL
                for line in log_data.strip().split('\n'):
                    if not line:
                        continue
                    
                    event = json.loads(line)
                    
                    # Apply filters
                    if event_type and event.get('event_type') != event_type:
                        continue
                    
                    if correlation_id and event.get('correlation_id') != correlation_id:
                        continue
                    
                    if user_id and event.get('user_id') != user_id:
                        continue
                    
                    events.append(event)
                    
                    if len(events) >= limit:
                        break
            
            except Exception as e:
                logger.debug("Log file not found or error", key=log_key, error=str(e))
            
            # Move to next day
            from datetime import timedelta
            current_date += timedelta(days=1)
        
        return events[:limit]

# Global audit logger instance
audit_logger = AuditLogger()
```

#### 2. Audit Middleware (`backend/app/api/middleware/audit.py`)

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.audit_log import audit_logger
import time
import uuid

class AuditMiddleware(BaseHTTPMiddleware):
    """
    Middleware to automatically log API requests.
    """
    
    async def dispatch(self, request: Request, call_next):
        # Generate correlation ID
        correlation_id = str(uuid.uuid4())
        request.state.correlation_id = correlation_id
        
        # Record start time
        start_time = time.time()
        
        # Determine event type from path
        path = request.url.path
        if '/query' in path:
            event_type = 'query'
        elif '/ingest' in path:
            event_type = 'ingestion'
        elif '/verify' in path:
            event_type = 'verification'
        elif '/session' in path:
            event_type = 'checkpoint'
        else:
            event_type = 'api_request'
        
        # Process request
        try:
            response = await call_next(request)
            
            # Calculate duration
            duration_ms = int((time.time() - start_time) * 1000)
            
            # Log successful request
            audit_logger.log_event(
                event_type=event_type,
                action=f"{request.method} {path}",
                resource_type="api_endpoint",
                resource_id=path,
                correlation_id=correlation_id,
                status="success",
                duration_ms=duration_ms,
                metadata={
                    "method": request.method,
                    "status_code": response.status_code,
                    "client_host": request.client.host if request.client else None
                }
            )
            
            return response
        
        except Exception as e:
            # Log failed request
            duration_ms = int((time.time() - start_time) * 1000)
            
            audit_logger.log_event(
                event_type=event_type,
                action=f"{request.method} {path}",
                resource_type="api_endpoint",
                resource_id=path,
                correlation_id=correlation_id,
                status="failure",
                error_message=str(e),
                duration_ms=duration_ms
            )
            
            raise
```

#### 3. Audit API Endpoints (`backend/app/api/v1/audit.py`)

```python
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.utils.audit_log import audit_logger
from typing import List, Optional
from datetime import datetime, timedelta

router = APIRouter()

class AuditEvent(BaseModel):
    timestamp: str
    event_id: str
    event_type: str
    action: str
    resource_type: Optional[str]
    resource_id: Optional[str]
    user_id: Optional[str]
    correlation_id: str
    status: str
    error_message: Optional[str]
    duration_ms: Optional[int]
    metadata: dict
    event_hash: str
    previous_hash: Optional[str]

class AuditQueryResponse(BaseModel):
    events: List[AuditEvent]
    total_count: int
    start_date: str
    end_date: str

class VerifyChainRequest(BaseModel):
    events: List[AuditEvent]

class VerifyChainResponse(BaseModel):
    is_valid: bool
    message: str
    total_events: int

@router.get("/events", response_model=AuditQueryResponse)
async def query_audit_logs(
    start_date: Optional[str] = Query(None, description="ISO 8601 format"),
    end_date: Optional[str] = Query(None, description="ISO 8601 format"),
    event_type: Optional[str] = None,
    correlation_id: Optional[str] = None,
    user_id: Optional[str] = None,
    limit: int = Query(100, le=1000)
):
    """
    Query audit logs with filters.
    Returns matching events in chronological order.
    """
    # Parse dates
    start_dt = datetime.fromisoformat(start_date.replace('Z', '')) if start_date else None
    end_dt = datetime.fromisoformat(end_date.replace('Z', '')) if end_date else None
    
    # Query logs
    events = audit_logger.query_logs(
        start_date=start_dt,
        end_date=end_dt,
        event_type=event_type,
        correlation_id=correlation_id,
        user_id=user_id,
        limit=limit
    )
    
    return AuditQueryResponse(
        events=events,
        total_count=len(events),
        start_date=start_dt.isoformat() if start_dt else datetime.utcnow().replace(hour=0, minute=0).isoformat(),
        end_date=end_dt.isoformat() if end_dt else datetime.utcnow().isoformat()
    )

@router.post("/verify-chain", response_model=VerifyChainResponse)
async def verify_event_chain(request: VerifyChainRequest):
    """
    Verify integrity of event chain.
    Checks SHA256 hashes to detect tampering.
    """
    events = [event.dict() for event in request.events]
    
    is_valid = audit_logger.verify_chain(events)
    
    return VerifyChainResponse(
        is_valid=is_valid,
        message="Chain is valid" if is_valid else "Chain integrity compromised",
        total_events=len(events)
    )

@router.get("/stats")
async def get_audit_stats():
    """
    Get audit log statistics.
    """
    # Query recent events (last 24 hours)
    yesterday = datetime.utcnow() - timedelta(days=1)
    events = audit_logger.query_logs(start_date=yesterday, limit=10000)
    
    # Calculate statistics
    event_types = {}
    success_count = 0
    failure_count = 0
    total_duration = 0
    
    for event in events:
        event_type = event.get('event_type', 'unknown')
        event_types[event_type] = event_types.get(event_type, 0) + 1
        
        if event.get('status') == 'success':
            success_count += 1
        else:
            failure_count += 1
        
        if event.get('duration_ms'):
            total_duration += event['duration_ms']
    
    avg_duration = total_duration / len(events) if events else 0
    
    return {
        'total_events_24h': len(events),
        'event_types': event_types,
        'success_count': success_count,
        'failure_count': failure_count,
        'success_rate': success_count / len(events) * 100 if events else 0,
        'average_duration_ms': avg_duration
    }
```

### Acceptance Criteria

**✅ Event Logging:**
- [ ] All API requests logged automatically via middleware
- [ ] JSONL format valid (one JSON object per line)
- [ ] All required fields present (timestamp, event_type, correlation_id, etc.)
- [ ] S3 write succeeds for all events

**✅ Chain Linking:**
- [ ] SHA256 hashes generated correctly
- [ ] Previous hash included in each event
- [ ] Chain verification detects tampering (manual edit test)
- [ ] First event has null previous_hash

**✅ Correlation Tracking:**
- [ ] Correlation IDs generated for all requests
- [ ] Related events share same correlation_id
- [ ] Query by correlation_id returns all related events

**✅ S3 Storage:**
- [ ] Daily log files created (YYYY/MM/DD structure)
- [ ] Append operation works (no overwrites)
- [ ] Object immutability enabled (production)

**✅ Query API:**
- [ ] Date range filtering works
- [ ] Event type filtering works
- [ ] Correlation ID filtering works
- [ ] Limit parameter respected

**✅ Performance:**
- [ ] Logging doesn't add >10ms to request latency
- [ ] Query returns results in ≤500ms for 24-hour window
- [ ] No memory leaks during 10k events

**✅ API Endpoints:**
- [ ] GET /api/v1/audit/events returns events
- [ ] POST /api/v1/audit/verify-chain validates integrity
- [ ] GET /api/v1/audit/stats returns statistics

### Technical Specifications

**JSONL Event Schema:**
```json
{
  "timestamp": "2025-10-24T12:34:56.789Z",
  "event_id": "uuid",
  "event_type": "retrieval|ingestion|verification|checkpoint|query",
  "action": "string describing action",
  "resource_type": "api_endpoint|work|chunk|session",
  "resource_id": "string identifier",
  "user_id": "string or null",
  "correlation_id": "uuid",
  "status": "success|failure",
  "error_message": "string or null",
  "duration_ms": "integer or null",
  "metadata": {},
  "event_hash": "sha256 hex",
  "previous_hash": "sha256 hex or null"
}
```

**Hash Calculation:**
```python
event_string = json.dumps(event, sort_keys=True)
if previous_hash:
    event_string = f"{previous_hash}{event_string}"
hash = hashlib.sha256(event_string.encode('utf-8')).hexdigest()
```

**S3 Object Immutability:**
- Production: Enable S3 Object Lock with retention period
- Development: MinIO supports immutability via bucket policy
- Prevents deletion or modification of audit logs

### Testing Requirements

**Unit Tests:**
```python
def test_event_hashing():
    logger = AuditLogger()
    
    event1 = {
        "event_type": "query",
        "action": "search",
        "timestamp": "2025-10-24T00:00:00Z"
    }
    
    hash1 = logger._generate_event_hash(event1)
    hash2 = logger._generate_event_hash(event1)
    
    assert hash1 == hash2  # Deterministic
    assert len(hash1) == 64  # SHA256 hex length

def test_chain_verification():
    logger = AuditLogger()
    
    events = []
    for i in range(5):
        event_hash = logger.log_event(
            event_type="test",
            action=f"test_action_{i}",
            correlation_id="test-correlation"
        )
        # Mock event retrieval
        events.append({
            "event_type": "test",
            "action": f"test_action_{i}",
            "event_hash": event_hash,
            "previous_hash": logger.last_hash
        })
    
    # Verify valid chain
    assert logger.verify_chain(events) == True
    
    # Tamper with an event
    events[2]["action"] = "tampered"
    assert logger.verify_chain(events) == False
```

### Dependencies

**No new packages required** - uses hashlib, json, uuid (stdlib)

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| S3 write failures lose audit events | High | Add local backup log; retry logic; alert on failures |
| Log files grow too large | Medium | Daily rotation; compression; archival to Glacier |
| Chain verification is slow | Low | Optimize JSON parsing; limit verification to suspicious cases |

---

## PHASE 8: Next.js Frontend Development

**Duration:** 14 days  
**Dependencies:** All backend phases complete  
**Risk Level:** Medium  

### Objectives

1. Build Next.js 14 application with App Router
2. Configure Tailwind CSS and shadcn/ui components
3. Implement 7 main pages (Dashboard, Repository Manager, Query Interface, Knowledge Graph, Session Manager, Audit Log Viewer, Verifier Dashboard)
4. Create reusable component library
5. Integrate API client for backend communication
6. Add responsive design for mobile/tablet/desktop
7. Implement authentication (optional admin login)
8. Add loading states and error handling

### Deliverables

#### 1. API Client (`frontend/lib/api-client.ts`)

```typescript
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export class APIClient {
  private baseURL: string;

  constructor(baseURL: string = API_BASE_URL) {
    this.baseURL = baseURL;
  }

  private async request<T>(
    endpoint: string,
    options?: RequestInit
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`;
    
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options?.headers,
      },
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(error.detail || `HTTP ${response.status}`);
    }

    return response.json();
  }

  // Ingestion
  async ingestWork(data: {
    repo_url: string;
    target_file: string;
    source_slug: string;
    version: string;
    branch?: string;
  }) {
    return this.request('/ingest/add-work', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async getJobStatus(jobId: string) {
    return this.request(`/ingest/job/${jobId}`);
  }

  // Query
  async query(data: {
    query: string;
    top_k?: number;
    filters?: Record<string, any>;
    include_context?: boolean;
    include_summaries?: boolean;
  }) {
    return this.request('/query', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  // Verification
  async verifyClaims(data: { text: string; query_text?: string }) {
    return this.request('/verify/run', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  // Session
  async createCheckpoint(data: {
    session_id: string;
    condensed_summary: string;
    accepted_claims: any[];
    top_citations: string[];
    checkpoint_name?: string;
  }) {
    return this.request('/session/checkpoint', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async rehydrateSession(data: {
    checkpoint_id: number;
    include_full_chunks?: boolean;
  }) {
    return this.request('/session/rehydrate', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async getSessionHistory(sessionId: string) {
    return this.request(`/session/history/${sessionId}`);
  }

  // Audit
  async getAuditEvents(params: {
    start_date?: string;
    end_date?: string;
    event_type?: string;
    correlation_id?: string;
    limit?: number;
  }) {
    const query = new URLSearchParams(params as any).toString();
    return this.request(`/audit/events?${query}`);
  }

  async getAuditStats() {
    return this.request('/audit/stats');
  }
}

export const apiClient = new APIClient();
```

#### 2. Key Components

**Citation Badge** (`frontend/components/CitationBadge.tsx`):
```typescript
import { Badge } from '@/components/ui/badge';
import { CheckCircle, AlertCircle, XCircle } from 'lucide-react';

interface CitationBadgeProps {
  decision: 'pass' | 'partial' | 'fail';
  score: number;
}

export function CitationBadge({ decision, score }: CitationBadgeProps) {
  const config = {
    pass: {
      icon: CheckCircle,
      className: 'bg-green-100 text-green-800 border-green-300',
      label: 'Verified',
    },
    partial: {
      icon: AlertCircle,
      className: 'bg-yellow-100 text-yellow-800 border-yellow-300',
      label: 'Partial',
    },
    fail: {
      icon: XCircle,
      className: 'bg-red-100 text-red-800 border-red-300',
      label: 'Failed',
    },
  };

  const { icon: Icon, className, label } = config[decision];

  return (
    <Badge variant="outline" className={className}>
      <Icon className="w-3 h-3 mr-1" />
      {label} ({(score * 100).toFixed(0)}%)
    </Badge>
  );
}
```

**Metrics Card** (`frontend/components/MetricsCard.tsx`):
```typescript
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { LucideIcon } from 'lucide-react';

interface MetricsCardProps {
  title: string;
  value: string | number;
  change?: string;
  icon: LucideIcon;
  description?: string;
}

export function MetricsCard({ title, value, change, icon: Icon, description }: MetricsCardProps) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        <Icon className="h-4 w-4 text-muted-foreground" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
        {change && (
          <p className="text-xs text-muted-foreground">
            {change} from last period
          </p>
        )}
        {description && (
          <p className="text-xs text-muted-foreground mt-2">{description}</p>
        )}
      </CardContent>
    </Card>
  );
}
```

#### 3. Main Pages

**Dashboard** (`frontend/app/dashboard/page.tsx`):
- System health indicators (API, DB, S3 status)
- Ingestion progress (active jobs, completed works)
- Query performance metrics (latency, throughput)
- Verification accuracy stats
- Recent activity feed

**Query Interface** (`frontend/app/query/page.tsx`):
- Search bar with filters
- Results list with:
  - Chunk preview (first 200 chars)
  - Citation badges
  - Expand to full text
  - Context window toggle
  - Short summary display
- Hybrid score breakdown (semantic vs lexical)
- Export results (JSON, CSV)

**Verifier Dashboard** (`frontend/app/verifier/page.tsx`):
- Claim input textarea
- Citation input (retrieval_id)
- Verify button → shows result
- Batch verification (paste generated text)
- Results table with filters (pass/partial/fail)
- Statistics (accuracy, thresholds)

**Session Manager** (`frontend/app/sessions/page.tsx`):
- Active sessions list
- Checkpoint creation form
- Session history timeline
- Rehydration interface
- State visualization (claims, citations)

**Audit Log Viewer** (`frontend/app/audit/page.tsx`):
- Date range picker
- Event type filter
- Correlation ID search
- Events table with expandable rows
- Chain verification tool
- Export logs (JSON)

**Repository Manager** (`frontend/app/repositories/page.tsx`):
- Add work form (repo URL, target file, slug, version)
- Works table (status, chunks count, last updated)
- Ingestion job status
- Retry failed ingestions
- Delete work (with confirmation)

**Knowledge Graph** (`frontend/app/graph/page.tsx`):
- D3.js or React Flow visualization
- Nodes: works, chunks
- Edges: citations, dependencies
- Interactive (zoom, pan, select)
- Filter by work or version

### Acceptance Criteria

**✅ Application Setup:**
- [ ] Next.js 14 with App Router configured
- [ ] Tailwind CSS styling works
- [ ] shadcn/ui components installed and themed
- [ ] TypeScript compilation succeeds with no errors

**✅ API Integration:**
- [ ] API client connects to backend
- [ ] All endpoints accessible
- [ ] Error handling shows user-friendly messages
- [ ] Loading states visible during requests

**✅ Responsive Design:**
- [ ] Mobile-friendly (≤768px width)
- [ ] Tablet layout (768-1024px)
- [ ] Desktop optimized (≥1024px)
- [ ] Navigation menu works on all sizes

**✅ Functionality:**
- [ ] Query returns results and displays correctly
- [ ] Verification shows color-coded badges
- [ ] Checkpoint creation/rehydration works
- [ ] Audit log filtering works
- [ ] Repository ingestion form submits successfully

**✅ Performance:**
- [ ] Initial page load: ≤2 seconds
- [ ] Query response rendering: ≤500ms
- [ ] No layout shifts (CLS < 0.1)
- [ ] Lighthouse score: ≥90 (Performance, Accessibility)

**✅ User Experience:**
- [ ] Intuitive navigation
- [ ] Clear error messages
- [ ] Success notifications (toasts)
- [ ] Help tooltips for complex features
- [ ] Keyboard navigation support

### Technical Specifications

**Stack:**
- Next.js 14.0.4 with App Router
- React 18.2
- TypeScript 5.3
- Tailwind CSS 3.3
- shadcn/ui components
- Lucide React icons
- D3.js or React Flow for graphs

**Styling:**
- Tailwind utility classes
- CSS variables for theming
- Dark mode support (optional)
- Consistent spacing (4px grid)

**State Management:**
- React hooks (useState, useEffect)
- React Context for global state (optional)
- SWR or React Query for data fetching (optional)

### Testing Requirements

**Component Tests (Jest + React Testing Library):**
```typescript
import { render, screen } from '@testing-library/react';
import { CitationBadge } from '@/components/CitationBadge';

describe('CitationBadge', () => {
  it('renders pass badge correctly', () => {
    render(<CitationBadge decision="pass" score={0.95} />);
    expect(screen.getByText(/Verified/)).toBeInTheDocument();
    expect(screen.getByText(/95%/)).toBeInTheDocument();
  });

  it('renders fail badge with red styling', () => {
    const { container } = render(<CitationBadge decision="fail" score={0.65} />);
    expect(container.querySelector('.bg-red-100')).toBeInTheDocument();
  });
});
```

**Integration Tests:**
- Query flow: Enter query → Submit → See results
- Verification flow: Paste text → Verify → See annotated output
- Session flow: Create checkpoint → Rehydrate → View restored state

### Dependencies

**NPM Packages:**
```json
{
  "dependencies": {
    "next": "14.0.4",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "tailwindcss": "3.3.6",
    "d3": "^7.8.5",
    "lucide-react": "^0.294.0",
    "date-fns": "^2.30.0"
  },
  "devDependencies": {
    "@types/node": "20.10.4",
    "@types/react": "18.2.42",
    "typescript": "5.3.3",
    "jest": "^29.7.0",
    "@testing-library/react": "^14.1.2"
  }
}
```

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| API latency causes poor UX | High | Add loading skeletons; implement optimistic updates |
| Complex graph rendering is slow | Medium | Use canvas instead of SVG; limit nodes displayed; add virtualization |
| Mobile layout breaks | Medium | Test on real devices; use responsive design system |

---

## PHASE 9: Docker Deployment & Integration

**Duration:** 5 days  
**Dependencies:** Phases 0-8 complete  
**Risk Level:** Low  

### Objectives

1. Create production-ready Dockerfiles for backend and frontend
2. Build comprehensive docker-compose.yml with all services
3. Configure service networking and dependencies
4. Set up volume persistence for databases and indexes
5. Implement health checks for all services
6. Create environment variable management
7. Add development overrides for hot reload
8. Document deployment procedures

### Deliverables

#### 1. Backend Dockerfile (`backend/Dockerfile`)

```dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create data directories
RUN mkdir -p /app/data/faiss /app/data/whoosh

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run migrations and start server
CMD alembic upgrade head && \
    uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### 2. Frontend Dockerfile (`frontend/Dockerfile`)

```dockerfile
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build application
RUN npm run build

# Production image
FROM node:18-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

# Copy built files from builder
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000', (r) => {if (r.statusCode !== 200) throw new Error()})"

CMD ["npm", "start"]
```

#### 3. Comprehensive Docker Compose (`docker-compose.yml`)

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:15-alpine
    container_name: greds-postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-cosmology}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
      POSTGRES_DB: ${POSTGRES_DB:-greds_library}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - greds-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-cosmology}"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    container_name: greds-redis
    command: redis-server ${REDIS_PASSWORD:+--requirepass $REDIS_PASSWORD}
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - greds-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
    restart: unless-stopped

  minio:
    image: minio/minio:latest
    container_name: greds-minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: ${S3_ACCESS_KEY_ID:-minioadmin}
      MINIO_ROOT_PASSWORD: ${S3_SECRET_ACCESS_KEY:-minioadmin}
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - minio_data:/data
    networks:
      - greds-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3
    restart: unless-stopped

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: greds-backend
    ports:
      - "8000:8000"
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_USER: ${POSTGRES_USER:-cosmology}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
      POSTGRES_DB: ${POSTGRES_DB:-greds_library}
      POSTGRES_PORT: 5432
      REDIS_HOST: redis
      REDIS_PORT: 6379
      REDIS_PASSWORD: ${REDIS_PASSWORD:-}
      S3_ENDPOINT_URL: http://minio:9000
      S3_ACCESS_KEY_ID: ${S3_ACCESS_KEY_ID:-minioadmin}
      S3_SECRET_ACCESS_KEY: ${S3_SECRET_ACCESS_KEY:-minioadmin}
      S3_BUCKET_NAME: ${S3_BUCKET_NAME:-greds-audit-logs}
      ABACUSAI_API_KEY: ${ABACUSAI_API_KEY}
      ABACUSAI_MODEL_ID: ${ABACUSAI_MODEL_ID:-gpt-4-turbo}
      BACKEND_CORS_ORIGINS: ${BACKEND_CORS_ORIGINS:-http://localhost:3000}
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
      RANDOM_SEED: ${RANDOM_SEED:-42}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      minio:
        condition: service_healthy
    volumes:
      - ./backend:/app
      - faiss_indexes:/app/data/faiss
      - whoosh_indexes:/app/data/whoosh
    networks:
      - greds-network
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: greds-frontend
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: ${NEXT_PUBLIC_API_URL:-http://localhost:8000/api/v1}
    depends_on:
      - backend
    networks:
      - greds-network
    restart: unless-stopped

networks:
  greds-network:
    driver: bridge

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  minio_data:
    driver: local
  faiss_indexes:
    driver: local
  whoosh_indexes:
    driver: local
```

#### 4. Development Override (`docker-compose.dev.yml`)

```yaml
version: '3.9'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - ./backend:/app
    environment:
      DEBUG: "true"

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    command: npm run dev
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - /app/.next
```

#### 5. Deployment Script (`scripts/deploy.sh`)

```bash
#!/bin/bash

set -e

echo "🚀 Starting GREDs AI Reference Library deployment..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found. Copy .env.example to .env and configure it."
    exit 1
fi

# Source environment variables
source .env

# Validate required variables
if [ -z "$ABACUSAI_API_KEY" ]; then
    echo "❌ Error: ABACUSAI_API_KEY not set in .env"
    exit 1
fi

echo "✅ Environment validated"

# Build images
echo "🏗️  Building Docker images..."
docker-compose build --no-cache

# Start services
echo "🔧 Starting services..."
docker-compose up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to be healthy..."
sleep 10

# Check health
docker-compose ps

# Run database migrations
echo "🗄️  Running database migrations..."
docker-compose exec -T backend alembic upgrade head

echo "✅ Deployment complete!"
echo ""
echo "📊 Service URLs:"
echo "   Frontend:  http://localhost:3000"
echo "   Backend:   http://localhost:8000"
echo "   API Docs:  http://localhost:8000/docs"
echo "   MinIO UI:  http://localhost:9001"
echo ""
echo "📝 Next steps:"
echo "   1. Visit http://localhost:3000 to access the application"
echo "   2. Check logs: docker-compose logs -f"
echo "   3. Ingest COSMOLOGY repository via Repository Manager"
```

### Acceptance Criteria

**✅ Docker Images:**
- [ ] Backend image builds successfully
- [ ] Frontend image builds successfully
- [ ] Image sizes reasonable (backend <1GB, frontend <500MB)
- [ ] Multi-stage builds used for frontend

**✅ Service Orchestration:**
- [ ] All 5 services start successfully
- [ ] Health checks pass within 60 seconds
- [ ] Services can communicate via network
- [ ] Dependencies respected (backend waits for DB)

**✅ Data Persistence:**
- [ ] PostgreSQL data persists across restarts
- [ ] FAISS/Whoosh indexes persist
- [ ] MinIO objects persist
- [ ] Redis data optional persistence

**✅ Configuration:**
- [ ] Environment variables loaded from .env
- [ ] CORS configuration works
- [ ] API endpoints accessible from frontend

**✅ Development Workflow:**
- [ ] Hot reload works for backend (uvicorn --reload)
- [ ] Hot reload works for frontend (npm run dev)
- [ ] Volume mounts allow live code editing

**✅ Production Readiness:**
- [ ] Restart policies configured
- [ ] Resource limits set (optional)
- [ ] Logs accessible via docker-compose logs
- [ ] Backup strategy documented

### Technical Specifications

**Container Resources (Recommended):**
- Backend: 2 CPU, 4GB RAM
- Frontend: 1 CPU, 1GB RAM
- PostgreSQL: 1 CPU, 2GB RAM
- Redis: 0.5 CPU, 512MB RAM
- MinIO: 1 CPU, 1GB RAM

**Volume Sizes:**
- postgres_data: 10GB minimum
- faiss_indexes: 5GB (grows with documents)
- whoosh_indexes: 2GB (grows with documents)
- minio_data: 20GB (audit logs + artifacts)

**Network Configuration:**
- Bridge network for internal communication
- Published ports for external access
- No host network mode (security)

### Testing Requirements

**Deployment Tests:**
```bash
#!/bin/bash

# Test script: scripts/test-deployment.sh

# Check all services running
echo "Checking services..."
docker-compose ps | grep -q "Up" || exit 1

# Test backend health
echo "Testing backend..."
curl -f http://localhost:8000/health || exit 1

# Test frontend
echo "Testing frontend..."
curl -f http://localhost:3000 || exit 1

# Test database connection
echo "Testing database..."
docker-compose exec -T postgres psql -U cosmology -d greds_library -c "SELECT 1" || exit 1

# Test MinIO
echo "Testing MinIO..."
curl -f http://localhost:9000/minio/health/live || exit 1

echo "✅ All deployment tests passed!"
```

**Load Test:**
- 100 concurrent users
- Query endpoint load
- Response time ≤1s at 50 RPS

### Dependencies

**System Requirements:**
- Docker 20.10+
- Docker Compose 2.0+
- 16GB RAM minimum
- 50GB free disk space
- Linux/macOS/Windows with WSL2

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Service startup order issues | High | Use depends_on with health checks; add retry logic |
| Volume permission issues | Medium | Set correct user/group in Dockerfiles; use named volumes |
| Network conflicts on common ports | Low | Document port requirements; allow port customization |
| Large image download times | Low | Pre-pull images; use layer caching; consider registry |

---

## PHASE 10: Pilot Ingestion & Validation

**Duration:** 5 days  
**Dependencies:** All previous phases complete  
**Risk Level:** High (validation/testing phase)  

### Objectives

1. Clone COSMOLOGY repository from GitHub
2. Extract README.md and convert to appropriate format
3. Create metadata.yaml for COSMOLOGY work
4. Execute full ingestion pipeline end-to-end
5. Generate embeddings and build indexes
6. Create three-level summaries for all chunks
7. Test with 5 predefined queries about quantum research
8. Verify citation accuracy (target ≥90% pass rate)
9. Measure performance metrics (throughput, latency, accuracy)
10. Generate validation report with findings and recommendations

### Deliverables

#### 1. COSMOLOGY Metadata (`metadata.yaml`)

```yaml
title: "COSMOLOGY - Quantum Research Documentation"
authors:
  - "Research Team"
version: "v1.0"
publication_date: "2025-10-24"
description: |
  Comprehensive documentation on quantum research methodologies,
  experimental results, and theoretical foundations.
tags:
  - quantum-mechanics
  - research
  - physics
  - documentation
canonical_url: "https://github.com/nbbulk-dotcom/COSMOLOGY"
license: "MIT"
```

#### 2. Test Queries (`test-queries.json`)

```json
{
  "queries": [
    {
      "id": "Q1",
      "query": "What are the fundamental principles of quantum mechanics discussed?",
      "expected_topics": ["superposition", "entanglement", "wave function"],
      "context": "General overview query"
    },
    {
      "id": "Q2",
      "query": "How are quantum experiments conducted according to the documentation?",
      "expected_topics": ["experimental setup", "methodology", "measurement"],
      "context": "Methodological query"
    },
    {
      "id": "Q3",
      "query": "What are the key research findings presented?",
      "expected_topics": ["results", "conclusions", "observations"],
      "context": "Results-focused query"
    },
    {
      "id": "Q4",
      "query": "Explain the theoretical framework underlying the research",
      "expected_topics": ["theory", "mathematical models", "equations"],
      "context": "Theoretical query"
    },
    {
      "id": "Q5",
      "query": "What are the implications and future directions mentioned?",
      "expected_topics": ["future work", "applications", "implications"],
      "context": "Forward-looking query"
    }
  ]
}
```

#### 3. Validation Script (`scripts/validate-cosmology.py`)

```python
import json
import time
from datetime import datetime
from typing import List, Dict
import requests

API_BASE = "http://localhost:8000/api/v1"

class COSMOLOGYValidator:
    """
    Validates the COSMOLOGY ingestion and system performance.
    """
    
    def __init__(self):
        self.results = {
            "timestamp": datetime.utcnow().isoformat(),
            "ingestion": {},
            "queries": [],
            "verification": {},
            "performance": {},
            "summary": {}
        }
    
    def step_1_ingest(self):
        """Step 1: Ingest COSMOLOGY repository"""
        print("Step 1: Ingesting COSMOLOGY repository...")
        
        start_time = time.time()
        
        response = requests.post(f"{API_BASE}/ingest/add-work", json={
            "repo_url": "https://github.com/nbbulk-dotcom/COSMOLOGY",
            "target_file": "README.md",
            "source_slug": "cosmology-research",
            "version": "v1.0",
            "branch": "main"
        })
        
        job_id = response.json()["job_id"]
        print(f"   Job ID: {job_id}")
        
        # Poll for completion
        while True:
            status_response = requests.get(f"{API_BASE}/ingest/job/{job_id}")
            status_data = status_response.json()
            status = status_data["status"]
            
            print(f"   Status: {status}")
            
            if status == "completed":
                self.results["ingestion"] = {
                    "status": "success",
                    "duration_seconds": time.time() - start_time,
                    "work_id": status_data["work_id"],
                    "total_chunks": status_data["total_chunks"]
                }
                break
            elif status == "failed":
                self.results["ingestion"] = {
                    "status": "failure",
                    "error": status_data.get("error")
                }
                raise Exception(f"Ingestion failed: {status_data.get('error')}")
            
            time.sleep(5)
        
        print(f"   ✅ Ingestion complete: {status_data['total_chunks']} chunks")
    
    def step_2_generate_summaries(self):
        """Step 2: Generate summaries for all chunks"""
        print("\nStep 2: Generating summaries...")
        
        work_id = self.results["ingestion"]["work_id"]
        start_time = time.time()
        
        response = requests.post(f"{API_BASE}/summarize/work", json={
            "work_id": work_id,
            "levels": ["short", "medium", "long"]
        })
        
        # Wait for completion (simplified - in production, poll job status)
        time.sleep(30)  # Estimated time for summary generation
        
        duration = time.time() - start_time
        
        self.results["summarization"] = {
            "status": "completed",
            "duration_seconds": duration
        }
        
        print(f"   ✅ Summarization complete ({duration:.1f}s)")
    
    def step_3_test_queries(self):
        """Step 3: Test with predefined queries"""
        print("\nStep 3: Testing queries...")
        
        with open("test-queries.json") as f:
            test_data = json.load(f)
        
        query_results = []
        total_latency = 0
        
        for query_def in test_data["queries"]:
            query_text = query_def["query"]
            print(f"   Query {query_def['id']}: {query_text[:50]}...")
            
            start_time = time.time()
            
            response = requests.post(f"{API_BASE}/query", json={
                "query": query_text,
                "top_k": 10,
                "include_summaries": True
            })
            
            latency = (time.time() - start_time) * 1000  # ms
            total_latency += latency
            
            results = response.json()
            
            query_results.append({
                "query_id": query_def["id"],
                "query": query_text,
                "latency_ms": latency,
                "results_count": results["results_count"],
                "top_score": results["results"][0]["hybrid_score"] if results["results"] else 0,
                "top_retrieval_id": results["results"][0]["retrieval_id"] if results["results"] else None
            })
            
            print(f"      Latency: {latency:.0f}ms, Results: {results['results_count']}")
        
        self.results["queries"] = query_results
        self.results["performance"]["avg_query_latency_ms"] = total_latency / len(query_results)
        
        print(f"   ✅ Average query latency: {total_latency / len(query_results):.0f}ms")
    
    def step_4_verify_citations(self):
        """Step 4: Verify citation accuracy"""
        print("\nStep 4: Verifying citations...")
        
        # Create test claims with citations from query results
        test_claim = f"According to the documentation, quantum mechanics principles are discussed [{self.results['queries'][0]['top_retrieval_id']}]."
        
        response = requests.post(f"{API_BASE}/verify/run", json={
            "text": test_claim,
            "query_text": self.results['queries'][0]['query']
        })
        
        verification_data = response.json()
        
        self.results["verification"] = {
            "total_citations": verification_data["overall_stats"]["total_citations"],
            "pass_count": verification_data["overall_stats"]["pass_count"],
            "partial_count": verification_data["overall_stats"]["partial_count"],
            "fail_count": verification_data["overall_stats"]["fail_count"],
            "accuracy": verification_data["overall_stats"]["accuracy"]
        }
        
        print(f"   ✅ Verification accuracy: {verification_data['overall_stats']['accuracy']:.1f}%")
    
    def step_5_test_session(self):
        """Step 5: Test session checkpoint/rehydration"""
        print("\nStep 5: Testing session management...")
        
        # Create checkpoint
        checkpoint_response = requests.post(f"{API_BASE}/session/checkpoint", json={
            "session_id": "validation-session",
            "condensed_summary": "COSMOLOGY validation test session",
            "accepted_claims": [{"claim": "Test claim", "status": "pass"}],
            "top_citations": [self.results['queries'][0]['top_retrieval_id']],
            "checkpoint_name": "Validation Checkpoint"
        })
        
        checkpoint_id = checkpoint_response.json()["checkpoint_id"]
        
        # Rehydrate
        start_time = time.time()
        
        rehydrate_response = requests.post(f"{API_BASE}/session/rehydrate", json={
            "checkpoint_id": checkpoint_id,
            "include_full_chunks": True
        })
        
        rehydration_time = time.time() - start_time
        rehydration_data = rehydrate_response.json()
        
        self.results["session"] = {
            "checkpoint_id": checkpoint_id,
            "rehydration_time_seconds": rehydration_time,
            "context_overlap": rehydration_data["context_overlap"]
        }
        
        print(f"   ✅ Rehydration: {rehydration_time:.2f}s, Overlap: {rehydration_data['context_overlap']:.1f}%")
    
    def step_6_performance_metrics(self):
        """Step 6: Calculate overall performance metrics"""
        print("\nStep 6: Calculating performance metrics...")
        
        total_chunks = self.results["ingestion"]["total_chunks"]
        ingestion_time = self.results["ingestion"]["duration_seconds"]
        
        self.results["performance"].update({
            "ingestion_throughput_chunks_per_minute": (total_chunks / ingestion_time) * 60,
            "avg_query_latency_ms": self.results["performance"]["avg_query_latency_ms"],
            "rehydration_speed_seconds": self.results["session"]["rehydration_time_seconds"],
            "verifier_accuracy": self.results["verification"]["accuracy"]
        })
        
        print(f"   Ingestion: {self.results['performance']['ingestion_throughput_chunks_per_minute']:.1f} chunks/min")
        print(f"   Query latency: {self.results['performance']['avg_query_latency_ms']:.0f}ms")
        print(f"   Rehydration: {self.results['performance']['rehydration_speed_seconds']:.2f}s")
    
    def step_7_generate_report(self):
        """Step 7: Generate validation report"""
        print("\nStep 7: Generating validation report...")
        
        # Overall success criteria
        success = (
            self.results["ingestion"]["status"] == "success" and
            self.results["performance"]["avg_query_latency_ms"] <= 300 and
            self.results["verification"]["accuracy"] >= 90.0 and
            self.results["session"]["context_overlap"] >= 95.0
        )
        
        self.results["summary"] = {
            "overall_status": "PASS" if success else "FAIL",
            "success_criteria_met": {
                "ingestion_completed": self.results["ingestion"]["status"] == "success",
                "query_latency_acceptable": self.results["performance"]["avg_query_latency_ms"] <= 300,
                "verifier_accuracy_target": self.results["verification"]["accuracy"] >= 90.0,
                "rehydration_overlap_target": self.results["session"]["context_overlap"] >= 95.0
            }
        }
        
        # Save report
        with open("validation-report.json", "w") as f:
            json.dump(self.results, f, indent=2)
        
        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)
        print(f"Overall Status: {self.results['summary']['overall_status']}")
        print(f"\nIngestion: {self.results['ingestion']['total_chunks']} chunks")
        print(f"Query Latency: {self.results['performance']['avg_query_latency_ms']:.0f}ms (target: ≤300ms)")
        print(f"Verifier Accuracy: {self.results['verification']['accuracy']:.1f}% (target: ≥90%)")
        print(f"Rehydration Overlap: {self.results['session']['context_overlap']:.1f}% (target: ≥95%)")
        print("\nDetailed report saved to: validation-report.json")
        print("="*60)
    
    def run_validation(self):
        """Execute full validation pipeline"""
        try:
            self.step_1_ingest()
            self.step_2_generate_summaries()
            self.step_3_test_queries()
            self.step_4_verify_citations()
            self.step_5_test_session()
            self.step_6_performance_metrics()
            self.step_7_generate_report()
        except Exception as e:
            print(f"\n❌ Validation failed: {e}")
            with open("validation-report.json", "w") as f:
                self.results["summary"] = {
                    "overall_status": "ERROR",
                    "error": str(e)
                }
                json.dump(self.results, f, indent=2)

if __name__ == "__main__":
    validator = COSMOLOGYValidator()
    validator.run_validation()
```

### Acceptance Criteria

**✅ Ingestion:**
- [ ] COSMOLOGY repository cloned successfully
- [ ] README.md extracted and processed
- [ ] All chunks stored in database
- [ ] Embeddings generated for all chunks
- [ ] FAISS and Whoosh indexes built
- [ ] No errors during ingestion

**✅ Summarization:**
- [ ] Short summaries (50-100 chars) generated
- [ ] Medium summaries (150-300 words) generated
- [ ] Long summaries (400-800 words) generated
- [ ] All summaries stored in database

**✅ Query Performance:**
- [ ] All 5 test queries return results
- [ ] Median latency ≤300ms
- [ ] P95 latency ≤800ms
- [ ] Results relevant to query intent (manual review)

**✅ Verification Accuracy:**
- [ ] Citation verifier achieves ≥90% pass rate
- [ ] Partial/fail cases reviewed and justified
- [ ] No false positives in validation set

**✅ Session Management:**
- [ ] Checkpoint created successfully
- [ ] Rehydration completes in ≤2 seconds
- [ ] Context overlap ≥95%

**✅ Overall System:**
- [ ] All components functional
- [ ] No critical errors in logs
- [ ] Health checks passing
- [ ] Validation report generated

### Technical Specifications

**Performance Targets:**
- Ingestion throughput: ≥50 chunks/minute
- Query latency: median ≤300ms, p95 ≤800ms, p99 ≤1.5s
- Rehydration speed: ≤2s for 20 chunks
- Verifier accuracy: ≥90% pass rate

**Validation Metrics:**
```json
{
  "ingestion": {
    "throughput_chunks_per_minute": 50-100,
    "total_duration_seconds": "<120"
  },
  "queries": {
    "avg_latency_ms": "<300",
    "p95_latency_ms": "<800"
  },
  "verification": {
    "pass_rate_percent": ">90"
  },
  "session": {
    "rehydration_seconds": "<2",
    "context_overlap_percent": ">95"
  }
}
```

### Testing Requirements

**Pre-Validation Checklist:**
- [ ] All services running (docker-compose ps shows "Up")
- [ ] Database migrations applied
- [ ] API health check returns 200
- [ ] Frontend accessible
- [ ] Environment variables configured

**Manual Testing:**
- [ ] Query interface returns formatted results
- [ ] Citation badges display correctly
- [ ] Verifier dashboard shows accurate results
- [ ] Session manager creates/restores checkpoints
- [ ] Audit log viewer displays events

**Automated Tests:**
```bash
# Run validation script
python scripts/validate-cosmology.py

# Expected output:
# Step 1: ✅ Ingestion complete: X chunks
# Step 2: ✅ Summarization complete
# Step 3: ✅ Average query latency: Xms
# Step 4: ✅ Verification accuracy: X%
# Step 5: ✅ Rehydration: Xs, Overlap: X%
# Step 6: Performance metrics calculated
# Step 7: Validation report generated
# Overall Status: PASS
```

### Dependencies

**Required:**
- Docker deployment (Phase 9) complete and running
- COSMOLOGY repository accessible on GitHub
- Abacus.AI API key configured and working

### Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| COSMOLOGY repo unavailable | High | Cache repo locally; use backup sample document |
| Ingestion fails due to format issues | High | Add error handling; validate file format before processing |
| Query latency exceeds target | High | Optimize indexes; add caching; review FAISS configuration |
| Verification accuracy below 90% | High | Calibrate thresholds; review test cases; improve embeddings |
| System instability during load | Medium | Run load tests separately; scale resources if needed |

---

## Success Criteria (Overall Project)

### Functional Requirements ✅

**Phase Completion:**
- [ ] All 10 phases completed with acceptance criteria validated
- [ ] No critical bugs in production deployment
- [ ] All API endpoints functional and documented

**Data Processing:**
- [ ] COSMOLOGY repository fully indexed with metadata
- [ ] Embeddings generated for all chunks (384-dim vectors)
- [ ] Three-level summaries created for all chunks
- [ ] FAISS and Whoosh indexes built and searchable

**Retrieval System:**
- [ ] Hybrid retrieval (0.7 semantic + 0.3 lexical) returns relevant results
- [ ] Top-K results ranked correctly by hybrid score
- [ ] Query filtering (work_slug, version, tags) works
- [ ] Deterministic ranking with seed produces consistent results

**Verification System:**
- [ ] Citation verifier achieves ≥90% pass rate on test set
- [ ] Threshold-based decisions (pass/partial/fail) work correctly
- [ ] Claim extraction and parsing accurate
- [ ] Annotated output generated with verification markers

**Session Management:**
- [ ] Checkpoint creation stores complete state
- [ ] Rehydration reconstructs context with ≥95% overlap
- [ ] Session history tracking functional
- [ ] Parent-child checkpoint linkage preserved

**Audit Trail:**
- [ ] Immutable JSONL logs written to S3
- [ ] SHA256 chain linking implemented
- [ ] Correlation IDs track related events
- [ ] Chain verification detects tampering

**Frontend:**
- [ ] All 7 pages functional (Dashboard, Query, Verifier, Sessions, Audit, Repositories, Graph)
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] API integration complete
- [ ] User experience intuitive and polished

### Performance Benchmarks ✅

**Ingestion:**
- [ ] Throughput: ≥50 chunks/minute (including embeddings and indexing)
- [ ] Processing time: ~2-3 minutes for 100-chunk document
- [ ] No memory leaks during large ingestions

**Query:**
- [ ] Latency: median ≤300ms, p95 ≤800ms, p99 ≤1.5s
- [ ] Throughput: ≥50 queries/second under load
- [ ] Results accuracy: ≥85% relevant for top-10 results (manual eval)

**Verification:**
- [ ] Execution time: ≤500ms per claim
- [ ] Batch processing: ≤5s for 10 claims
- [ ] Accuracy: ≥90% pass rate on validation set

**Session:**
- [ ] Checkpoint creation: ≤100ms
- [ ] Rehydration: ≤2s for 20-chunk context
- [ ] Storage overhead: <100KB per checkpoint

**Audit:**
- [ ] Logging overhead: <10ms per event
- [ ] Query performance: ≤500ms for 24-hour window
- [ ] Storage efficiency: ~1KB per event (compressed)

### Operational Requirements ✅

**Deployment:**
- [ ] Docker Compose deployment successful on clean Ubuntu 22.04 host
- [ ] All services start without errors
- [ ] Health checks passing within 60 seconds
- [ ] Logs accessible and structured

**Accessibility:**
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend API accessible at http://localhost:8000
- [ ] API documentation at http://localhost:8000/docs
- [ ] MinIO console at http://localhost:9001

**Reliability:**
- [ ] Services restart automatically on failure
- [ ] Data persists across container restarts
- [ ] Graceful degradation when services unavailable
- [ ] Error messages informative and actionable

**Testing:**
- [ ] Unit test coverage ≥80% for core modules
- [ ] Integration tests passing for all workflows
- [ ] Load tests meet performance targets
- [ ] Validation script runs successfully

**Documentation:**
- [ ] API reference complete (OpenAPI/Swagger)
- [ ] Deployment guide with step-by-step instructions
- [ ] User manual for frontend features
- [ ] Architecture documentation with diagrams

---

## Conclusion

This comprehensive project plan provides a structured roadmap for building the **GREDs AI Reference Library** from initial repository setup through pilot validation. The 10-phase approach ensures systematic development with clear acceptance criteria and risk mitigation at each stage.

**Key Success Factors:**
1. **Deterministic Operations**: Reproducible results with fixed seeds and versioned prompts
2. **Hybrid Retrieval**: Balanced semantic and lexical search for optimal accuracy
3. **Citation Verification**: Automated fact-checking with transparent thresholds
4. **Immutable Audit**: Tamper-proof logging for compliance and debugging
5. **Scalable Architecture**: Docker-based deployment ready for production

**Timeline Summary:** 10-12 weeks for full implementation with 1 full-time developer. Parallel workstreams on frontend/backend can reduce duration to 8-9 weeks.

**Next Steps:**
1. Review and approve this plan
2. Set up development environment (Phase 0)
3. Begin Phase 1 (Core Backend Infrastructure)
4. Establish weekly progress checkpoints

For questions or clarifications, refer to phase-specific acceptance criteria and technical specifications. Each phase is designed to be independently testable and deployable.

---

**Document Version:** 1.0  
**Last Updated:** October 24, 2025  
**Status:** Ready for Implementation  
**Estimated Completion:** December 2025
