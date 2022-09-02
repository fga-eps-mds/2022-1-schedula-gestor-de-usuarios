import re
import os
import jwt
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import User

router = APIRouter()


class CredentialsTemplate(BaseModel):
    credential: str
    value: str

    class Config:
        schema_extra = {
            "example": {
                "credential": "Fulano",
                "value": "Problema123"
            }

        }


@router.post("/auth", tags=["Authentication"])
async def auth_user(data: CredentialsTemplate, db: Session = Depends(get_db)):
    credential = data.credential
    EMAIL_REGEX = r'^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$'  # noqa 501
    login_by_email = re.search(EMAIL_REGEX, credential) is not None
    if login_by_email:
        user: User = db.query(User).filter(
            User.email == data.credential,
            User.active == True).one_or_none()  # noqa 712
    else:
        user: User = db.query(User).filter(User.username ==
        data.credential, User.active == True).one_or_none()  # noqa 712
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
        if user.password == data.value:
            encoded = jwt.encode({
                "username": user.username,
                "name": user.name,
                "job_role": user.job_role,
                "access": user.acess
            }, key=os.getenv('secret'), algorithm="HS256")
            token = jsonable_encoder({'token': encoded})
            return JSONResponse(status_code=status.HTTP_200_OK,
                                content={
                                    "message": "Autenticação efetuada com sucesso.",  # noqa 501
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
