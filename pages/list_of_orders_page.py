from pages.base_page import BasePage
from api_framework.order_api import OrderApi
from locators import base_page_locators, list_of_orders_locators
import configuration
import allure


class ListOfOrdersPage(BasePage):

    @allure.step('Кликаем на карточку заказа')
    def click_to_order_card(self):
        self.go_to_page(configuration.order_list)
        self.click_to_element(list_of_orders_locators.order_card)
        self.wait_visibility_of_element(
            list_of_orders_locators.order_details)
        return self.find_element(
            list_of_orders_locators.order_details)

    @allure.step('Кликаем на Ленту заказов')
    def click_to_order_list(self):
        self.click_to_element(base_page_locators.order_list_button)
        self.wait_presence_of_element(
            list_of_orders_locators.order_list_header)
        return self.find_element(
            list_of_orders_locators.order_list_header)

    @allure.step('Ищем заказ в Ленте заказов')
    def find_order_in_list_of_orders(self, id_order):
        self.go_to_page(configuration.order_list)

        id_order_in_list_of_orders = (self.find_element_contain_text(
            list_of_orders_locators.order_card_all, id_order))

        return id_order_in_list_of_orders

    @allure.step('Создаем заказ')
    def post_place_order(self, data):

        response = data['order_api'].create_order(
            data['token_for_order'], data['ingredients'])
        id_order = response.json()['order']['number']
        return id_order

    @allure.step('Получаем значение счетчика заказов за всё время')
    def get_account_orders_all_time(self, id_order):
        self.go_to_page(configuration.order_list)
        account = self.find_element_contain_text(
            list_of_orders_locators.orders_completed_for_all_time, id_order)
        return account

    @allure.step('Получаем значение счетчика заказов за сегодня')
    def get_account_orders_today(self, account_orders_total_today_before):
        self.go_to_page(configuration.order_list)
        account_after_order = account_orders_total_today_before+1
        account = self.find_element_contain_text(
            list_of_orders_locators.orders_completed_for_today, str(account_after_order))
        return account

    @allure.step('Ждем появления заказа в разделе "В работе"')
    def wait_order_in_order_in_progress(self, id):
        return self.find_element_contain_text(list_of_orders_locators.order_in_progress, id)

    @allure.step('Получаем значение счетчика заказов за сегодня')
    def get_account_orders_total_today_api(self):
        return OrderApi().get_account_orders_total_today()
