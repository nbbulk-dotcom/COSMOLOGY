
# User Guide

## Getting Started

### Accessing the Application

Once deployed, access the GREDs AI Reference Library at:
- Frontend: http://localhost:3000
- API Documentation: http://localhost:8000/docs

### Main Features

#### 1. Dashboard

The dashboard provides an overview of:
- Total works ingested
- Total chunks indexed
- Active sessions
- Recent activity

#### 2. Repository Management

Navigate to **Repositories** to:
- View all ingested works
- Add new repositories
- View ingestion status
- Regenerate indexes if needed

**Adding a Repository:**
1. Click "Add Repository"
2. Enter the GitHub URL
3. Provide a unique slug (e.g., "cosmology-hub")
4. Configure metadata (title, authors, tags)
5. Click "Ingest"

#### 3. Query Interface

The **Query** page allows you to:
- Submit natural language questions
- View retrieved chunks
- See citation information
- Filter by tags or works

**Submitting a Query:**
1. Enter your question in the search box
2. Optionally filter by tags or specific works
3. Click "Search"
4. Review results with inline citations

#### 4. Knowledge Graph

The **Graph** visualization shows:
- Dependencies between works
- Citation relationships
- Concept clustering

#### 5. Session Management

The **Sessions** page allows you to:
- Create new sessions
- View active sessions
- Create checkpoints
- Rehydrate previous sessions

**Creating a Checkpoint:**
1. Navigate to your active session
2. Click "Create Checkpoint"
3. Provide a descriptive name
4. Checkpoint saved for later rehydration

#### 6. Verification Dashboard

The **Verifier** page displays:
- Recent verification runs
- Pass/fail statistics
- Failed claims for review
- Verifier performance metrics

#### 7. Audit Logs

The **Audit** page provides:
- Searchable audit trail
- Filtering by event type
- Download logs as JSON
- Compliance reporting

## Best Practices

### Query Formulation

- Be specific in your questions
- Use technical terms from your domain
- Reference specific concepts or papers
- Review multiple chunks for complete context

### Session Management

- Create checkpoints at major milestones
- Name checkpoints descriptively
- Rehydrate sessions when resuming work
- Review condensed summaries regularly

### Citation Verification

- Always review partial/failed citations
- Update source documents if needed
- Use verifier feedback to improve queries
- Monitor verifier thresholds

## Troubleshooting

### Common Issues

**Issue: Slow query responses**
- Check if indexes are built
- Reduce top-K parameter
- Verify backend health

**Issue: Low verification scores**
- Review query formulation
- Check chunk quality
- Adjust verifier thresholds

**Issue: Missing citations**
- Ensure work is fully ingested
- Check ingestion logs
- Regenerate indexes if needed

## Support

For additional help:
- Check the [Architecture](architecture.md) documentation
- Review [API Reference](api-reference.md)
- Submit issues on GitHub
