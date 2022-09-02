def test_zdelete_user(client):
    response = client.delete("/user/user_A")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Dados deletados com sucesso",
        "error": None,
        "data": None,
    }
