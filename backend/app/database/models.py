import uuid
from sqlalchemy import String, Text, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    # We map the Python UUID to the Postgres UUID. 
    # server_default tells SQLAlchemy that the database will generate the UUID automatically.
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))

    # Relationship: A user can have many snippets
    snippets = relationship("Snippet", back_populates="owner", cascade="all, delete-orphan")

class Snippet(Base):
    __tablename__ = "code_snippets"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    language: Mapped[str] = mapped_column(String(30), nullable=False)
    code: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))

    # Relationship: A snippet belongs to one owner
    owner = relationship("User", back_populates="snippets")