import pytest


MAX_RESPONSE_TIME_SECONDS = 1.0


@pytest.mark.smoke
@pytest.mark.api
def test_health_response_time(api_client):
    response = api_client.get("/health")

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME_SECONDS


@pytest.mark.smoke
@pytest.mark.api
def test_openapi_response_time(api_client):
    response = api_client.get("/openapi.json")

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME_SECONDS


@pytest.mark.smoke
@pytest.mark.api
def test_chat_sessions_response_time(api_client):
    response = api_client.get("/chat/sessions")

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME_SECONDS