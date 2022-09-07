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


def test_get_user_as_admin(client: TestClient):
    response = client.get("/user?username=user_A", headers=ADMIN_HEADER)

    assert response.status_code == 200
    assert response.json()["message"] == "dados buscados com sucesso"
    assert response.json()["data"]["name"] == "Nome A"
    assert response.json()["data"]["email"] == "email1@email.com"


def test_get_all_users_as_admin(client: TestClient):
    response = client.get('/user', headers=ADMIN_HEADER)
    assert response.status_code == 200
    assert len(response.json()['data']) == 8


def test_get_user_as_manager(client: TestClient):
    response = client.get("/user?username=user_A", headers=MANAGER_HEADER)
    assert response.status_code == 200
    assert response.json()["message"] == "dados buscados com sucesso"
    assert response.json()["data"]["name"] == "Nome A"
    assert response.json()["data"]["email"] == "email1@email.com"


def test_get_all_users_as_manager(client: TestClient):
    response = client.get('/user', headers=MANAGER_HEADER)
    assert response.status_code == 200
    assert len(response.json()['data']) == 8


def test_get_user_as_basic(client: TestClient):
    response = client.get("/user?username=user_A", headers=BASIC_HEADER)
    assert response.status_code == 200
    assert response.json()["message"] == "dados buscados com sucesso"
    assert response.json()["data"]["name"] == "Nome A"
    assert response.json()["data"]["email"] == "email1@email.com"


def test_get_all_users_as_basic(client: TestClient):
    response = client.get('/user', headers=BASIC_HEADER)

    assert response.status_code == 200
    assert len(response.json()['data']) == 8
