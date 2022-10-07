from http import client
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Auroshis!!"}

def test_data_fetch():
    param_dict = {"search":"Wheat"}
    response = client.get("/get_query", params=param_dict)
    assert response.status_code == 200