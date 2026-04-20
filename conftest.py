from selenium import webdriver
import pytest
import configuration
import data
from api_framework.user_api import UserApi
from api_framework.order_api import OrderApi
import pytest
from helpers import generate_data


@pytest.fixture
def data_for_create_user():
    email = generate_data.generate_email()
    password = generate_data.generate_random_string(10)
    name = generate_data.generate_random_string(10)
    return email, password, name


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        data.driver_name = 'chrome'
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        data.driver_name = 'firefox'
    driver.get(configuration.URL)
    yield driver
    driver.quit()


@pytest.fixture
def user(data_for_create_user):
    user_api = UserApi()
    email, password, name = data_for_create_user
    user = user_api.create_user(email, password, name)
    yield email, password
    user_api.delete_user(user.json()['accessToken'][7:])


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver_with_auth_user(request, user):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.get(configuration.URL)
    email, password = user
    login = UserApi().login_user(email, password)
    token = login.json()['accessToken']
    refresh_token = login.json()['refreshToken']
    driver.execute_script(
        f'window.localStorage.setItem("accessToken", "{token}");')
    driver.execute_script(
        f'window.localStorage.setItem("refreshToken", "{refresh_token}");')
    driver.refresh()
    yield driver, token
    driver.quit()


@pytest.fixture
def order(driver_with_auth_user):
    driver, token = driver_with_auth_user
    token = token[7:]
    order_api = OrderApi()
    ingredients = order_api.get_ingredients()[7]
    order_api.create_order(token, ingredients)
    response = order_api.get_orders(token)
    id_order = response.json()['orders'][0]['number']
    return driver, id_order


@pytest.fixture
def driver_with_auth_user_with_order(order):
    driver, id_order = order
    yield driver, id_order
    driver.quit()


@pytest.fixture
def driver_with_auth_user_and_data_for_order(driver_with_auth_user):
    driver, token = driver_with_auth_user
    order_api = OrderApi()
    token_for_order = token[7:]
    ingredients = order_api.get_ingredients()[7]
    yield {'driver': driver, 'order_api': order_api, 'token_for_order': token_for_order, 'ingredients': ingredients}
    driver.quit()
