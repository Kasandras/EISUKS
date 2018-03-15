from pages import *
import pytest
from seleniumrequests import Chrome
import requests


class TestSuite:

    driver = webdriver.Chrome("drivers/chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_salary_payments(self):
        """
        Формирование кадрового состава - Денежное содержание
        """
        page = MainPage(self.driver)
        page.login_button.click()

        page = AlternativeLoginPage(self.driver)
        # page.login(username='ivanovpa@quarta.su', password='123123/')
        # page.login(username='petrovpa@quarta.su', password='123123/')
        # page.login(username='ivanovpa@quarta.su', password='123123/')
        # page.login(username='ivanovpa@quarta.su', password='123123/', full_name='П. А. Иванов')
        page.username = "ivanovpa@quarta.su"
        page.password = "123123/"
        page.remember_me = True
        page.submit.click()

        sleep(4)



