# -*- coding: utf-8 -*-

from pages import *
import pytest


class TestSuite:
    """
    Содержание test-suite:
        Учет кадрового состава - Ведение электронных личных дел
        Организационно-штатная структура - Формирование организационно-штатной структуры
        Формирование кадрового состава - Назначение на должность
        Прохождение государственной гражданской службы - Присвоение классных чинов
        Прохождение государственной гражданской службы - Отпуска на государственной гражданской службе
        Прохождение государственной гражданской службы - График отпусков
        Прохождение государственной гражданской службы - Командировки
        Прохождение государственной гражданской службы - График служебных командировок
        Прохождение государственной гражданской службы - Учет периодов нетрудоспособности
        Прохождение государственной гражданской службы - Планирование диспансеризации
        Прохождение государственной гражданской службы - Диспансеризация
        Прохождение государственной гражданской службы - Дисциплинарные взыскания
        Прохождение государственной гражданской службы - Поощрения
        Формирование кадрового состава - Проведение конкурса на замещение вакантной должности
        Формирование кадрового состава - Комиссии
        Формирование кадрового состава - Денежное содержание
        Формирование кадрового состава - Увольнение с гражданской службы, расторжение контракта
        Справочники и классификаторы - 004 - Разделы реестра должностей
        Справочники и классификаторы - Организации
        Управление пользователями
        Управление ролями
        Список прав
    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.hr = get_data_by_number(cls.data, "accounts", 0)
        cls.admin = get_data_by_number(cls.data, "accounts", 1)
        cls.user = get_data_by_number(cls.data, "accounts", 2)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    @pytest.mark.parametrize("last_name", ["Автоматизация"])
    def test_new_personal_file(self, last_name):
        """
        Учет кадрового состава - Ведение электронных личных дел
        """
        data = get_data_by_value(self.data, "employees", "lastName", last_name)

        LoginPage(self.driver).login(data=self.hr)
        self.go_to(Links.personal_files)
        page = PersonalFilePage(self.driver)
        page.click_by_text("Добавить")
        page.new.last_name(data["lastName"])
        page.new.first_name(data["firstName"])
        page.new.middle_name(data["middleName"])
        page.new.birthday(data["birthday"])
        page.new.insurance_certificate_number(data["insuranceCertificateNumber"])
        page.new.username(data["username"])
        page.new.click_by_text("Сохранить")
        page.wait_for_text_appear("Личные сведения")
        page.general.general_edit()
        page.general.last_name(data["lastName"])
        page.general.first_name(data["firstName"])
        page.general.middle_name(data["middleName"])
        page.general.personal_file_number(data["personalFileNumber"])
        page.general.birthday(data["birthday"])
        page.general.okato(data["okato"])
        page.general.criminal_record(data["criminalRecord"])
        page.general.last_name_changing(data["lastNameChanging"])
        page.general.gender(data["gender"])
        page.general.click_by_text("Сохранить")
        assert page.wait_for_text_disappear("Сохранить")

    def test_new_department(self):
        """
        Организационно-штатная структура - Формирование организационно-штатной структуры
        """
        data = get_data_by_number(self.data, "departments")

        LoginPage(self.driver).login(data=self.hr)
        self.go_to(Links.staff_structure)
        page = StructureInfoPage(self.driver)
        page.wait_for_text_appear("Структура")
        page.click_by_text("Добавить")
        page.organization(data["organization"])
        page.name(data["name"])
        page.fot(data["fot"])
        page.limit(data["limit"])
        page.click_by_text("Сохранить")
        page.click_by_text(data["name"])
        for division in data["divisions"]:
            StructureDetailsPage(self.driver).forming()
            if division["parent"]:
                element = page.wait_for_element_appear((By.XPATH, "//tr[contains(., '%s')]" % division["parent"]))
                element.find_element(By.XPATH, ".//input[@type='checkbox']").click()
            page.click_by_text("Добавить")
            page = DepartmentPage(self.driver)
            page.name(division["name"])
            page.name_genitive(division["nameGenitive"])
            page.name_dative(division["nameDative"])
            page.name_accusative(division["nameAccusative"])
            page.limit(division["limit"])
            page.code(division["code"])
            page.launch_date(division["launchDate"])
            page.order_number(division["orderNumber"])
            page.order_date(division["orderDate"])
            page.click_by_text("Штатная численность")
            for staff in division["staffAmount"]:
                page.position(staff["position"])
                page.amount(staff["amount"])
                page.click_by_text("Добавить", 2)
            page.click_by_text("Сохранить")
        page = StructureDetailsPage(self.driver)
        page.launch()
        page.order_number(data["orderNumber"])
        page.order_date(data["orderDate"])
        page.launch_date(data["date"])
        page.click_by_text("Ввести в действие")
        self.go_to(Links.staff_structure)
        page = StructureDetailsPage(self.driver)
        page.click_by_text(data["name"])
        page.click_by_text("Показать все")
        page.wait_for_text_appear("Назначить")
        assert page.projects_check(), "Ошибка: На странице присутствует ярлык \"Проект\""

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_appointment(self, user):
        """
        Формирование кадрового состава - Назначение на должность
        """
        department = get_data_by_number(self.data, "departments")
        data = get_data_by_value(self.data, "employees", "lastName", user)["appointment"]

        LoginPage(self.driver).login(data=self.hr)
        page = StructureDetailsPage(self.driver)
        self.go_to(Links.staff_structure)
        page.click_by_text(department["name"])
        page.arrangement()
        page.department_select(department["divisions"][0]["name"])
        page.click_by_text("Назначить")

        page = AppointmentPage(self.driver)
        page.full_name(user)
        page.reason(data["reason"])
        page.duration(data["duration"])
        page.date_from(data["dateFrom"])
        page.trial(data["trial"])
        page.contract_date(data["contractDate"])
        page.contract_number(data["contractNumber"])
        page.click_by_text("Сохранить")
        sleep(10)
        self.go_to(Links.appointment)
        OrdersPage(self.driver).submit(user, data=data)
        self.go_to(Links.staff_structure)
        page = StructureDetailsPage(self.driver)
        page.click_by_text(department["name"])
        page.arrangement()
        page.department_select(department["divisions"][0]["name"])
        page.wait_for_text_appear("Создать")

    # тесты Головинского
    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_ranks(self, user):
        """
        Прохождение государственной гражданской службы - Присвоение классных чинов
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["ranks"]

        LoginPage(self.driver).login(data=self.hr)

        page = RanksPage(self.driver)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Сведения о чинах и званиях")
        page.scroll_to_top()
        page.click_by_text("Добавить")
        page.set_select("Проект приказа на присвоение классного чина")
        page.condition(data["condition"])
        page.type(data["type"])
        page.organization(data["organization"])
        page.date(data["date"])
        page.click_by_text("Сохранить")

        self.go_to(Links.ranks)
        OrdersPage(self.driver).submit(user, data=data)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Сведения о чинах и званиях")
        page.scroll_to_top()

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_holidays(self, user):
        """
        Прохождение государственной гражданской службы - Отпуска на государственной гражданской службе
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["holidays"]

        LoginPage(self.driver).login(data=self.hr)
        page = HolidaysPage(self.driver)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Отпуска")
        page.scroll_to_top()
        page.click_by_text("Добавить")

        page.statement_date(data["statementDate"])
        page.base(data["base"])
        page.type(data["type"])
        page.date_from(data["dateFrom"])
        page.count_days(data["countDays"])
        page.is_pay_once(data["isPayOnce"])
        page.is_material_aid(data["isMaterialAid"])
        page.click_by_text("Расчет")
        page.click_by_text("Сохранить")
        page.accept_alert()

        self.go_to(Links.holidays)
        OrdersPage(self.driver).submit(user, data=data)

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_holidays_schedule(self, user):
        """
        Прохождение государственной гражданской службы - График отпусков
        """
        LoginPage(self.driver).login(data=self.hr)
        page = HolidaysPage(self.driver)
        self.go_to(Links.holidays_schedule)
        page.click_by_text("Включить режим редактирования")
        page.set_select("2017")
        page.click((By.XPATH, "//span[@class='custom-icon-close']"))
        page.click((By.XPATH, "//span[@class='custom-icon-close']"))
        page.click_by_text("Добавить")
        page.set_date((By.XPATH, "(//input[@type='text'])[1]"), today(), "Дата с")
        page.set_text((By.XPATH, "(//input[@type='text'])[2]"), "14", "Количество дней")
        page.click_by_text("Сохранить")
        page.click_by_text(user)
        page.scroll_to_top()
        page.table_row_radio(2)
        page.click_by_text("Редактировать")
        page.statement_date(today())
        page.base("Заявление")
        page.type("ежегодный отпуск")
        page.date_from(today())
        page.count_days("14")
        page.is_pay_once(True)
        page.is_material_aid(True)
        page.click_by_text("Расчет")
        page.click_by_text("Сохранить")
        page.accept_alert()

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_business_trip(self, user):
        """
        Прохождение государственной гражданской службы - Командировки
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["businessTrips"]

        LoginPage(self.driver).login(data=self.hr)
        page = BusinessTripPage(self.driver)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Командировки")
        page.scroll_to_top()
        page.click_by_text("Добавить")
        page.date_start(data["dateStart"])
        page.date_end(data["dateEnd"])
        page.days_amount_without_road(data["daysAmountWithoutRoad"])
        page.source_financing(data["sourceFinancing"])
        page.purpose(data["purpose"])
        page.reason(data["reason"])
        page.route(data["route"])
        page.task_number(data["taskNumber"])
        page.task_date(data["taskDate"])
        page.click_by_text("Добавить", 2)
        page.routes.country(data["routeCountry"])
        page.routes.organization(data["routeOrganization"])
        page.routes.days_amount(data["routeDaysAmount"])
        page.routes.date_start(data["routeDateStart"])
        page.routes.date_end(data["routeDateEnd"])
        page.routes.submit()
        page.scroll_to_top()
        page.submit()
        self.go_to(Links.business_trips)
        OrdersPage(self.driver).submit_business_trips(user, data=data)

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_business_trip_schedule(self, user):
        """
        Прохождение государственной гражданской службы - График служебных командировок
        """
        LoginPage(self.driver).login(data=self.hr)
        page = BusinessTripPage(self.driver)
        self.go_to(Links.business_trips_index)
        page.click_by_text("Фильтр")
        page.set_text((By.XPATH, "(//input[@type='text'])[3]"), user, "ФИО")
        page.click_by_text("Применить")
        assert user in self.driver.page_source

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_disability_periods(self, user):
        """
        Прохождение государственной гражданской службы - Учет периодов нетрудоспособности
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["disabilityPeriods"]

        LoginPage(self.driver).login(data=self.hr)
        page = DisabilityPeriodsPage(self.driver)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Листки нетрудоспособности")
        page.scroll_to_top()

        page.click_by_text("Добавить")
        page.list_number(data["listNumber"])
        page.by(data["by"])
        page.period_from(data["periodFrom"])
        page.period_to(data["periodTo"])
        page.reason(data["reason"])
        page.submit()

        self.go_to(Links.dashboard)
        page.click_by_text("Прохождение государственной гражданской службы")
        page.click_by_text("Учет периодов нетрудоспособности")
        page.click_by_text("Фильтр")
        page.set_text((By.XPATH, "(//input[@type='text'])[8]"), data["listNumber"], "Номер листа")
        page.click_by_text("Применить")
        page.table_row_radio()
        page.click_by_text("Редактировать")
        page.editing.reason(data["reasonFix"])
        page.editing.submit()
        page.wait_for_text_appear("Фильтр")
        assert data["reasonFix"] in self.driver.page_source

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_dispensary_planning(self, user):
        """
        Прохождение государственной гражданской службы - Планирование диспансеризации
        """
        LoginPage(self.driver).login(data=self.hr)
        page = DispensaryPlanningPage(self.driver)
        self.go_to(Links.dispensary_planning)
        page.table_select_user(user)
        page.click_by_text("Включить в диспансеризацию")
        page.date_from(today())
        page.date_to(today())
        page.submit()

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_dispensary(self, user):
        """
        Прохождение государственной гражданской службы - Диспансеризация
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["dispensary"]

        LoginPage(self.driver).login(data=self.hr)
        page = DispensaryPage(self.driver)
        self.go_to(Links.dispensary_list)
        page.click_by_text("Проект")

        page.click_by_text("Печать приказа о диспансеризации")

        page.table_row_checkbox()
        page.click_by_text("Редактировать")
        page.dispensary_date(data["dispensaryDate"])
        page.reference_date(data["referenceDate"])
        page.reference_number(data["referenceNumber"])
        page.is_healthy(data["isHealthy"])
        page.click_by_text("Сохранить")
        page.click_by_text("Назад")

        page.table_row_checkbox()
        page.click_by_text("Редактировать")
        page.dispensary_date(data["dispensaryDate"])
        page.reference_date(data["referenceDate"])
        page.reference_number(data["referenceNumberFix"])
        page.is_healthy(False)
        page.click_by_text("Сохранить")
        page.click_by_text("Назад")

        page.table_row_checkbox()
        page.scroll_to_top()
        page.click_by_text("Формирование приказа об увольнении")
        self.driver.back()
        page.click_by_text("Назад")

        page.table_row_radio()
        page.click_by_text("Редактировать")
        page.date_from(data["dateFrom"])
        page.date_to(data["dateTo"])
        page.order_date(data["orderDate"])
        page.order_number(data["orderNumber"])
        page.institution(data["institution"])
        page.by(user)
        page.click_by_text("Сохранить")
        sleep(1)

        page.table_row_radio()
        page.click_by_text("Редактировать")
        page.click_by_text("Утвердить")

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_enforcements(self, user):
        """
        Прохождение государственной гражданской службы - Дисциплинарные взыскания
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["enforcements"]

        LoginPage(self.driver).login(data=self.hr)
        page = EnforcementPage(self.driver)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Взыскания")
        page.scroll_to_top()
        page.click_by_text("Добавить")

        page.reason(data["reason"])
        page.order_number(data["number"])
        page.order_date(data["date"])
        page.period_from(data["periodFrom"])
        page.period_to(data["periodTo"])
        page.action_date(data["actionDate"])
        page.action(data["action"])
        page.explanatory_date(data["explanatoryDate"])
        page.enforcement_reason(data["enforcementReason"])
        page.type(data["type"])
        page.copy_date(data["copyDate"])
        page.enforcement_date(data["enforcementDate"])
        page.click_by_text("Сохранить")

        self.go_to(Links.enforcement)
        OrdersPage(self.driver).submit(user, data=data)

        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Взыскания")
        page.scroll_to_top()
        page.table_row_radio()
        page.click_by_text("Редактировать")

        page.enforcement_expire_auto(data["enforcementExpireAuto"])
        page.enforcement_expire_date(data["enforcementExpireDate"])
        page.enforcement_expire_reason(data["enforcementExpireReason"])
        page.enforcement_expire_order_date(data["enforcementExpireOrderDate"])
        page.enforcement_expire_order_number(data["enforcementExpireOrderNumber"])
        page.click_by_text("Сохранить")

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_rewards(self, user):
        """
        Прохождение государственной гражданской службы - Поощрения
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["rewards"]

        LoginPage(self.driver).login(data=self.hr)
        page = AwardsPage(self.driver)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Награды и поощрения")

        page.scroll_to_top()
        page.click_by_text("Добавить")
        page.awards.type(data["awardsType"])
        page.awards.name(data["awardsName"])
        page.awards.date(data["awardsDate"])
        page.awards.amount(data["awardsAmount"])
        page.awards.unit(data["awardsUnit"])
        page.awards.note(data["awardsNote"])
        page.awards.should_be(data["awardsShouldBe"])
        page.awards.submit()

        page.scroll_to_top()
        page.click_by_text("Добавить", 2)
        page.state_awards.type(data["stateAwardsType"])
        page.state_awards.name(data["stateAwardsName"])
        page.state_awards.list_date(data["stateAwardsListDate"])
        page.state_awards.date(data["stateAwardsDate"])
        page.state_awards.order_number(data["stateAwardsOrderNumber"])
        page.state_awards.order_date(data["stateAwardsOrderDate"])
        page.state_awards.award_number(data["stateAwardsNumber"])
        page.state_awards.certificate_number(data["stateAwardsCertificateNumber"])
        page.state_awards.awarding_date(data["stateAwardsAwardingDate"])
        page.state_awards.note(data["stateAwardsNote"])
        page.state_awards.submit()

        page.scroll_to_top()
        page.click_by_text("Добавить", 3)
        page.department_awards.type(data["departmentAwardsType"])
        page.department_awards.name(data["departmentAwardsName"])
        page.department_awards.order_number(data["departmentAwardsOrderNumber"])
        page.department_awards.order_date(data["departmentAwardsOrderDate"])
        page.department_awards.award_number(data["departmentAwardsAwardNumber"])
        page.department_awards.certificate_number(data["departmentAwardsCertificateNumber"])
        page.department_awards.awarding_date(data["departmentAwardsAwardingDate"])
        page.department_awards.note(data["departmentAwardsNote"])
        page.department_awards.submit()

        self.go_to(Links.awards)
        OrdersPage(self.driver).submit(user, data=data)
        self.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Награды и поощрения")
    # end

    def tes1t_contest_replacement(self):
        """
        Формирование кадрового состава - Комиссии
        """
        structure_details_page = StructureDetailsPage(self.driver)
        page = AdvertisementPage(self.driver)
        vacancy_list_page = VacancyListPage(self.driver)

        department = get_data_by_number(load_data("testData"), "departments")
        advertisement = get_data_by_number(load_data("testData"), "advertisements")

        LoginPage(self.driver).login(data=self.hr)
        self.go_to(Links.staff_structure)
        structure_details_page.click_by_text(department["name"])
        structure_details_page.arrangement()
        structure_details_page.click_by_text("Показать все")
        structure_details_page.click_by_text("Создать", 2)
        # Основная информация
        page.type(advertisement["type"])
        page.organization(advertisement["organization"])
        page.is_competition(advertisement["isCompetition"])
        page.reason(advertisement["reason"])
        page.division(advertisement["division"])
        page.subdivision(advertisement["subdivision"])
        page.position(advertisement["position"])
        # Общие сведения
        page.profile(advertisement["profile"])
        page.okato_region(advertisement["okatoRegion"])
        page.okato_area(advertisement["okatoArea"])
        page.salary_from(advertisement["salaryFrom"])
        page.salary_to(advertisement["salaryTo"])
        page.buiseness_trip(advertisement["buisnessTrip"])
        page.work_schedule(advertisement["workSchedule"])
        page.is_fixed_schedule(advertisement["isFixedSchedule"])
        page.work_contract(advertisement["workContract"])
        page.guarantee(advertisement["guarantee"])
        page.additional_info(advertisement["additionalInfo"])
        # Должностные обязанности
        page.click_by_text("Должностные обязанности")
        page.job_responsibility(advertisement["jobResponsibility"])
        # Квалификационные требования
        page.click_by_text("Квалификационные требования")
        page.requirements(advertisement["requirements"])
        page.experience(advertisement["experience"])
        page.work_experience(advertisement["workExperience"])
        page.knowledge_description(advertisement["knowledgeDescription"])
        page.additional_requirements(advertisement["additionalRequirements"])
        # Документы
        page.click_by_text("Документы", 2)
        page.registration_address(advertisement["registrationAddress"])
        page.registration_time(advertisement["registrationTime"])
        page.expiry_date(change_date(21))
        page.announcement_date(today())
        # Контакты
        page.click_by_text("Контакты")
        page.post_index(advertisement["postIndex"])
        page.address_mail(advertisement["addressMail"])
        page.phone_1(advertisement["phone1"])
        page.phone_2(advertisement["phone2"])
        page.phone_3(advertisement["phone3"])
        page.email(advertisement["email"])
        page.person(advertisement["person"])
        page.site(advertisement["site"])
        page.additional(advertisement["additional"])
        page.click_by_text("Сохранить")
        #
        self.go_to(Links.vacancy_list)
        vacancy_list_page.check()
        vacancy_list_page.click_by_text("На рассмотрение")
        vacancy_list_page.check(2)
        vacancy_list_page.click_by_text("На публикацию")

        LoginPage(self.driver).login("1", "123123/")
        page.click_by_text("Управление объявлениями")
        vacancy_list_page.check(2)
        page.click_by_text("Опубликовать")
        LoginPage(self.driver).login("l&m", "123123/")
        self.go_to(Links.main_page)
        sleep(300)
        page.click_by_text("Вакансии")
        page.set_text((By.XPATH, "(//input[@type='text'])[2]"), "Automation")
        page.click((By.XPATH, "//li[.='Automation']"))
        page.click_by_text("Поиск")
        page.click((By.XPATH, "//div[@class='vacancy-block vacancy-hovered' and contains(., 'Automation')]"))
        page.click_by_text("Откликнуться")
        page.click_by_text("Продолжить")
        page.set_select("Анкета 667-р 20.07.2015")
        page.click_by_text("Откликнуться")

        LoginPage(self.driver).login(self.hr["username"], self.hr["password"])
        self.go_to(Links.vacancy_selection)
        page.click((By.XPATH, "//a[@data-ng-bind='item.responsesCount']"))
        page.click_by_text("Лобода Максим Юрьевич")
        self.driver.back()
        vacancy_list_page.check()
        page.click_by_text("Пригласить")
        page.click_by_text("Направить приглашение")

    def test_commissions(self):
        """
        Формирование кадрового состава - Комиссии
        """
        page = CommissionsPage(self.driver)
        data = get_data_by_number(self.data, "commissions")

        LoginPage(self.driver).login(data=self.hr)
        self.go_to(Links.commissions)
        page.click_by_text("Добавить")
        page.name(data["name"])
        page.organization(data["organization"])
        page.order_date(today())
        page.order_number(data["orderNumber"])
        page.full_name(data["fullName"])
        page.type(data["type"])
        page.start_date(today())
        page.end_date(change_date(3))
        page.click_by_text("Сохранить")
        page.table_row_checkbox()
        page.click_by_text("Редактировать")
        for member in data["members"]:
            page.members.click_by_text("Добавить")
            page.members.role(member["role"])
            page.members.full_name(member["fullName"])
            page.members.is_independent_expert(member["isIndependentExpert"])
            page.members.organization(member["organization"])
            page.members.position(member["position"])
            page.members.department(member["department"])
            page.members.phone(member["phone"])
            page.members.email(member["email"])
            page.members.personal_file_number(member["personalFileNumber"])
            page.members.click_by_text("Сохранить")
        for session in data["sessions"]:
            page.sessions.click_by_text("Добавить", 2)
            page.sessions.scroll_to_top()
            page.sessions.meeting_time(session["meeting_time"])
            page.sessions.place(session["place"])
            page.sessions.meeting_date(today())
            page.sessions.click_by_text("Сохранить")
            page.sessions.questions_amount()
            for question in session["questions"]:
                page.sessions.click_by_text("Добавить")
                page.sessions.content(question["content"])
                page.sessions.reporter(question["reporter"])
                page.sessions.click_by_text("Сохранить")
                page.sessions.table_row_checkbox()
                page.sessions.click_by_text("Вынести решение")
                page.sessions.decision(question["decision"])
                page.sessions.decision_reason(question["decisionReason"])
                page.sessions.click_by_text("Сохранить")
                page.sessions.click_by_text("Назад")
        page.click_by_text("Назад")
        page.wait_for_text_appear("Вид комиссии")
        page.table_row_checkbox()
        page.scroll_to_top()
        page.click_by_text("Экспорт")
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        page.wait_for_text_appear("Операция успешно выполнена")
        self.go_to(Links.independent_experts)
        assert page.wait_for_text_appear(data["members"][0]["fullName"])

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_salary_payments(self, user):
        """
        Формирование кадрового состава - Денежное содержание
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["salaryPayment"]

        LoginPage(self.driver).login(data=self.hr)
        page = SalaryPaymentsPage(self.driver)
        self.go_to(Links.personal_files)
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Денежное содержание")
        page.click_by_text("Добавить")
        page.type(data["type"])
        page.amount(data["amount"])
        page.date_from(data["dateFrom"])
        page.click_by_text("Сохранить")
        page.wait_for_text_disappear("Сохранить")
        page.table_row_radio()
        page.click_by_text("Редактировать")
        page.amount(data["amountFix"])
        page.click_by_text("Сохранить")
        page.table_row_radio()
        page.click_by_text("Удалить")
        page.click_by_text("Да")
        page.click_by_text("Добавить")
        page.type(data["type"])
        page.amount(data["amount"])
        page.date_from(data["dateFrom"])
        page.click_by_text("Сохранить")
        self.go_to(Links.salary_payments)
        OrdersPage(self.driver).submit(user, data=data)
        self.go_to(Links.personal_files)
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Денежное содержание")
        assert "Проект" not in self.driver.page_source

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_dismissal(self, user):
        """
        Формирование кадрового состава - Увольнение с гражданской службы, расторжение контракта
        """
        department = get_data_by_number(self.data, "departments")
        data = get_data_by_value(self.data, "employees", "lastName", user)["dismissal"]

        LoginPage(self.driver).login(data=self.hr)
        page = PersonalFileDismissalPage(self.driver)
        self.go_to(Links.personal_files)
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Сведения о назначении и освобождении от должности")
        page.check()
        page.click_by_text("Освободить")
        page.scroll_to_top()
        page = DismissalPage(self.driver)
        page.date(data["date"])
        page.reason(data["reason"])
        page.click_by_text("Сохранить")
        self.go_to(Links.dismissal)
        OrdersPage(self.driver).submit(user, data=data)
        self.go_to(Links.staff_structure)
        page = StructureDetailsPage(self.driver)
        page.click_by_text(department["name"])
        page.arrangement()
        page.click_by_text("Показать все")

    def test_organizations(self):
        """
        Справочники и классификаторы - Организации
        """
        data = get_data_by_number(self.data, "organizations")

        LoginPage(self.driver).login(data=self.admin)

        page = OrganizationsPage(self.driver)
        page.click_by_text("Справочники и классификаторы")
        page.click_by_text("Организации")
        page.filter.name("Федеральная таможенная служба")
        page.filter.click_by_text("Поиск")
        page.click((By.XPATH, "//a[@title='Редактировать']"), "")
        page.click_by_text("Отмена")
        page.scroll_to_top()
        page.click_by_text("Добавить организацию")

        page.new.code(data["code"])
        page.new.name(data["name"])
        page.new.name_genitive(data["nameGenitive"])
        page.new.name_dative(data["nameDative"])
        page.new.name_accusative(data["nameAccusative"])
        page.new.short_name(data["shortName"])
        page.new.source_type(data["sourceType"])
        page.new.region(data["region"])
        page.new.area(data["area"])
        page.new.profile(data["profile"])
        page.new.code_okogu(data["codeOKOGU"])
        page.new.code_okpo(data["codeOKPO"])
        page.new.limit(data["limit"])
        page.new.positions_registry(data["positionsRegistry"])
        page.new.site(data["site"])
        page.new.contacts(data["contacts"])
        page.new.participate_in_rotation(data["participateInRotation"])
        page.new.is_expired(data["isExpired"])
        page.new.for_public_open_part(data["forPublicOpenPart"])
        page.new.creation_order_number(data["creationOrderNumber"])
        page.new.creation_order_date(data["creationOrderDate"])
        page.new.creation_date(data["creationDate"])
        page.new.click_by_text("Сохранить")

        page.filter.status("Проект")
        page.filter.name(data["name"])
        page.filter.click_by_text("Поиск")
        page.edit.open()
        page.click_by_text("Ввести в действие")
        page.scroll_to_top()

        page.edit.click_by_text("Направления деятельности и функции")
        for direction in data["directions"]:
            page.edit.activity.click_by_text("Добавить")
            page.edit.activity.direction(direction["type"])
            page.edit.activity.click_by_text("Сохранить")

        page.edit.click_by_text("Должности")
        for position in data["positions"]:
            page.edit.positions.click_by_text("Добавить")
            page.edit.positions.filter(position["filter"])
            page.edit.positions.position(position["position"])
            page.edit.positions.holiday_for_irregular_day(position["holidayForIrregularDay"])
            page.edit.positions.code(position["code"])
            page.edit.positions.name(position["name"])
            page.edit.positions.short_name(position["shortName"])
            page.edit.positions.name_genitive(position["nameGenitive"])
            page.edit.positions.name_dative(position["nameDative"])
            page.edit.positions.name_accusative(position["nameAccusative"])
            page.edit.positions.name_instrumental(position["nameInstrumental"])
            page.edit.positions.can_be_rotated(position["canBeRotated"])
            page.edit.positions.submit_information_on_the_income(position["submitInformation"])
            page.edit.positions.click_by_text("Сохранить")

        page.edit.click_by_text("Курирующий государственный орган")
        page.edit.curator.applications(data["curator"])
        page.edit.curator.click_by_text("Сохранить")

        page.edit.click_by_text("Шаблон вакансии")
        page.edit.template.region(data["templateRegion"])
        page.edit.template.area(data["templateArea"])
        page.edit.template.business_trips(data["templateBusinessTrips"])
        page.edit.template.working_days(data["templateWorkingDays"])
        page.edit.template.working_schedule(data["templateWorkingSchedule"])
        page.edit.template.type(data["templateType"])
        page.edit.template.location(data["templateLocation"])
        page.edit.template.time(data["templateTime"])
        page.edit.template.post_index(data["templatePostIndex"])
        page.edit.template.web_site(data["templateWebSite"])
        page.edit.template.click_by_text("Сохранить")
        page.edit.template.wait_for_text_appear("Данные успешно сохранены")

        page.edit.click_by_text("К списку справочников")
        page.click_by_text("Организации")
        page.filter.status("Действующий")
        page.filter.name(data["name"])
        page.filter.click_by_text("Поиск")
        page.edit.open()
        page.edit.attributes.abolition_order_number(data["abolitionOrderNumber"])
        page.edit.attributes.abolition_order_date(data["abolitionOrderDate"])
        page.edit.attributes.abolition_date(data["abolitionDate"])
        page.edit.attributes.click_by_text("Упразднить")
        page.edit.attributes.click_by_text("Сохранить")

    def test_users_management(self):
        """
        Управление пользователями
        """
        LoginPage(self.driver).login(data=self.admin)

        page = MainPage(self.driver)
        page.click_by_text("Управление пользователями")
        page.search("Иван")
        page.table_row_checkbox()
        page.click_by_text("Управление ролями")
        page.click_by_value("Добавить")
        page.set_checkbox((By.XPATH, "//li[contains(., 'Кадровая служба')]//input"), True, "Кадрова служба")
        page.set_text((By.XPATH, "//input[@type='text']"), "Федеральная таможенная служба", "Организация")
        page.click((By.XPATH, "//div[@role='option']"))
        page.click_by_value("Далее")
        page.wait_for_text_appear("Кадровая служба")
        page.click_by_value("Удалить")
        page.set_checkbox_by_order(3)
        page.set_checkbox_by_order(4)
        page.click_by_value("Далее")

    def test_roles_management(self):
        """
        Управление ролями
        """
        data = get_data_by_number(self.data, "roles")

        LoginPage(self.driver).login(data=self.admin)

        page = RolesManagementPage(self.driver, 3)
        page.click_by_text("Управление ролями")
        page.search(data["name"]+Keys.RETURN)
        while True:
            try:
                page.table_row_radio()
                page.click_by_text("Удалить")
                page.click_by_text("Да")
            except (ec.NoSuchElementException, TimeoutException):
                break
        page.click_by_text("Добавить")
        page.name(data["name"])
        page.is_require_organization(data["isRequireOrganization"])
        page.level(data["level"])
        page.click_by_text("Сохранить")
        page.search(data["name"])

    def test_rules_list(self):
        """
        Список прав
        """
        LoginPage(self.driver).login(data=self.admin)

        page = MainPage(self.driver)
        page.click_by_text("Список прав")
        assert "Список прав системы безопасности" in self.driver.page_source
