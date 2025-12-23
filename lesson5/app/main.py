import uuid
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

from .routers import todo_router


app = FastAPI(title="Todo API - DB version")


class TraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = str(uuid.uuid4())
        request.state.trace_id = trace_id
        logger.bind(trace_id=trace_id).info(f"incoming {request.method} {request.url.path}")
        response = await call_next(request)
        response.headers["X-Trace-Id"] = trace_id
        return response


@app.on_event("startup")
async def startup_event():
    logger.info("Starting app")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down app")


app.add_middleware(TraceMiddleware)

app.include_router(todo_router.router)
