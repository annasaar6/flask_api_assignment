import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        yield client


def test_hello_default(client):
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, World!"


def test_hello_with_name(client):
    response = client.get("/hello?name=Alice")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, Alice!"


def test_sum_success(client):
    response = client.post("/sum", json={"numbers": [1, 2, 3]})

    data = response.get_json()

    assert response.status_code == 200
    assert data["sum"] == 6


def test_sum_missing_field(client):
    response = client.post("/sum", json={})

    assert response.status_code == 400


def test_sum_not_list(client):
    response = client.post("/sum", json={"numbers": 123})

    assert response.status_code == 400


def test_sum_invalid_values(client):
    response = client.post("/sum", json={"numbers": [1, "two", 3]})

    assert response.status_code == 400
