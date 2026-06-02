**Context:** To connect SQLAlchemy to Neon.tech, a connection URL containing username, password, and host was provided. Hardcoding this directly into database.py is the fastest approach, but entirely insecure.

**Decision:** Utilizing python-dotenv to inject environment variables from a .env file, which is strictly added to .gitignore.

**Why:**

*   **Credential Leaking:** It completely prevents production database passwords from being committed to public or private GitHub repositories.
    
*   **Environment Separation:** It allows seamless switch between environments. A developer can have a local SQLite database for testing and a Neon database for production, simply by swapping thier local .env file without changing a single line of Python code.
    

**The Trade-off:** Managing secrets via .env files adds a minor external dependency and introduces deployment complexity. During eventual deployment of this platform to the cloud, these environment variables have to be manually configured in CI/CD pipeline or hosting provider. The security guarantee makes this an acceptable cost.