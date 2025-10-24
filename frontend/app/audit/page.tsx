
export default function Audit() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Audit Logs</h1>
      
      <div className="space-y-4">
        <div className="flex gap-4">
          <input 
            type="date" 
            className="px-3 py-2 border rounded-lg" 
            disabled
          />
          <input 
            type="date" 
            className="px-3 py-2 border rounded-lg" 
            disabled
          />
          <select className="px-3 py-2 border rounded-lg" disabled>
            <option>All Events</option>
          </select>
        </div>

        <div className="p-6 border rounded-lg">
          <p className="text-muted-foreground">
            Audit log viewer will be implemented in Phase 8.
          </p>
          <p className="text-sm text-muted-foreground mt-2">
            Coming soon: Search logs, filter by type, download reports.
          </p>
        </div>
      </div>
    </div>
  )
}
