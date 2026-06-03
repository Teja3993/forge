## Context
As the API layer is built using FastAPI, a mechanism is needed to accept JSON payloads from the internet and save them into PostgreSQL database. 

A common anti-pattern in development is to use the Database ORM Model (SQLAlchemy) directly as the data validator for incoming API requests. Need to decide if coupling  API layer to Database layer, or separate them.

## Decision
Strictly separating API payloads from Database models by implementing the **DTO (Data Transfer Object) Pattern**. 
* **SQLAlchemy**  exclusively handles the physical database representation (`models.py`).
* **Pydantic** will exclusively handles the API validation and serialization (`schemas.py`).

## Rationale
1. **Security (Preventing Mass Assignment):** If the internet is allowed to send JSON directly into a SQLAlchemy model, a malicious user could send a payload like `{"title": "test", "language": "cpp", "id": "uuid-1234", "is_admin": true}`. By defining a strict `SnippetCreate` Pydantic schema that *only* accepts `title`, `language`, and `code`, any injected fields like `id` are automatically stripped and ignored by FastAPI before the data ever reaches the database.
2. **Separation of Concerns:** The shape of database tables often differs from the shape of the data that is exposed to the client. For example, store `password_hash` in the database, but *never* return it in the API response. Separate Pydantic response models (`SnippetResponse`) guarantee that there is never any accidental leaking of sensitive columns.
3. **Data Validation:** Pydantic provides rigorous, automatic type-checking and validation (e.g., ensuring an email string actually looks like an email) at the perimeter of the application, keeping core logic clean.

## Consequences
* **Pros:** Complete protection against over-posting attacks, automatic Swagger UI documentation generation, and decoupled architecture.
* **Cons:** Increased boilerplate.Have to write the fields (like `title` and `language`) twice—once in `models.py` and once in `schemas.py`. This can be mitigated slightly by using inheritance (e.g., `SnippetBase`) in Pydantic.