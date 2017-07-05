from pages import *
import pytest


class TestSuite:
    """
    Содержание test-suite:

    """
    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Chrome(Settings.path_to_driver)
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("test.gossluzhba.gov.ru")
        cls.hr = get_data_by_number(cls.data, "accounts", 0)
        cls.admin = get_data_by_number(cls.data, "accounts", 1)
        cls.user = get_data_by_number(cls.data, "accounts", 2)

    @classmethod
    def teardown_class(cls):

        cls.driver.quit()

    def get_page(self, value):
        sleep(1.5)
        print('Переход по ссылке: %s' % value)
        self.driver.get(value)

    @pytest.mark.parametrize("count", range(20))
    def test_new_department(self, count):
        """
        Организационно-штатная структура - Формирование организационно-штатной структуры
        """
        data = get_data_by_number(self.data, "departments")

        LoginPage(self.driver).login(data=self.hr)
        page = StructureInfoPage(self.driver)
        page.go_to(Links.staff_structure)
        page.wait_for_text_appear("Структура")
        page.click_by_text("Добавить")
        page.organization(data["organization"])
        page.name(data["name"])
        page.fot(data["fot"])
        page.limit(data["limit"])
        page.click_by_text("Сохранить")
        page.click_by_text(data["name"])
        for division in data["divisions"]:
            StructureDetailsPage(self.driver).forming()
            if division["parent"]:
                element = page.wait_for_element_appear((By.XPATH, "//tr[contains(., '%s')]" % division["parent"]))
                element.find_element(By.XPATH, ".//input[@type='checkbox']").click()
            page.click_by_text("Добавить")
            page = DepartmentPage(self.driver)
            page.name(division["name"])
            page.name_genitive(division["nameGenitive"])
            page.name_dative(division["nameDative"])
            page.name_accusative(division["nameAccusative"])
            page.limit(division["limit"])
            page.code(division["code"])
            page.launch_date(division["launchDate"])
            page.order_number(division["orderNumber"])
            page.order_date(division["orderDate"])
            page.click_by_text("Штатная численность")
            for staff in division["staffAmount"]:
                page.position(staff["position"])
                page.amount(staff["amount"])
                page.click_by_text("Добавить", 2)
            page.click_by_text("Сохранить")
        page = StructureDetailsPage(self.driver)
        page.launch()
        page.order_number(data["orderNumber"])
        page.order_date(data["orderDate"])
        page.launch_date(data["date"])
        page.click_by_text("Ввести в действие")
        page.go_to(Links.staff_structure)
        page = StructureDetailsPage(self.driver)
        page.click_by_text(data["name"])
        page.click_by_text("Показать все")
        page.wait_for_text_appear("Назначить")
        assert page.projects_check(), "Ошибка: На странице присутствует ярлык \"Проект\""
