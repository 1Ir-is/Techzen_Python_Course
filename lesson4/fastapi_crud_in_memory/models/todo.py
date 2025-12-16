from typing import Optional
from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: str | None = None
    priority: int = Field(..., ge=1, le=5)
    done: bool = False

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3)
    description: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=5)
    done: Optional[bool] = None

class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: int
    done: bool
