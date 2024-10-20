import allure
import requests
from data import Urls
from data import Responses
from data import API


class TestCreateUser:

    @allure.title('Проверка создания нового пользователя')
    def test_create_new_user(self, create_and_delete_user):

        data = create_and_delete_user

        response = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка создания уже зарегистрированного пользователя')
    def test_create_exist_user(self, create_and_delete_user):

        data = create_and_delete_user

        response = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data)
        assert response.status_code == 200

        response_2 = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data)
        assert response_2.status_code == 403
        assert response_2.json()['message'] == Responses.USER_EXIST

    @allure.title('Проверка создания пользователя без обязательного параметра')
    def test_login_user_without_name(self, create_and_delete_user):

        data = create_and_delete_user
        data_without_name = {"email": data["email"], "password": data["password"]}
        
        response = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data_without_name)
        assert response.status_code == 403
        assert response.json()['message'] == Responses.REQUIRED_FIELD

