from pages import *
from setup import *


class TestSuite:

    """
    Тест по сценарию "Поиск вакансий".
    Описывает работу раздела "Поиск вакансий" (заполнение фильтра, выполнение поиска и открытия вакансии)
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

    def test_vacancy_search(self):
        page = VacancySearchPage(self.driver)

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["full_name"])
        page.click_by_text("Поиск вакансий")
        page.click_by_text("Фильтр")
        page.click_by_text("Очистить")
        page.type_source_vacancy("ФОИВ")
        page.name_source_vacancy("Федеральная служба по гидрометеорологии и мониторингу окружающей среды")
        page.name_vacant_position("Руководитель федеральной службы")
        page.type_vacancy("Вакансия для замещения вакантной должности")
        page.substitution_competition("Нет")
        sleep(1)
        page.profile_activity_organization("Другое")
        page.key_word("Руководитель")
        page.click_by_text("Общие сведения")
        page.category_job("Руководители")
        page.group_job("Высшая")
        page.subject_workplace("г. Москва")
        page.region_workplace("Центральный")
        page.salary_from("20000")
        page.salary_to("30000")
        page.business_trip("10% служебного времени")
        page.work_day("5-ти дневная с.н. с 09-00 до 18-00")
        page.type_service_contract("Неважно")
        page.normal_workday("Да")
        page.click_by_text("Прием документов")
        page.day_start_accept_document_from("29.08.2016")
        page.day_stop_accept_document_to("19.09.2016")
        page.click_by_text("Квалификационные требования")
        page.level_education("Высшее образование")
        page.service_experience("Не менее 6 лет")
        page.work_experience_speciality("Не менее 7 лет")
        page.click_by_text("Применить")
        page.click_by_text("Руководитель федеральной службы")
        sleep(5)
        assert "Профиль деятельности организации" in self.driver.page_source
