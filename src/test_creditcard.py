import datetime

import pytest
import allure
import requests


@allure.title("Verifying the status code")
@allure.description("Verifying that while hitting base Url + Credit_cards endpoint where status code should be 200 OK")
def test_creditcard_status():
    credit_card_url = "https://random-data-api.com/api/v2/credit_cards"
    response = requests.get(credit_card_url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict), "Response should be a dictionary data type"
    print(data)
    #validate that fields [id, credit_card_Number, credit_card_type,uid,credit_card_expiry_date] are present into the response or not

    expected_data = ['id', 'uid', 'credit_card_number', 'credit_card_type', 'credit_card_expiry_date']
    for field in expected_data:
        assert field in data, f"Field '{field} is missing in the response body"
        print(field)

    assert isinstance(data['credit_card_number'], str), "Credit card number should be a string"
    assert isinstance(data['uid'], str), "Uid should be in string"
    assert isinstance(data['id'], int), "Id should be in integer"
    assert isinstance(data['credit_card_type'], str), "Credit Card Type should be in string"
    assert isinstance(data['credit_card_expiry_date'], str), "Credit Card Expiry Date should be in string"

    #Validate Headers like - COntent-Type = application/json or content length should be present
    headers = response.headers
    assert headers[
               'Content-Type'] == 'application/json; charset=utf-8', f"Expected Content-Type 'application/json; charset=utf-8',got {headers['Content-Type']}"
    assert 'Content-Length' in headers, "Content-Length header is missing"

    #Validate Cookies are present or not
    cookies = response.cookies
    assert cookies != True
    print(cookies)
