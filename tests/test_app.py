import pytest
from app import app

@pytest.fixture
def client():
    # Set up a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_home(client):
    # Simulate a GET request to the home ('/') route
    response = client.get('/')
    
    # Verify the status code is 200 (OK)
    assert response.status_code == 200
    
    # Verify the content returned is 'Hello, World!'
    assert response.data == b"Hello, World!"
