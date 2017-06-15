from pages import *
from setup import *


class TestSuite:

    """""
    Тест по сценарию "Вакансии на контроле".
    Описывает работу раздела "Вакансии на контроле" (направление приглашений на вакансии, 
    принятие и отклонение приглашений, поиск результатов)
    """""

    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_control_vacancy_invite(self):
        control_vacancy_invite = ControlVacancyPage(self.driver)
        LoginPage(self.driver).login("1", "123123/")
        control_vacancy_invite.click_by_text("Формирование кадрового состава")
        control_vacancy_invite.click_by_text("Проведение конкурса на замещение вакантной должности")
        control_vacancy_invite.scroll_to_top()
        control_vacancy_invite.click_by_text("Подбор")
        control_vacancy_invite.table_select_row(1, "Выбор первой вакансии")
        control_vacancy_invite.scroll_to_top()
        control_vacancy_invite.click_by_text("Добавить кандидата")
        control_vacancy_invite.table_select_row(1, "Выбор первого кандидата")
        control_vacancy_invite.scroll_to_top()
        control_vacancy_invite.click_by_text("Направить приглашение")
        control_vacancy_invite.click_by_text("Направить приглашение", 2)
        control_vacancy_invite.scroll_to_top()
        control_vacancy_invite.click_by_text("Подбор")
        control_vacancy_invite.scroll_to_top()
        control_vacancy_invite.click_by_text("Закрыть")
        control_vacancy_invite.table_select_row(2, "Выбор второй вакансии")
        control_vacancy_invite.click_by_text("Добавить кандидата")
        control_vacancy_invite.table_select_row(1, "Выбор кандидата")
        control_vacancy_invite.scroll_to_top()
        control_vacancy_invite.click_by_text("Направить приглашение")
        control_vacancy_invite.click_by_text("Направить приглашение", 2)

    def test_control_vacancy_statuses(self):
        control_vacancy_statuses = ControlVacancyPage(self.driver)
        LoginPage(self.driver).login("l&m", "123123/")
        control_vacancy_statuses.click_by_text("Вакансии на контроле")
        control_vacancy_statuses.click_by_text("Фильтр")
        control_vacancy_statuses.status_response("Направлено приглашение")
        control_vacancy_statuses.click_by_text("Применить")
        control_vacancy_statuses.table_select_row(1, "Выбор приглашения")
        control_vacancy_statuses.click_by_text("Принять приглашение")
        control_vacancy_statuses.click_by_text("Продолжить")
        assert "Ваш отклик успешно завершен." not in self.driver.page_source
        control_vacancy_statuses.click_by_text("Назад")
        control_vacancy_statuses.table_select_row(1, "Выбор приглашения")
        control_vacancy_statuses.click_by_text("Отклонить приглашение")
        control_vacancy_statuses.click_by_text("Фильтр")
        control_vacancy_statuses.select2_clear(ControlVacancyLocators.status_response)
        control_vacancy_statuses.status_response("Отклонил приглашение")
        control_vacancy_statuses.click_by_text("Применить")
        control_vacancy_statuses.wait_for_text_appear("Отклонил приглашение")
        control_vacancy_statuses.click_by_text("Дата события")
        control_vacancy_statuses.click_by_text("Дата события")
        assert control_vacancy_statuses.is_date_vacancy(), "Проверка \"Отклонил приглашение\" не прошла"
        control_vacancy_statuses.click_by_text("Фильтр")
        control_vacancy_statuses.select2_clear(ControlVacancyLocators.status_response)
        control_vacancy_statuses.status_response("Приглашен")
        control_vacancy_statuses.click_by_text("Применить")
        control_vacancy_statuses.wait_for_text_appear("Приглашен")
        control_vacancy_statuses.click_by_text("Дата события")
        control_vacancy_statuses.click_by_text("Дата события")
        assert control_vacancy_statuses.is_date_vacancy(), "Проверка \"Приглашен\" не прошла"
