from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages import login_page, addEssay_page, addMultipleChoice_page, addCaseStudy_page
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
AddMultipleChoice = addMultipleChoice_page.AddMultipleChoice
AddEssay = addEssay_page.AddEssay
AddCaseStudy = addCaseStudy_page.AddCaseStudy

def test_berhasil_login():    
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_email('linazulfikar99@gmail.com')
    login_page.enter_password('Testingautomation')
    login_page.click_masuk()

def test_berhasil_tambah_pilgan():
    tambah_pilgan = AddMultipleChoice(driver)
    tambah_pilgan.open_menu_tambah_pilgan()
#     tambah_pilgan.tambah_text('cke_1_contents','Soal nomor 2')
#     tambah_pilgan.pilih_tingkat_soal()
#     tambah_pilgan.tambah_jawaban('cke_2_contents', 'Jawaban A')
#     tambah_pilgan.tambah_jawaban('cke_3_contents', 'Jawaban B')
#     tambah_pilgan.tambah_jawaban('cke_4_contents', 'Jawaban C')
#     tambah_pilgan.tambah_jawaban('cke_5_contents', 'Jawaban D')
#     tambah_pilgan.jawaban_benar()
#     tambah_pilgan.tambah_text('cke_6_contents','Ini adalah penjelasan kedua.')
#     tambah_pilgan.simpan_soal()
    tambah_pilgan.cek_soal()

# def test_berhasil_tambah_essay():
#     tambah_essay = AddEssay(driver)
    # tambah_essay.open_menu_tambah_essay()
    # tambah_essay.tambah_text('cke_1_contents', 'Essay nomor 1')
    # tambah_essay.pilih_tingkat_soal()
    # tambah_essay.tambah_text('cke_2_contents', 'Kunci jawaban nomor 1')
    # tambah_essay.simpan_soal()
    # tambah_essay.cek_essay()

# def test_berhasil_tambah_studi_kasus():
#     tambah_studiKasus = AddCaseStudy(driver)
#     tambah_studiKasus.open_menu_tambah_studi_kasus()