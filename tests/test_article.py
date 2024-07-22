from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestBlog:

    def _get_access_token(self):
        """Creates a user and returns an auth access token."""
        payload = {
            "username": "test",
            "password": "test",
            "email": "test@test.com"
        }
        response = client.post('/user', json=payload)
        print(response.json())
        data = {
            "username": "test",
            "password": "test"
        }
        response = client.post('/token', data=data)
        access_token = response.json().get("access_token")
        return access_token

    def test_get_all_blogs(self):
        res = client.get("/blog/all")
        assert res.status_code == 200

    def test_post_article(self):
        payload = {
            "title": "Test-XXX",
            "content": "Test Content-XXX",
            "published": True,
            "creator_id": 1
        }
        headers = {
            "Authorization": "Bearer " + self._get_access_token()
        }
        response = client.post('/article/', json=payload, headers=headers)

        assert response.status_code == 200
