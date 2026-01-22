from pydantic import BaseModel
from typing import Optional
from datetime import date


class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    rating: Optional[int] = None


class BookCreate(BookBase):
    """
    Used when creating a book.
    """
    pass


class BookRead(BookBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
