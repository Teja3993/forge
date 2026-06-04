# ADR 017: Native Fetch API over Third-Party HTTP Clients

## Context
I need to make HTTP requests from React frontend to FastAPI backend. The industry standard has historically been `Axios`.

## Decision
Chose to use the native browser `fetch()` API combined with `async/await`.

## Consequences
1. Reduced dependency bloat. No need to install or maintain `Axios`.
2. Native `fetch` requires manual error handling for HTTP status codes (e.g., manually checking `response.ok`), which enforces stricter, more deliberate error-handling logic in frontend components.
3. Native `fetch` requires manual JSON serialization (`JSON.stringify`) and deserialization (`response.json()`).