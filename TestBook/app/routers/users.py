from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.db.session import get_db

from typing import List
from fastapi import Query


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(**user_in.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get(
    "/",
    response_model=List[UserRead]
)
def list_users(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100)
):
    return db.query(User).offset(skip).limit(limit).all()
