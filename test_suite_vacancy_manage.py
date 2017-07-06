from pages import *
from setup import *
import pytest


class TestSuite:
    """
    Управление объявлениями
    Публикация, закрытие, отправка в архив объявлений о вакансиях

    Предварительно вакансия создаётся и отправляется на рассмотрение
    """
    driver = webdriver.Chrome("chromedriver.exe")

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.admin = get_data_by_number(load_data("drozdovData")["users"], "accounts", 0)
        cls.account = get_data_by_number(load_data("drozdovData")["users"], "accounts", 1)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    def test_creation_vacancy(self):
        """
        Создание вакансий, которые будут использоваться в управлении объявлениями
        """
        page = VacancyCreatePage(self.driver)
        data = load_data("drozdovData")
        vacancy = data["vacancy"]["type"][0]

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        self.go_to(Links.vacancy_list)
        for i in range(2):
            page.click_by_text("Создать")
            page.type_vacancy(vacancy["type_vacancy"])
            page.organization(vacancy["organization"])
            page.wait_for_text_appear("Структурное подразделение")
            page.is_competition(vacancy["is_competition"])
            sleep(1)
            page.post_is_competition.structural_unit(vacancy["structural_unit"])
            page.post_is_competition.sub_structural(vacancy["sub_structural"])
            page.post_is_competition.staff_unit(vacancy["staff_unit"])
            page.post_is_competition.work_type(vacancy["work_type"])
            page.work_type_other_text(vacancy["work_type_other_text"])
            page.post_is_competition.position_category(vacancy["position_category"])
            page.post_is_competition.position_group(vacancy["position_group"])
            page.post_is_competition.okato_region(vacancy["okato_region"])
            page.post_is_competition.okato_area(vacancy["okato_area"])
            page.salary_from(vacancy["salary_from"])
            page.salary_to(vacancy["salary_to"])
            sleep(1)
            page.post_is_competition.business_trip(vacancy["business_trip"])
            page.post_is_competition.work_day(vacancy["work_day"])
            page.post_is_competition.work_schedule(vacancy["work_schedule"])
            page.post_is_competition.work_contract(vacancy["work_contract"])
            page.social_package_text(vacancy["social_package_text"])
            page.post_is_competition.social_package_files(vacancy["social_package_files"])
            sleep(1)
            page.additional_position_info_text(vacancy["additional_position_info_text"])
            page.post_is_competition.additional_position_info_file(vacancy["additional_position_info_file"])
            page.scroll_to_top()
            page.click_by_text("Должностные обязанности")
            page.job_responsibility_text(vacancy["job_responsibility_text"])
            page.post_is_competition.job_responsibility_files(vacancy["job_responsibility_files"])
            page.post_is_competition.position_rules_files(vacancy["position_rules_files"])
            page.click_by_text("Квалификационные требования")
            page.post_is_competition.education_level(vacancy["education_level"])
            page.post_is_competition.government_experience(vacancy["government_experience"])
            page.post_is_competition.professional_experience(vacancy["professional_experience"])
            page.knowledge_description_text(vacancy["knowledge_description_text"])
            page.post_is_competition.knowledge_description_files(vacancy["knowledge_description_files"])
            page.additional_requirements(vacancy["additional_requirements"])
            page.post_is_competition.test(vacancy["test"])
            page.click_by_text("Документы", 2)
            page.announcement_date()
            page.expiry_date(vacancy["expiry_date"])
            page.registration_address(vacancy["registration_address"])
            page.registration_time(vacancy["registration_time"])
            page.click_by_text("Добавить")
            page.post_is_competition.document_type(vacancy["document_type"])
            page.description(vacancy["description"])
            page.post_is_competition.template_file(vacancy["template_file"])
            sleep(1)
            page.click_by_text("Добавить", 2)
            sleep(1)
            page.set_checkbox_by_order(3, False)
            page.sel()
            page.delete()
            sleep(1)
            page.click_by_text("Контакты")
            page.wait_for_text_appear("Почтовый адрес")
            page.post_is_competition.organization_address(vacancy["organization_address"])
            page.address_mail(vacancy["address_mail"])
            page.phone(vacancy["phone"])
            page.phone2(vacancy["phone2"])
            page.phone3(vacancy["phone3"])
            page.email(vacancy["email"])
            page.contact_person_other(vacancy["contact_person_other"])
            page.web(vacancy["web"])
            page.additional_info_text(vacancy["additional_info_text"])
            sleep(0.5)
            page.post_is_competition.additional_info_files(vacancy["additional_info_files"])
            page.click_by_text("Сохранить")
            page.wait_for_text_appear("Создать")
            assert "Создать" in self.driver.page_source

    def test_publication_vacancy(self):
        """
        Отправка на рассмотрение, публикацию вакансий
        """
        page = VacancyManagePage(self.driver)
        data = load_data("drozdovData")
        manage_vacancy = data["manage_vacancy"]

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        self.go_to(Links.vacancy_list)
        for i in range(2):
            page.click_by_text("Фильтр")
            page.click_by_text("Очистить")
            page.status(manage_vacancy["project"])
            page.type(manage_vacancy["type"])
            page.create_date(today())
            page.click_by_text("Применить")
            page.scroll_to_top()
            page.checkbox()
            page.approve()
            page.wait_for_text_appear("завершена")
            page.click_by_text("Фильтр")
            page.click_by_text("Очистить")
            page.status((manage_vacancy["consideration"]))
            page.click_by_text("Применить")
            page.scroll_to_top()
            page.set_checkbox_by_order(2, True)
            page.publish()
            page.wait_for_text_appear("Публикация")

    def test_manage_vacancy_refine(self):
        """
        Отправка вакансии на доработку
        """
        page = VacancyManagePage(self.driver)
        data = load_data("drozdovData")
        manage_vacancy = data["manage_vacancy"]

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["full_name"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.refine()
        page.comment(manage_vacancy["comment"])
        page.click_by_text("Да")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["refine"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()

    def test_manage_vacancy_publish(self):
        """
        Отправка вакансии на публикацию
        """
        page = VacancyManagePage(self.driver)
        data = load_data("drozdovData")
        manage_vacancy = data["manage_vacancy"]

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["full_name"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["publish"])
        page.create_date(today())
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.published()
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["opened"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()

    def test_manage_vacancy_closed(self):
        """
        Закрытие вакансии
        """
        page = VacancyManagePage(self.driver)
        data = load_data("drozdovData")
        manage_vacancy = data["manage_vacancy"]

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["full_name"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["opened"])
        page.create_date(today())
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.close()
        page.comment(manage_vacancy["comment"])
        page.click_by_text("Да")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["close"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()

    def test_manage_vacancy_archive(self):
        """
        Закрытие вакансии
        """
        page = VacancyManagePage(self.driver)
        data = load_data("drozdovData")
        manage_vacancy = data["manage_vacancy"]

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["full_name"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["close"])
        page.create_date(today())
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.archive()
        page.click_by_text("Да")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(manage_vacancy["archive"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()
