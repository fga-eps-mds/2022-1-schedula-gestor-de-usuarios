from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)


@app.get("/")
def root():
    return {"APP": "Gestor de usuários is running"}
