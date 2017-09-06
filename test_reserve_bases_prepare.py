from pages import *
from setup import *
from selenium import webdriver


class TestSuite:
    """
    Подготовка документов для включения в Федеральный резерв управленческих кадров
    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
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

    def test_add_personal_file(self):
        page = ReserveBasesPreparePage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Дроздов")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.reserve_bases_prepare)
        page.click_by_text("Добавить")
        page.personal_file(data["personalFile"])
        page.presentation_reserve_level(data["presentationReserveLevel"])
        page.grade_of_post(data["gradeOfPost"])
        page.click("Сохранить")
        assert "Найдено" in self.driver.page_source

    def test_fill_resume(self):
        page = ReserveBasesPreparePage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Дроздов")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.reserve_bases_prepare)
        page.search(data["search"])
        page.documents()
        page.resume()
        self.driver.switch_to_window(self.driver.window_handles[1])
        page.click_by_text("Редактировать", 1)
        page.upload_file(data["photo"])
        page.last_name(data["lastName"])
        page.first_name(data["firstName"])
        page.middle_name(data["middleName"])
        page.gender(data["gender"])
        page.tax_certificate_number(data["taxCertificateNumber"])
        page.insurance_certificate_number(data["insuranceCertificateNumber"])
        page.birth_date(data["birthDate"])
        page.citizenship(data["citizenship"])
        page.birth_place(data["birthPlace"])
        page.was_convicted(data["wasConvicted"])
        page.marital_statuses(data["maritalStatuses"])
        page.name_was_changed(data["nameWasChanged"])
        page.click_by_text("Сохранить")
        page.click_by_text("Редактировать", 2)
        page.work_phone(data["workPhone"])
        page.mobile_phone(data["mobilePhone"])
        page.additional_phone(data["additionalPhone"])
        page.residence_phone(data["residencePhone"])
        page.fax(data["fax"])
        page.work_email(data["workEmail"])
        page.personal_email(data["personalEmail"])
        page.web(data["web"])
        page.registration_region(data["registrationRegion"])
        page.registration_area(data["registrationArea"])
        page.residence_region(data["residenceRegion"])
        page.residence_area(data["residenceArea"])
        page.click_by_text("Сохранить")
        page.scroll_to_top()
        page.click_by_text("Образование")
        page.click_by_text("Редактировать")
        page.education_level(data["educationLevel"])
        page.click_by_text("Сохранить")
        page.click_by_text("Добавить")
        page.education_kinds(data["educationKinds"])
        page.education_forms(data["educationForms"])
        page.place(data["place"])
        page.temp_institution(data["tempInstitution"])
        page.start_date(data["startDate"])
        page.end_date(data["endDate"])
        page.faculty(data["faculty"])
        page.education_doc_number(data["educationDocNumber"])
        page.speciality(data["speciality"])
        page.qualification(data["qualification"])
        page.specialization(data["specialization"])
        page.click_by_text("Сохранить")
        page.scroll_to_top()
        page.click_by_text("Трудовая деятельность")
        page.click_by_text("Добавить")
        page.begin_date(data["beginDate"])
        page.end_date(data["stopDate"])
        page.organization(data["organization"])
        page.address_organization(data["addressOrganization"])
        page.structural_division(data["structuralDivision"])
        page.post(data["post"])
        page.post_levels(data["postLevels"])
        page.employees_numbers(data["employeesNumbers"])
        page.profile(data["profile"])
        page.professional_activity_area(data["professionalActivityArea"])
        page.responsibilities(data["responsibilities"])
        page.click_by_text("Сохранить")
        page.scroll_to_top()
        page.click_by_text("Дополнительная информация")
        page.click_by_text("Редактировать")
        page.job_types(data["jobTypes"])
        page.expectations(data["expectations"])
        page.organization_sub_type(data["organizationSubType"])
        page.organization(data["organization_"])
        page.organization_other(data["organizationOther"])
        page.ready_to_move(data["readyToMove"])
        page.salary_from(data["salaryFrom"])
        page.salary_to(data["salaryTo"])
        page.computer_skills(data["computerSkills"])
        page.publications(data["publications"])
        page.recommendations(data["recommendations"])
        page.additional_info(data["additionalInfo"])
        page.agree_to_process_data(data["agreeToProcessData"])
        page.click_by_text("Сохранить")
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def test_fill_presentation(self):
        page = ReserveBasesPreparePage(self.driver, 3)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Дроздов")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.reserve_bases_prepare)
        page.search(data["search"])
        page.documents()
        page.presentation()
        self.driver.switch_to_window(self.driver.window_handles[1])
        page.availability_degree(data["availabilityDegree"])
        page.position(data["position"])
        page.recomendations(data["recomendations"])
        page.professional_achievements(data["professionalAchievements"])
        page.developement_area(data["developementArea"])
        page.additional_preperation_text(data["additionalPreperationText"])
        page.click_by_text("Сохранить")
        page.wait_for_loading()
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def test_send_resume(self):
        page = ReserveBasesPreparePage(self.driver)

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        self.go_to(Links.reserve_bases_prepare)
        page.set_checkbox_by_order()
        page.click_by_text("Направить на рассмотрение")
        assert "Отправлено" in self.driver.page_source
