from fastapi.testclient import TestClient

from routers.user import get_password_hash, pwd_context


def test_get_password_hash():
    psw = get_password_hash('fulano123')
    assert pwd_context.verify('fulano123', psw)


def test_auth_by_username(client: TestClient):
    response = client.post('/auth', json={
        "credential": "user_A",
        "pwd": "senha1"

    })

    assert response.json() == {
        "message": "Autenticação efetuada com sucesso.",
        "error": None,
        "data": {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXJfQSIsIm5hbWUiOiJOb21lIEEiLCJqb2Jfcm9sZSI6IlRyYWJhbGhvIDEiLCJhY2Nlc3MiOiJhZG1pbiJ9.cCarXgAlBG7HtaDXXv_UEwcEKuuIehM43_JwZQf_YCE"  # noqa 501
        }
    }
    assert response.status_code == 200
    assert not response.json()["error"]


def test_auth_by_email(client: TestClient):
    response = client.post('/auth', json={
        "credential": "email3@email.com",
        "pwd": "senha3"
    })
    assert response.status_code == 200
    assert not response.json()["error"]


def test_invalid_email(client: TestClient):
    response = client.post('/auth', json={
        "credential": "naoexiste@email.com",
        "pwd": "senha3"
    })

    assert response.json()["error"]
    assert response.json()["message"] == "Usuário não cadastrado."
    assert response.status_code == 200


def test_invalid_user(client: TestClient):
    response = client.post('/auth', json={
        "credential": "naoexiste",
        "pwd": "senha50"
    })

    assert response.json()["error"]
    assert response.json()["message"] == "Usuário não cadastrado."
    assert response.status_code == 200


def test_inactive_user(client: TestClient):
    response = client.post('/auth', json={
        "credential": "user_H",
        "pwd": "senha8"
    })

    assert response.json() == {
        "message": "Usuário não cadastrado.",
        "error": True,
        "data": []
    }
