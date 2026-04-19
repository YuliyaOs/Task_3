import allure
import configuration
from pages.constructor_page import ConstructorPage
from pages.list_of_orders_page import ListOfOrdersPage
import data


class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor = constructor_page.click_to_constructor()

        assert constructor_page.get_current_url(
        ) == configuration.URL and constructor.is_displayed()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_list(self, driver):
        order_page = ListOfOrdersPage(driver)
        orders = order_page.click_to_order_list()

        assert order_page.get_current_url() == configuration.URL + \
            configuration.order_list and orders.is_displayed()

    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_click_to_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        details = constructor_page.click_to_burger_ingredient()

        assert details.is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_with_details_of_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_to_burger_ingredient()
        close = constructor_page.click_close_button_details_ingredient()

        assert close == True

    @allure.title('При добавлении ингредиента в заказ увеличивается каунтер данного ингредиента')
    def test_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.put_ingredient()
        count = constructor_page.get_count_ingredient()

        assert count == data.count_bun

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_place_order(self, driver_with_auth_user):
        driver = driver_with_auth_user
        constructor_page = ConstructorPage(driver[0])
        constructor_page.put_ingredient()
        id_order = constructor_page.click_to_order_button()

        assert id_order != data.id_order_default and id_order.isnumeric
