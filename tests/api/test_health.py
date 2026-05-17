import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_health_status_code(api_client):
    response = api_client.get("/health")

    assert response.status_code == 200


@pytest.mark.smoke
@pytest.mark.api
def test_health_response_body(api_client):
    response = api_client.get("/health")

    assert response.json() == {"status": "ok"}


@pytest.mark.smoke
@pytest.mark.api
def test_unknown_endpoint_returns_404(api_client):
    response = api_client.get("/unknown-endpoint")

    assert response.status_code == 404