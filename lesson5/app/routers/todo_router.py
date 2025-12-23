from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session
from typing import List
from pydantic.generics import GenericModel
from typing import TypeVar, Generic

from ..db import get_db
from ..schemas.request.todo_schema import TodoCreate, TodoUpdate
from ..schemas.response.todo_out_schema import TodoOut
from ..services.todo_service import (
    create_todo,
    get_todo,
    list_todos,
    update_todo_put,
    update_todo_patch,
    delete_todo,
)

router = APIRouter(prefix="/todos", tags=["todos"])

T = TypeVar("T")


class StandardResponse(GenericModel, Generic[T]):
    trace_id: str
    data: T


@router.post("", status_code=status.HTTP_201_CREATED, response_model=StandardResponse[TodoOut], responses={409: {"description": "Conflict"}})
def post_todo(request: Request, payload: TodoCreate, db: Session = Depends(get_db)):
    todo = create_todo(db, payload)
    trace_id = getattr(request.state, "trace_id", "")
    return StandardResponse(trace_id=trace_id, data=todo)


@router.get("", response_model=StandardResponse[List[TodoOut]])
def get_todos(request: Request, done: bool | None = None, keyword: str | None = None, offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = list_todos(db, done, keyword, offset, limit)
    trace_id = getattr(request.state, "trace_id", "")
    return StandardResponse(trace_id=trace_id, data=todos)


@router.get("/{todo_id}", response_model=StandardResponse[TodoOut], responses={404: {"description": "Not found"}})
def get_todo_by_id(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    trace_id = getattr(request.state, "trace_id", "")
    return StandardResponse(trace_id=trace_id, data=todo)


@router.put("/{todo_id}", response_model=StandardResponse[TodoOut], responses={400: {"description": "Bad Request"}, 404: {"description": "Not found"}, 409: {"description": "Conflict"}})
def put_todo(request: Request, todo_id: int, payload: TodoCreate, db: Session = Depends(get_db)):
    todo = update_todo_put(db, todo_id, payload)
    trace_id = getattr(request.state, "trace_id", "")
    return StandardResponse(trace_id=trace_id, data=todo)


@router.patch("/{todo_id}", response_model=StandardResponse[TodoOut], responses={400: {"description": "Bad Request"}, 404: {"description": "Not found"}, 409: {"description": "Conflict"}})
def patch_todo(request: Request, todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)):
    todo = update_todo_patch(db, todo_id, payload)
    trace_id = getattr(request.state, "trace_id", "")
    return StandardResponse(trace_id=trace_id, data=todo)


@router.delete("/{todo_id}", status_code=204, responses={404: {"description": "Not found"}})
def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    delete_todo(db, todo_id)
    return None
