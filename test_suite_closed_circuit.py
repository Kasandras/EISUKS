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
        Профиль
        Управление базами резерва
        Подготовка документов для включения во ФРУК
        Просмотр участников ФРУК
        Документы
        Вакансии на контроле
        Создание вакансий
        Управление объявлениями
        Поиск вакансий
    """
    driver = webdriver.Chrome(path_to_driver)

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.hr = get_data_by_number(cls.data, "accounts", 0)
        cls.admin = get_data_by_number(cls.data, "accounts", 1)
        cls.user = get_data_by_number(cls.data, "accounts", 2)
        cls.hr2 = get_data_by_number(cls.data, "accounts", 3)
        cls.user2 = get_data_by_number(cls.data, "accounts", 4)
        # execute_script(Queries.delete_from_fruk)
        # execute_script(Queries.delete_personal_file)
        # execute_script(Queries.delete_all_dispensary_by_account)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("last_name", ["Автоматизация"])
    def test_new_personal_file(self, last_name):
        """
        Учет кадрового состава - Ведение электронных личных дел
        """
        data = get_data_by_value(self.data, "employees", "lastName", last_name)

        LoginPage(self.driver).login(data=self.hr)
        page = PersonalFilePage(self.driver)
        page.go_to(Links.personal_files)
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
        page.general.okato(data["birthPlace"])
        page.general.criminal_record(data["wasConvicted"])
        page.general.last_name_changing(data["nameWasChanged"])
        page.general.gender(data["gender"])
        page.general.click_by_text("Сохранить")
        assert page.wait_for_text_disappear("Сохранить")

    def test_new_department(self):
        """
        Организационно-штатная структура - Формирование организационно-штатной структуры
        """
        data = get_data_by_number(self.data, "departments")

        LoginPage(self.driver).login(data=self.hr)

        page = StructureInfoPage(self.driver)
        page.go_to(Links.staff_structure)
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
        page.go_to(Links.staff_structure)
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
        page = StructureDetailsPage(self.driver, timeout=60)
        page.go_to(Links.staff_structure)
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
        page.go_to(Links.appointment)
        OrdersPage(self.driver).submit(user, data=data)
        page.go_to(Links.staff_structure)
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
        page.go_to(Links.personal_files)
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

        page.go_to(Links.ranks)
        OrdersPage(self.driver).submit(user, data=data)
        page.go_to(Links.personal_files)
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
        page.go_to(Links.personal_files)
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
        page.scroll_to_top()
        page.click_by_text("Сохранить")
        page.accept_alert()

        page.go_to(Links.holidays)
        OrdersPage(self.driver).submit(user, data=data)

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_holidays_schedule(self, user):
        """
        Прохождение государственной гражданской службы - График отпусков
        """
        LoginPage(self.driver).login(data=self.hr)
        page = HolidaysPage(self.driver)
        page.go_to(Links.holidays_schedule)
        page.click_by_text("Включить режим редактирования")
        page.set_select("2018")
        page.click((By.XPATH, "//span[@class='custom-icon-close']"))
        page.click((By.XPATH, "//span[@class='custom-icon-close']"))
        page.click_by_text("Добавить")
        page.set_date((By.XPATH, "(//input[@type='text'])[1]"), "28.11.2018", "Дата с")
        page.set_text((By.XPATH, "(//input[@type='text'])[2]"), "14", "Количество дней")
        page.click_by_text("Сохранить")
        page.click_by_text(user)
        page.scroll_to_top()
        page.table_row_radio(2)
        page.click_by_text("Редактировать")
        page.statement_date("28.11.2018")
        page.base("Заявление")
        page.type("ежегодный отпуск")
        page.date_from("28.11.2018")
        page.count_days("14")
        page.is_pay_once(True)
        page.is_material_aid(True)
        page.scroll_to_bottom()
        page.click_by_text("Расчет")
        page.click_by_text("Сохранить", 2)
        page.accept_alert()

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_business_trip(self, user):
        """
        Прохождение государственной гражданской службы - Командировки
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["businessTrips"]

        LoginPage(self.driver).login(data=self.hr)
        page = BusinessTripPage(self.driver)
        page.go_to(Links.personal_files)
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
        page.go_to(Links.business_trips)
        OrdersPage(self.driver).submit_business_trips(user, data=data)

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_business_trip_schedule(self, user):
        """
        Прохождение государственной гражданской службы - График служебных командировок
        """
        LoginPage(self.driver).login(data=self.hr)
        page = BusinessTripPage(self.driver)
        page.go_to(Links.business_trips_index)
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
        page.go_to(Links.personal_files)
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

        page.go_to(Links.dashboard)
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
        page.go_to(Links.dispensary_planning)
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
        page.go_to(Links.dispensary_list)
        page.click_by_text("Проект")
        page.select_last_project()

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

        page.table_row_radio_by_text("Проект")
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
        page.go_to(Links.personal_files)
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

        page.go_to(Links.enforcement)
        OrdersPage(self.driver).submit(user, data=data)

        page.go_to(Links.personal_files)
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
        page.go_to(Links.personal_files)
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

        page.go_to(Links.awards)
        OrdersPage(self.driver).submit(user, data=data)
        page.go_to(Links.personal_files)
        page.click_by_text("Назначенные")
        page.search(user)
        page.click_by_text(user)
        page.click_by_text("Награды и поощрения")
    # end

    @pytest.mark.skip(reason="currently not working")
    def test_contest_replacement(self):
        """
        Формирование кадрового состава - Комиссии
        """
        structure_details_page = StructureDetailsPage(self.driver)
        page = AdvertisementPage(self.driver)
        vacancy_list_page = VacancyListPage(self.driver)

        department = get_data_by_number(load_data("testData"), "departments")
        advertisement = get_data_by_number(load_data("testData"), "advertisements")

        LoginPage(self.driver).login(data=self.hr)
        page.go_to(Links.staff_structure)
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
        page.go_to(Links.vacancy_list)
        vacancy_list_page.check()
        vacancy_list_page.click_by_text("На рассмотрение")
        vacancy_list_page.check(2)
        vacancy_list_page.click_by_text("На публикацию")

        LoginPage(self.driver).login("1", "123123/")
        page.click_by_text("Управление объявлениями")
        vacancy_list_page.check(2)
        page.click_by_text("Опубликовать")
        LoginPage(self.driver).login("l&m", "123123/")
        page.go_to(Links.main_page)
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
        page.go_to(Links.vacancy_selection)
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
        page.go_to(Links.commissions)
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
        page.go_to(Links.independent_experts)
        assert page.wait_for_text_appear(data["members"][0]["fullName"])

    @pytest.mark.parametrize("user", ['Автоматизация'])
    def test_salary_payments(self, user):
        """
        Формирование кадрового состава - Денежное содержание
        """
        data = get_data_by_value(self.data, "employees", "lastName", user)["salaryPayment"]

        LoginPage(self.driver).login(data=self.hr)
        page = SalaryPaymentsPage(self.driver)
        page.go_to(Links.personal_files)
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
        page.go_to(Links.salary_payments)
        OrdersPage(self.driver).submit(user, data=data)
        page.go_to(Links.personal_files)
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
        page.go_to(Links.personal_files)
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
        page.go_to(Links.dismissal)
        OrdersPage(self.driver).submit(user, data=data)
        page.go_to(Links.staff_structure)
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
        page.set_checkbox_by_order(1)
        page.set_checkbox_by_order(2)
        page.click_by_value("Далее")

    def test_roles_management(self):
        """
        Управление ролями
        """
        data = get_data_by_number(self.data, "roles")

        LoginPage(self.driver).login(data=self.admin)

        page = RolesManagementPage(self.driver, 3)
        page.click_by_text("Управление ролями")
        page.search(data["name"])
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

    def test_rules_list(self):
        """
        Список прав
        """
        LoginPage(self.driver).login(data=self.admin)

        page = MainPage(self.driver)
        page.click_by_text("Список прав")
        assert "Список прав системы безопасности" in self.driver.page_source

    def test_profile(self):
        """
        Профиль (тестирование раздела "Профиль")
        """
        page = ProfilePage(self.driver)
        data = get_data_by_value(self.data, "members", "upload_photo", "photo_male.jpg")

        LoginPage(self.driver).login(data=self.hr)
        page.click_by_text("Профиль", 2)
        page.scroll_to_top()
        page.click_by_text("Редактировать")
        page.upload_photo(data["upload_photo"])
        page.last_name(data["lastName"])
        page.first_name(data["firstName"])
        page.middle_name(data["middleName"])
        page.birth_date(data["birthDate"])
        page.insurance_certificate_number(data["insurance_certificate_number"])
        page.individual_taxpayer_number(data["individual_taxpayer_number"])
        page.email(data["email"])
        page.passport_info(data['passport_info'])
        page.registration_address(data["registration_address"])
        page.actual_address(data["actual_address"])
        page.click_by_text("Сохранить")
        page.scroll_to_top()
        page.click_by_text("Изменить пароль")
        page.old_password(data["old_password"])
        page.password(data["password"])
        page.password_confirm(data["password_confirm"])
        page.change()
        assert "Пароль изменен" in self.driver.page_source

    def test_manage_reserve_bases(self):
        """
        Управление базами резерва
        """
        page = ManageReserveBasesPage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_manage", "code", "999")

        LoginPage(self.driver).login(data=self.admin)
        page.go_to(Links.manage_reserve_bases)
        page.click_by_text("Добавить")
        page.code(data["code"])
        page.name(data["name"])
        page.set_checkbox_by_order(1, True)
        page.click_by_text("Сохранить")
        page.wait_for_text_appear("Статус")
        page.edit()
        page.set_checkbox_by_order(1, False)
        page.click_by_text("Сохранить")
        page.wait_for_text_appear("Статус")
        assert data["code"] in self.driver.page_source
        page.delete()
        page.edit_base()
        page.set_checkbox_by_order()
        page.click_by_text("Сохранить")

    def test_add_personal_file(self):
        """
        Подготовка документов для включения в Федеральный резерв управленческих кадров
        Добавление новой записи
        """
        page = ReserveBasesPreparePage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Авто")

        LoginPage(self.driver).login(data=self.hr)
        page.go_to(Links.reserve_bases_prepare)
        page.click_by_text("Добавить")
        page.personal_file(data["personalFile"])
        page.presentation_reserve_level(data["presentationReserveLevel"])
        page.grade_of_post(data["gradeOfPost"])
        page.save()
        page.wait_for_text_disappear("Категория резерва")

    def test_fill_resume(self):
        """
        Подготовка документов для включения в Федеральный резерв управленческих кадров
        Заполнение резюме
        """
        page = ReserveBasesPreparePage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Авто")

        LoginPage(self.driver).login(data=self.hr)
        page.go_to(Links.reserve_bases_prepare)
        page.search(data["search"])
        page.documents()
        page.resume()
        page.tab_switch(1)

        # Заполнение раздела "Общие сведения"
        page.click_by_text("Редактировать", 1)
        page.upload_photo(data["photo"])
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

        # Заполнение раздела Контактная информация
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
        page.wait.text_disappear("Сохранить")
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
        page.stop_date(data["stopDate"])
        sleep(0.5)
        page.organization_work(data["organization_work"])
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
        page.organization(data["organization"])
        page.organization_other(data["organizationOther"])
        page.ready_to_move(data["readyToMove"])
        page.salary_from(data["salaryFrom"])
        page.salary_to(data["salaryTo"])
        page.computer_skills(data["computerSkills"])
        page.publications(data["publications"])
        page.recommendations(data["recommendations"])
        page.additional_info(data["additionalInfo"])
        page.agree_to_process_data(data["agreeToProcessData"])
        page.click_by_text("Сохранить", 2)
        page.tab_close()
        page.tab_switch(0)

    def test_fill_presentation(self):
        """
        Подготовка документов для включения в Федеральный резерв управленческих кадров
        Заполнение представления
        """
        page = PresentationPage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Авто")

        LoginPage(self.driver).login(data=self.hr)
        page.go_to(Links.presentation_page)
        page.position(data["position"])
        page.availability_degree(data["availabilityDegree"])
        page.positions(data["positions"])
        page.recommendations(data["presentationRecommendations"])
        page.professional_achievements(data["professionalAchievements"])
        page.development_area(data["developmentArea"])
        page.additional_preparation(data["additionalPreparation"])
        page.submit()
        page.wait.text_disappear("Сохранить")

    def test_send_resume(self):
        """
        Подготовка документов для включения в Федеральный резерв управленческих кадров
        Отправка на рассмотрение
        """
        page = ReserveBasesPreparePage(self.driver)
        data = get_data_by_value(self.data, "reserve_bases_prepare", "personalFile", "Авто")

        LoginPage(self.driver).login(data=self.hr)
        page.go_to(Links.reserve_bases_prepare)
        page.search(data["search"])
        sleep(3)
        page.set_checkbox_by_order()
        page.click_by_text("Направить на рассмотрение")
        page.click_by_text("Да")
        sleep(3)
        assert "На рассмотрении" in self.driver.page_source

    def test_reserve_view_federal(self):
        """
        Просмотр участников резерва
        """
        page = ReserveViewFederal(self.driver)
        data = get_data_by_value(self.data, "reserve", "view", "")

        LoginPage(self.driver).login(data=self.admin)
        page.go_to(Links.permission_read_resume)
        page.permission_read_resume(True)
        page.wait_for_text_appear("Данные успешно сохранены")
        page.go_to(Links.reserve_view_federal)
        page.click_by_text("Фильтр")
        page.level_reserve(data["level_reserve"])
        page.click_by_text("Применить")
        page.wait_for_loading()
        page.click_by_text(data["participant"])
        page.resume()
        page.check_text_and_close("Место рождения")
        page.presentation()
        page.check_text_and_close("Категория")

    def test_doc_documents(self):
        """Вкладка "Документы" страницы "Документы" """
        data = get_data_by_value(self.data["application_form"], "documents", "type_doc", "Скан-копия паспорта")

        LoginPage(self.driver).login(data=self.hr)
        page = DocumentsPage(self.driver).documents
        page.scroll_to_bottom()
        page.click_by_text("Документы", 2)
        page.scroll_to_top()
        page.click_by_text("Документы", 2)
        sleep(0.5)
        page.click_by_text("Добавить")
        page.type_document(data["type_doc"])
        page.name_document(data["name_doc"])
        page.upload_file(data["upload_file"])
        sleep(2)
        page.click_by_text("Сохранить")

    def test_application_form(self):

        data = self.data["applicationForms"][0]['info']

        LoginPage(self.driver).login(data=self.hr)

        page = ApplicationFormPage(self.driver)
        page.go_to(Links.application_form)
        page.wait.text_appear("Анкеты")
        if "Действующая" in self.driver.page_source:
            page.set_radio_by_order(order=1)
            page.click_by_text("Удалить")
            page.click_by_text("Да")
        page.click_by_text("Добавить")

        # Заполнение раздела Личные сведения
        page.info.last_name(data['lastName'])
        page.info.first_name(data['firstName'])
        page.info.have_not_middle_name(data['haveNotMiddleName'])
        page.info.gender(data['gender'])
        page.info.have_not_tax_certificate_number(data["haveNotTaxCertificateNumber"])
        page.info.insurance_certificate_number(data['insuranceCertificateNumber'])
        page.info.birth_date(data['birthDate'])
        page.info.citizenship(data['citizenship'])
        page.info.citizenship_was_changed(data['citizenshipWasChanged'])
        page.info.subject(data['subject'])
        page.info.area(data['area'])
        page.info.birth_place(data['birthPlace'])
        page.info.was_convicted(data['wasConvicted'])
        page.info.marital_status(data['maritalStatus'])
        page.info.name_was_changed(data['nameWasChanged'])
        page.info.was_abroad(data['wasAbroad'])
        page.info.additional_info(data['additionalInfo'])
        page.info.click_by_text("Сохранить")
        page.info.wait.text_disappear("Сохранить")
        page.info.click_by_text("Редактировать", order=2)
        page.info.work_phone(data['workPhone'])
        page.info.personal_phone(data['personalPhone'])
        page.info.addition_phone(data['additionPhone'])
        page.info.fax(data['fax'])
        page.info.work_mail(data['workMail'])
        page.info.personal_mail(data['personalMail'])
        page.info.personal_site(data['personalSite'])
        page.info.register_subject(data['registerSubject'])
        page.info.register_area(data['registerArea'])
        page.info.register_address(data['registerAddress'])
        page.info.temporarily_register_subject(data['temporarilyRegisterSubject'])
        page.info.temporarily_register_area(data['temporarilyRegisterArea'])
        page.info.temporarily_register_address(data['temporarilyRegisterAddress'])
        page.info.actual_register_subject(data['actualRegisterSubject'])
        page.info.actual_register_area(data['actualRegisterArea'])
        page.info.actual_register_address(data['actualRegisterAddress'])
        page.info.click_by_text("Сохранить")
        page.info.wait.text_disappear("Сохранить")
        page.info.scroll_to_top()

        data = self.data["applicationForms"][0]['documents']

        # Заполнение раздела Документы, удостоверяющие личность
        page.click_by_text("Документы, удостоверяющие личность")
        for document in data:
            page.documents.click_by_text("Добавить")
            page.documents.type(document['type'])
            page.documents.series(document['series'])
            page.documents.number(document['number'])
            page.documents.date_from(document['dateFrom'])
            page.documents.date_to(document['dateTo'])
            page.documents.by(document['by'])
            page.documents.code(document['code'])
            page.documents.note(document['note'])
            page.documents.click_by_text("Сохранить")
            page.documents.wait.text_disappear("Сохранить")
            page.documents.scroll_to_top()

        data = self.data["applicationForms"][0]['education']

        # Заполнение раздела Образование - Основное профессиональное образование
        page.click_by_text("Образование")
        page.education.click_by_text("Редактировать")
        page.education.level(data['level'])
        page.education.click_by_text('Сохранить')
        page.education.wait.text_disappear('Сохранить')
        for main in data['main']:
            page.education.click_by_text('Добавить')
            page.education.main.wait.text_appear("Сохранить")
            page.education.main.type(main['type'])
            page.education.main.form(main['form'])
            page.education.main.placement(main['placement'])
            page.education.main.full_name(main['fullName'])
            page.education.main.is_state(main['isState'])
            page.education.main.date_from(main['dateFrom'])
            page.education.main.date_to(main['dateTo'])
            page.education.main.direction(main['direction'])
            page.education.main.faculty(main['faculty'])
            page.education.main.degree_number(main['degreeNumber'])
            page.education.main.degree_date(main['degreeDate'])
            page.education.main.is_honours_degree(main['isHonoursDegree'])
            if main['isDifferentSpeciality']:
                page.education.main.is_different_speciality(main['isDifferentSpeciality'])
                page.education.main.other_speciality(main['otherSpeciality'])
            else:
                page.education.main.speciality(main['speciality'])

            if main['isDifferentDegreeQualification']:
                page.education.main.is_different_degree_qualification(main['isDifferentDegreeQualification'])
                page.education.main.other_qualification(main['otherQualification'])
            else:
                page.education.main.degree_qualification(main['degreeQualification'])
            page.education.main.degree_speciality(main['degreeSpeciality'])
            page.education.main.is_main(main['isMain'])
            page.education.main.note(main['note'])
            page.education.main.click_by_text("Сохранить")
            page.education.main.level_modal(data['level'])
            page.education.main.submit_modal()
            page.education.main.wait.text_disappear("Сохранить")
            page.education.main.scroll_to_top()

        # Заполнение раздела
        # Образование - Послевузовское профессиональное образование: аспирантура, адъюнктура, докторантура
        if data['haveNotSecondary']:
            page.education.have_not_secondary(data['haveNotSecondary'])
        else:
            for secondary in data['secondary']:
                page.education.click_by_text("Добавить", order=2)
                page.education.secondary.wait.text_appear("Сохранить")
                page.education.secondary.type(secondary['type'])
                page.education.secondary.placement(secondary['placement'])
                page.education.secondary.full_name(secondary['fullName'])
                page.education.secondary.is_state(secondary['isState'])
                page.education.secondary.date_from(secondary['dateFrom'])
                page.education.secondary.date_to(secondary['dateTo'])
                page.education.secondary.advanced_degree(secondary['advancedDegree'])
                page.education.secondary.advanced_degree_date(secondary['advancedDegreeDate'])
                page.education.secondary.industry(secondary['industry'])
                page.education.secondary.degree_number(secondary['degreeNumber'])
                page.education.secondary.degree_date(secondary['degreeDate'])
                page.education.secondary.click_by_text("Сохранить", order=2)
                page.education.secondary.wait.text_disappear("Сохранить")

        # Заполнение раздела Образование - Ученое звание
        if data['haveNotAdvancedDegree']:
            page.education.have_not_advanced_degree(data['haveNotAdvancedDegree'])
        else:
            for degree in data['advancedDegrees']:
                page.education.click_by_text("Добавить", order=3)
                page.education.degree.wait.text_appear("Сохранить")
                page.education.degree.type(degree['type'])
                page.education.degree.date(degree['date'])
                page.education.degree.degree_number(degree['degreeNumber'])
                page.education.degree.click_by_text("Сохранить", order=3)
                page.education.degree.wait.text_disappear("Сохранить")
                page.education.degree.scroll_to_top()

        # Заполнение раздела Образование - Знание иностранных языков
        if data['haveNotLanguages']:
            page.education.have_not_advanced_degree(data['haveNotLanguages'])
        else:
            for language in data['languages']:
                page.education.click_by_text("Добавить", order=4)
                page.education.language.type(language['type'])
                page.education.language.level(language['level'])
                page.education.language.click_by_text("Сохранить", order=4)
                page.education.language.wait.text_disappear("Сохранить")

        # Заполнение раздела Образование - Дополнительное профессиональное образование
        if data['haveNotAdditionalEducation']:
            page.education.have_not_additional_education(data['haveNotAdditionalEducation'])
        else:
            for additional in data['additionalEducations']:
                page.education.click_by_text("Добавить", order=5)
                page.education.additional.direction(additional['direction'])
                page.education.additional.program_type(additional['programType'])
                page.education.additional.speciality(additional['speciality'])
                page.education.additional.program_name(additional['programName'])
                page.education.additional.form(additional['form'])
                page.education.additional.placement(additional['placement'])
                page.education.additional.name(additional['name'])
                page.education.additional.is_state(additional['isState'])
                page.education.additional.date_from(additional['dateFrom'])
                page.education.additional.date_to(additional['dateTo'])
                page.education.additional.hours(additional['hours'])
                page.education.additional.document(additional['document'])
                page.education.additional.document_date(additional['documentDate'])
                page.education.additional.finance_source(additional['financeSource'])
                page.education.additional.is_education_aboard(additional['isEducationAboard'])
                page.education.language.click_by_text("Сохранить", order=5)
                page.education.language.wait.text_disappear("Сохранить")

        page.scroll_to_top()
        data = self.data["applicationForms"][0]['labourActivity']

        # Заполнение раздела Трудовая деятельность - Информация о месте работы
        page.click_by_text("Трудовая деятельность")
        if data['haveNotExperience']:
            page.labour_activity.have_not_additional_education(data['haveNotExperience'])
        else:
            for main in data['main']:
                page.education.click_by_text("Добавить")
                page.labour_activity.main.date_from(main['dateFrom'])
                page.labour_activity.main.date_to(main['dateTo'])
                page.labour_activity.main.position(main['position'])
                page.labour_activity.main.organization_name(main['organizationName'])
                page.labour_activity.main.organization_address(main['organizationAddress'])
                page.labour_activity.main.employees_amount(main['employeesAmount'])
                page.labour_activity.main.organization_subject(main['organizationSubject'])
                page.labour_activity.main.organization_area(main['organizationArea'])
                page.labour_activity.main.organization_profile(main['organizationProfile'])
                page.labour_activity.main.is_selective_position(main['isSelectivePosition'])
                page.labour_activity.main.post_level(main['postLevel'])
                page.labour_activity.main.professional_field(main['professionalField'])
                page.labour_activity.main.department(main['department'])
                page.labour_activity.main.functions(main['functions'])
                for activity in main['projectActivities']:
                    page.education.click_by_text("Добавить", order=2)
                    page.labour_activity.main.project_activity.budget(activity['budget'])
                    page.labour_activity.main.project_activity.role(activity['role'])
                    page.labour_activity.main.project_activity.project_scale(activity['projectScale'])
                    page.labour_activity.main.project_activity.description(activity['description'])
                    page.education.language.click_by_text("Сохранить", order=2)
                    page.education.language.wait.text_disappear("Сохранить")
                page.education.language.click_by_text("Сохранить")
                page.education.language.wait.text_disappear("Сохранить")

        # Заполнение раздела Трудовая деятельность - Дополнительная информация
        additional = data['additional']
        page.labour_activity.click_by_text("Редактировать", order=3)
        page.labour_activity.additional.has_class_rank(additional['hasClassRank'])
        if data['additional']['hasClassRank'] == "Да":
            page.labour_activity.additional.class_rank_name(additional['classRankName'])
            page.labour_activity.additional.class_rank_date(additional['classRankDate'])
            page.labour_activity.additional.class_rank_by(additional['classRankBy'])
        page.labour_activity.additional.is_state(additional['stateOrMunicipalServices'])
        page.labour_activity.additional.personal_computer(additional['personalComputer'])
        page.labour_activity.additional.publications(additional['publications'])
        page.labour_activity.additional.recommendations(additional['recommendation'])
        page.labour_activity.additional.click_by_text("Сохранить", order=3)

        # Заполнение раздела Трудовая деятельность - Специализация
        for speciality in data["specialities"]:
            page.labour_activity.click_by_text("Добавить", order=3)
            page.labour_activity.speciality.name(speciality["name"])
            page.labour_activity.speciality.type(speciality["type"])
            page.labour_activity.speciality.click_by_text("Сохранить", order=3)

        page.scroll_to_top()
        data = self.data["applicationForms"][0]["promotions"]

        # Заполнение раздела Поощрения
        page.click_by_text("Поощрения")
        if data['haveNotPromotions']:
            page.promotions.have_not_promotions(data["haveNotPromotions"])
        else:
            for promotion in data["promotions"]:
                page.promotions.click_by_text("Добавить")
                page.promotions.type(promotion["type"])
                page.promotions.name(promotion["name"])
                page.promotions.date(promotion["date"])
                page.promotions.click_by_text("Сохранить")

        page.scroll_to_top()
        data = self.data["applicationForms"][0]["access"]

        # Заполнение раздела Доступ к государственной тайне
        page.click_by_text("Допуск к государственной тайне")
        if data['haveNotAccess']:
            page.access.have_not_access(data["haveNotAccess"])
        else:
            for access in data["accesses"]:
                page.access.click_by_text("Добавить")
                page.access.form(access["form"])
                page.access.number(access["number"])
                page.access.date(access["date"])
                page.access.click_by_text("Сохранить")

        page.scroll_to_top()
        data = self.data["applicationForms"][0]["military"]

        # Заполнение раздела Воинский учет
        page.click_by_text("Воинский учет")
        page.click_by_text("Редактировать")
        page.military.obligations(data["obligations"])
        page.military.rank(data["rank"])
        page.military.has_done(data["hasDone"])
        if data["hasDone"]:
            page.military.date_from(data["dateFrom"])
            page.military.date_to(data["dateTo"])
            page.military.type(data["type"])
        page.military.click_by_text("Сохранить")

        page.scroll_to_top()
        data = self.data["applicationForms"][0]["relatives"]

        # Заполнение раздела Сведения о близких родственниках
        page.click_by_text("Сведения о близких родственниках")
        if data['haveNotRelatives']:
            page.relatives.have_not_relatives(data['haveNotRelatives'])
        else:
            for member in data['members']:
                page.relatives.click_by_text("Добавить")
                page.relatives.degree(member["degree"])
                page.relatives.last_name(member["lastName"])
                page.relatives.first_name(member["firstName"])
                page.relatives.middle_name(member["middleName"])
                page.relatives.changed_name(member["changedName"])
                page.relatives.birth_date(member["birthDate"])
                page.relatives.birth_place_country(member["birthPlaceCountry"])
                if member["country"] == "Россия":
                    page.relatives.birth_place_subject(member["birthPlaceSubject"])
                    page.relatives.birth_place_area(member["birthPlaceArea"])
                page.relatives.birth_place(member["birthPlace"])
                page.relatives.work_place(member["workPlace"])
                page.relatives.country(member["country"])
                page.relatives.is_resident(member["isResident"])
                page.relatives.residence_permit(member["residencePermit"])
                if member["country"] != "Россия":
                    page.relatives.resident_date(member["residentDate"])
                page.relatives.address(member["address"])
                page.relatives.click_by_text("Сохранить")

    def test_vacancy_control_invite(self):
        """
        Вакансии на контроле.
        Направление приглашения.
        """
        page = VacancyControlPage(self.driver)
        LoginPage(self.driver).login(data=self.admin)
        page.click_by_text("Формирование кадрового состава")
        page.click_by_text("Проведение конкурса на замещение вакантной должности")
        page.scroll_to_top()
        page.click_by_text("Подбор")
        page.table_select_row(1, "Выбор первой вакансии")
        page.scroll_to_top()
        page.click_by_text("Добавить кандидата")
        page.click_by_text("Фильтр")
        page.key_word("Дроздов")
        page.click_by_text("Применить")
        page.table_select_row(1, "Выбор первого кандидата")
        page.scroll_to_top()
        page.click_by_text("Направить приглашение")
        page.click_by_text("Направить приглашение", 2)
        page.scroll_to_top()
        page.click_by_text("Подбор")
        page.scroll_to_top()
        page.click_by_text("Закрыть")
        page.table_select_row(2, "Выбор второй вакансии")
        page.click_by_text("Добавить кандидата")
        page.click_by_text("Фильтр")
        page.key_word("Дроздов")
        page.click_by_text("Применить")
        page.table_select_row(1, "Выбор кандидата")
        page.scroll_to_top()
        page.click_by_text("Направить приглашение")
        page.click_by_text("Направить приглашение", 2)

    def t1est_vacancy_control_statuses(self):
        """
        Вакансии на контроле.
        Принятие приглашения.
        """
        page = VacancyControlPage(self.driver)
        LoginPage(self.driver).login(data=self.user)
        page.click_by_text("Вакансии на контроле")
        page.click_by_text("Фильтр")
        page.status_response("Направлено приглашение")
        page.click_by_text("Применить")
        page.click_by_text("3")
        sleep(1)
        page.table_select_row(1, "Выбор приглашения")
        page.click_by_text("Принять приглашение")
        page.send_document()
        page.click_by_text("Продолжить")
        page.upload_file("Проверочный.pdf")
        sleep(5)
        page.checkbox_accept(True)
        page.click_by_text("Подать документы")
        page.wait_for_text_appear("успешно")
        assert "Ваш отклик успешно завершен." in self.driver.page_source
        page.click_by_text("Назад")
        page.table_select_row(1, "Выбор приглашения")
        page.click_by_text("Отклонить приглашение")
        page.click_by_text("Фильтр")
        page.select2_clear(VacancyControlLocators.status_response)
        page.status_response("Отклонил приглашение")
        page.click_by_text("Применить")
        page.wait_for_text_appear("Отклонил приглашение")
        page.click_by_text("Дата события")
        page.click_by_text("Дата события")
        assert page.is_date_vacancy(), "Проверка \"Отклонил приглашение\" не прошла"
        page.click_by_text("Фильтр")
        page.wait_for_loading()
        page.select2_clear(VacancyControlLocators.status_response)
        page.status_response("Приглашен")
        page.click_by_text("Применить")
        page.wait_for_text_appear("Приглашен")
        page.click_by_text("Дата события")
        page.click_by_text("Дата события")
        assert page.is_date_vacancy(), "Проверка \"Приглашен\" не прошла"

    def test_new_department_for_vacancy(self):

        """
        Организационно-штатная структура - Формирование организационно-штатной структуры
        """
        data = get_data_by_number(self.data, "departments", 1)

        LoginPage(self.driver).login(data=self.hr2)

        page = StructureInfoPage(self.driver)
        page.go_to(Links.staff_structure)
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
        page.go_to(Links.staff_structure)
        page = StructureDetailsPage(self.driver)
        page.click_by_text(data["name"])
        page.click_by_text("Показать все")
        page.wait_for_text_appear("Назначить")
        assert page.projects_check(), "Ошибка: На странице присутствует ярлык \"Проект\""

    @pytest.mark.parametrize("order", [1, 2, 3, 4, 5, 6])
    def test_vacancy_create(self, order):
        """
        Создание вакансий всех 6 типов
        """
        data = load_data("gossluzhba1")["advertisements"][order]

        LoginPage(self.driver).login(data=self.hr2)
        page = VacancyCreatePage(self.driver, 5)
        page.go_to(Links.vacancy_list)
        page.click_by_text("Создать")
        sleep(1)
        page.type_vacancy(data["type_vacancy"])
        page.organization(data["organization"])
        # page.click_by_text("Закрыть", 2) нет такой кнопки
        page.wait_for_text_appear("Структурное подразделение")
        if order == 1:
            sleep(2)
            page.is_competition(data["is_competition"])
            sleep(2)
            page.post_is_competition.competition(data["competition"])
            sleep(2)
            page.post_is_competition.structural_unit(data["structural_unit"])
            page.post_is_competition.sub_structural(data["sub_structural"])
            page.post_is_competition.staff_unit(data["staff_unit"])
            page.click_by_text("Закрыть", 2)
            page.post_is_competition.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.post_is_competition.job_type(data["job_type"])
            page.job_type_other_text(data["job_type_other_text"])
            page.post_is_competition.position_category(data["position_category"])
            page.post_is_competition.position_group(data["position_group"])
            page.post_is_competition.okato_region(data["okato_region"])
            page.post_is_competition.okato_area(data["okato_area"])
            page.salary_from(data["salary_from"])
            page.salary_to(data["salary_to"])
            sleep(1)
            page.post_is_competition.business_trip(data["business_trip"])
            sleep(1)
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
        if order == 2:
            page.reason(data["reason"])
            page.post_is_competition.structural_unit(data["structural_unit"])
            page.post_is_competition.sub_structural(data["sub_structural"])
            page.post_is_competition.staff_unit(data["staff_unit"])
            page.click_by_text("Закрыть", 2)
            page.post_is_competition.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.post_is_competition.job_type(data["job_type"])
            page.job_type_other_text(data["job_type_other_text"])
            page.post_is_competition.position_category(data["position_category"])
            page.post_is_competition.position_group(data["position_group"])
            page.post_is_competition.okato_region(data["okato_region"])
            page.post_is_competition.okato_area(data["okato_area"])
            page.salary_from(data["salary_from"])
            page.salary_to(data["salary_to"])
            sleep(1)
            page.post_is_competition.business_trip(data["business_trip"])
            sleep(1)
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
            # page.post_is_competition.education_level(data["education_level"])
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
        if order == 3:
            page.reserve_post.reserve(data["reserve"])
            page.reserve_post.structural_unit(data["structural_unit"])
            page.reserve_post.sub_structural(data["sub_structural"])
            page.reserve_post.post(data["post"])
            page.reserve_post.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.reserve_post.job_type(data["job_type"])
            page.job_type_other_text(data["job_type_other_text"])
            page.reserve_post.reserve_group(data["reserve_group"])
            page.reserve_post.okato_region(data["okato_region"])
            page.reserve_post.okato_area(data["okato_area"])
            page.salary_from(data["salary_from"])
            page.salary_to(data["salary_to"])
            sleep(1)
            page.reserve_post.business_trip(data["business_trip"])
            sleep(1)
            page.reserve_post.work_day(data["work_day"])
            page.reserve_post.work_schedule(data["work_schedule"])
            page.reserve_post.work_contract(data["work_contract"])
            page.social_package_text(data["social_package_text"])
            page.reserve_post.social_package_files(data["social_package_files"])
            page.additional_position_info_text(data["additional_position_info_text"])
            page.reserve_post.additional_position_info_file(data["additional_position_info_file"])
            page.scroll_to_top()
            page.click_by_text("Должностные обязанности")
            page.job_responsibility_text(data["job_responsibility_text"])
            page.reserve_post.job_responsibility_files(data["job_responsibility_files"])
            page.reserve_post.position_rules_files(data["position_rules_files"])
            page.click_by_text("Квалификационные требования")
            page.reserve_post.education_level(data["education_level"])
            page.reserve_post.government_experience(data["government_experience"])
            page.reserve_post.professional_experience(data["professional_experience"])
            page.knowledge_description_text(data["knowledge_description_text"])
            page.reserve_post.knowledge_description_files(data["knowledge_description_files"])
            page.additional_requirements(data["additional_requirements"])
            page.reserve_post.test(data["test"])
            page.click_by_text("Документы", 2)
            page.announcement_date()
            page.expiry_date(data["expiry_date"])
            page.registration_address(data["registration_address"])
            page.registration_time(data["registration_time"])
            page.click_by_text("Контакты")
            page.wait_for_text_appear("Почтовый адрес")
            page.reserve_post.organization_address(data["organization_address"])
            page.address_mail(data["address_mail"])
            page.phone(data["phone"])
            page.phone2(data["phone2"])
            page.phone3(data["phone3"])
            page.email(data["email"])
            page.contact_person_other(data["contact_person_other"])
            page.web(data["web"])
            page.additional_info_text(data["additional_info_text"])
            sleep(0.5)
            page.reserve_post.additional_info_files(data["additional_info_files"])
        if order == 4:
            page.reserve_group_posts.reserve(data["reserve"])
            page.reserve_group_posts.structural_unit(data["structural_unit"])
            page.reserve_group_posts.sub_structural(data["sub_structural"])
            page.reserve_group_posts.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.reserve_group_posts.job_type(data["job_type"])
            page.job_type_other_text(data["job_type_other_text"])
            page.reserve_group_posts.reserve_group(data["reserve_group"])
            page.reserve_group_posts.okato_region(data["okato_region"])
            page.reserve_group_posts.okato_area(data["okato_area"])
            page.salary_from(data["salary_from"])
            page.salary_to(data["salary_to"])
            sleep(1)
            page.reserve_group_posts.business_trip(data["business_trip"])
            sleep(1)
            page.reserve_group_posts.work_day(data["work_day"])
            page.reserve_group_posts.work_schedule(data["work_schedule"])
            page.reserve_group_posts.work_contract(data["work_contract"])
            page.social_package_text(data["social_package_text"])
            page.reserve_group_posts.social_package_files(data["social_package_files"])
            page.additional_position_info_text(data["additional_position_info_text"])
            page.reserve_group_posts.additional_position_info_file(data["additional_position_info_file"])
            page.scroll_to_top()
            page.click_by_text("Должностные обязанности")
            page.job_responsibility_text(data["job_responsibility_text"])
            page.reserve_group_posts.job_responsibility_files(data["job_responsibility_files"])
            page.reserve_group_posts.position_rules_files(data["position_rules_files"])
            page.click_by_text("Квалификационные требования")
            page.reserve_group_posts.education_level(data["education_level"])
            page.reserve_group_posts.government_experience(data["government_experience"])
            page.reserve_group_posts.professional_experience(data["professional_experience"])
            page.knowledge_description_text(data["knowledge_description_text"])
            page.reserve_group_posts.knowledge_description_files(data["knowledge_description_files"])
            page.additional_requirements(data["additional_requirements"])
            page.reserve_group_posts.test(data["test"])
            page.click_by_text("Документы", 2)
            page.announcement_date()
            page.expiry_date(data["expiry_date"])
            page.registration_address(data["registration_address"])
            page.registration_time(data["registration_time"])
            page.click_by_text("Контакты")
            page.wait_for_text_appear("Почтовый адрес")
            page.reserve_group_posts.organization_address(data["organization_address"])
            page.address_mail(data["address_mail"])
            page.phone(data["phone"])
            page.phone2(data["phone2"])
            page.phone3(data["phone3"])
            page.email(data["email"])
            page.contact_person_other(data["contact_person_other"])
            page.web(data["web"])
            page.additional_info_text(data["additional_info_text"])
            sleep(0.5)
            page.reserve_group_posts.additional_info_files(data["additional_info_files"])
        if order == 5:
            page.vacant_study.structural_unit(data["structural_unit"])
            page.vacant_study.sub_structural(data["sub_structural"])
            page.vacant_study.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.vacant_study.job_type(data["job_type"])
            page.job_type_other_text(data["job_type_other_text"])
            page.vacant_study.position_category(data["position_category"])
            page.vacant_study.position_group(data["position_group"])
            page.vacant_study.okato_region(data["okato_region"])
            page.vacant_study.okato_area(data["okato_area"])
            page.salary_from(data["salary_from"])
            page.salary_to(data["salary_to"])
            sleep(1)
            page.vacant_study.business_trip(data["business_trip"])
            sleep(1)
            page.vacant_study.work_schedule(data["work_schedule"])
            page.vacant_study.work_day(data["work_day"])
            page.vacant_study.work_contract(data["work_contract"])
            page.social_package_text(data["social_package_text"])
            page.vacant_study.social_package_files(data["social_package_files"])
            page.additional_position_info_text(data["additional_position_info_text"])
            page.vacant_study.additional_position_info_file(data["additional_position_info_file"])
            page.scroll_to_top()
            page.click_by_text("Должностные обязанности")
            page.job_responsibility_text(data["job_responsibility_text"])
            page.vacant_study.job_responsibility_files(data["job_responsibility_files"])
            page.vacant_study.position_rules_files(data["position_rules_files"])
            page.click_by_text("Квалификационные требования")
            page.vacant_study.education_level(data["education_level"])
            page.vacant_study.government_experience(data["government_experience"])
            page.vacant_study.professional_experience(data["professional_experience"])
            page.knowledge_description_text(data["knowledge_description_text"])
            page.vacant_study.knowledge_description_files(data["knowledge_description_files"])
            page.additional_requirements(data["additional_requirements"])
            page.vacant_study.test(data["test"])
            page.click_by_text("Документы", 2)
            page.announcement_date()
            page.expiry_date(data["expiry_date"])
            page.registration_address(data["registration_address"])
            page.registration_time(data["registration_time"])
            page.click_by_text("Контакты")
            page.wait_for_text_appear("Почтовый адрес")
            page.vacant_study.organization_address(data["organization_address"])
            page.address_mail(data["address_mail"])
            page.phone(data["phone"])
            page.phone2(data["phone2"])
            page.phone3(data["phone3"])
            page.email(data["email"])
            page.contact_person_other(data["contact_person_other"])
            page.web(data["web"])
            page.additional_info_text(data["additional_info_text"])
            sleep(0.5)
            page.vacant_study.additional_info_files(data["additional_info_files"])
        if order == 6:
            page.vacant_state.structural_unit(data["structural_unit"])
            page.vacant_state.sub_structural(data["sub_structural"])
            page.vacant_state.staff_unit(data["staff_unit"])
            page.vacant_state.work_type(data["work_type"])
            page.work_type_other_text(data["work_type_other_text"])
            page.vacant_state.job_type(data["job_type"])
            page.job_type_other_text(data["job_type_other_text"])
            page.vacant_state.position_category(data["position_category"])
            page.vacant_state.position_group(data["position_group"])
            page.click_by_text("Должностные обязанности")
            page.job_responsibility_text(data["job_responsibility_text"])
            page.vacant_state.job_responsibility_files(data["job_responsibility_files"])
            page.vacant_state.position_rules_files(data["position_rules_files"])
        page.scroll_to_bottom()
        page.click_by_text("Сохранить")
        sleep(2)
        page.wait_for_text_appear("Создать")
        assert "Создать" in self.driver.page_source

    def te1st_creation_vacancy(self):
        """
        Создание вакансий, которые будут использоваться в управлении объявлениями
        """
        page = VacancyCreatePage(self.driver)
        data = load_data("gossluzhba1")["advertisements"][1]

        LoginPage(self.driver).login(data=self.hr2)
        page.go_to(Links.vacancy_list)
        for i in range(2):
            page.click_by_text("Создать")
            page.type_vacancy(data["type_vacancy"])
            page.organization(data["organization"])
            page.click_by_text("Закрыть", 2)
            page.wait_for_text_appear("Структурное подразделение")
            page.is_competition(data["is_competition"])
            sleep(1)
            page.post_is_competition.structural_unit(data["structural_unit"])
            page.post_is_competition.sub_structural(data["sub_structural"])
            page.post_is_competition.staff_unit(data["staff_unit"])
            page.click_by_text("Закрыть", 2)
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
            sleep(1)
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
        Управление объявлениями.
        Отправка на рассмотрение, публикацию вакансий.
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(data=self.hr2)
        page.go_to(Links.vacancy_list)
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
        Управление объявлениями.
        Отправка вакансии на доработку.
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(data=self.admin)
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
        Управление объявлениями.
        Отправка вакансии на публикацию.
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(data=self.admin)
        page.click_by_text("Управление объявлениями")
        page.wait_for_loading()
        page.click_by_text("Фильтр")
        page.click_by_text("Очистить")
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
        Управление объявлениями.
        Закрытие вакансии.
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(data=self.admin)
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
        Управление объявлениями.
        Архивирование вакансии.
        """
        page = VacancyManagePage(self.driver)
        data = get_data_by_value(self.data, "manage_vacancy", "project", "Проект")

        LoginPage(self.driver).login(data=self.admin)
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

    def test_vacancy_search(self):
        """
        Тест по сценарию "Поиск вакансий".
        Описывает работу раздела "Поиск вакансий" (заполнение фильтра, выполнение поиска и открытия вакансии)
        """
        page = VacancySearchPage(self.driver)

        LoginPage(self.driver).login(data=self.admin)
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
        page.level_education("Высшее образование – специалитет")
        page.service_experience("Не менее 4 лет")
        page.work_experience_speciality("Не менее 4 лет")
        page.click_by_text("Применить")
        page.click_by_text("Директор департамента")
        page.wait_for_text_appear("Код вакансии")
        assert "Профиль деятельности организации" in self.driver.page_source
