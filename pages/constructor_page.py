from pages.base_page import BasePage
from locators import constructor_page_locators, base_page_locators
import configuration
import allure


class ConstructorPage(BasePage):

    @allure.step('Кликаем на "Конструктор"')
    def click_to_constructor(self):
        self.go_to_page(configuration.order_list)
        self.click_to_element_with_wait(
            constructor_page_locators.modal_window)
        self.click_to_element(base_page_locators.constructor_button)
        self.wait_presence_of_element(
            constructor_page_locators.make_burger_header)
        return self.find_element(
            constructor_page_locators.make_burger_header)

    @allure.step('Кликаем на "Оформить заказ"')
    def click_to_order_button(self):
        self.click_to_element(constructor_page_locators.place_order_button)

        self.wait_element_is_unvisible(
            constructor_page_locators.id_order)
        self.wait_element_is_unvisible(
            constructor_page_locators.id_order)
        id_order = self.find_element(constructor_page_locators.id_order).text
        return id_order

    @allure.step('Кликаем на ингредиент в конструкторе')
    def click_to_burger_ingredient(self):
        self.click_to_element(constructor_page_locators.burger_ingredient)
        self.wait_presence_of_element(
            constructor_page_locators.ingredient_details)
        self.wait_url_contains('ingredient')
        return self.find_element(
            constructor_page_locators.ingredient_details)

    @allure.step('Кликаем на кнопку закрытия окна с деталями ингредиента')
    def click_close_button_details_ingredient(self):
        details_opened_class_attribute = (self.find_element(
            constructor_page_locators.modal_with_details)).get_attribute('class')
        self.click_to_element(constructor_page_locators.close_details_button)
        details_closed_class_attribute = (self.find_element(
            constructor_page_locators.modal_with_details)).get_attribute('class')
        set1 = set(details_opened_class_attribute.split())
        set2 = {details_closed_class_attribute}
        difference = str(set1.difference(set2)).split('_')
        if 'opened' in difference:
            return True

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_ingredient(self):
        element = self.find_element(constructor_page_locators.count_ingredient)
        count = element.text
        return count

    @allure.step('Добавляем игредиент')
    def put_ingredient(self):
        ingredient = self.find_element(
            constructor_page_locators.burger_ingredient)
        basket = self.find_element(constructor_page_locators.basket)
        self.drag_and_drop_element(ingredient, basket)
