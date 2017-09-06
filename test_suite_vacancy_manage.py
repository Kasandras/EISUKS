from pages import *
from setup import *


class TestSuite:
    """
    Управление объявлениями
    Публикация, закрытие, отправка в архив объявлений о вакансиях

    Предварительно вакансия создаётся и отправляется на рассмотрение
    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.admin = get_data_by_number(load_data("gossluzhba1"), "accounts", 1)
        cls.account = get_data_by_number(load_data("gossluzhba1"), "accounts", 3)

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
        data = load_data("gossluzhba1")["advertisements"][1]

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.vacancy_list)
        for i in range(2):
            page.click_by_text("Создать")
            page.type_vacancy(data["type_vacancy"])
            page.organization(data["organization"])
            page.wait_for_text_appear("Структурное подразделение")
            page.is_competition(data["is_competition"])
            sleep(1)
            page.post_is_competition.structural_unit(data["structural_unit"])
            page.post_is_competition.sub_structural(data["sub_structural"])
            page.post_is_competition.staff_unit(data["staff_unit"])
            page.post_is_competition.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.post_is_competition.position_category(data["position_category"])
            page.post_is_competition.position_group(data["position_group"])
            page.post_is_competition.okato_region(data["okato_region"])
            page.post_is_competition.okato_area(data["okato_area"])
            page.salary_from(data["salary_from"])
            page.salary_to(data["salary_to"])
            sleep(1)
            page.post_is_competition.business_trip(data["business_trip"])
            page.post_is_competition.work_day(data["work_day"])
            page.post_is_competition.work_schedule(data["work_schedule"])
            page.post_is_competition.work_contract(data["work_contract"])
            page.social_package_text(data["social_package_text"])
            page.post_is_competition.social_package_files(data["social_package_files"])
            sleep(1)
            page.additional_position_info_text(data["additional_position_info_text"])
            page.post_is_competition.additional_position_info_file(data["additional_position_info_file"])
            page.scroll_to_top()
            page.click_by_text("Должностные обязанности")
            page.job_responsibility_text(data["job_responsibility_text"])
            page.post_is_competition.job_responsibility_files(data["job_responsibility_files"])
            page.post_is_competition.position_rules_files(data["position_rules_files"])
            page.click_by_text("Квалификационные требования")
            page.post_is_competition.education_level(data["education_level"])
            page.post_is_competition.government_experience(data["government_experience"])
            page.post_is_competition.professional_experience(data["professional_experience"])
            page.knowledge_description_text(data["knowledge_description_text"])
            page.post_is_competition.knowledge_description_files(data["knowledge_description_files"])
            page.additional_requirements(data["additional_requirements"])
            page.post_is_competition.test(data["test"])
            page.click_by_text("Документы", 2)
            page.announcement_date()
            page.expiry_date(data["expiry_date"])
            page.registration_address(data["registration_address"])
            page.registration_time(data["registration_time"])
            page.click_by_text("Добавить")
            page.post_is_competition.document_type(data["document_type"])
            page.description(data["description"])
            page.post_is_competition.template_file(data["template_file"])
            sleep(1)
            page.click_by_text("Добавить", 2)
            sleep(1)
            page.set_checkbox_by_order(4, False)
            page.sel()
            page.delete()
            sleep(1)
            page.click_by_text("Контакты")
            page.wait_for_text_appear("Почтовый адрес")
            page.post_is_competition.organization_address(data["organization_address"])
            page.address_mail(data["address_mail"])
            page.phone(data["phone"])
            page.phone2(data["phone2"])
            page.phone3(data["phone3"])
            page.email(data["email"])
            page.contact_person_other(data["contact_person_other"])
            page.web(data["web"])
            page.additional_info_text(data["additional_info_text"])
            sleep(0.5)
            page.post_is_competition.additional_info_files(data["additional_info_files"])
            page.click_by_text("Сохранить")
            page.wait_for_text_appear("Создать")
            assert "Создать" in self.driver.page_source

    def test_publication_vacancy(self):
        """
        Отправка на рассмотрение, публикацию вакансий
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.vacancy_list)
        for i in range(2):
            page.click_by_text("Фильтр")
            page.click_by_text("Очистить")
            page.status(data["project"])
            page.type(data["type"])
            page.create_date(today())
            page.click_by_text("Применить")
            page.scroll_to_top()
            page.checkbox()
            page.approve()
            page.wait_for_text_appear("завершена")
            page.click_by_text("Фильтр")
            page.click_by_text("Очистить")
            page.status((data["consideration"]))
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
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["fullName"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.refine()
        page.comment(data["comment"])
        page.click_by_text("Да")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["refine"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()

    def test_manage_vacancy_publish(self):
        """
        Отправка вакансии на публикацию
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["fullName"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["publish"])
        page.create_date(today())
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.published()
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["opened"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()

    def test_manage_vacancy_closed(self):
        """
        Закрытие вакансии
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["fullName"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["opened"])
        page.create_date(today())
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.close()
        page.comment(data["comment"])
        page.click_by_text("Да")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["close"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()

    def test_manage_vacancy_archive(self):
        """
        Закрытие вакансии
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(self.admin["username"], self.admin["password"], self.admin["fullName"])
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["close"])
        page.create_date(today())
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.set_checkbox_by_order(2, True)
        page.archive()
        page.click_by_text("Да")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.status(data["archive"])
        page.create_date(today())
        page.click_by_text("Применить")
        assert page.is_date_vacancy()
