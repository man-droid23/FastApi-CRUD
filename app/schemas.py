from turtle import title
from pydantic import BaseModel
from datetime import datetime

#for request body
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

#for response body
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True