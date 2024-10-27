from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recognize_gesture():
    with open("tests/sample_image.png", "rb") as file:
        response = client.post("/api/v1/gestures/recognize", files={"file": file})
    assert response.status_code == 200
    assert response.json()["gesture"] in ["saludo", "gracias", "No reconocido"]
