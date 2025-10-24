
# GREDs AI Reference Library

Welcome to the **GREDs AI Reference Library** (COSMOLOGY) documentation.

## Overview

The GREDs AI Reference Library is an enterprise-grade knowledge management system designed to ingest, index, retrieve, and verify scientific research documents with deterministic, auditable operations.

## Key Features

- **Hybrid Retrieval**: Combines semantic (FAISS) and lexical (BM25) search for optimal accuracy
- **Three-Level Summarization**: Short, medium, and long summaries for each chunk
- **Citation Verification**: Automated fact-checking with cosine similarity thresholds
- **Session Management**: Stateful context preservation with checkpoint/rehydration
- **Immutable Audit Trail**: SHA256-chained JSONL logs for compliance
- **Knowledge Graphs**: Visual dependency mapping between research artifacts

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend API | FastAPI + Uvicorn |
| Frontend | Next.js 14 (App Router) |
| Database | PostgreSQL 15+ |
| Vector Store | FAISS |
| Lexical Search | Whoosh (BM25) |
| Embeddings | sentence-transformers |
| LLM Provider | Abacus.AI APIs |
| Object Storage | S3-compatible (MinIO/AWS S3) |
| Task Queue | Redis + RQ |

## Quick Start

See the [Deployment Guide](deployment.md) for detailed setup instructions.

```bash
# Clone the repository
git clone https://github.com/nbbulk-dotcom/COSMOLOGY.git
cd COSMOLOGY

# Copy environment variables
cp .env.example .env
# Edit .env with your configuration

# Start services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## Documentation Structure

- **[Architecture](architecture.md)**: System design and component interactions
- **[API Reference](api-reference.md)**: Complete API endpoint documentation
- **[User Guide](user-guide.md)**: How to use the system
- **[Deployment](deployment.md)**: Installation and configuration guide

## Support

For issues and questions, please visit our [GitHub repository](https://github.com/nbbulk-dotcom/COSMOLOGY/issues).
