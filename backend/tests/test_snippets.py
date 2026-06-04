from fastapi.testclient import TestClient
from app.main import app
import uuid

# Initialize the simulated browser
client = TestClient(app)

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_snippet_invalid_payload_422():
    # Missing 'language' and 'code'
    payload = {
        "title": "Broken Snippet",
        "user_id": str(uuid.uuid4())
    }
    response = client.post("/snippets/", json=payload)
    
    # Assert that Pydantic caught the error
    assert response.status_code == 422

def test_get_snippet_not_found_404():
    # Generate a random UUID that definitely doesn't exist in Neon
    fake_id = str(uuid.uuid4())
    response = client.get(f"/snippets/{fake_id}")
    
    # Assert our 404 logic triggers
    assert response.status_code == 404