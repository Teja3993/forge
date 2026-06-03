Implemented database version control by initializing Alembic, securely configuring env.py to use .env variables instead of hardcoded strings, connecting it to my SQLAlchemy metadata, generating the initial schema migration, and applying it to Neon PostgreSQL database.

Base.metadata.create\_all() cannot handle schema migrations (like adding a new column later) without destroying the existing table data.

Alembic creates a hidden table in PostgreSQL called alembic\_version. This is how the database "remembers" exactly which migration script was applied last.

Explicitly imported my Base from models.py and assigned it to target\_metadata. Intercepted the configuration object (config.set\_main\_option) to force it to use DATABASE\_URL instead of looking at the plaintext alembic.ini file.

Database migrations are exactly like Git, but for the _shape_ of the database instead of code files.

*   alembic revision --autogenerate is like running git add and git commit. It packages the changes into a traceable file.
    
*   alembic upgrade head is like running git push. It actually applies the changes to the live cloud database.
    
*   alembic downgrade is like running git revert.