from fastapi import FastAPI
from controllers.todo_controller import router as todo_router

app = FastAPI(title="In-memory Todo API (MVC + Service)")

app.include_router(todo_router)
