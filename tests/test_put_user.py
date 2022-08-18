def test_put_user(client):
    user_id = "string"
    response = client.put(
        f"/user/{user_id}",
        json={
            "username": "string",
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
