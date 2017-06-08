from pages import *
from setup import *


class TestSuite:
    """
    Тест по сценарию "Профиль".
    Описывает работу с разделом "Профиль" (заполнение формы, изменение пароля)
    """
    driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_profile(self):
        LoginPage(self.driver).login("ahabanovaal@gmail.com", "123123/")
        page = ProfilePage(self.driver)
        page.click_by_text("Профиль", 2)
        page.click_by_text("Редактировать")
        page.upload_photo("C:\\Users\\drozdoviv\\Desktop\\1.jpg")
        page.lastname("Шабанова")
        page.firstname("Анна")
        page.middlename("Леонидовна")
        page.birthdate("18061988")
        page.insurance_certificate_number("00102456767")
        page.individual_taxpayer_number("6449013711")
        page.email("ahabanovaal@gmail.com")
        page.passport_info('4455 625896 Выдан ОВД "Замоскворечье" 14.09.2006')
        page.registration_address("г.Москва, Ленинградский проспект, д. 46, кв. 211")
        page.actual_address("г.Москва, Ленинградский проспект, д. 46, кв. 211")
        page.click_by_text("Сохранить")
        page.click_by_text("Изменить пароль")
        page.old_password("123123/")
        page.password("123123/")
        page.password_confirm("123123/")
        page.change()
        assert "Пароль изменен" in self.driver.page_source
