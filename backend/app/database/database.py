import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Load environment variables from the .env file
load_dotenv()

# Get the URL. SQLAlchemy requires 'postgresql://' not 'postgres://'
DATABASE_URL = os.getenv("DATABASE_URL")

# 1. The Engine (The connection pool)
# echo=True prints the raw SQL SQLAlchemy generates to the terminal (Great for debugging!)
engine = create_engine(DATABASE_URL, echo=True)

# 2. The SessionLocal class (Each instance of this will be a database session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. The Declarative Base (The parent class for all our Models)
class Base(DeclarativeBase):
    pass

# Dependency Injector
def get_db():
    db = SessionLocal()
    try:
        # yield pauses the execution here, hands the 'db' to the route, 
        # and waits for the route to finish before moving to the 'finally' block.
        yield db
    finally:
        db.close()