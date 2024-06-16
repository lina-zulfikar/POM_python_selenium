from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = self.wait.until(EC.presence_of_element_located(by_locator))
        assert web_element.text == element_text