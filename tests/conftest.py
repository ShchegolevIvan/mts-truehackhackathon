import pytest
import requests


BASE_URL = "http://localhost:8000"


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, json=None):
        return self.session.post(f"{self.base_url}{endpoint}", json=json)


@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)