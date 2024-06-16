from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages import login_page, simulasi_pusat_page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time
sys.path.append('.')



options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
driver.get("http://127.0.0.1:8080")

LoginPage = login_page.LoginPage
CGAAPusat = simulasi_pusat_page.CGAAPusat

def test_berhasil_login():    
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_email('linazulfikar16@gmail.com')
    login_page.enter_password('Testingpeserta')
    login_page.click_masuk()
    login_page.success_login('/html/body/main/p[1]')

def test_simulasi_pusat():
    kerjakan_soal = CGAAPusat(driver)
    kerjakan_soal.start_simulasi()
    # kerjakan_soal.kerjakan_soal()
    kerjakan_soal.selesaikan_sesi()
    kerjakan_soal.lanjutkan_sesi()