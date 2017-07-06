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
        cls.account = get_data_by_number(load_data("drozdovData")["users"], "accounts", 1)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_doc_documents(self):
        """Вкладка "Документы" страницы "Документы" """
        document = get_data_by_number(load_data("drozdovData")["application_form"], "documents")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        page = DocumentsPage(self.driver).documents
        page.scroll_to_bottom()
        page.click_by_text("Документы", 2)
        page.click_by_text("Документы", 2)
        sleep(2)
        page.click_by_text("Добавить")
        page.name_document(document["name_document"])
        page.upload_file(document["upload_file"])
        page.click_by_text("Добавить")

    def test_doc_appform_personal_main(self):
        """Анкеты - раздел "Личные сведения", блок "Общие сведения" """
        personal_main = get_data_by_number(load_data("drozdovData")["application_form"], "personal_main")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        parent(self.driver).go_to(Links.application_form)
        page = DocumentsPage(self.driver).personal_main
        # Если анкета присутствует на странице, удаляем и создаём новую, проверяя добавление анкет
        if "Анкета 667" in self.driver.page_source:
            page.selection_radio()
            page.click_by_text("Удалить")
            page.click_by_text("Да")
            page.click_by_text("Добавить")
        page.upload_photo(personal_main["upload_photo"])
        page.last_name(personal_main["last_name"])
        page.first_name(personal_main["first_name"])
        page.middle_name(personal_main["middle_name"])
        page.gender(personal_main["gender"])
        page.individual_taxpayer_number(personal_main["individual_taxpayer_number"])
        page.insurance_certificate_number(personal_main["insurance_certificate_number"])
        page.birth_date(personal_main["birth_date"])
        page.citizenship(personal_main["citizenship"])
        page.change_citizenship(personal_main["change_citizenship"])
        page.birthplace(personal_main["birthplace"])
        page.was_convicted(personal_main["was_convicted"])
        page.marital_statuses(personal_main["marital_statuses"])
        page.name_was_changed(personal_main["name_was_changed"])
        page.was_abroad(personal_main["was_abroad"])
        page.click_by_text("Сохранить")

    def test_doc_appform_personal_contact(self):
        """Анкеты - раздел "Личные сведения", блок "Контакты" """
        personal_contact = get_data_by_number(load_data("drozdovData")["application_form"], "personal_contact")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).personal_contact
        if "Загрузить" in self.driver.page_source:
            page.click_by_text("Редактировать")
        else:
            page.click_by_text("Редактировать", 2)
        page.work_phone(personal_contact["work_phone"])
        page.mobile_phone(personal_contact["mobile_phone"])
        page.additional_phone(personal_contact["additional_phone"])
        page.fax(personal_contact["fax"])
        page.work_email(personal_contact["work_email"])
        page.personal_email(personal_contact["personal_email"])
        page.web_address(personal_contact["web_address"])
        page.permanent_registration_sub(personal_contact["permanent_registration_sub"])
        page.permanent_registration_reg(personal_contact["permanent_registration_reg"])
        page.temp_registration_sub(personal_contact["temp_registration_sub"])
        page.temp_registration_reg(personal_contact["temp_registration_reg"])
        page.fact_registration_sub(personal_contact["fact_registration_sub"])
        page.fact_registration_reg(personal_contact["fact_registration_reg"])
        page.click_by_text("Сохранить")

    def test_doc_appform_identification_document(self):
        """Анкеты - раздел "Документы" """
        identification_document = get_data_by_number(
            load_data("drozdovData")["application_form"], "identification_document")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).identification_document
        page.click_by_text("Документы, удостоверяющие")
        page.click_by_text("Добавить")
        page.type_document(identification_document["type_document"])
        page.series(identification_document["series"])
        page.number(identification_document["number"])
        page.date_issued(identification_document["date_issued"])
        page.issue_by(identification_document["issue_by"])
        page.issue_code(identification_document["issue_code"])
        page.click_by_text("Сохранить")

    def test_doc_appform_education_main(self):
        """Анкеты - раздел "Образование", блок "Основное" """
        education_main = get_data_by_number(load_data("drozdovData")["application_form"], "education_main")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        page = DocumentsPage(self.driver).education.main
        DocumentsPage(self.driver).has_appform()
        page.click_by_text("Образование")
        page.click_by_text("Редактировать")
        page.education_level(education_main["education_level"])
        page.click_by_text("Сохранить")
        page.click_by_text("Добавить")
        page.education(education_main["education"])
        page.education_form(education_main["education_form"])
        page.place_institution(education_main["place_institution"])
        page.full_name_institution(education_main["full_name_institution"])
        page.start_date_education(education_main["start_date_education"])
        page.end_date_education(education_main["end_date_education"])
        page.education_directions(education_main["education_directions"])
        page.faculty(education_main["faculty"])
        page.education_doc_number(education_main["education_doc_number"])
        page.speciality(education_main["speciality"])
        page.qualification(education_main["qualification"])
        page.specialization(education_main["specialization"])
        page.is_main(education_main["is_main"])
        page.education_doc_date(education_main["education_doc_date"])
        page.click_by_text("Сохранить")

    def test_doc_appform_education_egc(self):
        """Анкеты - раздел "Образование", блок "Послевузовское" """
        education_egc = get_data_by_number(load_data("drozdovData")["application_form"], "education_egc")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.egc
        page.click_by_text("Образование")
        page.click_by_text("Добавить", 2)
        page.wait_for_loading()
        page.education(education_egc["education"])
        page.place(education_egc["place"])
        page.name_institution(education_egc["name_institution"])
        page.start_date(education_egc["start_date"])
        page.academic_degree(education_egc["academic_degree"])
        page.academic_degree_date(education_egc["academic_degree_date"])
        page.end_date(education_egc["end_date"])
        page.knowledge_branches(education_egc["knowledge_branches"])
        page.diplom_number(education_egc["diplom_number"])
        page.diplom_date(education_egc["diplom_date"])

    def test_doc_appform_education_degree(self):
        """Анкеты - раздел "Образование", блок "Ученое звание" """
        education_degree = get_data_by_number(load_data("drozdovData")["application_form"], "education_degree")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.degree
        page.click_by_text("Образование")
        page.click_by_text("Добавить", 3)
        page.academic_statuses(education_degree["academic_statuses"])
        page.diplom_number(education_degree["diplom_number"])
        page.assigment_date(education_degree["assigment_date"])

    def test_doc_appform_education_languages(self):
        """Анкеты - раздел "Образование", блок "Знание иностранных языков" """
        education_languages = get_data_by_number(load_data("drozdovData")["application_form"], "education_languages")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.languages
        page.click_by_text("Образование")
        page.click_by_text("Добавить", 4)
        page.languages(education_languages["languages"])
        page.language_degrees(education_languages["language_degrees"])
        page.click_by_text("Сохранить", 4)

    def test_doc_appform_education_dpo(self):
        """Анкеты - раздел "Образование", блок "Дополнительное профессиональное образование" """
        education_dpo = get_data_by_number(load_data("drozdovData")["application_form"], "education_dpo")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).education.dpo
        page.click_by_text("Образование")
        page.scroll_to_bottom()
        page.click_by_text("Добавить", 5)
        page.wait_for_loading()
        page.education_direction(education_dpo["education_direction"])
        page.education_kind(education_dpo["education_kind"])
        page.kind(education_dpo["kind"])
        page.name_program(education_dpo["name_program"])
        page.education_form(education_dpo["education_form"])
        page.place(education_dpo["place"])
        page.name_institution(education_dpo["name_institution"])
        page.start_date(education_dpo["start_date"])
        page.end_date(education_dpo["end_date"])
        page.hours(education_dpo["hours"])
        page.document_number(education_dpo["document_number"])
        page.funding_sources(education_dpo["funding_sources"])
        page.document_date(education_dpo["document_date"])

    def test_doc_appform_labor_activity(self):
        """Анкеты - раздел "Трудовая деятельность" """
        labor_activity = get_data_by_number(load_data("drozdovData")["application_form"], "labor_activity")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).labor_activity
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Добавить")
        page.start_date(labor_activity["start_date"])
        page.post(labor_activity["post"])
        page.organization(labor_activity["organization"])
        page.address_organization(labor_activity["address_organization"])
        page.employees_number(labor_activity["employees_number"])
        page.subject(labor_activity["subject"])
        page.region(labor_activity["region"])
        page.profile(labor_activity["profile"])
        page.is_elective(labor_activity["is_elective"])
        page.post_level(labor_activity["post_level"])
        page.activity_area(labor_activity["activity_area"])
        page.structural_division(labor_activity["structural_division"])
        page.responsibilities(labor_activity["responsibilities"])
        page.click_by_text("Сохранить")

    def test_doc_appform_class_rank(self):
        """Анкеты - раздел "Трудовая деятельность", блок классных чинов"""
        class_rank = get_data_by_number(load_data("drozdovData")["application_form"], "class_rank")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).class_rank
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Редактировать", 3)
        sleep(1)
        page.has_class_rank(class_rank["has_class_rank"])
        page.class_rank(class_rank["class_rank"])
        sleep(2)
        page.assigned_by(class_rank["assigned_by"])
        page.has_government_service(class_rank["has_government_service"])
        page.org_sub_types(class_rank["org_sub_types"])
        page.organization_name(class_rank["organization_name"])
        page.computer_skills(class_rank["computer_skills"])
        page.publications(class_rank["publications"])
        page.recommendations(class_rank["recommendations"])
        page.assigned_date(class_rank["assigned_date"])
        sleep(1)
        self.driver.refresh()
        page.scroll_to_bottom()

    def test_doc_appform_specialization(self):
        """Анкеты - раздел "Трудовая деятельность" анкеты, блок специализации"""
        specialization = get_data_by_number(load_data("drozdovData")["application_form"], "specialization")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).specialization
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Добавить", 3)
        page.scroll_to_bottom()
        sleep(1)
        page.specialization(specialization["specialization"])
        page.is_main(specialization["is_main"])
        page.click_by_text("Сохранить", 3)

    def test_doc_appform_award(self):
        """Анкеты - раздел "Поощрения" анкеты"""
        award = get_data_by_number(load_data("drozdovData")["application_form"], "award")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).award
        page.click_by_text("Поощрения")
        page.click_by_text("Добавить")
        page.type(award["type"])
        page.name(award["name"])
        page.date(award["date"])
        page.click_by_text("Сохранить")

    def test_doc_appform_state_secret(self):
        """Анкеты - раздел "Допуск к государственной тайне" """
        state_secret = get_data_by_number(load_data("drozdovData")["application_form"], "state_secret")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).state_secret
        page.click_by_text("Допуск к государственной тайне")
        page.click_by_text("Добавить")
        page.admission_form(state_secret["admission_form"])
        page.approval_number(state_secret["approval_number"])
        page.issue_date(state_secret["issue_date"])

    def test_doc_appform_military(self):
        """Анкеты - раздел "Воинский учет" """
        military = get_data_by_number(load_data("drozdovData")["application_form"], "military")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).military
        page.click_by_text("Воинский учет")
        page.click_by_text("Редактировать")
        page.rank(military["rank"])
        page.duty(military["duty"])
        page.has_service(military["has_service"])
        page.arm_kind(military["arm_kind"])
        page.service_from(military["service_from"])
        page.service_to(military["service_to"])
        self.driver.refresh()

    def test_doc_appform_kin(self):
        """Анкеты - раздел "Сведения о близких родственниках" """
        kin = get_data_by_number(load_data("drozdovData")["application_form"], "kin")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        DocumentsPage(self.driver).has_appform()
        page = DocumentsPage(self.driver).kin
        page.click_by_text("Сведения о близких родственниках")
        page.click_by_text("Добавить")
        page.kin_ship(kin["kin_ship"])
        page.last_name(kin["last_name"])
        page.first_name(kin["first_name"])
        page.middle_name(kin["middle_name"])
        page.name_changes(kin["name_changes"])
        page.birth_country(kin["birth_country"])
        page.birth_region(kin["birth_region"])
        sleep(1)
        page.birth_area(kin["birth_area"])
        page.birth_place(kin["birth_place"])
        page.work_place(kin["work_place"])
        page.living_country(kin["living_country"])
        page.living_address(kin["living_address"])
        page.birth_date(kin["birth_date"])
