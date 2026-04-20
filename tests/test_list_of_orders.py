import allure
import configuration
from pages.list_of_orders_page import ListOfOrdersPage


class TestListOfOrders:

    @allure.title('При клике на заказ открывается всплывающее окно с деталями')
    def test_click_to_order(self, driver):
        order = ListOfOrdersPage(driver)
        order_details = order.click_to_order_card()

        assert order_details.is_displayed()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_on_history_of_orders_and_list_of_orders(self, driver_with_auth_user_with_order):
        driver, id_order = driver_with_auth_user_with_order
        order = ListOfOrdersPage(driver)
        order_in_list_of_orders = order.find_order_in_list_of_orders(
            str(id_order))

        assert order_in_list_of_orders is True

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_accounter_orders_for_all_time(self, driver_with_auth_user_and_data_for_order):
        driver = driver_with_auth_user_and_data_for_order
        order = ListOfOrdersPage(driver['driver'])
        id_order = str(order.post_place_order(driver))
        account_orders_total = order.get_account_orders_all_time(id_order)

        assert account_orders_total == True

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_accounter_orders_for_today(self, driver_with_auth_user_and_data_for_order):
        driver = driver_with_auth_user_and_data_for_order
        order = ListOfOrdersPage(driver['driver'])
        account_orders_total_today_before = int(
            order.get_account_orders_total_today_api())
        order.post_place_order(driver)
        account_orders_total_today = order.get_account_orders_today(
            account_orders_total_today_before)

        assert account_orders_total_today == True

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_order_in_progress(self, driver_with_auth_user_and_data_for_order):
        driver = driver_with_auth_user_and_data_for_order
        order = ListOfOrdersPage(driver['driver'])
        order.go_to_page(configuration.order_list)
        id_order = str(order.post_place_order(driver))
        order_in_order_in_progress = order.wait_order_in_order_in_progress(
            id_order)

        assert order_in_order_in_progress == True
