# ADR 013: APIRouter and Modular Architecture

## Context
As the API expands to include authentication, user profiles, and AI integrations, managing all endpoints within a single `main.py` file becomes an anti-pattern. It violates the Single Responsibility Principle, makes the codebase difficult to navigate, and increases the likelihood of Git merge conflicts in a team environment.

## Decision
Refactored the application to use FastAPI's `APIRouter`. Established an `app/` package structure with dedicated directories for `routers`, `models`, `schemas`, and `database`.

## Consequences
1. `main.py` is now strictly an entry point responsible only for global configurations (CORS, Middleware, Router instantiation).
2. Domain logic (e.g., Snippets) is highly encapsulated.
3. Import paths must now be absolute relative to the `app` package (e.g., `from app.schemas import...`), requiring `PYTHONPATH=.` for execution outside of Docker.