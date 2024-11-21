from fastapi.testclient import TestClient
from fast_API.main import app


def test_read_root():
    client = TestClient(app)

    response = client.get('/')


