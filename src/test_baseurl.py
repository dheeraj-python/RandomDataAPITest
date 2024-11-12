import pytest
import allure
import requests


@allure.title("Verifying the status code")
@allure.description("Verifying that while hitting base Url status code should be 200 OK")
def test_baseurl():
    base_url = "https://random-data-api.com/api/v2/"
    response = requests.get(base_url)
    assert response.status_code == 200
