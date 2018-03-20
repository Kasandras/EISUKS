from pages import *
import pytest


class TestSuite:
    """
    Сценарий: Учет кадрового состава - Ведение электронных личных дел
    """

    __file__ = "123123"

    driver = webdriver.Chrome(path_to_driver)

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_create_new_user(self):
        print('s1-t1')

    def test_fill_general_info_for_created_user(self):
        print('s1-t2')
