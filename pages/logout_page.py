from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LogOut(BasePage):
    BUTTON_KELUAR = (By.XPATH, "//button[normalize-space()='Keluar']")
    BUTTON_USER = (By.XPATH, "//a[@role='button']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_user(self):
        self.click(self.BUTTON_USER)
        time.sleep(1) 
        
    def keluar(self):
        self.click(self.BUTTON_KELUAR)

##########aksi##########
    def log_out(self):
        self.click_user()
        self.keluar()
