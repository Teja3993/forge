**What I Built Today**

I built the Python bridge to my Neon PostgreSQL database using SQLAlchemy 2.0 by creating an Engine, configuring database Sessions, defining ORM models, and successfully inserting data into the cloud database using Python objects instead of writing raw SQL manually.

What I Learned

I learned how SQLAlchemy maps Python classes to database tables using declarative models.

Instead of thinking: SQL Tables —> INSERT statements —> Manual SQL Queries

I can now think: Python Objects —> ORM Translation Layer —> Generated SQL —>Database

I also learned that ORMs are are abstractions that still generate real SQL underneath.

**What Confused Me**

The difference between Engine vs Session was initially confusing. I realized:

Engine = the long-lived connection manager / connection pool

Session = the temporary workspace where objects are staged before being committed.

I got confused because running:

python database/test\_db.py

behaves differently from:

python -m database.test\_db

which taught me how Python package execution affects imports.

**My Analogy For The Day**

The Engine is the physical telephone line connecting my laptop to the Neon server.

The Session is the actual phone call.

db.add() is me preparing what I want to say.

db.commit() is me actually speaking into the receiver and sending the information.

db.rollback() is hanging up and pretending the conversation never happened.

**What’s Next**

Next I will learn database migrations using Alembic. Instead of manually editing schemas and recreating tables, migrations will allow schema evolution using version-controlled changes.