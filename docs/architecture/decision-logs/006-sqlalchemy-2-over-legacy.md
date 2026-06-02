**Context:** SQLAlchemy recently underwent a massive paradigm shift from the 1.x series to 2.0, fundamentally changing how models and queries are constructed to align with modern Python typing.

**Decision:** Strictly using the SQLAlchemy 2.0 declarative syntax (Mapped\[T\] and mapped\_column()).

**Why:**

*   **Strict Type-Hinting:** The Mapped\[str\] syntax integrates perfectly with Mypy and Python's built-in type checker.
    
*   **IDE Auto-Completion:** Because the models are strongly typed, IDEs like VS Code can provide real-time auto-completion when we interact with our database objects.
    
*   **Fail Fast:** Schema mismatches and type errors are caught by the linter _before_ the code even executes, drastically reducing runtime crashes.
    

**The Trade-off:** The downside is a slightly steeper learning curve and a more verbose syntax compared to the legacy Column(String) approach.