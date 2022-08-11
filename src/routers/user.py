from cmath import e

from fastapi import APIRouter, Depends, status, Path
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
    active: bool = True
    updated_at: str = None
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


class UserTemplatePut(BaseModel):
    username: str
    job_role: str
    name: str
    email: str
    password: str
    active: bool = True
    acess: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Fulano",
                "job_role": "Agente",
                "name": "Fulano de Tal",
                "email": "novoemail@gmail.com",
                "password": "Problema123",
                "acess": "manager",
            }
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
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "dados buscados com sucesso",
                "error": None,
                "data": all_data_json,
            },
        )

    else:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "dados não encontrados",
                "error": str(e),
                "data": None,
            },
        )


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

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Dados cadastrados com sucesso",
                "error": None,
                "data": new_object_json,
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Erro ao obter dados",
                "error": str(e),
                "data": None,
            },
        )


@router.delete("/user/{username}", tags=["User"])
async def delete_user(username: str, db: Session = Depends(get_db)):

    try:
        user = (
            db.query(models.User)
            .filter(models.User.username == username)
            .first()
        )
        if user:
            user.active = False
            db.commit()
            return JSONResponse(
                status_code=200,
                content={
                    "message": "Dados deletados com sucesso",
                    "error": None,
                    "data": None,
                },
            )

        else:
            return JSONResponse(
                status_code=200,
                content={
                    "message": "Usuario não encontrado",
                    "error": None,
                    "data": None,
                },
            )

    except Exception as e:
        return JSONResponse(
            status_code=404,
            content={
                "message": "Erro ao processar dados",
                "error": str(e),
                "data": None,
            },
        )


@router.put("/user/{username}", tags=["User"])
async def update_user(
    data: UserTemplatePut,
    username: str = Path(title="Username"),
    db: Session = Depends(get_db),
):
    try:
        db.query(models.User).filter_by(username=username).update(data.dict())
        db.commit()
        response_data = jsonable_encoder(
            {
                "message": "Dado atualizado com sucesso",
                "error": None,
                "data": None,
            }
        )

        return JSONResponse(
            content=response_data, status_code=status.HTTP_200_OK
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Erro ao processar dados",
                "error": str(e),
                "data": None,
            },
        )


async def get_problem_from_db(nameuser: str, db: Session):
    return db.query(models.User).filter_by(username=nameuser).one_or_none()
