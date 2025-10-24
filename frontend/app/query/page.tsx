
export default function Query() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Query Interface</h1>
      
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium mb-2">
            Enter your question
          </label>
          <textarea
            className="w-full p-3 border rounded-lg"
            rows={4}
            placeholder="What is quantum resonance gravity?"
            disabled
          />
        </div>
        
        <button 
          className="px-6 py-2 bg-primary text-primary-foreground rounded-lg"
          disabled
        >
          Search
        </button>

        <div className="p-6 border rounded-lg">
          <p className="text-muted-foreground">
            Query interface will be implemented in Phase 8.
          </p>
          <p className="text-sm text-muted-foreground mt-2">
            Coming soon: Hybrid retrieval, citation display, result filtering.
          </p>
        </div>
      </div>
    </div>
  )
}
