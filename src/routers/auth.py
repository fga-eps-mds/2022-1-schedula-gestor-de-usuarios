import re

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import User

router = APIRouter()


class CredentialsTemplate(BaseModel):
    credential: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "credential": "fulano",
                "password": "fulano123"
            }

        }


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


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
        return {"erro": True, "message": "Usuário não encontrado"}
    else:
        v = pwd_context.verify(hash=user.password, secret=data.password)
        return JSONResponse({
            "valid": v
        })
