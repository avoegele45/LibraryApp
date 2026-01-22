from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    """
    Used when a client creates a user.
    """
    pass


class UserRead(UserBase):
    """
    Used when returning a user from the API.
    """
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
