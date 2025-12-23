from pydantic import BaseModel, Field
from typing import Optional


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    priority: int = Field(..., ge=1, le=5)
    done: Optional[bool] = False

    class Config:
        orm_mode = True


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    description: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=5)
    done: Optional[bool] = None

    class Config:
        orm_mode = True
