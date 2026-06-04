from fastapi import FastAPI, Depends 
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Snippet
from schemas import SnippetCreate, SnippetResponse

# Initialize the FastAPI application
app = FastAPI(
    title="Forge API",
    description="The backend engine for the Forge engineering workspace.",
    version="1.0.0"
)

# A basic health-check route to ensure the server is alive
@app.get("/")
async def root():
    return {"status": "ok", "message": "Welcome to the Forge API"}

# 1. response_model=SnippetResponse tells FastAPI to automatically filter the output through your Pydantic schema
@app.post("/snippets/", response_model=SnippetResponse)
def create_snippet(snippet_in: SnippetCreate, db: Session = Depends(get_db)):
    # 2. Convert Pydantic DTO to SQLAlchemy Model
    # We never pass `snippet_in` directly to the DB. We explicitly map the fields.
    new_snippet = Snippet(
        user_id=snippet_in.user_id,
        title=snippet_in.title,
        language=snippet_in.language,
        code=snippet_in.code
    )
    
    # 3. Database Transaction Lifecycle
    db.add(new_snippet)
    db.commit()           # Saves to Postgres
    db.refresh(new_snippet) # Retrieves the Postgres-generated UUID and created_at timestamp
    
    # 4. Return the SQLAlchemy object. FastAPI will automatically convert it to SnippetResponse!
    return new_snippet