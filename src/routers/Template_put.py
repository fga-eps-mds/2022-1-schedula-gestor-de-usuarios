import models
from pydantic import BaseModel
from database import engine, get_db

class UserTemp(BaseModel):
    username: str | None = None
    job_role: str | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None
    active: bool = True
    updated_at: str | None = None
    acess: str | None = None