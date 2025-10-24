
import Link from 'next/link'

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-4xl mx-auto">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">
            Welcome to GREDs AI Reference Library
          </h1>
          <p className="text-xl text-muted-foreground mb-6">
            Enterprise-grade knowledge management for quantum research corpus
          </p>
          <div className="flex gap-4 justify-center">
            <Link 
              href="/dashboard"
              className="px-6 py-3 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition"
            >
              Open Dashboard
            </Link>
            <Link
              href="http://localhost:8000/docs"
              target="_blank"
              className="px-6 py-3 border border-border rounded-lg hover:bg-accent transition"
            >
              API Documentation
            </Link>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 gap-6 mb-12">
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">🔍 Hybrid Retrieval</h3>
            <p className="text-sm text-muted-foreground">
              0.7 semantic (FAISS) + 0.3 lexical (BM25) scoring for optimal accuracy
            </p>
          </div>
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">📝 Three-Level Summarization</h3>
            <p className="text-sm text-muted-foreground">
              Short, medium, and long summaries for each chunk
            </p>
          </div>
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">✅ Citation Verification</h3>
            <p className="text-sm text-muted-foreground">
              Cosine similarity-based fact-checking with ≥80% pass threshold
            </p>
          </div>
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">💾 Session Checkpointing</h3>
            <p className="text-sm text-muted-foreground">
              Stateful context preservation and rehydration
            </p>
          </div>
        </div>

        {/* Navigation Cards */}
        <div className="grid md:grid-cols-3 gap-4">
          <Link href="/repositories" className="p-4 border rounded-lg hover:bg-accent transition">
            <h4 className="font-semibold mb-1">📚 Repositories</h4>
            <p className="text-sm text-muted-foreground">Manage ingested works</p>
          </Link>
          <Link href="/query" className="p-4 border rounded-lg hover:bg-accent transition">
            <h4 className="font-semibold mb-1">🔎 Query</h4>
            <p className="text-sm text-muted-foreground">Search knowledge base</p>
          </Link>
          <Link href="/graph" className="p-4 border rounded-lg hover:bg-accent transition">
            <h4 className="font-semibold mb-1">🕸️ Knowledge Graph</h4>
            <p className="text-sm text-muted-foreground">Visualize dependencies</p>
          </Link>
          <Link href="/sessions" className="p-4 border rounded-lg hover:bg-accent transition">
            <h4 className="font-semibold mb-1">💬 Sessions</h4>
            <p className="text-sm text-muted-foreground">Manage checkpoints</p>
          </Link>
          <Link href="/verifier" className="p-4 border rounded-lg hover:bg-accent transition">
            <h4 className="font-semibold mb-1">🔬 Verifier</h4>
            <p className="text-sm text-muted-foreground">Citation verification</p>
          </Link>
          <Link href="/audit" className="p-4 border rounded-lg hover:bg-accent transition">
            <h4 className="font-semibold mb-1">📊 Audit</h4>
            <p className="text-sm text-muted-foreground">System audit logs</p>
          </Link>
        </div>

        {/* Status Section */}
        <div className="mt-12 p-6 bg-accent rounded-lg">
          <h3 className="text-lg font-semibold mb-3">🚀 Project Status</h3>
          <div className="space-y-2 text-sm">
            <div className="flex justify-between">
              <span>Phase 0: Repository Initialization</span>
              <span className="text-green-600 font-semibold">✅ Complete</span>
            </div>
            <div className="flex justify-between text-muted-foreground">
              <span>Phase 1: Core Backend Infrastructure</span>
              <span>🔄 Next</span>
            </div>
            <div className="flex justify-between text-muted-foreground">
              <span>Estimated Total Duration</span>
              <span>~12 weeks</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
