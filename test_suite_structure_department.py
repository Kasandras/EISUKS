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
        cls.account = get_data_by_number(load_data("testData"), "accounts")

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
        data = get_data_by_number(load_data("testData"), "departments")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        page = StructureInfoPage(self.driver)
        page.go_to(Links.staff_structure)
        page.wait_for_text_appear("Структура")
        page.click_by_text("Добавить")
        # p.organization(data["organization"])
        page.name(data["name"])
        page.fot(data["fot"])
        page.limit(data["limit"])
        page.click_by_text("Сохранить")
        page.click_by_text(data["name"])
        for i in data["divisions"]:
            StructureDetailsPage(self.driver).forming()
            if i["parent"]:
                element = page.wait_for_element_appear((By.XPATH, "//tr[contains(., '%s')]" % i["parent"]))
                element.find_element(By.XPATH, ".//input[@type='checkbox']").click()
            page.click_by_text("Добавить")
            page = DepartmentPage(self.driver)
            page.name(i["name"])
            page.name_genitive(i["nameGenitive"])
            page.name_dative(i["nameDative"])
            page.name_accusative(i["nameAccusative"])
            page.limit(i["limit"])
            page.code(i["code"])
            page.launch_date(i["launchDate"])
            page.order_number(i["orderNumber"])
            page.order_date(i["orderDate"])
            page.click_by_text("Штатная численность")
            for j in i["staffAmount"]:
                page.position(j["position"])
                page.amount(j["amount"])
                page.click_by_text("Добавить", 2)
            page.click_by_text("Сохранить")
        page = StructureDetailsPage(self.driver)
        page.launch()
        page.order_number(data["orderNumber"])
        page.order_date(data["orderDate"])
        page.launch_date(data["date"])
        page.click_by_text("Ввести в действие")
        page = StructureDetailsPage(self.driver)
        page.click_by_text(data["name"])
        assert page.projects_check(), "Ошибка: На странице присутствует ярлык \"Проект\""
