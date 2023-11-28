from selenium import webdriver 
from selenium.webdriver.common.by import By
from locators.admin_locator import TambahPilihanGanda
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
        target_element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Next']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="Next"]')))

        try:
            # Cari semua elemen yang memiliki class 'page-item' kecuali yang terakhir (biasanya 'Next')
            page_items = self.driver.find_elements(By.CSS_SELECTOR, "li.page-item:not(:last-child)")
            
            # Dapatkan link dari elemen terakhir (yang sebelum 'Next')
            last_page_link = page_items[-1].find_element(By.TAG_NAME, "a")
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((last_page_link)))

            # Klik link untuk navigasi ke halaman tersebut
            last_page_link.click()
            
            # Cari soal yang sebelumnya ditambahkan
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Soal nomor 2')]")))
            self.driver.save_screenshot("pilgan_tersimpan.png")
        
        except NoSuchElementException:
            print("Tidak dapat menemukan elemen pagination")

        # finally:
        #     # Jangan lupa untuk menutup driver setelah tes selesai
        #     self.driver.quit()















        


