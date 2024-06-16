from selenium import webdriver 
from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.admin_locator import TambahStudiKasus
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import time

class AddCaseStudy(BasePage):
    def open_menu_tambah_studi_kasus(self):
        element = self.driver.find_element(*TambahStudiKasus.MENU_TAMBAH_STUDI_KASUS)
        element.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div/form/div[24]/div')))

    # def isi_elemen(self, elemen_id, nilai):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, elemen_id)))
    #     # Temukan elemen yang ingin di-scroll
    #     target_element = self.driver.find_element(By.ID, elemen_id)

    #     # Scroll ke elemen
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    #     time.sleep(1)  
             
    #     editorFrame = self.driver.find_element(By.CSS_SELECTOR, f"#{elemen_id} > iframe")
    #     self.driver.switch_to.frame(editorFrame)
    #     body = self.driver.find_element(By.TAG_NAME, 'body')
    #     body.click()
    #     body.send_keys(nilai)
    #     self.driver.switch_to.default_content()
    
    # def tambah_instruksi(self, text_id, ini_text):
    #     self.isi_elemen(text_id, ini_text)

    # def tambah_kunci_jawaban(self, text_id, ini_text):
    #     self.isi_elemen(text_id, ini_text)
