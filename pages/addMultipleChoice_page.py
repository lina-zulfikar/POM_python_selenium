from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import random
import time

class AddMultipleChoice(BasePage):
    HEADER = (By.XPATH, '/html/body/div/main/div/p')
    MENU_TAMBAH_PILGAN = (By.XPATH, '/html/body/div/div[2]/a[5]')
    TAMBAH_PERTANYAAN = '#cke_1_contents'
    TINGKAT_SOAL = (By.ID, 'question_type')
    BODY = (By.TAG_NAME, 'body')
    PILGAN_A = ('#cke_2_contents')
    PILGAN_B = ('#cke_3_contents')
    PILGAN_C = ('#cke_4_contents')
    PILGAN_D = ('#cke_5_contents')
    KUNCI_JAWABAN = (By.ID, 'correct_answer')
    PENJELASAN = (By.XPATH, '/html/body/div/main/div/form/div[5]/div/div/div')
    BUTTON_SIMPAN = (By.XPATH, '/html/body/div/main/div/form/div[6]/div/button')
    PAGINATION = (By.XPATH, '/html/body/div/main/div/nav/ul/li[{nomor_halaman}]/a')

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_tambah_pilgan(self):
        
        # element = self.driver.find_element(*TambahPilihanGanda.MENU_TAMBAH_PILGAN)
        element = self.driver.find_element(By.XPATH, "//p[normalize-space()='Tambah Pilihan Ganda']")
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
        element = self.driver.find_element(*self.BUTTON_SIMPAN)
        element.click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/div/div[1]/a")))

    # def cek_soal(self):
    
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
    #         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Soal nomor 2')]")))
    #         self.driver.save_screenshot("pilgan_tersimpan.png")
        
    #     except NoSuchElementException:
    #         print("Tidak dapat menemukan elemen pagination")


###############aksi#################
    def add_multiplechoice(self):
        self.open_menu_tambah_pilgan()
        self.tambah_text('cke_1_contents','Lina sidang november')
        self.pilih_tingkat_soal()
        self.tambah_jawaban('cke_2_contents', 'Jawaban A')
        self.tambah_jawaban('cke_3_contents', 'Jawaban B')
        self.tambah_jawaban('cke_4_contents', 'Jawaban C')
        self.tambah_jawaban('cke_5_contents', 'Jawaban D')
        self.jawaban_benar()
        self.tambah_text('cke_6_contents','Lina lulus kuliah')
        self.simpan_soal()
            














        




