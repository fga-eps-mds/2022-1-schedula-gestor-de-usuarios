def test_post_user(client):

    response = client.post(
        "/user",
        json={
            "username": "string",
            "job_role": "string",
            "name": "string",
            "email": "string",
            "password": "string",
            "active": True,
            "acess": "basic",
        },
    )
    assert response.status_code == 201
    da = response.json()
    data = da["data"]
    assert data["username"] == "string"
    assert data["job_role"] == "string"

def test_post_user_used_email(client):
    response = client.post(
        "/user",
        json={
            "username": "user",
            "job_role": "trabalho 2",
            "name": "José Antônio",
            "email": "email1@email.com",
            "password": "senhasegura",
            "active": True,
            "acess": "basic",
        },
    )
    assert response.status_code == 409
    assert response.json()['message'] == "O email já está em uso"