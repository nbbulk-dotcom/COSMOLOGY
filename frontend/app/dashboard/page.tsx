
export default function Dashboard() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      
      <div className="grid md:grid-cols-4 gap-6 mb-8">
        <div className="p-6 border rounded-lg">
          <p className="text-sm text-muted-foreground mb-1">Total Works</p>
          <p className="text-3xl font-bold">0</p>
        </div>
        <div className="p-6 border rounded-lg">
          <p className="text-sm text-muted-foreground mb-1">Total Chunks</p>
          <p className="text-3xl font-bold">0</p>
        </div>
        <div className="p-6 border rounded-lg">
          <p className="text-sm text-muted-foreground mb-1">Active Sessions</p>
          <p className="text-3xl font-bold">0</p>
        </div>
        <div className="p-6 border rounded-lg">
          <p className="text-sm text-muted-foreground mb-1">Verifications</p>
          <p className="text-3xl font-bold">0</p>
        </div>
      </div>

      <div className="p-6 border rounded-lg">
        <h2 className="text-xl font-semibold mb-4">System Status</h2>
        <p className="text-muted-foreground">
          Dashboard metrics will be implemented in Phase 8.
        </p>
      </div>
    </div>
  )
}
