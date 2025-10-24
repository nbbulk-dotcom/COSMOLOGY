# Contributing to GREDs AI Reference Library

Thank you for your interest in contributing to the GREDs AI Reference Library! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Docker 20.10+ with Compose plugin
- Git 2.30+
- Python 3.12+ (for local backend development)
- Node.js 18+ (for local frontend development)
- A GitHub account

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork:**
```bash
git clone https://github.com/YOUR_USERNAME/COSMOLOGY.git
cd COSMOLOGY
```

3. **Add upstream remote:**
```bash
git remote add upstream https://github.com/nbbulk-dotcom/COSMOLOGY.git
```

4. **Create environment file:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Start development services:**
```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

## Development Workflow

### Creating a Feature Branch

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
```

### Branch Naming Conventions

- `feature/` - New features (e.g., `feature/hybrid-retrieval`)
- `fix/` - Bug fixes (e.g., `fix/embedding-cache`)
- `docs/` - Documentation updates (e.g., `docs/api-reference`)
- `refactor/` - Code refactoring (e.g., `refactor/chunker-module`)
- `test/` - Test additions or modifications (e.g., `test/verifier-suite`)

## Coding Standards

### Python (Backend)

**Style Guide:**
- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints for function signatures
- Maximum line length: 120 characters
- Use `black` for formatting
- Use `flake8` for linting

**Example:**
```python
from typing import List, Optional
import structlog

logger = structlog.get_logger()


def process_chunks(
    text: str,
    chunk_size: int = 1024,
    overlap: float = 0.2
) -> List[str]:
    """
    Process text into chunks.
    
    Args:
        text: Input text to chunk
        chunk_size: Size of each chunk in tokens
        overlap: Overlap ratio between chunks
        
    Returns:
        List of text chunks
    """
    logger.info("Processing chunks", size=chunk_size)
    # Implementation here
    return []
```

**Run Linting:**
```bash
cd backend
black app/
flake8 app/ --max-line-length=120
mypy app/
```

### TypeScript/React (Frontend)

**Style Guide:**
- Follow [TypeScript ESLint](https://typescript-eslint.io/) rules
- Use functional components with hooks
- Use TypeScript for all new code
- Prefer explicit types over `any`
- Use `camelCase` for variables/functions, `PascalCase` for components

**Example:**
```typescript
import { useState, useEffect } from 'react'
import { apiClient } from '@/lib/api-client'

interface QueryResult {
  answer: string
  citations: string[]
}

export function QueryInterface() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<QueryResult | null>(null)
  
  const handleSubmit = async () => {
    const response = await apiClient.query({
      session_id: 'test',
      user_query: query
    })
    setResults(response)
  }
  
  return (
    <div>
      {/* Component JSX */}
    </div>
  )
}
```

**Run Linting:**
```bash
cd frontend
npm run lint
npm run type-check
```

### Database Models

- Use descriptive table and column names
- Add indexes for frequently queried columns
- Include `created_at` and `updated_at` timestamps
- Document relationships clearly
- Use Alembic for all schema changes

### API Endpoints

- Follow RESTful conventions
- Use appropriate HTTP methods (GET, POST, PUT, DELETE)
- Return consistent error formats
- Include Pydantic models for request/response validation
- Document with OpenAPI/Swagger

## Testing Guidelines

### Backend Tests

**Location:** `backend/tests/`

**Running Tests:**
```bash
cd backend
pytest --cov=app --cov-report=term-missing
```

**Test Structure:**
```python
import pytest
from app.core.chunker import DeterministicChunker


def test_chunker_reproducibility():
    """Chunks should be identical with same seed."""
    chunker = DeterministicChunker(seed=42)
    
    text = "Sample text for testing..."
    chunks1 = chunker.chunk_text(text)
    chunks2 = chunker.chunk_text(text)
    
    assert chunks1 == chunks2
```

### Frontend Tests

**Location:** `frontend/__tests__/`

**Running Tests:**
```bash
cd frontend
npm run test
```

### Test Coverage Requirements

- Minimum 80% code coverage for core modules
- All new features must include tests
- Bug fixes should include regression tests

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test additions or modifications
- `chore`: Build process or auxiliary tool changes

### Examples

```
feat(retrieval): implement hybrid scoring algorithm

Add hybrid retrieval that combines FAISS semantic search
with Whoosh BM25 lexical search using 0.7/0.3 weighting.

Closes #42
```

```
fix(embeddings): handle empty text inputs

Added validation to prevent embedding generation errors
when text is empty or whitespace-only.

Fixes #67
```

## Pull Request Process

### Before Submitting

1. **Update your branch:**
```bash
git checkout main
git pull upstream main
git checkout your-feature-branch
git rebase main
```

2. **Run tests:**
```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm run test && npm run build
```

3. **Run linting:**
```bash
# Backend
cd backend && black app/ && flake8 app/

# Frontend
cd frontend && npm run lint
```

4. **Update documentation** if needed

### Submitting Pull Request

1. **Push your branch:**
```bash
git push origin your-feature-branch
```

2. **Open Pull Request** on GitHub

3. **Fill out PR template:**
   - Describe the changes
   - Reference related issues
   - Include screenshots for UI changes
   - List breaking changes

4. **Request review** from maintainers

### PR Review Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] No breaking changes (or properly documented)
- [ ] Commit messages follow conventions
- [ ] Branch is up to date with main

### After PR Approval

- Maintainer will merge using "Squash and merge"
- Delete your feature branch
- Update your local main branch

## Project Structure

```
COSMOLOGY/
├── backend/          # Python FastAPI backend
│   ├── app/
│   │   ├── api/     # API endpoints
│   │   ├── core/    # Core business logic
│   │   ├── db/      # Database models
│   │   └── utils/   # Utilities
│   └── tests/       # Backend tests
├── frontend/         # Next.js frontend
│   ├── app/         # Next.js pages
│   ├── components/  # React components
│   └── lib/         # Utilities
├── docs/            # Documentation
└── .github/         # GitHub workflows
```

## Development Phases

The project is being developed in phases:

- **Phase 0**: Repository Initialization ✅
- **Phase 1**: Core Backend Infrastructure (Next)
- **Phase 2**: Ingestion Pipeline
- **Phase 3**: Summarization System
- **Phase 4**: Hybrid Retrieval
- **Phase 5**: Citation Verification
- **Phase 6**: Session Management
- **Phase 7**: Immutable Audit Trail
- **Phase 8**: Frontend Development
- **Phase 9**: Docker Deployment
- **Phase 10**: Pilot Validation

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for detailed phase descriptions.

## Questions?

- Open an [issue](https://github.com/nbbulk-dotcom/COSMOLOGY/issues) for bugs or feature requests
- Start a [discussion](https://github.com/nbbulk-dotcom/COSMOLOGY/discussions) for questions
- Check the [documentation](docs/) for guidance

## Recognition

Contributors will be recognized in the project README and release notes.

Thank you for contributing to GREDs AI Reference Library! 🚀
