import pytest


@pytest.mark.api
def test_openapi_contains_required_paths(api_client):
    response = api_client.get("/openapi.json")

    assert response.status_code == 200

    paths = response.json()["paths"]

    assert "/health" in paths
    assert "/generate" in paths
    assert "/model/check" in paths


@pytest.mark.api
def test_openapi_health_path_has_get_method(api_client):
    response = api_client.get("/openapi.json")

    paths = response.json()["paths"]

    assert "get" in paths["/health"]


@pytest.mark.api
def test_openapi_generate_path_has_post_method(api_client):
    response = api_client.get("/openapi.json")

    paths = response.json()["paths"]

    assert "post" in paths["/generate"]