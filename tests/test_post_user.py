from xmlrpc.client import boolean

user = {
    'username': 'teste',
    'job_role': 'trabalho 1',
    'name': 'fulano',
    'email': 'dsahu@email.com',
    'password': 'ssjaidas',
    'active': True,
    'acess': 'basic'
}


def test_post_user(client):

    response = client.post(
        "/user",
        json=user,
    )
    assert response.status_code == 201
    da = response.json()
    data = da["data"]
    assert data["username"] == "teste"
    assert data["job_role"] == "trabalho 1"


def test_post_user_used_email(client):
    user['username'] = 'teste255'
    user['email'] = 'email1@email.com'
    response = client.post(
        "/user",
        json=user,
    )
    assert response.status_code == 409
    assert response.json()['message'] == "O email já está em uso"
