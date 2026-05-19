import pytest
import allure


@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
def test_get_chat_sessions_returns_200(api_client):
    response = api_client.get("/chat/sessions")

    assert response.status_code == 200


@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
def test_get_chat_sessions_returns_list(api_client):
    response = api_client.get("/chat/sessions")
    body = response.json()

    assert isinstance(body, list)

@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
def test_get_unknown_session_runs_returns_empty_list(api_client):
    response = api_client.get("/chat/sessions/unknown-session-id/runs")
    body = response.json()

    assert response.status_code == 200
    assert body == []


@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
@pytest.mark.negative
def test_get_unknown_session_history_returns_404(api_client):
    response = api_client.get("/chat/sessions/unknown-session-id/history")

    assert response.status_code in (404, 422)

@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
@pytest.mark.negative
def test_get_unknown_session_returns_404(api_client):
    response = api_client.get("/chat/sessions/unknown-session-id")

    assert response.status_code == 404

@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
def test_chat_session_item_has_required_fields(api_client):
    response = api_client.get("/chat/sessions")
    body = response.json()

    assert response.status_code == 200

    if not body:
        pytest.skip("No chat sessions found")

    session = body[0]

    assert "id" in session
    assert "session_id" in session
    assert "title" in session
    assert "created_at" in session
    assert "updated_at" in session


@allure.feature("Chat Sessions")
@allure.story("Get chat sessions")
@pytest.mark.api
def test_chat_session_field_types(api_client):
    response = api_client.get("/chat/sessions")
    body = response.json()

    assert response.status_code == 200

    if not body:
        pytest.skip("No chat sessions found")

    session = body[0]

    assert isinstance(session["id"], int)
    assert isinstance(session["session_id"], str)
    assert isinstance(session["title"], str)
    assert isinstance(session["created_at"], str)
    assert isinstance(session["updated_at"], str)