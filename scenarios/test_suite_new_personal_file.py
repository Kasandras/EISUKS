from pages import *
from setup import driver


class TestSuite:
    driver = driver

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_name(self):
        print('test suite 1')
        