import allure
import configuration
from pages.login_page import LoginPage


class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account()

        assert login_page.get_current_url() == configuration.URL + \
            configuration.login_page

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_history_of_orders(self, driver_with_auth_user):
        login_page = LoginPage(driver_with_auth_user[0])
        login_page.click_orders_history_button()

        assert login_page.get_current_url() == configuration.URL + \
            configuration.order_history

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver_with_auth_user):
        login_page = LoginPage(driver_with_auth_user[0])
        login_page.logout()

        assert login_page.get_current_url() == configuration.URL + \
            configuration.login_page
