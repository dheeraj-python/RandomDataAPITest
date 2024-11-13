import datetime

import pytest
import allure
import requests


@allure.title("Verifying the beer endpoints")
@allure.description("Verifying the status code")
def test_beer_status():
    beer_url = "https://random-data-api.com/api/v2/beers"
    response = requests.get(beer_url)
    response.raise_for_status()
    assert response.status_code == 200
    print(response.status_code)


@allure.title("Verifying the response data should be in dictionary type")
def test_beer_dict():
    beer_url = "https://random-data-api.com/api/v2/beers"
    response = requests.get(beer_url)
    response.raise_for_status()
    data = response.json()
    assert isinstance(data, dict), "Response should be a dictionary data type"
    print(data)


@allure.title("Verifying JSON fields are present in the response body")
def test_beer_json_fields():
    beer_url = "https://random-data-api.com/api/v2/beers"
    response = requests.get(beer_url)
    response.raise_for_status()
    data = response.json()
    expected_data = ['id', 'uid', 'brand', 'name', 'style', 'hop', 'yeast', 'malts', 'ibu', 'alcohol', 'blg']
    for field in expected_data:
        assert field in data, f"Field '{field} is missing in the response body"
        print(field)


@allure.title("Verifying JSON fields data type")
def test_beer_json_fields_data_type():
    beer_url = "https://random-data-api.com/api/v2/beers"
    response = requests.get(beer_url)
    response.raise_for_status()
    data = response.json()
    assert isinstance(data['brand'], str), "Brand Name should be a string"
    assert isinstance(data['uid'], str), "Uid should be in string"
    assert isinstance(data['id'], int), "Id should be in integer"
    assert isinstance(data['name'], str), "Name should be in string"
    assert isinstance(data['style'], str), "Style should be in string"
    assert isinstance(data['hop'], str), "Hop should be in string"
    assert isinstance(data['yeast'], str), "Yeast should be in string"
    assert isinstance(data['malts'], str), "Malts should be in string"
    assert isinstance(data['ibu'], str), "ibu should be in string"
    assert isinstance(data['style'], str), "Style should be in string"
    assert isinstance(data['alcohol'], str), "Alcohol should be in string"
    assert isinstance(data['blg'], str), "Blg should be in string"


@allure.title("Verifying Headers like - Content-Type & Content Length")
def test_beer_headers():
    beer_url = "https://random-data-api.com/api/v2/beers"
    response = requests.get(beer_url)
    response.raise_for_status()
    headers = response.headers
    expected_content_type = 'application/json; charset=utf-8'
    actual_content_type = headers.get('Content-Type', '')
    assert actual_content_type == expected_content_type, f"Expected Content-Type '{expected_content_type}', got '{actual_content_type}'"
    assert 'Content-Length' in headers, "Content-Length header is missing"
    print(response.headers)


@allure.title("Verifying Cookies are present or not")
def test_beer_headers():
    beer_url = "https://random-data-api.com/api/v2/beers"
    response = requests.get(beer_url)
    response.raise_for_status()
    cookies = response.cookies
    assert cookies != True
    print(cookies)
