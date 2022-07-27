from fastapi import APIRouter, Depends
from pydantic import BaseModel

from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session

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
    active: bool
    updated_at: str
    acess: str

models.Base.metadata.create_all(bind = engine)

@router.get("/user/", tags = ["User"])
def get_user(db: Session = Depends(get_db)):
    all_data = db.query(models.User).all()
    return{
        "message": "dados buscados com sucesso",
        "error": None,
        "data": all_data,

    }

@router.post("/user/", tags = ["User"])
def post_chamado(data: UserTemplate, db: Session = Depends(get_db)):
    new_object = models.User(**data.dict())
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return{
        "message": "Dados buscados com sucesso",
        "error": None,
        "data": new_object,
    }
