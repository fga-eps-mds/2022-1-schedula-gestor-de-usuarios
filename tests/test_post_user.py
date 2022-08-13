import json
from datetime import datetime
import string
from fastapi.encoders import jsonable_encoder
from datetime import timedelta

now = datetime.now()+timedelta(hours=3)
round = now.replace(microsecond=0)

def test_post_user(client):

    response = client.post(
        "/user/",
        json = {
            "username": "string",
            "job_role": "string",
            "name": "string",
            "email": "string",
            "password": "string",
            "active": True,
            "acess": "basic"
        },
    )
    assert response.status_code == 201
    da = response.json()
    data = da["data"]
    assert data["username"] == "string"
    print(data)
    
