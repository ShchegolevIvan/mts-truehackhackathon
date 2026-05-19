import pytest
import allure


@allure.feature("API Availability")
@allure.story("OpenAPI schema")
@pytest.mark.smoke
@pytest.mark.api
def test_openapi_schema_is_available(api_client):
    response = api_client.get("/openapi.json")

    assert response.status_code == 200
    assert "openapi" in response.json()
    assert "paths" in response.json()


@allure.feature("API Availability")
@allure.story("Swagger docs")
@pytest.mark.smoke
@pytest.mark.api
def test_swagger_docs_are_available(api_client):
    response = api_client.get("/docs")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


@allure.feature("API Availability")
@allure.story("Root endpoint")
@pytest.mark.api
@pytest.mark.negative
def test_root_endpoint_returns_404(api_client):
    response = api_client.get("/")

    assert response.status_code == 404