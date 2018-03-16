from pages import *


class TestSuite:
    driver = webdriver.Chrome("drivers/chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_name(self):
        """
        testinfo
        """

        page = Page(self.driver, test='info')
        