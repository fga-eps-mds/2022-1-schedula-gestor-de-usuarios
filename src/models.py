from sqlalchemy import Column, String, Boolean, DateTime, LargeBinary, Enum, Text

import enum

from database import Base

class AcessEnum(enum.Enum):
    basic = 1
    manager = 2
    admin = 3


class User(Base):
    __tablename__ = "user"

    username = Column(String(100), nullable=False, primary_key=True)
    job_role = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(Text, nullable=False)
    active = Column(Boolean, default = True)
    updated_at = Column(DateTime(timezone=True), nullable=False)
    acess  = Column(Enum(AcessEnum), nullable=False, default = AcessEnum.basic)

