from typing import List, Optional
from fastapi import HTTPException

from lesson4.fastapi_crud_in_memory.models.todo import TodoCreate, TodoUpdate

# In-memory storage
_todos: List[dict] = []
_id_counter = 1


def _next_id() -> int:
    global _id_counter
    curr = _id_counter
    _id_counter += 1
    return curr


def _title_exists(title: str, exclude_id: Optional[int] = None) -> bool:
    t = title.strip().lower()
    for item in _todos:
        if exclude_id is not None and item["id"] == exclude_id:
            continue
        if item["title"].strip().lower() == t:
            return True
    return False


def create_todo(data: TodoCreate) -> dict:
    if _title_exists(data.title):
        raise HTTPException(status_code=409, detail="Todo title already exists")
    todo = {
        "id": _next_id(),
        "title": data.title.strip(),
        "description": data.description,
        "priority": data.priority,
        "done": data.done,
    }
    _todos.append(todo)
    return todo


def list_todos(done: Optional[bool] = None, keyword: Optional[str] = None, limit: int = 10) -> List[dict]:
    results = _todos
    if done is not None:
        results = [t for t in results if t["done"] == done]
    if keyword:
        kw = keyword.strip().lower()
        results = [t for t in results if kw in t["title"].strip().lower()]
    return results[:limit]


def get_todo(todo_id: int) -> Optional[dict]:
    for t in _todos:
        if t["id"] == todo_id:
            return t
    return None


def replace_todo(todo_id: int, data: TodoCreate) -> Optional[dict]:
    todo = get_todo(todo_id)
    if todo is None:
        return None
    if _title_exists(data.title, exclude_id=todo_id):
        raise HTTPException(status_code=409, detail="Todo title already exists")
    todo.update({
        "title": data.title.strip(),
        "description": data.description,
        "priority": data.priority,
        "done": data.done,
    })
    return todo


def update_todo_partial(todo_id: int, data: TodoUpdate) -> Optional[dict]:
    todo = get_todo(todo_id)
    if todo is None:
        return None
    if data.title is not None:
        if _title_exists(data.title, exclude_id=todo_id):
            raise HTTPException(status_code=409, detail="Todo title already exists")
        todo["title"] = data.title.strip()
    if data.description is not None:
        todo["description"] = data.description
    if data.priority is not None:
        todo["priority"] = data.priority
    if data.done is not None:
        todo["done"] = data.done
    return todo


def delete_todo(todo_id: int) -> bool:
    for idx, t in enumerate(_todos):
        if t["id"] == todo_id:
            _todos.pop(idx)
            return True
    return False
