def test_put_user(client):
    user_id = "string"
    response = client.put(
        f"/user/{user_id}",
        json={
            "job_role": "string",
            "name": "string",
            "email": "string@email.com",
            "password": "string",
            "active": True,
            "acess": "basic"
        },
    )
    assert response.status_code == 200
    da = response.json()
    data = da["data"]
    assert da["message"] == "Dado atualizado com sucesso"
    assert data["email"] == "string@email.com"
    assert data["job_role"] == "string"
    assert data["name"] == "string"
    assert data["acess"] == "basic"


def test_put_userfail(client):
    user_id = "nao tem"
    response = client.put(
        f"/user/{user_id}",
        json={
            "job_role": "string",
            "name": "string",
            "email": "string@email.com",
            "password": "string",
            "active": True,
            "acess": "basic"
        },
    )

    assert response.status_code == 404
    assert response.json() == {
        "message": "Dado não encontrado na base",
        "error": None,
        "data": None,
    }


def test_put_user_unico(client):
    user_id = "User K"
    response = client.put(
        f"/user/{user_id}",
        json={
            "job_role": "estagiario",
            "name": "stng",
            "email": "stg@email.com"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Dado atualizado com sucesso"
    assert data["data"]["email"] == "stg@email.com"
    assert data["data"]["job_role"] == "estagiario"
    assert data["data"]["name"] == "stng"
