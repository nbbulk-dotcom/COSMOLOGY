# GREDs AI Reference Library (COSMOLOGY)

[![CI Pipeline](https://i.ytimg.com/vi/fx1Jttnj2vc/sddefault.jpg)
[![License: MIT](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/MIT_Logo_New.svg/1200px-MIT_Logo_New.svg.png)

> **Enterprise-grade knowledge management system for quantum research corpus with deterministic, auditable operations.**

## 🌟 Overview

The **GREDs AI Reference Library** is a production-ready full-stack application designed to solve the fundamental challenge of AI session context loss. It provides hybrid retrieval (semantic + lexical), citation verification, session checkpointing, and immutable audit trails for scientific research documents.

### Key Capabilities

- **Hybrid Retrieval**: 0.7 semantic (FAISS) + 0.3 lexical (BM25) scoring
- **Three-Level Summarization**: Short, medium, and long summaries per chunk
- **Citation Verification**: Cosine similarity-based fact-checking (≥80% pass threshold)
- **Session Checkpointing**: Stateful context preservation and rehydration
- **Immutable Audit Trail**: SHA256-chained JSONL logs in S3
- **Knowledge Graphs**: Visual dependency mapping between research artifacts

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (Next.js 14)                  │
│  Dashboard │ Query │ Graph │ Sessions │ Verifier │ Audit   │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP/REST
┌──────────────────────────▼──────────────────────────────────┐
│              Backend (FastAPI + Uvicorn)                    │
│  Ingestion │ Retrieval │ Verification │ Checkpointing      │
└─────┬────────┬──────────┬──────────┬────────────┬──────────┘
      │        │          │          │            │
   ┌──▼──┐  ┌─▼───┐  ┌───▼───┐  ┌──▼───┐    ┌───▼────┐
   │ PG  │  │Redis│  │ FAISS │  │Whoosh│    │MinIO/S3│
   │15+  │  │  7  │  │Vector │  │ BM25 │    │ Audit  │
   └─────┘  └─────┘  └───────┘  └──────┘    └────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker 20.10+ with Compose plugin
- Git 2.30+
- 8GB RAM minimum (16GB recommended)
- Abacus.AI API key ([Get one here](https://abacus.ai))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/nbbulk-dotcom/COSMOLOGY.git
cd COSMOLOGY

# 2. Configure environment
cp .env.example .env
nano .env  # Add your ABACUSAI_API_KEY

# 3. Start all services
docker-compose up -d

# 4. Verify health
curl http://localhost:8000/health

# 5. Access the application
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
# MinIO Console: http://localhost:9001
```

### First Ingestion

```bash
# Ingest the COSMOLOGY repository itself
curl -X POST http://localhost:8000/api/v1/ingest/add-work \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/nbbulk-dotcom/COSMOLOGY",
    "slug": "cosmology-hub",
    "force_regenerate": false
  }'
```

## 📚 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 14, React 18, TypeScript | Server-side rendering UI |
| **Styling** | Tailwind CSS, shadcn/ui | Component design system |
| **Backend** | FastAPI, Uvicorn, Python 3.12+ | Async REST API |
| **Database** | PostgreSQL 15+ | Metadata, chunks, sessions |
| **Vector Search** | FAISS | Semantic similarity (384-dim) |
| **Lexical Search** | Whoosh | BM25 keyword ranking |
| **Embeddings** | sentence-transformers | all-MiniLM-L6-v2 model |
| **LLM** | Abacus.AI APIs | Summarization (temp=0.2) |
| **Object Storage** | MinIO / AWS S3 | Immutable audit logs |
| **Task Queue** | Redis + RQ | Background job processing |
| **Containerization** | Docker + Compose | Unified deployment |
| **CI/CD** | GitHub Actions | Automated testing |

## 🎯 Project Status

**Current Phase**: Phase 0 - Repository Initialization ✅

### Milestone Progress

| Phase | Status | Duration | Description |
|-------|--------|----------|-------------|
| **Phase 0** | ✅ Complete | 3 days | Repository scaffolding, Docker setup |
| **Phase 1** | 🔄 Next | 5 days | Database models, S3 client, FastAPI app |
| **Phase 2** | 📋 Planned | 7 days | Ingestion pipeline, chunking, embeddings |
| **Phase 3** | 📋 Planned | 5 days | Three-level summarization system |
| **Phase 4** | 📋 Planned | 7 days | Hybrid retrieval (FAISS + Whoosh) |
| **Phase 5** | 📋 Planned | 7 days | Citation verification engine |
| **Phase 6** | 📋 Planned | 5 days | Session checkpointing & rehydration |
| **Phase 7** | 📋 Planned | 4 days | Immutable audit trail |
| **Phase 8** | 📋 Planned | 14 days | Frontend development |
| **Phase 9** | 📋 Planned | 5 days | Docker deployment optimization |
| **Phase 10** | 📋 Planned | 5 days | Pilot validation & testing |

**Estimated Completion**: ~12 weeks (67 days)

## 📖 Documentation

- **[Project Plan](PROJECT_PLAN.md)**: Complete 10-phase development roadmap
- **[Architecture](docs/architecture.md)**: System design and component interactions
- **[API Reference](docs/api-reference.md)**: Complete endpoint documentation
- **[User Guide](docs/user-guide.md)**: How to use the system
- **[Deployment Guide](docs/deployment.md)**: Installation and configuration

## 🧪 Development

### Running Tests

```bash
# Backend tests
cd backend
pip install -r requirements-dev.txt
pytest --cov=app

# Frontend tests
cd frontend
npm install
npm run test
npm run type-check
```

### Code Quality

```bash
# Backend linting
cd backend
black app/
flake8 app/ --max-line-length=120

# Frontend linting
cd frontend
npm run lint
```

### Database Migrations

```bash
# Create new migration
docker-compose exec backend alembic revision --autogenerate -m "description"

# Apply migrations
docker-compose exec backend alembic upgrade head

# Rollback migration
docker-compose exec backend alembic downgrade -1
```

## 🔧 Configuration

Key environment variables (see `.env.example` for complete list):

```bash
# Database
POSTGRES_PASSWORD=changeme

# Abacus.AI
ABACUSAI_API_KEY=your_key_here

# Retrieval Tuning
SEMANTIC_WEIGHT=0.7  # 70% semantic score
LEXICAL_WEIGHT=0.3   # 30% lexical score
TOP_K=20             # Return top 20 results

# Verification
VERIFIER_PASS_THRESHOLD=0.80    # Pass if ≥80% similarity
VERIFIER_PARTIAL_THRESHOLD=0.75 # Partial if ≥75%

# Chunking
CHUNK_SIZE=1024       # Token count per chunk
CHUNK_OVERLAP=0.2     # 20% overlap
RANDOM_SEED=42        # For reproducibility
```

## 🐛 Troubleshooting

### Common Issues

**Services won't start:**
```bash
# Check port conflicts
lsof -i :8000 -i :3000 -i :5432

# View service logs
docker-compose logs -f
```

**Database connection errors:**
```bash
# Verify PostgreSQL is ready
docker-compose exec postgres pg_isready -U cosmology

# Check migrations
docker-compose exec backend alembic current
```

**Out of memory:**
```bash
# Increase Docker memory limit (Settings > Resources)
# Or reduce worker count in .env
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `pytest && npm test`
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📊 Performance Benchmarks

| Metric | Target | Current |
|--------|--------|---------|
| Ingestion Rate | ≥50 chunks/min | TBD |
| Query Latency (median) | ≤300ms | TBD |
| Query Latency (p95) | ≤800ms | TBD |
| Rehydration Speed | ≤2s (20 chunks) | TBD |
| Verifier Execution | ≤500ms per claim | TBD |

## 🔒 Security

- Environment-based configuration (no hardcoded secrets)
- CORS restricted to frontend origin
- S3 object immutability for audit logs
- JWT authentication (coming in Phase 1)
- Rate limiting on API endpoints (coming in Phase 2)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Abacus.AI** for LLM API access
- **FAISS** (Facebook AI Similarity Search) for vector indexing
- **Whoosh** for pure-Python full-text indexing
- **sentence-transformers** for embedding generation
- **shadcn/ui** for beautiful React components

## 📧 Contact

**Project Maintainer**: Nicolas Brett

- GitHub: [@nbbulk-dotcom](https://github.com/nbbulk-dotcom)
- Repository: [COSMOLOGY](https://github.com/nbbulk-dotcom/COSMOLOGY)
- Issues: [GitHub Issues](https://github.com/nbbulk-dotcom/COSMOLOGY/issues)

---

**Built with ❤️ for the quantum research community**
