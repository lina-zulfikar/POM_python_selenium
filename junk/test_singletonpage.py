from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

class LoginPage:
    button_login = (By.XPATH, '//a[normalize-space()="Login"]')
    email_input = (By.XPATH, '//input[@placeholder="Email"]')
    password_input = (By.XPATH, '//input[@placeholder="Password"]')
    button_masuk = (By.XPATH, '//button[normalize-space()="Masuk"]')

    def __init__(self):
        # Inisialisasi WebDriver di dalam LoginPage
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        
    def open(self):
        self.driver.get('http://127.0.0.1:8080')

    def click_login(self):
        self.driver.maximize_window()
        self.click(self.button_login) 

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_masuk(self):
        self.click(self.button_masuk) 

    def success_login(self, cek_elemen):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, cek_elemen)))

    def quit(self):
        self.driver.quit()

    def login(self, url, email, password):
        self.open(url)
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_masuk()
