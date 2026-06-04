# ADR 010: Dependency Injection for Database Sessions


## Context
When a web server handles concurrent incoming traffic, database connections must be managed carefully. If the application opens a single, global database connection at startup, concurrent requests will attempt to use the same transaction simultaneously, leading to race conditions and data corruption. Alternatively, if we force every individual API route to manually write boilerplate code to open and close connections, we risk developers forgetting to close the connection, causing connection pool exhaustion.

## Decision
Utilizing FastAPI's native Dependency Injection (`Depends`) combined with Python generator functions (`yield`) to manage SQLAlchemy sessions.

## Consequences
1. **Request Isolation:** Every single API request is dynamically injected with its own isolated database session workspace.
2. **Guaranteed Cleanup:** By using the `yield` keyword, the generator pauses to allow the route logic to execute, and resumes afterward. This guarantees that the `finally: db.close()` block is executed, returning the connection to the engine pool even if the API route throws an exception.
3. **Testability:** In the future, Dependency Injection allows effortless swapping of the production database with a mock testing database by overriding the dependency during `pytest` execution.