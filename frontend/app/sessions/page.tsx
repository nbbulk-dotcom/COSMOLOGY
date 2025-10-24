
export default function Sessions() {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Sessions</h1>
        <button className="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90">
          New Session
        </button>
      </div>
      
      <div className="p-6 border rounded-lg">
        <p className="text-muted-foreground">
          Session management will be implemented in Phase 8.
        </p>
        <p className="text-sm text-muted-foreground mt-2">
          Coming soon: Create checkpoints, rehydrate sessions, view history.
        </p>
      </div>
    </div>
  )
}
