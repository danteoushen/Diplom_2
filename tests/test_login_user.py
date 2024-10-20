import allure
import requests
from data import Urls
from data import Responses
from data import API


class TestLoginUser:
    @allure.title('Проверка авторизации существующего пользователя')
    def test_login_user(self, create_and_delete_user):

        data = create_and_delete_user

        response = requests.post(f'{Urls.URL}{API.CREATE_USER}', json=data)
        assert response.status_code == 200 and response.json()['success']

        response_2 = requests.post(f'{Urls.URL}{API.LOGIN_USER}', json=data)
        assert response_2.status_code == 200 and response.json()['success']


    @allure.title('Проверка авторизации с неверным логином')
    def test_login_user_with_wrong_login(self, create_and_delete_user):

        data = create_and_delete_user.copy()
        data["email"] = 'test@for.example'

        response = requests.post(f'{Urls.URL}{API.LOGIN_USER}', json=data)
        assert response.status_code == 401
        assert response.json()['message'] == Responses.INVALID_DATA

    @allure.title('Проверка авторизации с неверным паролем')
    def test_login_user_with_wrong_password(self, create_and_delete_user):

        data = create_and_delete_user.copy()
        data["password"] = 'пароль_для_примера'

        response = requests.post(f'{Urls.URL}{API.LOGIN_USER}', json=data)
        assert response.status_code == 401
        assert response.json()['message'] == Responses.INVALID_DATA

