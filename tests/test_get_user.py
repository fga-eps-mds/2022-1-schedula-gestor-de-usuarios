from fastapi.testclient import TestClient


def test_get_user(client: TestClient):
    response = client.get("/user?username=user_A")
    assert response.status_code == 200
    assert response.json()["message"] == "dados buscados com sucesso"
    assert response.json()["data"]["name"] == "Nome A"
    assert response.json()["data"]["email"] == "email1@email.com"


def test_get_all_users(client: TestClient):
    response = client.get('/user')
    assert response.status_code == 200
    assert len(response.json()['data']) == 8
