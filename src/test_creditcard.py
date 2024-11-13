

import pytest
import allure
import requests


@allure.title("Verifying the status code")
@allure.description("Verifying the status code")
def test_creditcard_status():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    response.raise_for_status()
    assert response.status_code == 200
    print(response.status_code)


@allure.title("Verifying the response data should be in dictionary type")
def test_creditcard_dict():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    response.raise_for_status()
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        pytest.fail("Response content is not valid JSON")
    assert isinstance(data, dict), "Response should be a dictionary data type"
    print(data)


@allure.title("Verifying JSON fields are present in the response body")
def test_creditcard_json_fields():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    response.raise_for_status()
    data = response.json()
    expected_data = ['id', 'uid', 'credit_card_number', 'credit_card_type', 'credit_card_expiry_date']
    for field in expected_data:
        assert field in data, f"Field '{field} is missing in the response body"
        print(field)


@allure.title("Verifying JSON fields data type")
def test_creditcard_json_fields_data_type():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    response.raise_for_status()
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        pytest.fail("Response content is not valid JSON")
    assert isinstance(data['credit_card_number'], str), "Credit card number should be a string"
    assert isinstance(data['uid'], str), "Uid should be in string"
    assert isinstance(data['id'], int), "Id should be in integer"
    assert isinstance(data['credit_card_type'], str), "Credit Card Type should be in string"
    assert isinstance(data['credit_card_expiry_date'], str), "Credit Card Expiry Date should be in string"


@allure.title("Verifying Headers like - Content-Type & Content Length")
def test_creditcard_headers():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    response.raise_for_status()
    headers = response.headers
    expected_content_type = 'application/json; charset=utf-8'
    actual_content_type = headers.get('Content-Type', '')
    assert actual_content_type == expected_content_type, f"Expected Content-Type '{expected_content_type}', got '{actual_content_type}'"
    assert 'Content-Length' in headers, "Content-Length header is missing"

    print(response.headers)


@allure.title("Verifying Cookies are present or not")
def test_creditcard_cookies():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    response.raise_for_status()
    cookies = response.cookies
    assert cookies != True
    print(cookies)
