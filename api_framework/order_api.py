from api_framework.base_api import BaseApi
import configuration
import allure


class OrderApi(BaseApi):

    @allure.step('Получаем информацию об ингредиентах')
    def get_ingredients(self):
        response = self.get_request(
            configuration.GET_INGREDIENTS)
        id_ingredients = []
        for n in response.json()['data']:
            id_ingredients.append(n['_id'])
        return id_ingredients

    @allure.step('Создаем заказ')
    def create_order(self, token, *ingredients):
        headers = {'Authorization': 'Bearer ' + token}
        payload = {"ingredients": [ingredients]}
        response = self.post_request(
            configuration.CREATE_ORDER, data=payload, headers=headers)
        return response

    @allure.step('Создаем заказ без авторизации')
    def create_order_no_authorization(self, *ingredients):
        payload = {"ingredients": [ingredients]}
        response = self.post_request(
            configuration.CREATE_ORDER, data=payload)
        return response

    @allure.step('Получаем заказы конкретного пользователя')
    def get_orders(self, token):
        headers = {'Authorization': 'Bearer ' + token}
        response = self.get_request(
            configuration.GET_ORDERS, headers=headers)
        return response

    @allure.step('Получаем общее число заказов')
    def get_account_orders_total(self):
        response = self.get_request(
            configuration.GET_ORDERS_ALL)
        total = response.json()['total']
        return total

    @allure.step('Получаем число заказов за сегодня')
    def get_account_orders_total_today(self):
        response = self.get_request(
            configuration.GET_ORDERS_ALL)
        totalToday = response.json()['totalToday']
        return totalToday
