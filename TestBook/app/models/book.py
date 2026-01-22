from sqlalchemy import (
    Column, Integer, String, Text, Boolean,
    Date, Numeric, TIMESTAMP, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    isbn = Column(String(20))
    description = Column(Text)
    language = Column(Text)
    translated = Column(Boolean, default=False)
    book_link = Column(Text)

    status = Column(Text)
    priority = Column(Integer)
    rating = Column(Integer)
    number_of_copies = Column(Integer, default=1)
    times_read = Column(Integer, default=0)
    dnf = Column(Boolean, default=False)
    annotated = Column(Boolean, default=False)
    acquired = Column(Boolean, default=True)
    notes = Column(Text)
    price = Column(Numeric(6, 2))

    main_genre = Column(Text)
    sub_genre = Column(Text)
    nonfiction = Column(Boolean, default=False)
    intended_audience = Column(Text)
    diverse = Column(Boolean, default=False)
    lgbtqi_rep = Column(Boolean, default=False)

    format = Column(Text)
    medium = Column(Text)
    publisher = Column(Text)
    imprint = Column(Text)
    publication_type = Column(Text)
    release_date = Column(Date)
    series = Column(Text)
    series_number = Column(Integer)
    collection = Column(Text)

    year_added = Column(Integer)
    year_read = Column(Integer)
    month_read = Column(Integer)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship("User", backref="books")
