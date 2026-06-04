from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database.database import get_db
from app.database.models import Snippet
from app.schemas import SnippetCreate, SnippetResponse
from app.logger import logger

# Initialize the router
router = APIRouter(prefix="/snippets", tags=["Snippets"])

@router.post("/", response_model=SnippetResponse)
def create_snippet(snippet_in: SnippetCreate, db: Session = Depends(get_db)):
    try:
        new_snippet = Snippet(
            user_id=snippet_in.user_id,
            title=snippet_in.title,
            language=snippet_in.language,
            code=snippet_in.code
        )
        db.add(new_snippet)
        db.commit()
        db.refresh(new_snippet)
        
        logger.info(f"Successfully created snippet with ID: {new_snippet.id}")
        return new_snippet
    except Exception as e:
        logger.error(f"Failed to create snippet: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/", response_model=List[SnippetResponse])
def get_all_snippets(db: Session = Depends(get_db)):
    return db.query(Snippet).all()

@router.get("/{snippet_id}", response_model=SnippetResponse)
def get_snippet(snippet_id: UUID, db: Session = Depends(get_db)):
    snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
    if not snippet:
        logger.warning(f"Snippet lookup failed. ID not found: {snippet_id}")
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet