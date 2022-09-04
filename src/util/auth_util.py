import os
import jwt
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from typing import Union, Any, List
from fastapi import Request, status


ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: Union[dict, Any]) -> str:
    return jwt.encode(subject, JWT_SECRET_KEY, ALGORITHM)

def get_authorization(request: Request) -> str:
    authorization = request.cookies.get('Authorization')
    if authorization:
        auth = decode_access_token(authorization)
    else:
        auth = 'public'
    return auth

def decode_access_token(encoded_jwt: str) -> str:
    return jwt.decode(encoded_jwt, key=JWT_SECRET_KEY, algorithms=[ALGORITHM])['access']

def manage_authorization(allowed_profiles: List[str], request: Request):
    auth = get_authorization(request)
    if auth in allowed_profiles:
        return JSONResponse({"message": "Acesso negado!",
                             "error": True,
                             "data": None,
                             }, status.HTTP_401_UNAUTHORIZED)
    else:
        return None
