import allure
import requests
from data import Urls
from data import API
from data import Responses

class TestUpdateUserData:
    @allure.title('Проверка изменения данных с авторизацией')
    def test_login_user_change_name(self, token):

        user_token = token
        new_name = 'Test_name'
        data = {"name": new_name}

        response = requests.patch(f'{Urls.URL}{API.DELETE_USER}', headers={'Authorization': user_token}, json=data)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Проверка изменения данных без авторизации')
    def test_not_authorized_error(self, create_and_delete_user):

        data = create_and_delete_user
        
        response = requests.patch(f'{Urls.URL}{API.DELETE_USER}', json=data)
        assert response.status_code == 401
        assert Responses.NOT_AUTHORIZED in response.text

