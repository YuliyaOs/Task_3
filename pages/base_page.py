from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import login_page_locators
import configuration
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    def find_element_contain_text(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.text_to_be_present_in_element(locator, text))

    def enter_data_in_field(self, locator, data):
        self.find_element(locator).send_keys(data)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_element_to_clickable(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_to_change_color(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            lambda d: "rgb(76, 76, 255)" in element.value_of_css_property("border"))

    def wait_element_is_unvisible(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until_not(
                expected_conditions.text_to_be_present_in_element(locator, '9999'))

        except TimeoutError:
            pass

    def wait_url_contains(self, fragment_url, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.url_contains(fragment_url))

    def wait_staleness_of(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.staleness_of(element))

    def wait_visibility_of_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_unvisibility_of_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until_not(
            expected_conditions.visibility_of_element_located(locator))

    def wait_presence_of_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator))

    def click_to_element(self, locator):
        self.find_element(locator).click()

    def click_to_element_with_wait(self, locator):
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_personal_account(self):
        self.wait_element_to_clickable(
            login_page_locators.personal_account_button)
        self.click_to_element(login_page_locators.personal_account_button)
        self.wait_element_to_clickable(
            login_page_locators.login_button)

    def go_to_site(self):
        self.driver.get(configuration.URL)

    def go_to_page(self, url):
        self.driver.get(configuration.URL+url)
        self.wait_url_contains(url)

    def go_to_login_page(self):
        self.driver.get(configuration.URL+configuration.login_page)

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop_element(self, source_element, target_element):
        script = """
        function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragStartEvent);
            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            destinationNode.dispatchEvent(dropEvent);

            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragEndEvent);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source_element, target_element)
