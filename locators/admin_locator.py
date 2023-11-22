from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    BUTTON_LOGIN = (By.XPATH, '//a[normalize-space()="Login"]')
    EMAIL_FIELD = (By.XPATH, '//input[@placeholder="Email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@placeholder="Password"]')
    BUTTON_MASUK = (By.XPATH, '//button[normalize-space()="Masuk"]')

class DashboardLocators(object):
    BUTTON_ADMIN = (By.XPATH, '/html/body/div/main/nav/div/div[2]/li/a/div')
    BUTTON_SIGN_OUT = (By.XPATH, '/html/body/div/main/nav/div/div[2]/li/ul/li/form/button')

class TambahPilihanGanda(object):
    HEADER = (By.XPATH, '/html/body/div/main/div/p')
    MENU_TAMBAH_PILGAN = (By.XPATH, '/html/body/div/div[2]/a[5]')
    TAMBAH_PERTANYAAN = 'cke_1_contents'
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