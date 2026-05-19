import pytest


@pytest.mark.api
def test_existing_run_has_required_fields(api_client):
    sessions_response = api_client.get("/chat/sessions")
    sessions = sessions_response.json()

    if not sessions:
        pytest.skip("No chat sessions found")

    session_id = sessions[0]["session_id"]

    runs_response = api_client.get(f"/chat/sessions/{session_id}/runs")
    runs = runs_response.json()

    if not runs:
        pytest.skip("No runs found")

    run_id = runs[0]["id"]

    response = api_client.get(f"/runs/{run_id}")
    body = response.json()

    assert response.status_code == 200
    assert "id" in body
    assert "status" in body
    assert "created_at" in body
    assert "finished_at" in body
    assert "steps" in body