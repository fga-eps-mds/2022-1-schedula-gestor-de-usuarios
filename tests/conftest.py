from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import pytest
import os
import sys

try:
    sys.path.append(os.getcwd() + "/src")
except Exception:
    pass

from main import app
from database import get_db
import models

engine = create_engine("sqlite:///test.db")
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

models.Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="session")
def session():
    session = TestingSessionLocal()

    # Para o momento em que se for realizar testes nos enpoints
    # with open("data/insert_user.sql", "r") as f:
    #     session.execute(f.read())
    #     session.commit()
    yield session
    os.remove("test.db")


@pytest.fixture(scope="function")
def client(session):
    def get_db_test():
        db = session
        try:
            yield db
        finally:
            db.close()

    with TestClient(app) as client:
        app.dependency_overrides[get_db] = get_db_test
        yield client
