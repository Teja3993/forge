**Context:** On Day 1, database schema was designed and data was inserted using raw SQL queries via DBeaver. As the application scales, managing hundreds of raw SQL strings inside Python files becomes a massive bottleneck and a security liability.

**Decision:** Adopting the **SQLAlchemy Object-Relational Mapper (ORM)** to interact with Neon PostgreSQL database using Python classes.

**Why:**

*   **SQL Injection Prevention:** SQLAlchemy uses parameterized queries. It separates the SQL logic from the user input, making standard injection attacks nearly impossible.
    
*   **Maintainability:** Refactoring a Python class (e.g., renaming a property) is natively supported by IDE. Grepping and replacing text across dozens of raw SQL strings is error-prone.
    
*   **Database Agnosticism:** The ORM abstracts the SQL dialect. If ever migrating from PostgreSQL to MySQL, there's no need to rewrite queries; the ORM handles the dialect translation.
    

**The Trade-off:** The downside of an ORM is that it adds processing overhead and abstracts the underlying SQL execution. If not careful, this can lead to highly inefficient queries, such as the **N+1 problem** (making 100 queries to fetch 100 users' snippets instead of 1 JOIN). However, for current monolithic foundation, the development velocity and type-safety heavily outweigh this performance risk.