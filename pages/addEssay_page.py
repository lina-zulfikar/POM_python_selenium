from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import random
import time

class AddEssay(BasePage):
    MENU_TAMBAH_ESSAY = (By.XPATH, "//p[normalize-space()='Tambah Esai']")
    OBJEK = (By.XPATH, '/html/body/div/main/div/form/div[4]/div')
    TINGKAT_SOAL = (By.XPATH, "//*[@id='question_type']")
    BUTTON_SIMPAN = (By.XPATH, '/html/body/div/main/div/form/div[4]/div')

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_tambah_essay(self):
        self.click(self.MENU_TAMBAH_ESSAY)
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
        element = self.driver.find_element(*self.TINGKAT_SOAL)        
        dropdown = Select(element)

        # Pilih secara acak antara "Pusat" dan "Daerah"
        pilihan_acak = random.choice(["Pusat", "Daerah"])
        dropdown.select_by_visible_text(pilihan_acak)

    def simpan_soal(self):
        element = self.driver.find_element(*self.BUTTON_SIMPAN)
        element.click()
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div/div[1]/a")))

    # !!! cek coal !!! #
    # def cek_essay(self):
    
    #     # Temukan elemen yang ingin di-scroll
    #     time.sleep(2)
    #     target_element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Next']")
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    #     time.sleep(3)

    #     try:
    #         # Cari semua elemen yang memiliki class 'page-item' kecuali yang terakhir (biasanya 'Next')
    #         page_items = self.driver.find_elements(By.CSS_SELECTOR, "li.page-item:not(:last-child)")
            
    #         # Dapatkan link dari elemen terakhir (yang sebelum 'Next')
    #         last_page_link = page_items[-1].find_element(By.TAG_NAME, "a")
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((last_page_link)))

    #         # Klik link untuk navigasi ke halaman tersebut
    #         last_page_link.click()
            
    #         # Cari soal yang sebelumnya ditambahkan
    #         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Essay nomor 1')]")))
    #         self.driver.save_screenshot("essay_tersimpan.png")
        
    #     except NoSuchElementException:
    #         print("Tidak dapat menemukan elemen pagination")

#########aksi##########
    def add_esai(self):
        self.open_menu_tambah_essay()
        self.tambah_text('cke_1_contents', 'Lina sidang')
        self.pilih_tingkat_soal()
        self.tambah_text('cke_2_contents', 'Lina pasti sidang')
        self.simpan_soal()

