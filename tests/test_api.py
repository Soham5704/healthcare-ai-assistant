from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Tests if the health endpoint is returning the correct 200 OK status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API is running smoothly."}