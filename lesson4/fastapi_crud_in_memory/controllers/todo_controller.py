# File: `controllers/todo_controller.py`
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, Response, status
from lesson4.fastapi_crud_in_memory.models.todo import TodoCreate, TodoOut, TodoUpdate
from lesson4.fastapi_crud_in_memory.services import todo_service as svc
router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("", response_model=TodoOut, status_code=201)
def create_todo_endpoint(payload: TodoCreate):
    todo = svc.create_todo(payload)
    return todo


@router.get("", response_model=List[TodoOut])
def list_todos_endpoint(
    done: Optional[bool] = None,
    keyword: Optional[str] = None,
    limit: int = Query(10, ge=1, le=50),
):
    todos = svc.list_todos(done=done, keyword=keyword, limit=limit)
    return todos


@router.get("/{todo_id}", response_model=TodoOut)
def get_todo_endpoint(todo_id: int):
    todo = svc.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoOut)
def replace_todo_endpoint(todo_id: int, payload: TodoCreate):
    todo = svc.replace_todo(todo_id, payload)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoOut)
def update_todo_endpoint(todo_id: int, payload: TodoUpdate):
    todo = svc.update_todo_partial(todo_id, payload)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_endpoint(todo_id: int):
    ok = svc.delete_todo(todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Todo not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
