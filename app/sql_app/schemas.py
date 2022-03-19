from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    pass

class PostCreate(PostBase):
    title: str
    content: str
    published_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class PostUpdate(PostBase):
    id: int
    title: Optional[str]
    content: Optional[str]
    published_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class Post(PostBase):
    id: int
    title: Optional[str]
    content: Optional[str]
    published_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
