import pytest


@pytest.mark.api
@pytest.mark.negative
def test_generate_without_body_returns_422(api_client):
    response = api_client.post("/generate")

    assert response.status_code == 422


@pytest.mark.api
@pytest.mark.negative
def test_generate_with_empty_body_returns_422(api_client):
    response = api_client.post("/generate", json={})

    assert response.status_code == 422


@pytest.mark.api
@pytest.mark.negative
def test_generate_with_invalid_prompt_type_returns_422(api_client):
    payload = {
        "prompt": 123
    }

    response = api_client.post("/generate", json=payload)

    assert response.status_code == 422


@pytest.mark.api
@pytest.mark.integration
@pytest.mark.skip(reason="Requires available local LLM model")
def test_generate_with_valid_prompt_returns_code(api_client):
    payload = {
        "prompt": "print hello world in Lua"
    }

    response = api_client.post("/generate", json=payload)
    body = response.json()

    assert response.status_code == 200
    assert "code" in body
    assert isinstance(body["code"], str)
    assert len(body["code"]) > 0

@pytest.mark.smoke
@pytest.mark.api
def test_model_check_endpoint_is_available(api_client):
    response = api_client.post("/model/check")

    assert response.status_code != 404    