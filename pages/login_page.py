from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage  # Mengimpor BasePage

class LoginPage(BasePage):  # Login mewarisi BasePage
    button_login = (By.XPATH, '//a[normalize-space()="Login"]')
    email_input = (By.XPATH, '//input[@placeholder="Email"]')
    password_input = (By.XPATH, '//input[@placeholder="Password"]')
    button_masuk = (By.XPATH, '//button[normalize-space()="Masuk"]')

    def __init__(self, driver, user_type="admin"):
        super().__init__(driver)  # Memanggil konstruktor BasePage
        self.user_type = user_type

    def click_login(self):
        self.driver.maximize_window()
        self.click(self.button_login)  # Menggunakan metode click dari BasePage
        

    def enter_email(self):
        email_input = self.driver.find_element(*self.email_input)
        if self.user_type == "admin":
            email_input.send_keys('linazulfikar99@gmail.com')
        elif self.user_type == "peserta":
            email_input.send_keys('linazulfikar16@gmail.com')

    def enter_password(self):
        password_input = self.driver.find_element(*self.password_input)
        if self.user_type == "admin":
            password_input.send_keys('Testingautomation')
        elif self.user_type == "peserta":
            password_input.send_keys('Testingpeserta')

    def click_masuk(self):
        self.click(self.button_masuk)  # Menggunakan metode click dari BasePage

    def success_login(self, cek_elemen):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, cek_elemen)))

#########aksi############
    def login(self):
        self.open('http://127.0.0.1:8080')
        self.click_login()
        self.enter_email()
        self.enter_password()
        self.click_masuk()
