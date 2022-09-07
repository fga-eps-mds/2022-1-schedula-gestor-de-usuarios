from fastapi.testclient import TestClient
from requests.structures import CaseInsensitiveDict

ADMIN_HEADER = CaseInsensitiveDict(
    data={"Cookie":
          'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6ImFkbWluIn0.vu3T9_4xAf2UWL8n4c-Wm3pM8JZTAmwdBubrFWgX7nM'})  # noqa 501
MANAGER_HEADER = CaseInsensitiveDict(
    data={"Cookie":
    'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6Im1hbmFnZXIifQ.zftUNuBvt8G19eq0Wqvnd52wBuxzIatQLcSpwIrWkUQ'})  # noqa 501
BASIC_HEADER = CaseInsensitiveDict(
    data={"Cookie":
    'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6ImJhc2ljIn0.YOEKPNoyA5xK0X4R1z3KNB-v9E2Oy1AokmzArx-2bks'})  # noqa 501


def test_put_user_as_admin(client: TestClient):
    response = client.put(
        "/user/user_I",
        json={
            "job_role": "string",
            "name": "fulano",
            "email": "novoemail@email.com",
            "password": "string",
            "active": True,
            "acess": "basic"
        },
        headers=ADMIN_HEADER
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Dado atualizado com sucesso"
    data = response.json()["data"]
    assert data["email"] == "novoemail@email.com"
    assert data["name"] == "fulano"


def test_put_non_existing_user(client: TestClient):
    response = client.put(
        "/user/nao_tem",
        json={
            "job_role": "string",
            "name": "string",
            "email": "string@email.com",
            "password": "string",
            "active": True,
            "acess": "basic"
        },
        headers=ADMIN_HEADER
    )
    assert response.status_code == 404
    assert response.json() == {
        "message": "Dado não encontrado na base",
        "error": None,
        "data": None,
    }


def test_put_user_as_manager(client: TestClient):
    response = client.put(
        "/user/user_K",
        json={
            "job_role": "estagiario",
            "name": "stng",
            "email": "stg@email.com"
        },
        headers=MANAGER_HEADER
    )
    assert response.status_code == 200
    da = response.json()
    data = da["data"]
    assert da["message"] == "Dado atualizado com sucesso"
    assert data["email"] == "stg@email.com"


def test_put_user_as_basic(client: TestClient):
    response = client.put(
        "/user/user_C",
        json={
            "job_role": "estagiario",
            "name": "stng",
            "email": "stg@email.com"
        },
        headers=BASIC_HEADER
    )
    assert response.status_code == 401
    assert response.json()["message"] == "Acesso negado"
