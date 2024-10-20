import allure
import requests
from data import Urls
from data import API
from data import Ingredients
from data import Responses

class TestCreateOrder:
    @allure.title('Проверка создания заказа с авторизацией и с ингредиентами')
    def test_create_order_with_auth_and_ingredients(self, token):

        user_token = token
        data = Ingredients.VALID_INGREDIENTS

        response = requests.post(f'{Urls.URL}{API.ORDER}', headers={'Authorization': user_token}, json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка создания заказа без авторизации и с ингредиентами')
    def test_create_order_with_ingredients_user_no_auth(self):

        data = Ingredients.VALID_INGREDIENTS

        response = requests.post(f'{Urls.URL}{API.ORDER}', json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):

        data = Ingredients.WITHOUT_INGREDIENTS

        response = requests.post(f'{Urls.URL}{API.ORDER}', json=data)
        assert response.status_code == 400
        assert response.json()['message'] == Responses.EMPTY_ORDER


    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash(self):

        data = Ingredients.INVALID_INGREDIENTS

        response = requests.post(f'{Urls.URL}{API.ORDER}', json=data)
        assert response.status_code == 500
        assert Responses.SERVER_ERROR in response.text


class TestGetOrder:
    @allure.title('Проверка получаения заказа авторизованного пользователя')
    def test_get_order_auth_user(self, token):

        user_token = token

        response = requests.get(f'{Urls.URL}{API.ORDER}', headers={'Authorization': user_token})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка получаения заказа неавторизованного пользователя')
    def test_get_order_no_auth_user(self):

        response = requests.get(f'{Urls.URL}{API.ORDER}')
        assert response.status_code == 401
        assert Responses.NOT_AUTHORIZED in response.text

