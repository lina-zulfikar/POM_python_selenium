from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_login = (By.XPATH, '//a[normalize-space()="Login"]')
        self.email_input = (By.XPATH, '//input[@placeholder="Email"]')
        self.password_input = (By.XPATH, '//input[@placeholder="Password"]')
        self.button_masuk = (By.XPATH, '//button[normalize-space()="Masuk"]')

    def click_login(self):
        self.driver.maximize_window()
        self.driver.find_element(*self.button_login).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_masuk(self):
        self.driver.find_element(*self.button_masuk).click()
        # WebDriverWait(self.driver, 20).until(EC._element_if_visible('/html/body/main/div[1]'))
        time.sleep(3)
        