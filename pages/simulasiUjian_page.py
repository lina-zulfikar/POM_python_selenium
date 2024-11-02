from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

class SimulasiUjian(BasePage):
    MULAI_SIMULASI = (By.XPATH, "//i[@class='bi bi-chevron-right']")
    CGAA_PUSAT = (By.XPATH, "//a[normalize-space()='CGAA Pusat']")
    MULAI_SIMULAI2 = (By.XPATH, "//button[normalize-space()='Mulai Simulasi']")
    JAWABAN_A = (By.XPATH, "//label[@for='answer1']")
    JAWABAN_B = (By.XPATH, "//label[@for='answer2']")
    JAWABAN_C = (By.XPATH, "//label[@for='answer3']")
    JAWABAN_D = (By.XPATH, "//label[@for='answer4']")
    SIMPAN_ESAI = (By.XPATH, "//button[normalize-space()='Simpan']")
    PESAN_TERSIMPAN = (By.XPATH, "//div[@class='toast-body']")
    STUDI_KASUS = (By.XPATH, "//a[@id='cs-1']")
    UJIAN_SELESAI = (By.XPATH, "//button[@id='submit']")
    SELESAI_SESI_1 = (By.XPATH, "//button[@id='submit']")
    DASHBOARD = (By.XPATH, "//a[normalize-space()='Dashboard']")
    xpaths = [
    "//button[@value='1']",
    "//button[@value='2']",
    "//button[@value='3']",
    "//button[@value='4']",
    "//button[@value='5']"
    ]

    def __init__(self, driver):
        super().__init__(driver)
    
    def start_simulasi(self):
        element1 = self.driver.find_element(By.XPATH, "//i[@class='bi bi-chevron-right']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        time.sleep(3)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//i[@class='bi bi-chevron-right']")))
        element1.click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="h2-text p-semi-bold d-flex mt-3 font-blue-dark2"]')))
        element2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='CGAA Pusat']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        time.sleep(2)
        element2.click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[normalize-space()="Mulai Simulasi"]')))
        element3 = self.driver.find_element(By.XPATH, "//button[normalize-space()='Mulai Simulasi']")
        element3.click()

        # self.driver.quit()

    def pilih_jawaban(self):
        time.sleep(4)
        # XPath untuk jawaban A, B, C, dan D
        jawaban_xpath = [
        "//label[@for='answer1']",
        "//label[@for='answer2']",
        "//label[@for='answer3']",
        "//label[@for='answer4']"
        ]
    
        # Pilih jawaban secara acak
        jawaban_dipilih = random.choice(jawaban_xpath)
              
        # Tunggu sampai jawaban bisa di-klik dan klik
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, jawaban_dipilih))
        ).click()

        

    # Fungsi untuk navigasi ke soal selanjutnya
    def navigasi_soal_selanjutnya(self):
        button_xpath = "//div[@class='text']"
        scroll = self.driver.find_element(By.XPATH, "//div[@class='text']" )

        # Tunggu sampai tombol muncul dan bisa diinteraksikan
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
        # Buat ActionChains object untuk melakukan aksi
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
        actions = ActionChains(self.driver)
        # Lakukan hover ke tombol dan klik
        actions.move_to_element(button).click().perform()

    # Fungsi untuk menyelesaikan sesi
    def selesaikan_sesi(self):
        tombol_submit_xpath = "//button[@id='submit']"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, tombol_submit_xpath))).click()

        # Mengerjakan soal
    def kerjakan_soal(self):
        jumlah_soal = 60  # Sesuaikan dengan jumlah soal yang ada
        for _ in range(jumlah_soal):
            self.pilih_jawaban()
            self.navigasi_soal_selanjutnya()
        
    def lanjutkan_sesi(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Lanjutkan Sesi']")))
        button_sesi2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Lanjutkan Sesi']")
        button_sesi2.click()

        time.sleep(3)

    # def kerjakan_soal(self):
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Lanjutkan Sesi']")))

    def isi_element(self, element_id, nilai):
        # Temukan element yang ingin discroll
        target_element = self.driver.find_element(By.ID, element_id)

        # Scroll ke element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        time.sleep(1)

        editorFrame = self.driver.find_element(By.CSS_SELECTOR,  f"#{element_id} > iframe")
        self.driver.switch_to.frame(editorFrame)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.click()
        body.send_keys(nilai)
        self.driver.switch_to.default_content()

    def simpan_esai(self):
        simpan = self.driver.find_element(*self.SIMPAN_ESAI)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.SIMPAN_ESAI))
        simpan.click()
        WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.PESAN_TERSIMPAN)
            )
        time.sleep(1)

    def jawab_esai(self, text_id, jawab_esai):
        time.sleep(1)
        self.isi_element(text_id, jawab_esai)
        time.sleep(2)

        self.simpan_esai()
        time.sleep(1)
        self.navigasi_soal_selanjutnya()

    def studi_kasus(self):
        kerjakan_studikasus = self.driver.find_element(*self.STUDI_KASUS)
        kerjakan_studikasus.click()

        time.sleep(1)

    def jawab_studi_kasus(self, text_id, jawab_studi_kasus, xpath_simpan):
        time.sleep(1)
        self.isi_element(text_id, jawab_studi_kasus)
        time.sleep(2)
        
        # Klik tombol simpan
        try:
            button = self.driver.find_element(By.XPATH, xpath_simpan)
            button.click()
            print(f"Tombol dengan XPath {xpath_simpan} berhasil diklik.")
        except Exception as e:
            print(f"Error mengklik tombol dengan XPath {xpath_simpan}: {e}")

    def selesaikan_ujian(self):
        selesaikan_ujian = self.driver.find_element(*self.UJIAN_SELESAI)
        selesaikan_ujian.click()
        time.sleep(2)

    def dahsboard(self):
        dashboard = self.driver.find_element(*self.DASHBOARD)
        dashboard.click()
        time.sleep(1)

##########aksi###########
    def kerjakan_simulasi(self):
        self.start_simulasi()
        self.kerjakan_soal()
        self.selesaikan_sesi()
        self.lanjutkan_sesi()
        for _ in range(5):
            self.jawab_esai('cke_1_contents', 'Jawab Esai Simulasi Pusat')
        self.studi_kasus()
        form_data = [
            ('cke_1_contents', 'Jawaban untuk studi kasus 1', "//button[@value='1']"),
            # ('cke_2_contents', 'Jawaban untuk studi kasus 2', "//button[@value='2']"),
            # ('cke_3_contents', 'Jawaban untuk studi kasus 3', "//button[@value='3']"),
            # ('cke_4_contents', 'Jawaban untuk studi kasus 4', "//button[@value='4']"),
            # ('cke_5_contents', 'Jawaban untuk studi kasus 5', "//button[@value='5']"),
            # ('cke_6_contents', 'Jawaban untuk studi kasus 6', "//button[@value='6']")
        ]
        for text_id, jawaban, xpath_simpan in form_data:
            self.jawab_studi_kasus(text_id, jawaban, xpath_simpan)
        self.selesaikan_ujian()
        self.dahsboard()
