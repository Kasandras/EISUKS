from pages import *
from setup import *


class TestSuite:

    """""
    Тест по сценарию "Документы".
    Описывает работу раздела "Документы" (добавление документов, добавление и заполнение анкет)
    """""

    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1.qtestweb.office.quarta-vk.ru")["application_form"]
        cls.account = get_data_by_number(load_data("gossluzhba1.qtestweb.office.quarta-vk.ru"), "accounts", 3)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_doc_documents(self):
        """Вкладка "Документы" страницы "Документы" """
        data = get_data_by_value(self.data, "documents", "name_document", "Анкета регионального резерва")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        page = DocumentsPage(self.driver).documents
        page.scroll_to_bottom()
        page.click_by_text("Документы", 2)
        page.click_by_text("Документы", 2)
        sleep(2)
        page.click_by_text("Добавить")
        page.name_document(data["name_document"])
        page.upload_file(data["upload_file"])
        page.click_by_text("Добавить")

    def test_doc_appform_personal_main(self):
        """Анкеты - раздел "Личные сведения", блок "Общие сведения" """
        data = get_data_by_value(self.data, "personal_main", "upload_photo", "photo_male.jpg")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        parent(self.driver).go_to(Links.application_form)
        page = DocumentsPage(self.driver).personal_main
        # Если анкета присутствует на странице, удаляем и создаём новую, проверяя добавление анкет
        if "Анкета 667" in self.driver.page_source:
            page.selection_radio()
            page.click_by_text("Удалить")
            page.click_by_text("Да")
            page.click_by_text("Добавить")
        page.upload_photo(data["upload_photo"])
        page.last_name(data["last_name"])
        page.first_name(data["first_name"])
        page.middle_name(data["middle_name"])
        page.gender(data["gender"])
        page.individual_taxpayer_number(data["individual_taxpayer_number"])
        page.insurance_certificate_number(data["insurance_certificate_number"])
        page.birth_date(data["birth_date"])
        page.citizenship(data["citizenship"])
        page.change_citizenship(data["change_citizenship"])
        page.birthplace(data["birthplace"])
        page.was_convicted(data["was_convicted"])
        page.marital_statuses(data["marital_statuses"])
        page.name_was_changed(data["name_was_changed"])
        page.was_abroad(data["was_abroad"])
        page.click_by_text("Сохранить")

    def test_doc_appform_personal_contact(self):
        """Анкеты - раздел "Личные сведения", блок "Контакты" """
        data = get_data_by_value(self.data, "personal_contact", "work_phone", "9453513517")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).personal_contact
        if "Загрузить" in self.driver.page_source:
            page.click_by_text("Редактировать")
        else:
            page.click_by_text("Редактировать", 2)
        page.work_phone(data["work_phone"])
        page.mobile_phone(data["mobile_phone"])
        page.additional_phone(data["additional_phone"])
        page.fax(data["fax"])
        page.work_email(data["work_email"])
        page.personal_email(data["personal_email"])
        page.web_address(data["web_address"])
        page.permanent_registration_sub(data["permanent_registration_sub"])
        page.permanent_registration_reg(data["permanent_registration_reg"])
        page.temp_registration_sub(data["temp_registration_sub"])
        page.temp_registration_reg(data["temp_registration_reg"])
        page.fact_registration_sub(data["fact_registration_sub"])
        page.fact_registration_reg(data["fact_registration_reg"])
        page.click_by_text("Сохранить")

    def test_doc_appform_identification_document(self):
        """Анкеты - раздел "Документы" """
        data = get_data_by_value(self.data, "identification_document", "type_document", "Паспорт гражданина РФ")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).identification_document
        page.click_by_text("Документы, удостоверяющие")
        page.click_by_text("Добавить")
        page.type_document(data["type_document"])
        page.series(data["series"])
        page.number(data["number"])
        page.date_issued(data["date_issued"])
        page.issue_by(data["issue_by"])
        page.issue_code(data["issue_code"])
        page.click_by_text("Сохранить")

    def test_doc_appform_education_main(self):
        """Анкеты - раздел "Образование", блок "Основное" """
        data = get_data_by_value(self.data, "education_main", "education_level", "Высшее образование")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        page = DocumentsPage(self.driver).education.main
        DocumentsPage(self.driver).has_appform()
        page.click_by_text("Образование")
        page.click_by_text("Редактировать")
        page.education_level(data["education_level"])
        page.click_by_text("Сохранить")
        page.click_by_text("Добавить")
        page.education(data["education"])
        page.education_form(data["education_form"])
        page.place_institution(data["place_institution"])
        page.full_name_institution(data["full_name_institution"])
        page.start_date_education(data["start_date_education"])
        page.end_date_education(data["end_date_education"])
        page.education_directions(data["education_directions"])
        page.faculty(data["faculty"])
        page.education_doc_number(data["education_doc_number"])
        page.speciality(data["speciality"])
        page.qualification(data["qualification"])
        page.specialization(data["specialization"])
        page.is_main(data["is_main"])
        page.education_doc_date(data["education_doc_date"])
        page.click_by_text("Сохранить")

    def test_doc_appform_education_egc(self):
        """Анкеты - раздел "Образование", блок "Послевузовское" """
        data = get_data_by_value(self.data, "education_egc", "education", "Аспирантура")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.egc
        page.click_by_text("Образование")
        page.click_by_text("Добавить", 2)
        page.wait_for_loading()
        page.education(data["education"])
        page.place(data["place"])
        page.name_institution(data["name_institution"])
        page.start_date(data["start_date"])
        page.academic_degree(data["academic_degree"])
        page.academic_degree_date(data["academic_degree_date"])
        page.end_date(data["end_date"])
        page.knowledge_branches(data["knowledge_branches"])
        page.diplom_number(data["diplom_number"])
        page.diplom_date(data["diplom_date"])

    def test_doc_appform_education_degree(self):
        """Анкеты - раздел "Образование", блок "Ученое звание" """
        data = get_data_by_value(self.data, "education_degree", "academic_statuses", "Доцент")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.degree
        page.click_by_text("Образование")
        page.click_by_text("Добавить", 3)
        page.academic_statuses(data["academic_statuses"])
        page.diplom_number(data["diplom_number"])
        page.assigment_date(data["assigment_date"])

    def test_doc_appform_education_languages(self):
        """Анкеты - раздел "Образование", блок "Знание иностранных языков" """
        data = get_data_by_value(self.data, "education_languages", "languages", "Немецкий")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.languages
        page.click_by_text("Образование")
        page.click_by_text("Добавить", 4)
        page.languages(data["languages"])
        page.language_degrees(data["language_degrees"])
        page.click_by_text("Сохранить", 4)

    def test_doc_appform_education_dpo(self):
        """Анкеты - раздел "Образование", блок "Дополнительное профессиональное образование" """
        data = get_data_by_value(self.data, "education_dpo", "education_direction", "Организационно-экономическое")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.dpo
        page.click_by_text("Образование")
        page.scroll_to_bottom()
        page.click_by_text("Добавить", 5)
        page.wait_for_loading()
        page.education_direction(data["education_direction"])
        page.education_kind(data["education_kind"])
        page.kind(data["kind"])
        page.name_program(data["name_program"])
        page.education_form(data["education_form"])
        page.place(data["place"])
        page.name_institution(data["name_institution"])
        page.start_date(data["start_date"])
        page.end_date(data["end_date"])
        page.hours(data["hours"])
        page.document_number(data["document_number"])
        page.funding_sources(data["funding_sources"])
        page.document_date(data["document_date"])

    def test_doc_appform_labor_activity(self):
        """Анкеты - раздел "Трудовая деятельность" """
        data = get_data_by_value(self.data, "labor_activity", "start_date", "20092009")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).labor_activity
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Добавить")
        page.start_date(data["start_date"])
        page.post(data["post"])
        page.organization(data["organization"])
        page.address_organization(data["address_organization"])
        page.employees_number(data["employees_number"])
        page.subject(data["subject"])
        page.region(data["region"])
        page.profile(data["profile"])
        page.is_elective(data["is_elective"])
        page.post_level(data["post_level"])
        page.activity_area(data["activity_area"])
        page.structural_division(data["structural_division"])
        page.responsibilities(data["responsibilities"])
        page.click_by_text("Сохранить")

    def test_doc_appform_class_rank(self):
        """Анкеты - раздел "Трудовая деятельность", блок классных чинов"""
        data = get_data_by_value(self.data, "class_rank", "has_class_rank", "True")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).class_rank
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Редактировать", 3)
        sleep(1)
        page.has_class_rank(data["has_class_rank"])
        page.class_rank(data["class_rank"])
        sleep(2)
        page.assigned_by(data["assigned_by"])
        page.has_government_service(data["has_government_service"])
        page.org_sub_types(data["org_sub_types"])
        page.organization_name(data["organization_name"])
        page.computer_skills(data["computer_skills"])
        page.publications(data["publications"])
        page.recommendations(data["recommendations"])
        page.assigned_date(data["assigned_date"])
        sleep(1)
        self.driver.refresh()
        page.scroll_to_bottom()

    def test_doc_appform_specialization(self):
        """Анкеты - раздел "Трудовая деятельность" анкеты, блок специализации"""
        data = get_data_by_value(self.data, "specialization", "specialization", "Экономика и финансы")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).specialization
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Добавить", 3)
        page.scroll_to_bottom()
        sleep(1)
        page.specialization(data["specialization"])
        page.is_main(data["is_main"])
        page.click_by_text("Сохранить", 3)

    def test_doc_appform_award(self):
        """Анкеты - раздел "Поощрения" анкеты"""
        data = get_data_by_value(self.data, "award", "type", "благодарность")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).award
        page.click_by_text("Поощрения")
        page.click_by_text("Добавить")
        page.type(data["type"])
        page.name(data["name"])
        page.date(data["date"])
        page.click_by_text("Сохранить")

    def test_doc_appform_state_secret(self):
        """Анкеты - раздел "Допуск к государственной тайне" """
        data = get_data_by_value(self.data, "state_secret", "admission_form", "Вторая форма")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).state_secret
        page.click_by_text("Допуск к государственной тайне")
        page.click_by_text("Добавить")
        page.admission_form(data["admission_form"])
        page.approval_number(data["approval_number"])
        page.issue_date(data["issue_date"])

    def test_doc_appform_military(self):
        """Анкеты - раздел "Воинский учет" """
        data = get_data_by_value(self.data, "military", "rank", "ефрейтор")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).military
        page.click_by_text("Воинский учет")
        page.click_by_text("Редактировать")
        page.rank(data["rank"])
        page.duty(data["duty"])
        page.has_service(data["has_service"])
        page.arm_kind(data["arm_kind"])
        page.service_from(data["service_from"])
        page.service_to(data["service_to"])
        self.driver.refresh()

    def test_doc_appform_kin(self):
        """Анкеты - раздел "Сведения о близких родственниках" """
        data = get_data_by_value(self.data, "kin", "kin_ship", "Сын")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).kin
        page.click_by_text("Сведения о близких родственниках")
        page.click_by_text("Добавить")
        page.kin_ship(data["kin_ship"])
        page.last_name(data["last_name"])
        page.first_name(data["first_name"])
        page.middle_name(data["middle_name"])
        page.name_changes(data["name_changes"])
        page.birth_country(data["birth_country"])
        page.birth_region(data["birth_region"])
        sleep(1)
        page.birth_area(data["birth_area"])
        page.birth_place(data["birth_place"])
        page.work_place(data["work_place"])
        page.living_country(data["living_country"])
        page.living_address(data["living_address"])
        page.birth_date(data["birth_date"])
