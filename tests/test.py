import pytest
from junk.test_singletonpage import LoginPage

@pytest.fixture(scope="function")
def login_page():
    login = LoginPage()  # LoginPage akan membuat driver baru untuk setiap tes
    yield login
    login.close()  # Menggunakan close() untuk menutup driver setelah tes selesai

def test_login_success(login_page):
    login_page.open()
    login_page.click_login()
    login_page.enter_email('linazulfikar99@gmail.com')
    login_page.enter_password('Testingautomation')
    login_page.click_masuk()


