from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import func
from ..models.todo import Todo


class TodoRepository:
    def get(self, db: Session, todo_id: int) -> Optional[Todo]:
        return db.get(Todo, todo_id)

    def get_by_title(self, db: Session, title: str) -> Optional[Todo]:
        stmt = select(Todo).where(func.lower(Todo.title) == title.lower())
        return db.scalar(stmt)

    def create(self, db: Session, obj: Todo) -> Todo:
        db.add(obj)
        db.flush()
        return obj

    def delete(self, db: Session, obj: Todo) -> None:
        db.delete(obj)

    def search(self, db: Session, *, done: Optional[bool] = None, keyword: Optional[str] = None, offset: int = 0, limit: int = 100) -> List[Todo]:
        stmt = select(Todo)
        if done is not None:
            stmt = stmt.where(Todo.done == done)
        if keyword:
            stmt = stmt.where(Todo.title.ilike(f"%{keyword}%"))
        stmt = stmt.offset(offset).limit(limit)
        return list(db.execute(stmt).scalars().all())
