from fastapi.testclient import TestClient


def test_get_user(client: TestClient):
    response = client.get("/user?username=user_A")
    assert response.status_code == 200
    assert response.json() == {
        "message": "dados buscados com sucesso",
        "error": None,
        "data":
            {
                "username": "user_A",
                "job_role": "Trabalho 1",
                "name": "Nome A",
                "email": "email1@email.com",
                "password": "$2b$12$lwmIAGrr/7SNAyRWEpA1Nu.N5qx4QUMUN8pKocYv8iP5TahRwRkk2",  # noqa 501
                "active": True,
                "updated_at": "2020-01-01T00:00:00",
                "acess": "admin",
            }}


def test_get_all_users(client: TestClient):
    response = client.get('/user')
    assert response.status_code == 200
    assert len(response.json()['data']) == 8
