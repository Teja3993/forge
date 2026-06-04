from database.database import SessionLocal
from database.models import User

def test_insert():
    # Open a new database transaction workspace
    db = SessionLocal()
    
    try:
        # 1. Create a Python object
        new_user = User(
            username="ai_engineer_2026", 
            email="elite@forge.com", 
            password_hash="securehash123"
        )
        
        # 2. Add to the session (It is NOT in the database yet)
        db.add(new_user)
        
        # 3. Commit the transaction (This actually executes the INSERT in Postgres)
        db.commit()
        
        # 4. Refresh to get the UUID that Postgres generated
        db.refresh(new_user)
        print(f"Success! User inserted with ID: {new_user.id}")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback() # If something fails, undo everything to prevent corruption
    finally:
        db.close() # Always close the telephone line!

if __name__ == "__main__":
    test_insert()