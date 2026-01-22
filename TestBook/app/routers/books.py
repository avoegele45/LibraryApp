from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.book import BookCreate, BookRead
from app.models.book import Book
from app.models.user import User
from app.db.session import get_db

from typing import List
from fastapi import Query



router = APIRouter(
    prefix="/users/{user_id}/books",
    tags=["books"]
)


@router.post(
    "/",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    user_id: int,
    book_in: BookCreate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    book = Book(**book_in.dict(), user_id=user_id)
    db.add(book)
    db.commit()
    db.refresh(book)

    return book


@router.get(
    "/",
    response_model=List[BookRead]
)
def list_books(
    user_id: int,
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    return (
        db.query(Book)
        .filter(Book.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
