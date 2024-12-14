import pytest
from fastapi.testclient import TestClient
from fast_API.main import app

@pytest.fixture()
def client():
    return TestClient(app)