from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func, UniqueConstraint
from ..db import Base


class TimeMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class Todo(Base, TimeMixin):
    __tablename__ = "todos"
    __table_args__ = (UniqueConstraint("title", name="uq_todos_title"),)

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    priority = Column(Integer, nullable=False)
    done = Column(Boolean, nullable=False, default=False, server_default="false")

    def __repr__(self) -> str:
        return f"<Todo id={self.id} title={self.title!r}>"
