from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import time

class AddCaseStudy(BasePage):
    TAMBAH_STUDY_KASUS = (By.XPATH, "//p[normalize-space()='Tambah Studi Kasus']")
    SIMPAN = (By.XPATH, "//button[normalize-space()='Simpan']")
    PILIH_TINGKAT_SOAL = (By.XPATH, "//select[@id='question_type']")
    JUMLAH_INSTRUKSI = (By.XPATH, "//select[@id='instruction_count']")
    TAMBAH_PERTANYAAN = (By.ID, 'cke_1_contents')
    TAMBAH_INSTRUKSI_A = (By.ID, 'cke_2_contents')
    TAMBAH_INSTRUKSI_B = (By.ID, 'cke_3_contents')
    ELEMEN = (By.XPATH, '/html/body/div/main/div/div[1]/a')

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_tambah_studi_kasus(self):
        self.click(self.TAMBAH_STUDY_KASUS)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div/form/div[24]/div')))

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

    def pilih_tingkat_soal(self):
        element = self.driver.find_element(*self.PILIH_TINGKAT_SOAL)
        dropdown = Select(element)

        # Pilih secara acak antara "Pusat" dan "Daerah"
        pilihan_acak = random.choice(["Pusat", "Daerah"])
        dropdown.select_by_visible_text(pilihan_acak)
        time.sleep(3)

    def tambah_instruksi(self, text_id, ini_text):
        self.isi_elemen(text_id, ini_text)

    def tambah_kunci_jawaban(self, text_id, ini_text):
        self.isi_elemen(text_id, ini_text)

    def pilih_jumlah_instruksi(self):
        element = self.driver.find_element(*self.JUMLAH_INSTRUKSI)
        dropdown = Select(element)

        dropdown.select_by_visible_text('1')
        time.sleep(3)
    
    def simpan_soal(self):
        target_element = self.driver.find_element(By.XPATH, "//button[normalize-space()='Simpan']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        time.sleep(1)  # Tambahkan jeda waktu setelah di-scroll ke dalam pandangan
        
        # Tunggu hingga elemen bisa diklik
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target_element))
        
        # Klik elemen
        target_element.click()
        
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.ELEMEN))

##########aksi############
    def add_studykasus(self):
        self.open_menu_tambah_studi_kasus()
        self.tambah_instruksi('cke_1_contents', 'Bismillah sidang')
        self.pilih_tingkat_soal()
        self.pilih_jumlah_instruksi()
        self.tambah_instruksi('cke_2_contents', 'Instruksi sidang')
        self.tambah_kunci_jawaban('cke_3_contents', 'Jawab sidang')
        self.simpan_soal()