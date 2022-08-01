from sqlalchemy import Column, String, Boolean, TIMESTAMP, Enum, Text
from sqlalchemy.sql import func

import enum

from database import Base


class AcessEnum(str, enum.Enum):
    basic = "basic"
    manager = "manager"
    admin = "admin"


class User(Base):
    __tablename__ = "user"

    username = Column(String(100), nullable=False, primary_key=True)
    job_role = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(Text, nullable=False)
    active = Column(Boolean, default=True)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
    )
    acess = Column(Enum(AcessEnum), nullable=False, default=AcessEnum.basic)
