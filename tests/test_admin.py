import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.logout_page import LogOut
from pages.addCaseStudy_page import AddCaseStudy
from pages.addEssay_page import AddEssay
from pages.addMultipleChoice_page import AddMultipleChoice
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

class TestAdminWorkflow:
    def test_login_admin(self):    
        login_page = LoginPage(user_type ="admin")
        login_page.login()

    def test_berhasil_tambah_pilgan(self, driver):
        tambah_pilgan = AddMultipleChoice(driver)
        tambah_pilgan.add_multiplechoice()

    def test_berhasil_tambah_essay(self,driver):
        tambah_essay = AddEssay(driver)
        tambah_essay.add_esai()

    def test_berhasil_tambah_studi_kasus(self,driver):
        tambah_studiKasus = AddCaseStudy(driver)
        tambah_studiKasus.add_studykasus()

    def test_logout(self,driver):
        log_out = LogOut(driver)
        log_out.log_out