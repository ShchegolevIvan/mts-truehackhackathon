import pytest


@pytest.mark.api
def test_get_chat_sessions_returns_200(api_client):
    response = api_client.get("/chat/sessions")

    assert response.status_code == 200


@pytest.mark.api
def test_get_chat_sessions_returns_list(api_client):
    response = api_client.get("/chat/sessions")
    body = response.json()

    assert isinstance(body, list)


@pytest.mark.api
def test_get_unknown_session_runs_returns_empty_list(api_client):
    response = api_client.get("/chat/sessions/unknown-session-id/runs")
    body = response.json()

    assert response.status_code == 200
    assert body == []


@pytest.mark.api
@pytest.mark.negative
def test_get_unknown_session_history_returns_404(api_client):
    response = api_client.get("/chat/sessions/unknown-session-id/history")

    assert response.status_code in (404, 422)

@pytest.mark.api
@pytest.mark.negative
def test_get_unknown_session_returns_404(api_client):
    response = api_client.get("/chat/sessions/unknown-session-id")

    assert response.status_code == 404