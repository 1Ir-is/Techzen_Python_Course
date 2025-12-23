from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..repositories.todo_repository import TodoRepository
from ..models.todo import Todo
from ..schemas.request.todo_schema import TodoCreate, TodoUpdate


repo = TodoRepository()


def create_todo(db: Session, data: TodoCreate) -> Todo:
    existing = repo.get_by_title(db, data.title)
    if existing:
        raise HTTPException(status_code=409, detail="Todo with this title already exists")
    if data.priority < 1 or data.priority > 5:
        raise HTTPException(status_code=400, detail="priority must be between 1 and 5")

    todo = Todo(
        title=data.title,
        description=data.description,
        priority=data.priority,
        done=bool(data.done),
    )
    repo.create(db, todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo(db: Session, todo_id: int) -> Todo:
    todo = repo.get(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


def list_todos(db: Session, done: bool | None, keyword: str | None, offset: int, limit: int) -> List[Todo]:
    return repo.search(db, done=done, keyword=keyword, offset=offset, limit=limit)


def update_todo_put(db: Session, todo_id: int, data: TodoCreate) -> Todo:
    todo = get_todo(db, todo_id)
    found = repo.get_by_title(db, data.title)
    if found and found.id != todo.id:
        raise HTTPException(status_code=409, detail="Todo with this title already exists")

    todo.title = data.title
    todo.description = data.description
    todo.priority = data.priority
    todo.done = bool(data.done)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo_patch(db: Session, todo_id: int, data: TodoUpdate) -> Todo:
    todo = get_todo(db, todo_id)
    if data.title:
        found = repo.get_by_title(db, data.title)
        if found and found.id != todo.id:
            raise HTTPException(status_code=409, detail="Todo with this title already exists")
        todo.title = data.title
    if data.description is not None:
        todo.description = data.description
    if data.priority is not None:
        if data.priority < 1 or data.priority > 5:
            raise HTTPException(status_code=400, detail="priority must be between 1 and 5")
        todo.priority = data.priority
    if data.done is not None:
        todo.done = data.done

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo_id: int) -> None:
    todo = get_todo(db, todo_id)
    repo.delete(db, todo)
    db.commit()
