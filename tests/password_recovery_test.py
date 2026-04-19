import allure
import configuration
from pages.login_page import LoginPage
import data


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()

        assert login_page.get_current_url() == configuration.URL + \
            configuration.recovery_password

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_button_recovery(self, driver):
        login_page = LoginPage(driver)
        login_page.input_email_for_reset_password(data.email)
        login_page.click_to_recovery_button()

        assert login_page.get_current_url() == configuration.URL + \
            configuration.reset_password

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_show_hide_password_button(self, driver):
        login_page = LoginPage(driver)
        color, type_password = login_page.click_show_hide_password_button()

        assert color == data.password_field_highlight and type_password == data.password_visible_type_attribute
