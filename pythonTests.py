from urllib import response
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200


def test_hello_world_json():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200


def test_list_size():
    response = client.get("/products")
    assert len(response.json()) == 3
