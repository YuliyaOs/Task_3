from api_framework.base_api import BaseApi
import configuration
import allure


class UserApi(BaseApi):

    @allure.step('Создаем пользователя')
    def create_user(self, email, password, name):
        payload = {"email": email,
                   "password": password,
                   "name": name}
        response = self.post_request(
            configuration.CREATE_USER, data=payload)
        return response

    @allure.step('Авторизуем пользователя')
    def login_user(self, email, password):
        payload = {"email": email,
                   "password": password}
        response = self.post_request(
            configuration.LOGIN_USER, data=payload)
        return response

    @allure.step('Удаляем пользователя')
    def delete_user(self, token):
        headers = {'Authorization': 'Bearer ' + token}
        response = self.delete_request(
            configuration.DELETE_USER, headers=headers)
        return response

    @allure.step('Обновляем информацию о пользователе')
    def patch_user(self, token, email=None, password=None, name=None):
        headers = {'Authorization': 'Bearer ' + token}
        payload = {}
        for n in (email, password, name):
            if n != None:
                payload['"'+n+'"'] = n
        response = self.patch_request(
            configuration.PATCH_USER, data=payload, headers=headers)
        return response
