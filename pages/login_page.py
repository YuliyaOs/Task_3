from pages.base_page import BasePage
from locators import login_page_locators, base_page_locators
from selenium.webdriver.common.keys import Keys
import configuration
import allure


class LoginPage(BasePage):

    @allure.step('Авторизуемся')
    def login(self, email, password):
        self.click_personal_account()
        self.enter_data_in_field(login_page_locators.email_field, email)
        self.enter_data_in_field(
            login_page_locators.email_field, Keys.ENTER)
        self.enter_data_in_field(login_page_locators.password_field, password)
        self.enter_data_in_field(
            login_page_locators.password_field, Keys.ENTER)
        self.wait_presence_of_element(
            base_page_locators.place_order_button)
        return self.find_element(base_page_locators.place_order_button)

    @allure.step('Выходим из аккаунта')
    def logout(self):
        self.click_to_element(login_page_locators.personal_account_button)
        self.click_to_element_with_wait(login_page_locators.logout_button)
        self.wait_url_contains('login')

    @allure.step('Кликаем по ссылке восстановления пароля')
    def click_password_recovery_button(self):
        self.wait_element_to_clickable(
            login_page_locators.personal_account_button)
        self.click_to_element(login_page_locators.personal_account_button)
        self.wait_element_to_clickable(
            login_page_locators.login_button)
        self.scroll_to_element(login_page_locators.password_recovery_button)
        self.click_to_element(
            login_page_locators.password_recovery_button)
        self.wait_visibility_of_element(
            login_page_locators.password_recovery_header)

    @allure.step('Вводим почту для восстановления пароля')
    def input_email_for_reset_password(self, email):
        self.go_to_page(configuration.forgot_password)
        self.enter_data_in_field(login_page_locators.email_field, email)

    @allure.step('Кликаем по кнопке для восстановления пароля')
    def click_to_recovery_button(self):
        self.wait_element_to_clickable(login_page_locators.recovery_button)
        self.click_to_element_with_wait(
            login_page_locators.recovery_button)
        self.wait_url_contains(configuration.reset_password)

    @allure.step('Кликаем по кнопке показать/скрыть пароль')
    def click_show_hide_password_button(self):
        self.go_to_login_page()
        self.click_to_element_with_wait(
            login_page_locators.show_hide_password_button)
        element = self.find_element(login_page_locators.password_field_color)
        self.wait_to_change_color(element)
        color = element.value_of_css_property('border')
        password = self.find_element(login_page_locators.password_field)
        type_password = password.get_attribute('type')

        return color, type_password

    @allure.step('Кликаем на историю заказов')
    def click_orders_history_button(self):
        self.click_to_element(login_page_locators.personal_account_button)
        self.wait_visibility_of_element(login_page_locators.wait_account)
        self.wait_element_to_clickable(
            login_page_locators.history_of_orders_button)
        self.click_to_element_with_wait(
            login_page_locators.history_of_orders_button)
        self.wait_url_contains(configuration.order_history)
