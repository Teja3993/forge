# ADR 011: Structured Logging and Middleware


## Context
As the API grows, tracking down bugs using standard `print()` statements becomes impossible, especially when deployed to cloud containers where standard output is ephemeral. Furthermore, manually adding request tracking to every new endpoint violates the DRY principle and relies on developer memory.

## Decision
Implemented Python's standard `logging` module to provide timestamped, severity-leveled (INFO, WARNING, ERROR) logs. Also implemented a FastAPI `@app.middleware("http")` to intercept and log the execution time and status code of every incoming request automatically.

## Consequences
1. **Request Tracing:** We can now see exactly how long a request took to process.
2. **Graceful Error Tracking:** By using `exc_info=True` in try/catch blocks, database failures will log full stack traces without exposing those stack traces to the end-user (who just sees a 500 error).