from pages import *
from setup import *


class TestSuite:

    """
    Вакансии на контроле.
    Описывает работу раздела "Вакансии на контроле" (направление приглашений на вакансии, 
    принятие и отклонение приглашений, поиск результатов)
    """

    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.account = get_data_by_number(load_data("gossluzhba1"), "accounts", 1)
        cls.user = get_data_by_number(load_data("gossluzhba1"), "accounts", 2)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_vacancy_control_invite(self):
        page = VacancyControlPage(self.driver)
        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        page.click_by_text("Формирование кадрового состава")
        page.click_by_text("Проведение конкурса на замещение вакантной должности")
        page.scroll_to_top()
        page.click_by_text("Подбор")
        page.table_select_row(1, "Выбор первой вакансии")
        page.scroll_to_top()
        page.click_by_text("Добавить кандидата")
        page.click_by_text("Фильтр")
        page.key_word("Лобода")
        page.click_by_text("Применить")
        page.table_select_row(1, "Выбор первого кандидата")
        page.scroll_to_top()
        page.click_by_text("Направить приглашение")
        page.click_by_text("Направить приглашение", 2)
        page.scroll_to_top()
        page.click_by_text("Подбор")
        page.scroll_to_top()
        page.click_by_text("Закрыть")
        page.table_select_row(2, "Выбор второй вакансии")
        page.click_by_text("Добавить кандидата")
        page.click_by_text("Фильтр")
        page.key_word("Лобода")
        page.click_by_text("Применить")
        page.table_select_row(1, "Выбор кандидата")
        page.scroll_to_top()
        page.click_by_text("Направить приглашение")
        page.click_by_text("Направить приглашение", 2)

    def test_vacancy_control_statuses(self):
        page = VacancyControlPage(self.driver)
        LoginPage(self.driver).login(self.user["username"], self.user["password"], self.user["fullName"])
        page.click_by_text("Вакансии на контроле")
        page.click_by_text("Фильтр")
        page.status_response("Направлено приглашение")
        page.click_by_text("Применить")
        page.table_select_row(1, "Выбор приглашения")
        page.click_by_text("Принять приглашение")
        page.click_by_text("Продолжить")
        page.click_by_text("Подать документы")
        page.wait_for_text_appear("успешно")
        assert "Ваш отклик успешно завершен." in self.driver.page_source
        page.click_by_text("Назад")
        page.table_select_row(1, "Выбор приглашения")
        page.click_by_text("Отклонить приглашение")
        page.click_by_text("Фильтр")
        page.select2_clear(VacancyControlLocators.status_response)
        page.status_response("Отклонил приглашение")
        page.click_by_text("Применить")
        page.wait_for_text_appear("Отклонил приглашение")
        page.click_by_text("Дата события")
        page.click_by_text("Дата события")
        assert page.is_date_vacancy(), "Проверка \"Отклонил приглашение\" не прошла"
        page.click_by_text("Фильтр")
        page.wait_for_loading()
        page.select2_clear(VacancyControlLocators.status_response)
        page.status_response("Приглашен")
        page.click_by_text("Применить")
        page.wait_for_text_appear("Приглашен")
        page.click_by_text("Дата события")
        page.click_by_text("Дата события")
        assert page.is_date_vacancy(), "Проверка \"Приглашен\" не прошла"
