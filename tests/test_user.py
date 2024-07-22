from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestUser:

    def test_create_initial_user(self):
        """Creates a user in DB."""
        payload = {
            "username": "test",
            "password": "test",
            "email": "test@test.com"
        }
        client.post('/user', json=payload)

    def test_create_user_success(self):
        """Creates a user in DB."""
        payload = {
            "username": "test-custom",
            "password": "test-custom",
            "email": "test-custom@test.com"
        }
        response = client.post('/user', json=payload)

        assert response.status_code == 200
        assert response.json().get("username") == "test-custom"

    def test_auth_error(self):
        data = {
            "username": "fail",
            "password": "failedPass"
        }
        response = client.post('/token', data=data)
        access_token = response.json().get("access_token")
        assert access_token is None
        assert response.status_code == 404


    def test_auth_success(self):
        data = {
            "username": "test",
            "password": "test"
        }
        response = client.post('/token', data=data)
        access_token = response.json().get("access_token")
        assert access_token
