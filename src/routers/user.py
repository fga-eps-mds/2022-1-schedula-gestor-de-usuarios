from cmath import e

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import engine, get_db

router = APIRouter()


class UserTemplate(BaseModel):
    username: str
    job_role: str
    name: str
    email: str
    password: str
    active: bool | None = None
    updated_at: str | None = None
    acess: str


    class Config:
        schema_extra = {
            "example": {
                "username": "Fulano",
                "job_role": "Estagiario",
                "name": "Fulano de Tal",
                "email": "email@gmail.com",
                "password": "Problema123",
                "acess": "basic",
            }
        }

def get_error_response(e: Exception):
    return {
        "message": "Erro ao processar dados",
        "error": str(e),
        "data": None
    }

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(passe):
    return pwd_context.hash(passe)


@router.get("/user/", tags=["User"])
async def get_user(db: Session = Depends(get_db)):
    all_data = db.query(models.User).filter_by(active=True).all()
    if all_data != []:
        all_data_json = jsonable_encoder(all_data)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={
            "message": "dados buscados com sucesso",
            "error": None,
            "data": all_data_json,
        })

    else:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={
                                "message": "dados não encontrados",
                                "error": str(e),
                                "data": None,
                            })


@router.post("/user/", tags=["User"])
async def post_user(data: UserTemplate, db: Session = Depends(get_db)):
    try:
        new_object = models.User(**data.dict())
        new_object.password = str(get_password_hash(new_object.password))
        db.add(new_object)
        db.commit()
        db.refresh(new_object)

        new_object.updated_at = str(new_object.updated_at)

        new_object_json = jsonable_encoder(new_object)

        return JSONResponse(status_code=status.HTTP_201_CREATED, content={
            "message": "Dados cadastrados com sucesso",
            "error": None,
            "data": new_object_json,
        })
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Erro ao obter dados",
                "error": str(e),
                "data": None,
            })


@router.delete("/user/{username}", tags=["User"])
async def delete_user(username: str, db: Session = Depends(get_db)):

    try:
        user = db.query(
            models.User).filter(
            models.User.username == username).first()
        if user:
            user.active = False
            db.commit()
            return JSONResponse(status_code=200, content={
                "message": "Dados deletados com sucesso",
                "error": None,
                "data": None,
            })

        else:
            return JSONResponse(status_code=200, content={
                "message": "Usuario não encontrado",
                "error": None,
                "data": None,
            })

    except Exception as e:
        return JSONResponse(status_code=404, content={
            "message": "Erro ao processar dados",
            "error": str(e),
            "data": None,
        })


@router.put("/user/{username}", tags=["User"])
async def update_user(data: UserTemplate , nameuser: str ,db: Session=Depends(get_db)):
    try:
        input_values = models.User(**data.dict())
        User = await get_problem_from_db(nameuser, db)
        if User:

            User.username = input_values.username
            User.job_role = input_values.job_role
            User.email = input_values.email
            User.name = input_values.name
            User.password = input_values.password
            User.active = input_values.active
            User.updated_at = input_values.updated_at
            User.acess = input_values.acess

            db.add(User)
            db.commit()
            db.refresh(User)

            User = jsonable_encoder(User)
            response_data = jsonable_encoder({
                "message": "Usuário atualizado com sucesso",
                "error": None,
                "data": User
            })
        else:
            response_data = jsonable_encoder({
                "message": f"Usuário não encontrado",
                "error": None,
                "data": None
            })
        return JSONResponse(content=response_data,status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content=get_error_response(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

async def get_problem_from_db(nameuser: str, db: Session):
    return db.query(models.User).filter_by(username=nameuser).one_or_none()