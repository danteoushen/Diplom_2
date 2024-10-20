import pytest
import requests
import helpers
from data import Urls
from data import API



@pytest.fixture(scope="function")
def create_and_delete_user(token):
    user_data = helpers.generate_user()

    yield user_data

    data = {
        "email": user_data["email"],
        "password": user_data["password"],
    }
    response = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data)
    token = response.json().get("accessToken")

    if token:
        requests.delete(f'{Urls.URL}{API.DELETE_USER}', headers={'Authorization': token})


@pytest.fixture
def token():

    data = helpers.generate_user()
    response = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data)
    token = response.json().get("accessToken")

    yield token
    requests.delete(f'{Urls.URL}{API.DELETE_USER}', headers={'Authorization': token})

