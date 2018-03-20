from pages import *


class TestSuite:
    """
    Сценарий: Организационно-штатная структура - Формирование организационно-штатной структуры
    """

    driver = webdriver.Chrome(path_to_driver)

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_create_new_structure(self):
        print('s2-t1')

    def test_create_new_department(self):
        print('s2-t2')

    def test_make_active(self):
        print('s2-t3')
