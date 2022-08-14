def test_zdelete_user(client):
    user_id = "string"
    response = client.delete(f"/user/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Dados deletados com sucesso",
        "error": None,
        "data": None,
    }
