from pages import *
from setup import *
from selenium import webdriver


class TestSuite:
    """
    Управление базами резерва
    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.admin = get_data_by_number(load_data("gossluzhba1"), "accounts", 1)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    def test_manage_reserve_bases(self):
        """
        Управление базами резерва
        """
        page = ManageReserveBasesPage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_manage", "code", "60")

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["fullName"])
        self.go_to(Links.manage_reserve_bases)
        page.click_by_text("Добавить")
        page.code(data["code"])
        page.name(data["name"])
        page.set_checkbox_by_order(1, True)
        page.click_by_text("Сохранить")
        page.wait_for_text_appear("Статус")
        page.edit()
        page.set_checkbox_by_order(1, False)
        page.click_by_text("Сохранить")
        page.wait_for_text_appear("Статус")
        assert data["code"] in self.driver.page_source
        page.delete()
