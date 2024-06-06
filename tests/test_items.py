import os
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import engine, SessionLocal

# Load test environment variables
os.environ["TESTING"] = "True"
os.environ["SQLALCHEMY_DATABASE_URL"] = os.getenv("SQLALCHEMY_DATABASE_URL_TEST")

# Create a test client
client = TestClient(app)


def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[SessionLocal] = override_get_db


def test_create_item():
    response = client.post(
        "/items/", json={"name": "Test Item", "description": "This is a test item"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["description"] == "This is a test item"


def test_read_item():
    response = client.post(
        "/items/", json={"name": "Test Item", "description": "This is a test item"}
    )
    item_id = response.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"


def test_update_item():
    response = client.post(
        "/items/", json={"name": "Test Item", "description": "This is a test item"}
    )
    item_id = response.json()["id"]
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated Item", "description": "This item has been updated"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"


def test_delete_item():
    response = client.post(
        "/items/", json={"name": "Test Item", "description": "This is a test item"}
    )
    item_id = response.json()["id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"
