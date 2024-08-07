
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# tests/test_tasks.py
def test_create_task():
    response = client.post("/tasks", json={"title": "Test Task", "description": "Test Description", "priority": 1})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
