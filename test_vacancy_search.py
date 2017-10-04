from pages import *
from setup import *


class TestSuite:

    """
    Тест по сценарию "Поиск вакансий".
    Описывает работу раздела "Поиск вакансий" (заполнение фильтра, выполнение поиска и открытия вакансии)
    """

    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.admin = get_data_by_number(load_data("gossluzhba1"), "accounts", 1)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_vacancy_search(self):
        page = VacancySearchPage(self.driver)

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["fullName"])
        page.scroll_to_bottom()
        page.click_by_text("Поиск вакансий")
        page.click_by_text("Фильтр")
        page.click_by_text("Очистить")
        page.type_source_vacancy("ФОИВ")
        page.name_source_vacancy("Министерство природных ресурсов и экологии Российской Федерации")
        page.name_vacant_position("Директор департамента")
        page.type_vacancy("Вакансия для замещения вакантной должности")
        page.substitution_competition("Нет")
        page.electronic_documents("Да")
        sleep(1)
        page.profile_activity_organization("Другое")
        page.key_word("Директор")
        page.click_by_text("Общие сведения")
        page.category_job("Руководители")
        page.group_job("Высшая")
        page.subject_workplace("г. Москва")
        sleep(1)
        page.region_workplace("Центральный")
        page.salary_from("20000")
        page.salary_to("30000")
        page.business_trip("10% служебного времени")
        page.work_day("5-ти дневная с.н. с 09-00 до 18-00")
        page.type_service_contract("Неважно")
        page.normal_workday("Да")
        page.click_by_text("Прием документов")
        page.day_start_accept_document_from("29.08.2017")
        page.day_stop_accept_document_to("19.09.2018")
        page.click_by_text("Квалификационные требования")
        page.level_education("Высшее образование")
        page.service_experience("Не менее 6 лет")
        page.work_experience_speciality("Не менее 7 лет")
        page.click_by_text("Применить")
        page.click_by_text("Директор департамента")
        page.wait_for_text_appear("Код вакансии")
        assert "Профиль деятельности организации" in self.driver.page_source
