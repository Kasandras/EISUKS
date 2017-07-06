from pages import *
from setup import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSuite:
    """
    Просмотр участников федерального резерва управленческих кадров

    Просмотр и фильтрация по участникам резерва
    """
    driver = webdriver.Chrome("chromedriver.exe")

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.admin = get_data_by_number(load_data("drozdovData")["users"], "accounts", 0)

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
        Создание вакансий, которые будут использоваться в управлении объявлениями
        """
        page = ReserveViewFederal(self.driver)
        body = self.driver.find_element_by_tag_name("body")
        data = load_data("drozdovData")
        reserve = data["reserve"]

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["full_name"])
        self.go_to(Links.permission_read_resume)
        page.permission_read_resume(True)
        page.wait_for_text_appear("Данные успешно сохранены")
        self.go_to(Links.reserve_view_federal)
        page.click_by_text("Фильтр")
        page.level_reserve(reserve["level_reserve"])
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.click_by_text(reserve["participant"])
        page.resume()
        page.check_text_and_close("Рабочий телефон")
        page.presentation()
        page.check_text_and_close("Целевой орган")
