from datetime import datetime
from datetime import timedelta

now = datetime.now()+timedelta(hours=3)
round = now.replace(microsecond=0)

def test_get_user(client):
    response = client.get("/user/")
    assert response.status_code == 201
    assert response.json() == {
        "message": "dados buscados com sucesso",
        "error": None,
        "data": [
            {"username":'User A', "job_role": 'Trabalho 1', "name": 'Nome A', "email": 'email 1', "password": 'senha1', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User B', "job_role": 'Trabalho 2', "name": 'Nome A', "email": 'email 2', "password": 'senha2', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User C', "job_role": 'Trabalho 3', "name": 'Nome A', "email": 'email 3', "password": 'senha3', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User D', "job_role": 'Trabalho 4', "name": 'Nome A', "email": 'email 4', "password": 'senha4', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User E', "job_role": 'Trabalho 5', "name": 'Nome A', "email": 'email 5', "password": 'senha5', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User F', "job_role": 'Trabalho 6', "name": 'Nome A', "email": 'email 6', "password": 'senha6', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User G', "job_role": 'Trabalho 7', "name": 'Nome A', "email": 'email 7', "password": 'senha7', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User H', "job_role": 'Trabalho 8', "name": 'Nome A', "email": 'email 8', "password": 'senha8', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User I', "job_role": 'Trabalho 9', "name": 'Nome A', "email": 'email 9', "password": 'senha9', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
            {"username":'User J', "job_role": 'Trabalho 10', "name": 'Nome A', "email": 'email 10', "password": 'senha10', "active": True, "updated_at": str(datetime.isoformat(round)), "acess": 'basic'},
        ]
    }