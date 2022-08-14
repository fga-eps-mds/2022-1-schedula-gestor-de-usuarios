def test_post_user(client):

    response = client.post(
        "/user/",
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
