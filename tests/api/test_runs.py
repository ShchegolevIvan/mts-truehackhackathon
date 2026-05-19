import pytest


@pytest.mark.api
@pytest.mark.negative
def test_get_nonexistent_run_returns_404(api_client):
    response = api_client.get("/runs/999999")

    assert response.status_code == 404


@pytest.mark.api
@pytest.mark.negative
def test_get_run_with_invalid_id_returns_422(api_client):
    response = api_client.get("/runs/invalid-id")

    assert response.status_code == 422