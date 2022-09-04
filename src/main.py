import time

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from routers import auth, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)


@app.middleware("http")
async def process_request_headers(request: Request, call_next):

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process time"] = str(process_time)
    return response


@app.get("/")
def root():
    return {"APP": "Gestor de usuários is running"}
