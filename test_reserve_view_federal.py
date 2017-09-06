from pages import *
from setup import *
from selenium import webdriver


class TestSuite:
    """
    Просмотр участников федерального резерва управленческих кадров
    Просмотр и фильтрация по участникам резерва
    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.account = get_data_by_number(load_data("gossluzhba1"), "accounts", 1)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    def test_reserve_view_federal(self):
        """
        Просмотр участников резерва
        """
        page = ReserveViewFederal(self.driver)
        data = get_data_by_value(self.data, "reserve", "view", "")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.permission_read_resume)
        page.permission_read_resume(True)
        page.wait_for_text_appear("Данные успешно сохранены")
        self.go_to(Links.reserve_view_federal)
        page.click_by_text("Фильтр")
        page.level_reserve(data["level_reserve"])
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.click_by_text(data["participant"])
        page.resume()
        page.check_text_and_close("Рабочий телефон")
        page.presentation()
        page.check_text_and_close("Целевой орган")
