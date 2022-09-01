import re
import jwt
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CredentialsTemplate(BaseModel):
    credential: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "credential": "Fulano",
                "password": "Problema123"
            }

        }


@router.post("/auth", tags=["Authentication"])
async def auth_user(data: CredentialsTemplate, db: Session = Depends(get_db)):
    credential = data.credential
    EMAIL_REGEX = r'^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$'
    login_by_email = re.search(EMAIL_REGEX, credential) is not None

    if login_by_email:
        user: User = db.query(User).filter(
            User.email == data.credential, User.active == True).one_or_none()  # noq 712
    else:
        user: User = db.query(User).filter(
            User.username == data.credential, User.active == True).one_or_none()  # noq 712
    if not user:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Usuário não cadastrado.",
                "error": True,
                "data": []
            },
        )
    else:
        valid = pwd_context.verify(hash=user.password, secret=data.password)
        if valid:
            encoded = jwt.encode({
                "username": user.username,
                "name": user.name,
                "job_role": user.job_role,
                "access": user.acess
            }, key="schedula", algorithm="HS256")
            token = jsonable_encoder({'token': encoded})
            {"username": "usuario1", "name": "Fulano",
                "job_role": "Policial", "access": "admin"}

            return JSONResponse(status_code=status.HTTP_200_OK,
                                content={
                                    "message": "Autenticação efetuada com sucesso.",
                                    "error": None,
                                    "data": token
                                },)
        else:
            return JSONResponse(status_code=status.HTTP_200_OK,
                                content={
                                    "message": "Senha inválida.",
                                    "error": True,
                                    "data": []
                                },)
