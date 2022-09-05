import os

from fastapi.testclient import TestClient
from requests.structures import CaseInsensitiveDict

user = {
    'username': 'teste',
    'job_role': 'trabalho 1',
    'name': 'fulano',
    'email': 'dsahu@email.com',
    f'{os.getenv("parameter")}': 'ssjaidas',
    'active': True,
    'acess': 'basic'
}

ADMIN_HEADER = CaseInsensitiveDict(
    data={"Cookie":
          'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6ImFkbWluIn0.vu3T9_4xAf2UWL8n4c-Wm3pM8JZTAmwdBubrFWgX7nM'})  # noqa 501
MANAGER_HEADER = CaseInsensitiveDict(
    data={"Cookie":
    'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6Im1hbmFnZXIifQ.zftUNuBvt8G19eq0Wqvnd52wBuxzIatQLcSpwIrWkUQ'})  # noqa 501
BASIC_HEADER = CaseInsensitiveDict(
    data={"Cookie":
    'Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hbmFnZXIiLCJuYW1lIjoiRnVsYW5vIGRlIFRhbCIsImpvYl9yb2xlIjoiRXN0YWdpYXJpbyIsImFjY2VzcyI6ImJhc2ljIn0.YOEKPNoyA5xK0X4R1z3KNB-v9E2Oy1AokmzArx-2bks'})  # noqa 501


def test_post_user_as_admin(client: TestClient):
    response = client.post(
        url="/user",
        json=user,
        headers=ADMIN_HEADER
    )
    assert response.status_code == 201
    da = response.json()
    data = da["data"]
    assert data["username"] == "teste"
    assert data["job_role"] == "trabalho 1"
    client.delete('/user/teste', headers=ADMIN_HEADER)


def test_post_user_used_email_as_admin(client: TestClient):
    user['username'] = 'teste255'
    user['email'] = 'email1@email.com'
    response = client.post(
        "/user",
        json=user,
        headers=ADMIN_HEADER
    )
    assert response.status_code == 409
    assert response.json()['message'] == "O email já está em uso"


def test_post_user_username_as_admin(client: TestClient):
    user['username'] = 'user_A'
    user['email'] = 'email50@email.com'
    response = client.post(
        "/user",
        json=user,
        headers=ADMIN_HEADER
    )
    assert response.status_code == 409
    assert response.json()['message'] == "O username já está em uso"


def test_post_user_as_manager(client: TestClient):
    user["username"] = "teste2"
    user["email"] = "hsuh@email.com"
    response = client.post(
        "/user",
        json=user,
        headers=MANAGER_HEADER
    )
    assert response.status_code == 201
    da = response.json()
    data = da["data"]
    assert data["username"] == "teste2"
    assert data["job_role"] == "trabalho 1"
    client.delete('/user/teste2', headers=ADMIN_HEADER)


def test_post_user_used_email_as_manager(client: TestClient):
    user['username'] = 'teste255'
    user['email'] = 'email1@email.com'
    response = client.post(
        "/user",
        json=user,
        headers=MANAGER_HEADER
    )
    assert response.status_code == 409
    assert response.json()['message'] == "O email já está em uso"


def test_post_user_username_as_manager(client: TestClient):
    user['username'] = 'user_A'
    user['email'] = 'email50@email.com'
    response = client.post(
        "/user",
        json=user,
        headers=MANAGER_HEADER
    )
    assert response.status_code == 409
    assert response.json()['message'] == "O username já está em uso"


def test_post_user_as_basic(client: TestClient):
    user["username"] = "teste3"
    user["email"] = "sahuisha@email.com"
    response = client.post(
        "/user",
        json=user,
        headers=BASIC_HEADER
    )
    assert response.status_code == 401
    assert response.json()["message"] == "Acesso negado"


def test_post_user_used_email_as_basic(client: TestClient):
    user['username'] = 'teste255'
    user['email'] = 'email1@email.com'
    response = client.post(
        "/user",
        json=user,
        headers=BASIC_HEADER
    )
    assert response.status_code == 401
    assert response.json()["message"] == "Acesso negado"


def test_post_user_username_as_basic(client: TestClient):
    user['username'] = 'user_A'
    user['email'] = 'email50@email.com'
    response = client.post(
        "/user",
        json=user,
        headers=BASIC_HEADER
    )
    assert response.status_code == 401
    assert response.json()["message"] == "Acesso negado"
