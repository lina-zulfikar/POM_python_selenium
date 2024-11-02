import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogOut
from pages.simulasiUjian_page import SimulasiUjian
import sys
sys.path.append('.')

@pytest.fixture(scope="module")  # Set scope ke module agar WebDriver tetap hidup selama tes modul berjalan
def driver():
    # Inisialisasi WebDriver untuk setiap test
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Tutup WebDriver setelah semua test di modul selesai
    driver.quit()

class TestPesertaWorkflow():
    def test_login_peserta(self,driver):    
        login_page = LoginPage(driver,user_type ="peserta")
        login_page.login()

    def test_simulasi_pusat(self,driver):
        kerjakan_soal = SimulasiUjian(driver)
        kerjakan_soal.kerjakan_simulasi()

    def test_logout(self,driver):
        log_out = LogOut(driver)
        log_out.log_out()