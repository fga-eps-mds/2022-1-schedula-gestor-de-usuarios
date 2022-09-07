import re

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import User
from util.auth_util import create_access_token, verify_password

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
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "message": "Usuário não cadastrado.",
                "error": True,
                "data": []
            },
        )
    else:
        if verify_password(data.value, user.password):
            token = create_access_token({
                                        "username": user.username,
                                        "name": user.name,
                                        "job_role": user.job_role,
                                        "access": user.acess
                                        })
            response = JSONResponse(status_code=status.HTTP_200_OK,
                                    content={
                                        "message": "Autenticação efetuada com sucesso.",  # noqa 501
                                        "error": None,
                                        "data": []
                                    })
            response.set_cookie(key='Authorization', value=token)
            return response
        else:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                                content={
                                    "message": "Senha inválida.",
                                    "error": True,
                                    "data": []
                                },)
