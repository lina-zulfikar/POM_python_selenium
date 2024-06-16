from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.admin_locator import TambahStudiKasus
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import time

class CGAAPusat(BasePage):
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


    def cek_soal(self):
        # Mendapatkan semua nomor soal dari sidebar
        nomor_soal_elems = self.driver.find_elements(By.CSS_SELECTOR, "button.number")

        # Loop melalui semua elemen nomor soal untuk memeriksa statusnya
        for elem in nomor_soal_elems:
            classes = elem.get_attribute('class')
            if 'btn-success' not in classes:  # Jika bukan hijau, berarti belum diisi atau ragu-ragu
                # Mendapatkan ID dari elemen
                nomor_soal_id = elem.get_attribute('id')
                # Jika ada flag merah, berarti ragu-ragu
                try:
                    flag = elem.find_element(By.XPATH, ".//div[contains(@class, 'flag bg-red-normal')]")
                    if flag.is_displayed():
                        # Mengklik soal untuk menghilangkan tanda ragu-ragu
                        elem.click()
                        self.pilih_jawaban()
                        self.navigasi_soal_selanjutnya()
                except NoSuchElementException:
                    # Tidak ada flag merah, berarti belum diisi
                    # Mengklik soal untuk mengisi
                    elem.click()
                    # Lakukan tindakan untuk mengisi soal di sini
                    # ...
        
    def lanjutkan_sesi(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Lanjutkan Sesi']")))
        button_sesi2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Lanjutkan Sesi']")
        button_sesi2.click()

    # def kerjakan_soal(self):
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Lanjutkan Sesi']")))


