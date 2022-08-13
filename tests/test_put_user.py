def test_put_user(client):
    user_id = "string"
    response = client.put(
        f"/user/{user_id}",
        json = {
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
    assert response.json() == {
                "message": "Dado atualizado com sucesso",
                "error": None,
                "data": None,
            }
    