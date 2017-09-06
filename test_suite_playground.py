from pages import *
import pytest


class TestSuite:

    driver = webdriver.Chrome()

    @classmethod
    def setup_class(cls):
        #cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.hr = get_data_by_number(cls.data, "accounts", 0)
        cls.admin = get_data_by_number(cls.data, "accounts", 1)
        cls.user = get_data_by_number(cls.data, "accounts", 2)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    @pytest.mark.parametrize("user", ['Бойко', 'Бунин', 'Бурагина', 'Быкова', 'Васильева',
                                      'Волков', 'Воробушек', 'Воронов', 'Воронцов', 'Врагов'])
    def test_salary_payments(self, user):
        """
        Формирование кадрового состава - Денежное содержание
        """
        data = get_data_by_value(self.data, "employees", "lastName", "Автоматизация")["salaryPayment"]

        LoginPage(self.driver).login("ivanovpa@quarta.su", "123123/", "П. А. Иванов")
        print("=====Start of test for user: %s=====" % user)
        page = SalaryPaymentsPage(self.driver, 600)
        self.go_to(Links.personal_files)
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Денежное содержание")
        page.click_by_text("Добавить")
        page.scroll_to_top()
        page.wait_for_text_appear("Служащий должен")
        page.type(data["type"])
        page.amount(data["amount"])
        page.date_from(data["dateFrom"])
        page.click_by_text("Сохранить")
        page.wait_for_text_disappear("Сохранить")
        self.go_to(Links.salary_payments)
        OrdersPage(self.driver).submit(user)
        self.go_to(Links.personal_files)
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Денежное содержание")
        print("=====End of test for user: %s=====" % user)
        assert "Проект" not in self.driver.page_source
