from cmath import e
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.responses import JSONResponse, HTMLResponse
import json
from sqlalchemy import inspect
from fastapi.encoders import jsonable_encoder


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

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

models.Base.metadata.create_all(bind = engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(passe):
    return pwd_context.hash(passe)


@router.get("/user/", tags = ["User"])
def get_user(db: Session = Depends(get_db)):
    all_data = db.query(models.User).all()
    if(all_data != []):
        all_data_json = jsonable_encoder(all_data)
        return JSONResponse(status_code = status.HTTP_201_CREATED, content = {
                "message": "dados buscados com sucesso",
                "error": None,
                "data": all_data_json,
            })

    else:
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, content = {
            "message": "dados não encontrados",
            "error": str(e),
            "data": None,
        })

@router.post("/user/", tags = ["User"])
def post_chamado(data: UserTemplate, db: Session = Depends(get_db)):
    try:
        new_object = models.User(**data.dict())
        new_object.password = str(get_password_hash(new_object.password))
        db.add(new_object)
        db.commit()
        db.refresh(new_object)


        new_object.updated_at = str(new_object.updated_at) 
        new_object.active = str(new_object.active)

        new_object_json = jsonable_encoder(new_object)

        return JSONResponse(status_code = status.HTTP_201_CREATED, content = {
            "message": "Dados buscados com sucesso",
            "error": None,
            "data": new_object_json,
        })
    except Exception as e:
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, content = {
            "message": "Erro ao obter dados",
            "error": str(e),
            "data": None,
        })

@router.delete("/user/{username}", tags=["User"])
def delete_user(username: str, db: Session = Depends(get_db)):

    try:
        deluser = find_user(username, db)
        db.delete(deluser)
        db.commit()
        return JSONResponse(status_code = 200, content = {
            "message": "Dados deletados com sucesso",
            "error": None,
            "data": None,
        })

    except Exception as e:
        return JSONResponse(status_code = 404, content = {
            "message": "Erro ao encontrar dados",
            "error": str(e),
            "data": None,
        })

#usado para encontrar user pelo username
@router.get("/items/")
def find_user(us, db):
    db_user = db.query(models.User).filter(models.User.username == us).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
