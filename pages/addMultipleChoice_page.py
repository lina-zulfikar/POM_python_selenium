from selenium import webdriver 
from selenium.webdriver.common.by import By
from locators.admin_locator import TambahPilihanGanda
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import time

class AddMultipleChoice:
    def __init__(self, driver):
        self.driver = driver
        self.element = TambahPilihanGanda

    def open_menu_tambah_pilgan(self):
        
        # element = self.driver.find_element(*TambahPilihanGanda.MENU_TAMBAH_PILGAN)
        element = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/a[3]')
        element.click()
        time.sleep(3)
        # WebDriverWait(self.driver, 20).until(EC._element_if_visible(*TambahPilihanGanda.HEADER))

    def isi_elemen(self, elemen_id, nilai):
        # Temukan elemen yang ingin di-scroll
        target_element = self.driver.find_element(By.ID, elemen_id)

        # Scroll ke elemen
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        time.sleep(1)  
             
        editorFrame = self.driver.find_element(By.CSS_SELECTOR, f"#{elemen_id} > iframe")
        self.driver.switch_to.frame(editorFrame)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.click()
        body.send_keys(nilai)
        self.driver.switch_to.default_content()
    
    def tambah_text(self, text_id, ini_text):
        self.isi_elemen(text_id, ini_text)
        
    def pilih_tingkat_soal(self):    
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/form/div[2]/select")        
        dropdown = Select(element)

        # Pilih secara acak antara "Pusat" dan "Daerah"
        pilihan_acak = random.choice(["Pusat", "Daerah"])
        dropdown.select_by_visible_text(pilihan_acak)

    def tambah_jawaban(self, jawaban_id, jawaban):
        self.isi_elemen(jawaban_id, jawaban)

    def jawaban_benar(self):    
        element = self.driver.find_element(By.ID, 'correct_answer')        
        dropdown = Select(element)

        # Pilih secara acak
        pilihan_acak = random.choice(['A', 'B', 'C', 'D'])
        dropdown.select_by_visible_text(pilihan_acak)

    def simpan_soal(self):
        element = self.driver.find_element(*TambahPilihanGanda.BUTTON_SIMPAN)
        element.click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div/div[1]/a")))

    def cek_soal(self):
    
        # Temukan elemen yang ingin di-scroll
        target_element = self.driver.find_element(By.XPATH, '/html/body/div/main/div/nav/ul/li[1]/a')

        pagination = self.driver.find_element(By.XPATH, f'/html/body/div/main/div/nav/ul/li[{8}]/a')
        pagination.click()

        soal_teks = "soal no 1"
        try:
            # Tunggu hingga elemen dengan teks soal tertentu muncul
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/main/div/div[2]"), soal_teks)
            )
            print(f"Soal dengan teks '{soal_teks}' sudah tersimpan!")
        except:
            print(f"Soal dengan teks '{soal_teks}' tidak ditemukan. Mungkin belum tersimpan.")

        # i = 2
        # while i < 100:
        #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div/nav/ul/li[1]/a")))
        #     self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

        #     pagination = self.driver.find_element(By.XPATH, f'/html/body/div/main/div/nav/ul/li[{i}]/a')
        #     pagination.click()
            
        # i = 1
        # while i < 100:  # Mulai dari halaman pertama
        #     pagination_xpath = f'/html/body/div/main/div/nav/ul/li[{i}]/a'
            
















        


