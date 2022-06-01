from fastapi.testclient import TestClient

from main_mask import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "All right, there is a connection."}
