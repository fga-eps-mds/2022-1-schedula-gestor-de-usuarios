from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#DATABASE_URL = os.getenv("DATABASE_URL", "")

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/gestor_de_usuarios"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
