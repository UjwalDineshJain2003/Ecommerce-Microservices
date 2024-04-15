import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == "Hello world"

def test_check(client):
    response = client.get('/check')
    assert response.status_code == 200
    assert response.json in [0, 1]  # Ensure response is either 0 or 1
