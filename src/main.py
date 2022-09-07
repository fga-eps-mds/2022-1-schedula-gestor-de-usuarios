from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from routers import auth, user
from util.auth_util import get_authorization

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://2022-1-schedula-front-homol.vercel.app",
        "http://localhost:3000",
    ],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)


response_unauthorized = JSONResponse({
    "message": "Acesso negado",
    "error": True,
    "data": None,

}, status.HTTP_401_UNAUTHORIZED)


@app.middleware("http")
async def process_request_headers(request: Request, call_next):
    auth = str(get_authorization(request))
    method = str(request.method)
    if 'user' in str(request.url):
        if method == 'DELETE':
            if auth != 'admin':
                return response_unauthorized
        elif method in ['POST', 'PUT']:
            if auth not in ['admin', 'manager']:
                return response_unauthorized
        elif method == 'GET':
            if auth not in ['admin', 'manager', 'basic']:
                return response_unauthorized
    return await call_next(request)

app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"APP": "Gestor de usuários is running"}
