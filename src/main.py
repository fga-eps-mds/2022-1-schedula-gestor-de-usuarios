import time
from urllib import response

from fastapi import FastAPI, Request, Header
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

@app.get("/")
def root():
    return {"APP": "Gestor de usuários is running"}

@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}