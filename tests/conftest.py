import os

import pytest
import requests


BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
REQUEST_TIMEOUT = 10


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )

    def post(self, endpoint, json=None, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=json,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )


@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)