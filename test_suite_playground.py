from pages import *


class TestSuite:

    driver = webdriver.Chrome("drivers/chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.hr = get_data_by_number(cls.data, "accounts", 0)
        cls.admin = get_data_by_number(cls.data, "accounts", 1)
        cls.user = get_data_by_number(cls.data, "accounts", 2)
        cls.hr2 = get_data_by_number(cls.data, "accounts", 3)
        cls.user2 = get_data_by_number(cls.data, "accounts", 4)
        execute_script(Queries.delete_from_fruk)
        execute_script(Queries.delete_personal_file)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_salary_payments(self):
        """
        Учет кадрового состава - Ведение электронных личных дел
        """

        AlternativeLoginPage(self.driver).login(data=self.hr)

        page = AlternativePersonalFilePage(self.driver, test='Создание нового пользователя')
        page.go_to(Links.personal_files)
        page.add.click()
        page.new.last_name = "Автоматизация"
        page.new.first_name = "Автоматизация"
        page.new.middle_name = "Автоматизация"
        page.new.birth_date = "04.09.1970"
        page.new.insurance_certificate_number = "00193214196"
        page.new.save.click()

        page.wait.text_appear("Личные сведения")

        page.general.general_edit.click()
        page.general.last_name = "Автоматизация"
        page.general.first_name = "Автоматизация"
        page.general.middle_name = "Автоматизация"
        page.general.gender = "Мужской"
        page.general.birth_date = "22.11.1979"
        page.general.citizenship = "Гражданин Российской Федерации"
        page.general.birth_place = "Москва, Лубянка 9"
        page.general.was_convicted = "Нет"
        page.general.name_was_changed = "Не менял"
        page.general.insurance_certificate_number = "00193214196"
        page.general.save.click()

        page.wait.text_disappear("Сохранить")



