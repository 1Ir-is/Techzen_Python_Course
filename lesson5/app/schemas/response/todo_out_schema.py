from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: int
    done: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
