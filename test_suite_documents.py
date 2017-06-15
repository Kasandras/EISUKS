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

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_doc_documents(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # documents - вкладка "Документы" страницы "Документы"
        documents = DocumentsPage(self.driver).documents
        documents.scroll_to_bottom()
        documents.click_by_text("Документы", 2)
        documents.click_by_text("Документы", 2)
        sleep(2)
        documents.click_by_text("Добавить")
        documents.name_document("Эссе")
        documents.upload_file("C:\\Users\\drozdoviv\\Desktop\\Проверочный.docx")
        documents.click_by_text("Добавить")

    def test_doc_appform_personal_main(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # personal - Раздел "Личные сведения" анкеты, блок "Общие сведения"
        personal = DocumentsPage(self.driver).personal_main
        self.driver.get(Links.appform)
        Browser(self.driver).wait_for_loading()
        # Если анкета присутствует на странице, удаляем и создаём новую, проверяя добавление анкет
        if "Анкета 667" in self.driver.page_source:
            personal.selection_radio()
            personal.click_by_text("Удалить")
            personal.click_by_text("Да")
            personal.click_by_text("Добавить")
        personal.upload_photo("C:\\Users\\drozdoviv\\Desktop\\1.jpg")
        personal.last_name("Дроздов")
        personal.first_name("Илья")
        personal.middle_name("Владимирович")
        personal.gender("Мужской")
        personal.individual_taxpayer_number("6449013711")
        personal.insurance_certificate_number("001-024-567 67")
        personal.birth_date("01061980")
        personal.citizenship("Гражданин Российской Федерации")
        personal.change_citizenship("Нет")
        personal.birthplace("г. Москва")
        personal.wasconvicted("Нет")
        personal.maritalstatuses("Состоит в зарегистрированном браке")
        personal.namewaschanged("Не менял")
        personal.wasabroad("Нет")
        personal.click_by_text("Сохранить")

    def test_doc_appform_personal_contact(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # contact - Раздел "Личные сведения" анкеты, блок "Контакты"
        contact = DocumentsPage(self.driver).personal_contact
        DocumentsPage(self.driver).has_appform()
        if "Загрузить" in self.driver.page_source:
            contact.click_by_text("Редактировать")
        else:
            contact.click_by_text("Редактировать", 2)
        contact.work_phone("9453513517")
        contact.mobile_phone("5435643865")
        contact.additional_phone("4675346743")
        contact.fax("4675346744")
        contact.work_email("kandidat@mail.net")
        contact.personal_email("kandidathome@mail.net")
        contact.web_address("kandidat.com")
        contact.permanent_registration_sub("Алтайский край")
        contact.permanent_registration_reg("Алейский район")
        contact.temp_registration_sub("Алтайский край")
        contact.temp_registration_reg("Алейский район")
        contact.fact_registration_sub("Алтайский край")
        contact.fact_registration_reg("Алейский район")
        contact.click_by_text("Сохранить")

    def test_doc_appform_identification_document(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # identification_document - Раздел "Документы" анкеты
        identification_document = DocumentsPage(self.driver).identification_document
        DocumentsPage(self.driver).has_appform()
        identification_document.click_by_text("Документы, удостоверяющие")
        identification_document.click_by_text("Добавить")
        identification_document.type_document("Паспорт гражданина РФ")
        identification_document.series("2654")
        identification_document.number("132456")
        identification_document.date_issued("15062005")
        identification_document.issue_by("ОВД Замоскворечье")
        identification_document.issue_code("223658")
        identification_document.click_by_text("Сохранить")

    def test_doc_appform_education_main(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # education_main - Раздел "Образование" анкеты, блок "Основное"
        main = DocumentsPage(self.driver).education.main
        DocumentsPage(self.driver).has_appform()
        main.click_by_text("Образование")
        main.click_by_text("Редактировать")
        main.education_level("Высшее образование")
        main.click_by_text("Сохранить")
        main.click_by_text("Добавить")
        main.education("Высшее образование – специалитет")
        main.education_form("Очное")
        main.place_institution("г. Москва")
        main.full_name_institution("Мытищинский институт экономики")
        main.start_date_education("2002")
        main.end_date_education("2007")
        main.education_directions("Экономика и управление")
        main.faculty("Экономика")
        main.education_doc_number("35-ГС")
        main.speciality("080100")
        main.qualification("51 - Экономист")
        main.specialization("Экономика")
        main.is_main("True")
        main.education_doc_date("04072017")
        main.click_by_text("Сохранить")

    def test_doc_appform_education_egc(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # education_egc - Раздел "Образование" анкеты, блок "Послевузовское"
        egc = DocumentsPage(self.driver).education.egc
        DocumentsPage(self.driver).has_appform()
        egc.click_by_text("Образование")
        egc.click_by_text("Добавить", 2)
        egc.education("Аспирантура")
        egc.place("г. Москва")
        egc.name_institution("МАИ")
        egc.start_date("2007")
        egc.academic_degree("Кандидат наук")
        egc.academic_degree_date("20082008")
        egc.end_date("2008")
        egc.knowledge_branches("Экономические науки")
        egc.diplom_number("34358-П")
        egc.diplom_date("20092008")

    def test_doc_appform_education_degree(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # education_degree - Раздел "Образование" анкеты, блок "Ученое звание"
        degree = DocumentsPage(self.driver).education.degree
        DocumentsPage(self.driver).has_appform()
        degree.click_by_text("Образование")
        degree.click_by_text("Добавить", 3)
        degree.academic_statuses("Доцент")
        degree.diplom_number("348-А")
        degree.assigment_date("20092008")

    def test_doc_appform_education_languages(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # education_languages - Раздел "Образование" анкеты, блок "Знание иностранных языков"
        languages = DocumentsPage(self.driver).education.languages
        DocumentsPage(self.driver).has_appform()
        languages.click_by_text("Образование")
        languages.click_by_text("Добавить", 4)
        languages.languages("Немецкий")
        languages.language_degrees("Владеет свободно")
        languages.click_by_text("Сохранить", 4)

    def test_doc_appform_education_dpo(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # education_dpo - Раздел "Образование" анкеты, блок "Дополнительное профессиональное образование"
        dpo = DocumentsPage(self.driver).education.dpo
        DocumentsPage(self.driver).has_appform()
        dpo.click_by_text("Образование")
        dpo.scroll_to_bottom()
        dpo.click_by_text("Добавить", 5)
        dpo.education_direction("Организационно-экономическое")
        dpo.education_kind("Профессиональная переподготовка")
        dpo.kind("Профессиональная переподготовка")
        dpo.name_program("Профессиональное развитие персонала")
        dpo.education_form("Заочное")
        dpo.place("г. Москва")
        dpo.name_institution("МАИ")
        dpo.start_date("2008")
        dpo.end_date("2009")
        dpo.hours("120")
        dpo.document_number("89П6")
        dpo.funding_sources("За счет средств Федерального бюджета")
        dpo.document_date("20092009")

    def test_doc_appform_labor_activity(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # labor_activity - Раздел "Трудовая деятельность" анкеты
        labor_activity = DocumentsPage(self.driver).labor_activity
        DocumentsPage(self.driver).has_appform()
        labor_activity.click_by_text("Трудовая деятельность")
        labor_activity.click_by_text("Добавить")
        labor_activity.start_date("20092009")
        labor_activity.post("Специалист")
        labor_activity.organization("Федеральная Таможенная Служба")
        labor_activity.address_organization("г. Москва")
        labor_activity.employees_number("11 - 100 человек")
        labor_activity.subject("Алтайский край")
        labor_activity.region("Алейский район")
        labor_activity.profile("Текстильное производство")
        labor_activity.is_elective("True")
        labor_activity.post_level("Специалист")
        labor_activity.activity_area("Другое")
        labor_activity.structural_division("Бухгалтерский учет")
        labor_activity.responsibilities("Рассчет заработной платы сотрудников организации")
        labor_activity.click_by_text("Сохранить")

    def test_doc_appform_class_rank(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # class_rank - Раздел "Трудовая деятельность" анкеты, блок классных чинов
        class_rank = DocumentsPage(self.driver).class_rank
        DocumentsPage(self.driver).has_appform()
        class_rank.click_by_text("Трудовая деятельность")
        class_rank.click_by_text("Редактировать", 3)
        sleep(1)
        class_rank.has_class_rank("True")
        class_rank.class_rank("Секретарь государственной гражданской службы Российской Федерации 1 класса")
        sleep(2)
        class_rank.assigned_by("Федеральная Таможенная Служба")
        class_rank.has_government_service("True")
        class_rank.org_sub_types("Городской округ")
        class_rank.organization_name("Федеральная Таможенная Служба")
        class_rank.computer_skills("Продвинутый пользователь")
        class_rank.publications("Отсутствуют")
        class_rank.recommendations("Отсутствуют")
        class_rank.assigned_date("20092009")
        sleep(1)
        self.driver.refresh()
        class_rank.scroll_to_bottom()

    def test_doc_appform_specialization(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # specialization - Раздел "Трудовая деятельность" анкеты, блок специализации
        specialization = DocumentsPage(self.driver).specialization
        DocumentsPage(self.driver).has_appform()
        specialization.click_by_text("Трудовая деятельность")
        specialization.click_by_text("Добавить", 3)
        specialization.scroll_to_bottom()
        sleep(1)
        specialization.specialization("Экономика и финансы")
        specialization.is_main("True")
        specialization.click_by_text("Сохранить", 3)

    def test_doc_appform_award(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # award - Раздел "Поощрения" анкеты
        award = DocumentsPage(self.driver).award
        DocumentsPage(self.driver).has_appform()
        award.click_by_text("Поощрения")
        award.click_by_text("Добавить")
        award.type("благодарность")
        award.name("За заслуги")
        award.date("16042016")
        award.click_by_text("Сохранить")

    def test_doc_appform_state_secret(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # state_secret - Раздел "Допуск к государственной тайне" анкеты
        state_secret = DocumentsPage(self.driver).state_secret
        DocumentsPage(self.driver).has_appform()
        state_secret.click_by_text("Допуск к государственной тайне")
        state_secret.click_by_text("Добавить")
        state_secret.admission_form("Вторая форма")
        state_secret.approval_number("85")
        state_secret.issue_date("11022015")

    def test_doc_appform_military(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # military - Раздел "Воинский учет" анкеты
        military = DocumentsPage(self.driver).military
        DocumentsPage(self.driver).has_appform()
        military.click_by_text("Воинский учет")
        military.click_by_text("Редактировать")
        military.rank("ефрейтор")
        military.duty("Военнообязанный")
        military.has_service("True")
        military.arm_kind("Сухопутные")
        military.service_from("20022000")
        military.service_to("20022001")
        self.driver.refresh()

    def test_doc_appform_kin(self):
        LoginPage(self.driver).login("drozdoviv@quarta.su", "123123/")
        # kin - Раздел "Сведения о близких родственниках" анкеты
        kin = DocumentsPage(self.driver).kin
        DocumentsPage(self.driver).has_appform()
        kin.click_by_text("Сведения о близких родственниках")
        kin.click_by_text("Добавить")
        kin.kin_ship("Сын")
        kin.last_name("Иванов")
        kin.first_name("Илья")
        kin.middle_name("Глебович")
        kin.name_changes("Не менял")
        kin.birth_country("Россия")
        kin.birth_region("г. Москва")
        sleep(1)
        kin.birth_area("Центральный")
        kin.birth_place("г. Москва")
        kin.work_place("Отсутствует")
        kin.living_country("Россия")
        kin.living_address("Москва")
        kin.birth_date("15062009")
