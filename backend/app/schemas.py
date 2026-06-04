from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

# 1. Shared properties (Everything a snippet naturally has)
class SnippetBase(BaseModel):
    title: str
    language: str
    code: str

# 2. Properties to receive on snippet creation (The user shouldn't send an ID or Date)
class SnippetCreate(SnippetBase):
    user_id: UUID # Temporary: We require the client to send this until we build JWT Auth!

# 3. Properties to return to the client (The API Response)
class SnippetResponse(SnippetBase):
    id: UUID
    user_id: UUID
    created_at: datetime

    # Pydantic V2 Config: This tells Pydantic to read data even if it's not a strict dictionary.
    # It allows Pydantic to read SQLAlchemy ORM objects (e.g., snippet.title instead of snippet["title"])
    model_config = ConfigDict(from_attributes=True)