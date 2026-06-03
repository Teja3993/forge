**Context:** On Day 2, the database schema was abstracted into SQLAlchemy Python classes (Models). In a local tutorial environment, one might use Base.metadata.create\_all(bind=engine) to instantly create these tables. However, create\_all() is "blind" and it only creates new tables, it cannot detect if a column was added, renamed, or deleted after the initial creation.

**Decision:** Adopting **Alembic** as the database migration and schema version control tool.

**Why:**

*   **Schema Evolution:** As the forge platform grows, columns will be added inevitably (e.g., is\_active for users) or relationships will be changed. Alembic detects these changes in Python models and generates the exact ALTER TABLE SQL commands needed to update the production database without dropping existing data.
    
*   **Disaster Recovery (Rollbacks):** Every Alembic migration contains an upgrade() and a downgrade() function. If a database deployment breaks production, running alembic downgrade -1 acts as an immediate undo button, reverting the database to its previous stable state.
    
*   **Security & Credential Management:** By overriding Alembic's default alembic.ini behavior and dynamically injecting the database URL directly into env.py using python-dotenv, database credentials are ensured to never accidentally get leaked into version control.
    

**The Trade-off:** The downside of using Alembic is that it adds operational overhead to the deployment pipeline. Furthermore, --autogenerate is not perfect. It can sometimes misinterpret a renamed column as a "Drop Table and Recreate Table" command. The trade-off is that engineers must adopt the discipline of manually reading and verifying every generated migration script before running upgrade head.