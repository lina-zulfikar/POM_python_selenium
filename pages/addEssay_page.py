from selenium import webdriver 
from selenium.webdriver.common.by import By
from locators.admin_locator import TambahEssay
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import time

class AddEssay:
    def __init__(self, driver):
        self.driver = driver
        self.element = TambahEssay

    def open_menu_tambah_essay(self):
        element = self.driver.find_element(*TambahEssay.MENU_TAMBAH_ESSAY)
        element.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div/form/div[4]/div')))

    def isi_elemen(self, elemen_id, nilai):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, elemen_id)))
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
        element = self.driver.find_element(*TambahEssay.TINGKAT_SOAL)        
        dropdown = Select(element)

        # Pilih secara acak antara "Pusat" dan "Daerah"
        pilihan_acak = random.choice(["Pusat", "Daerah"])
        dropdown.select_by_visible_text(pilihan_acak)

    def simpan_soal(self):
        element = self.driver.find_element(*TambahEssay.BUTTON_SIMPAN)
        element.click()
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div/div[1]/a")))

        

