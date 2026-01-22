from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
