from pages import *
import pytest


class TestSuite:
    """
    Содержание test-suite:

    """
    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):

        cls.driver.quit()

    def get_page(self, value):
        sleep(1.5)
        print('Переход по ссылке: %s' % value)
        self.driver.get(value)

    @pytest.mark.parametrize('amount', range(10))
    def test_new_department(self, amount):

        data = get_data_by_number(load_data("testData"), "departments")

        self.get_page(Links.staff_structure)
        p = StructureInfoPage(self.driver)
        p.wait_for_text_appear("Структура")
        p.click_by_text("Добавить")
        # p.organization(data["organization"])
        p.name(data["name"])
        p.fot(data["fot"])
        p.limit(data["limit"])
        p.click_by_text("Сохранить")
        p.click_by_text(data["name"])
        for i in data["divisions"]:
            StructureDetailsPage(self.driver).forming()
            if i["parent"]:
                element = p.wait_for_element_appear((By.XPATH, "//tr[contains(., '%s')]" % i["parent"]))
                element.find_element(By.XPATH, ".//input[@type='checkbox']").click()
            p.click_by_text("Добавить")
            p = DepartmentPage(self.driver)
            p.name(i["name"])
            p.name_genitive(i["nameGenitive"])
            p.name_dative(i["nameDative"])
            p.name_accusative(i["nameAccusative"])
            p.limit(i["limit"])
            p.code(i["code"])
            p.launch_date(i["launchDate"])
            p.order_number(i["orderNumber"])
            p.order_date(i["orderDate"])
            p.click_by_text("Штатная численность")
            for j in i["staffAmount"]:
                p.position(j["position"])
                p.amount(j["amount"])
                p.click_by_text("Добавить", 2)
            p.click_by_text("Сохранить")
        p = StructureDetailsPage(self.driver)
        p.launch()
        p.order_number(data["orderNumber"])
        p.order_date(data["orderDate"])
        p.launch_date(data["date"])
        p.click_by_text("Ввести в действие")
        sleep(1)
        assert "Ошибка на сервере." not in self.driver.page_source
        sleep(1)
        self.get_page(Links.staff_structure)
        sleep(60)
        p = StructureDetailsPage(self.driver)
        p.click_by_text(data["name"])
        sleep(5)
        p.click_by_text("Показать все")
        p.wait_for_text_appear("Назначить")
        flag = True
        for i in self.driver.find_elements(By.XPATH, "//small[.='Проект']"):
            if i.is_displayed():
                webdriver.ActionChains(self.driver).move_to_element(i).perform()
                flag = False
                break
        sleep(2)
        assert flag, "Ошибка: На странице присутствует ярлык \"Проект\""
