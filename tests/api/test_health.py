import allure
import pytest


@allure.feature("Health API")
@allure.story("Service health")
@pytest.mark.smoke
@pytest.mark.api
def test_health_status_code(api_client):
    response = api_client.get("/health")

    assert response.status_code == 200


@allure.feature("Health API")
@allure.story("Service health")
@pytest.mark.smoke
@pytest.mark.api
def test_health_response_body(api_client):
    response = api_client.get("/health")

    assert response.json() == {"status": "ok"}


@allure.feature("Health API")
@allure.story("Error handling")
@pytest.mark.smoke
@pytest.mark.api
def test_unknown_endpoint_returns_404(api_client):
    response = api_client.get("/unknown-endpoint")

    assert response.status_code == 404