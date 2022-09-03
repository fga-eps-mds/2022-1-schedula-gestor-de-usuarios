import time
from urllib import response

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from routers import auth, user

app = FastAPI()

@app.get("/items/")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process time"] = str(process_time)
    return response
