from selenium.webdriver.common.by import By

password_recovery_button = [
    By.XPATH, "//a[contains(@href, '/forgot-password')]"]
password_recovery_header = [By.XPATH, ".//h2[text()='Восстановление пароля']"]
login_button = [By.XPATH, ".//button[text()='Войти']"]
logout_button = [By.XPATH, ".//button[text()='Выход']"]
personal_account_button = [By.XPATH, ".//p[text()='Личный Кабинет']"]
recovery_button = [By.XPATH, ".//button[text()='Восстановить']"]
email_field = [By.XPATH, ".//input[@name='name']"]
show_hide_password_button = [By.XPATH, "(.//*[local-name()='svg'])[5]"]
button_save = [By.XPATH, ".//button[text()='Сохранить']"]
password_field_active = [
    By.XPATH, ".//div[contains(text(),'input_status_active')]"]
password_field_color = [By.XPATH, ".//label[text()='Пароль']/parent::div"]
password_field = [By.XPATH, ".//input[@name='Пароль']"]
history_of_orders_button = [By.XPATH, ".//a[text()='История заказов']"]
profile_button = [By.XPATH, ".//a[text()='Профиль']"]
wait_account = [
    By.XPATH, ".//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]"]
