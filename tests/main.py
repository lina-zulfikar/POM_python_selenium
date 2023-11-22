from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.addMultipleChoice_page import AddMultipleChoice
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

ids = driver.find_elements(By.TAG_NAME, 'div')
print(ids)
print('hello lina')

def test_berhasil_login():    
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_email('linazulfikar99@gmail.com')
    login_page.enter_password('Testingautomation')
    login_page.click_masuk()

    # Tambahkan asser untuk memeriksa hasil pengujian
    # assert "Welcome" in driver.page_source

def test_berhasil_tambah_soal():
    tambah_soal = AddMultipleChoice(driver)
    tambah_soal.open_menu_tambah_pilgan()
    # tambah_soal.tambah_text('cke_1_contents','Soal nomor 2')
    # tambah_soal.pilih_tingkat_soal()
    # tambah_soal.tambah_jawaban('cke_2_contents', 'Jawaban A')
    # tambah_soal.tambah_jawaban('cke_3_contents', 'Jawaban B')
    # tambah_soal.tambah_jawaban('cke_4_contents', 'Jawaban C')
    # tambah_soal.tambah_jawaban('cke_5_contents', 'Jawaban D')
    # tambah_soal.jawaban_benar()
    # tambah_soal.tambah_text('cke_6_contents','Ini adalah penjelasan kedua.')
    # tambah_soal.simpan_soal()
    tambah_soal.cek_soal()
    





