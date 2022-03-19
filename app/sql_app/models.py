from sqlalchemy import Column, Integer, String, Text, DateTime

from .database import Base


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    content = Column(Text)
    published_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)