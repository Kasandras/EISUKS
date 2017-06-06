from pages import *
from setup import *


class TestSuite:

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_search_vacancy(self):
        LoginPage(self.driver).login("1", "123123/")
        search_vacancy = SearchVacancyPage(self.driver)
        search_vacancy.click_by_text("Поиск вакансий")
        search_vacancy.click_by_text("Фильтр")
        search_vacancy.click_by_text("Очистить")
        search_vacancy.type_source_vacancy("ФОИВ")
        search_vacancy.name_source_vacancy("Федеральная служба по гидрометеорологии и мониторингу окружающей среды")
        search_vacancy.name_vacant_position("Руководитель федеральной службы")
        search_vacancy.type_vacancy("Вакансия для замещения вакантной должности")
        search_vacancy.substitution_competition("Нет")
        search_vacancy.profile_activity_organization("Другое")
        search_vacancy.key_word("Руководитель")
        search_vacancy.click_by_text("Общие сведения")
        search_vacancy.category_job("Руководители")
        search_vacancy.group_job("Высшая")
        search_vacancy.subject_workplace("г. Москва")
        search_vacancy.region_workplace("Центральный")
        search_vacancy.salary_from("20000")
        search_vacancy.salary_to("30000")
        search_vacancy.business_trip("10% служебного времени")
        search_vacancy.work_day("5-ти дневная с.н. с 09-00 до 18-00")
        search_vacancy.type_service_contract("Неважно")
        search_vacancy.normal_workday("Да")
        search_vacancy.click_by_text("Прием документов")
        search_vacancy.day_start_accept_document_from("29.08.2016")
        search_vacancy.day_stop_accept_document_to("19.09.2016")
        search_vacancy.click_by_text("Квалификационные требования")
        search_vacancy.level_education("Высшее образование")
        search_vacancy.service_experience("Не менее 6 лет")
        search_vacancy.work_experience_speciality("Не менее 7 лет")
        search_vacancy.click_by_text("Применить")
        search_vacancy.click_by_text("Руководитель федеральной службы")
        sleep(5)
        assert "Профиль деятельности организации" in self.driver.page_source
