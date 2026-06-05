# ADR 019: Observability-First Debugging


## Context
When integrating distributed systems (Next.js client and FastAPI server), failures are inevitable. Relying on "guess and check" modifications to code is inefficient and dangerous.

## Decision
Enforcing a strict, observability-first debugging protocol utilizing Chrome DevTools (Network/Console tabs) and Python Structured Logging. 

## Consequences
1. Network Tab analysis allows us to immediately isolate whether a bug is a Client-Side payload generation error or a Server-Side processing error.
2. We treat HTTP status codes as the primary diagnostic indicator (4xx = Client fault, 5xx = Server fault).
3. The system is hardened to ensure backend stack traces are logged securely via middleware but never leaked to the client response payload.