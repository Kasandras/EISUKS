from locators import *
from setup import *
from framework import *


def change_date(amount=0):
    date = datetime.date.today()
    delta = datetime.timedelta(days=amount)
    now_date = date + delta
    return '%s.%s.%s' % (now_date.day, now_date.month, now_date.year)


def today():
    return datetime.date.today().strftime("%d.%m.%Y")


parent = Browser


class MainPage(parent):

    def logout(self):
        self.driver.get(Links.main_page)
        self.wait_for_loading()
        self.scroll_to_top()
        self.click((By.XPATH, "//input[@type='submit']"))


class LoginPage(parent):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Имя пользователя")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click(LoginLocators.submit, "Войти")

    def login(self, username, password):
        self.driver.get(Links.main_page)
        if "Войти" in self.driver.page_source:
            self.click_by_text("Войти")
            try:
                self.click_by_text("Войти", 2)
            except EC.NoSuchElementException:
                pass
            self.username(username)
            self.password(password)
            self.submit()
            self.wait_for_text_appear("Личные данные")
        else:
            self.scroll_to_top()
            self.logout()
            self.login(username, password)

    def logout(self):
        self.driver.get(Links.main_page)
        self.wait_for_loading()
        self.scroll_to_top()
        self.click((By.XPATH, "//input[@type='submit']"))


class PersonalPage(parent):

    def last_name(self, value):
        self.set_text(PersonalLocators.last_name, value, "Фамилия")

    def first_name(self, value):
        self.set_text(PersonalLocators.first_name, value, "Имя")

    def middle_name(self, value):
        self.set_text(PersonalLocators.middle_name, value, "Отчество")

    def birthday(self, value):
        self.set_date(PersonalLocators.birthday, value, "Дата рождения")

    def insurance_certificate_number(self, value):
        self.set_text(PersonalLocators.insurance_certificate_number, value, "СНИЛС")

    def username(self, value):
        self.set_text(PersonalLocators.username, value, "Учетная запись")


class PersonalFilePage(parent):

    def general_edit(self):
        self.click(PersonalFileLocators.general_edit, "Редактировать общие сведения")

    def last_name(self, value):
        self.set_text(PersonalFileLocators.last_name, value, "Фамилия")

    def first_name(self, value):
        self.set_text(PersonalFileLocators.first_name, value, "Имя")

    def middle_name(self, value):
        self.set_text(PersonalFileLocators.middle_name, value, "Отчество")

    def gender(self, value):
        self.set_select2(PersonalFileLocators.gender, value, "Пол")

    def personal_file_number(self, value):
        self.set_text(PersonalFileLocators.personal_file_number, value, "Номер личного дела")

    def birthday(self, value):
        self.set_date(PersonalFileLocators.birthday, value, "Дата рождения")

    def okato(self, value):
        self.set_text(PersonalFileLocators.okato, value, "Место рождения, код по ОКАТО")

    def criminal_record(self, value):
        self.set_select(value, 1, "Наличие судимости")

    def last_name_changing(self, value):
        self.set_select(value, 2, "Сведения об изменении ФИО")

    def addresses_edit(self):
        self.click(PersonalFileLocators.addresses_edit, "Редактировать адреса")

    def contacts_edit(self):
        self.click(PersonalFileLocators.contact_edit, "Редактировать контактную информацию")


class StructureInfoPage(parent):

    def organization(self, value):
        self.set_select2(StructureInfoLocators.organization, value, "Организация")

    def name(self, value):
        self.set_text(StructureInfoLocators.name, value, "Наименование")

    def fot(self, value):
        self.set_text(StructureInfoLocators.fot, value, "ФОТ, руб.")

    def limit(self, value):
        self.set_text(StructureInfoLocators.limit, value, "Предельная штатная численность")


class StructureDetailsPage(parent):

    def general(self):
        self.click(StructureDetailsLocators.general, "Общие сведения")

    def forming(self):
        self.click(StructureDetailsLocators.forming, "Формирование организационной структуры")
        self.wait_for_element_appear((By.XPATH, "//th[.='Подразделения']"))

    def structure(self):
        self.click(StructureDetailsLocators.structure, "Штатная структура")

    def arrangement(self):
        self.click(StructureDetailsLocators.arrangement, "Штатная расстановка")

    def launch(self):
        self.click(StructureDetailsLocators.launch, "Введение в действие штатного расписания")
        self.wait_for_element_appear((By.XPATH, "//label[.='Номер приказа']"))

    def order_number(self, value):
        self.set_text(StructureDetailsLocators.order_number, value, "Номер приказа")

    def order_date(self, value):
        self.set_date(StructureDetailsLocators.order_date, value, "Дата приказа")

    def launch_date(self, value):
        self.set_text(StructureDetailsLocators.launch_date, value, "Дата ввода в действие")

    def department_select(self, value):
        self.click((By.XPATH, "//h4[contains(normalize-space(), '%s')]" % value))


class DepartmentPage(parent):

    def name(self, value):
        self.set_text(DepartmentLocators.name, value, "Наименование")

    def name_genitive(self, value):
        self.set_text(DepartmentLocators.name_genitive, value, "Наименование в родительном падеже")

    def name_dative(self, value):
        self.set_text(DepartmentLocators.name_dative, value, "Наименование в дательном падеже")

    def name_accusative(self, value):
        self.set_text(DepartmentLocators.name_accusative, value, "Наименование в винительном падеже")

    def limit(self, value):
        self.set_text(DepartmentLocators.limit, value, "Предельная штатная численность")

    def code(self, value):
        self.set_text(DepartmentLocators.code, value, "Код")

    def launch_date(self, value):
        self.set_date(DepartmentLocators.launch_date, value, "Дата ввода в действие")

    def order_number(self, value):
        self.set_text(DepartmentLocators.order_number, value, "Номер приказа")

    def order_date(self, value):
        self.set_date(DepartmentLocators.order_date, value, "Дата приказа")

    def position(self, value):
        self.set_select2(DepartmentLocators.position, value, "Штатная единица")

    def amount(self, value):
        self.set_text(DepartmentLocators.amount, value, "Количество штатных единиц")


class AppointmentPage(parent):

    def full_name(self, value):
        self.set_select2(AppointmentLocators.full_name, value, "фио назначаемого лица")

    def reason(self, value):
        self.set_select2(AppointmentLocators.reason, value, "в соответствии с")

    def duration(self, value):
        if not value:
            self.click(AppointmentLocators.duration, "на неопределенный срок")

    def date_from(self, value):
        self.set_date(AppointmentLocators.date_from, value, "с")

    def trial(self, value):
        if not value:
            self.click(AppointmentLocators.trial, "без испытательного срока")

    def contract_date(self, value):
        self.set_date(AppointmentLocators.contract_date, value, "дата служебного контракта")

    def contract_number(self, value):
        self.set_text(AppointmentLocators.contract_number, value, "номер служебного контракта")


class SalaryPaymentsPage(parent):

    def type(self, value):
        self.set_select2(SalaryPaymentsLocators.type, value, "Тип денежного содержания")

    def amount(self, value):
        self.set_text(SalaryPaymentsLocators.amount, value, "Значение")

    def date_from(self, value):
        self.set_date(SalaryPaymentsLocators.date_from, value, "Дата с")


class PersonalFileDismissalPage(parent):

    def check(self):
        self.click(PersonalFileDismissalLocators.check, "Флагу для выбора сотрудника")


class DismissalPage(parent):

    def date(self, value):
        self.set_date(DismissalLocators.date, value, "Дата увольнения")

    def reason(self, value):
        self.set_select2(DismissalLocators.reason, value, "В соответствии с")


class StagesPage(parent):

    def check(self):
        self.click(StagesLocators.check, "Флагу для выбора сотрудника")

    def order(self, value):
        self.set_text(StagesLocators.order, value, "Номер приказа")

    def date(self, value):
        self.set_date(StagesLocators.date, value, "Дата приказа")

    def full_name(self, value):
        self.set_select2(StagesLocators.full_name, value, "ФИО подписанта")

    def position(self, value):
        self.set_select2(StagesLocators.position, value, "Должность подписанта")

    def submit(self):
        self.click(StagesLocators.submit, "Сохранить")


class AdvertisementPage(parent):

    def type(self, value):
        self.set_select2(AdvertisementLocators.type, value, "Тип объявления")

    def organization(self, value):
        self.set_select2(AdvertisementLocators.organization, value, "Организация")

    def is_competition(self, value):
        self.set_checkbox(AdvertisementLocators.is_competition, value, "Замещение по конкурсу")

    def reason(self, value):
        self.set_text(AdvertisementLocators.reason, value, "Причина")

    def division(self, value):
        self.set_select2(AdvertisementLocators.division, value, "Структурное подразделение")

    def subdivision(self, value):
        self.set_select2(AdvertisementLocators.subdivision, value, "Подразделение в структурном подразделении")

    def position(self, value):
        self.set_select2(AdvertisementLocators.position, value, "Штатная единица")

    def profile(self, value):
        self.set_select2(AdvertisementLocators.profile, value, "Профиль деятельности организации")

    def okato_region(self, value):
        self.set_select2(AdvertisementLocators.okato_region,
                         value, "Расположение рабочего места по вакантной должности")

    def okato_area(self, value):
        self.set_select2(AdvertisementLocators.okato_area,
                         value, "Расположение рабочего места по вакантной должности")

    def salary_from(self, value):
        self.set_text(AdvertisementLocators.salary_from,
                      value, "Примерный размер денежного содержания (оплаты труда) от")

    def salary_to(self, value):
        self.set_text(AdvertisementLocators.salary_to,
                      value, "Примерный размер денежного содержания (оплаты труда) до")

    def buiseness_trip(self, value):
        self.set_select2(AdvertisementLocators.buisness_trip, value, "Командировки")

    def work_schedule(self, value):
        self.set_select2(AdvertisementLocators.work_schedule, value, "Служебное (рабочее) время")

    def is_fixed_schedule(self, value):
        self.set_select2(AdvertisementLocators.is_fixed_schedule, value, "Нормированность рабочего дня")

    def work_contract(self, value):
        self.set_select2(AdvertisementLocators.work_contract, value, "Тип служебного контракта (трудового договора)")

    def guarantee(self, value):
        self.set_text(AdvertisementLocators.guarantee,
                      value, "Гарантии, предоставляемые государственному служащему/социальный пакет")

    def additional_info(self, value):
        self.set_text(AdvertisementLocators.additional_info,
                      value, "Дополнительная информация о вакантной должности")

    def job_responsibility(self, value):
        self.set_text(AdvertisementLocators.job_responsibility, value, "Краткое описание должностных обязанностей")

    def requirements(self, value):
        self.set_select2(AdvertisementLocators.requirements,
                         value, "Требования к вакантной должности - уровень профессионального образования")

    def experience(self, value):
        self.set_select2(AdvertisementLocators.experience, value, "Стаж государственной службы")

    def work_experience(self, value):
        self.set_select2(AdvertisementLocators.work_experience, value, "Стаж работы по специальности")

    def knowledge_description(self, value):
        self.set_text(AdvertisementLocators.knowledge_description, value, "Знания и навыки")

    def additional_requirements(self, value):
        self.set_text(AdvertisementLocators.additional_requirements,
                      value, "Дополнительные требования к кандидатам")

    def announcement_date(self, value):
        self.set_text(AdvertisementLocators.announcement_date, value, "Дата начала приема документов")

    def expiry_date(self, value):
        self.set_text(AdvertisementLocators.expiry_date, value, "Дата окончания приема документов")

    def registration_address(self, value):
        self.set_text(AdvertisementLocators.registration_address, value, "Место приема документов")

    def registration_time(self, value):
        self.set_text(AdvertisementLocators.registration_time, value, "Время приема документов")

    def post_index(self, value):
        self.set_select2(AdvertisementLocators.post_index, value, "Почтовый адрес")

    def address_mail(self, value):
        self.set_text(AdvertisementLocators.address_mail, value, "Почтовый адрес (другое)")

    def phone_1(self, value):
        self.set_text(AdvertisementLocators.phone_1, value, "Телефон №1")

    def phone_2(self, value):
        self.set_text(AdvertisementLocators.phone_2, value, "Телефон №2")

    def phone_3(self, value):
        self.set_text(AdvertisementLocators.phone_3, value, "Телефон №3")

    def email(self, value):
        self.set_text(AdvertisementLocators.email, value, "Email")

    def person(self, value):
        self.set_text(AdvertisementLocators.person, value, "Контактное лицо")

    def site(self, value):
        self.set_text(AdvertisementLocators.site, value, "Интернет-сайт органа или организации")

    def additional(self, value):
        self.set_text(AdvertisementLocators.additional, value, "Дополнительная информация")


class VacancyListPage(parent):

    def check(self, value=1):
        self.set_checkbox((By.XPATH, "(//input[@type='checkbox'])[%s]" % value), True)


class CommissionsPage(parent):

    _var = 1
    __var = 2

    @property
    def members(self):
        return self.Members(self.driver)

    @property
    def sessions(self):
        return self.Sessions(self.driver)

    def name(self, value):
        self.set_text(CommissionsLocators.name, value, "Наименование комиссии")

    def organization(self, value):
        self.set_select2(CommissionsLocators.organization, value, "Организация")

    def order_date(self, value):
        self.set_text(CommissionsLocators.order_date, value, "Дата приказа")

    def order_number(self, value):
        self.set_text(CommissionsLocators.order_number, value, "Номер приказа")

    def full_name(self, value):
        self.set_select2(CommissionsLocators.full_name, value, "Кто подписал")

    def type(self, value):
        self.set_select2(CommissionsLocators.type, value, "Вид комиссии")

    def start_date(self, value):
        self.set_text(CommissionsLocators.start_date, value, "Период действия с")

    def end_date(self, value):
        self.set_text(CommissionsLocators.end_date, value, "Период действия по")

    class Members(parent):

        def role(self, value):
            self.set_select2(CommissionsLocators.Members.role, value, "Роль в комиссии")

        def full_name(self, value):
            self.set_select2(CommissionsLocators.Members.full_name, value, "Фамилия Имя Отчество")

        def is_independent_expert(self, value):
            self.set_checkbox(CommissionsLocators.Members.is_independent_expert, value, "Организация")

        def organization(self, value):
            self.set_text(CommissionsLocators.Members.organization, value, "Должность")

        def position(self, value):
            self.set_text(CommissionsLocators.Members.position, value, "Подразделение")

        def department(self, value):
            self.set_text(CommissionsLocators.Members.department, value, "Телефон")

        def phone(self, value):
            self.set_text(CommissionsLocators.Members.phone, value, "E-mail")

        def email(self, value):
            self.set_text(CommissionsLocators.Members.email, value, "Номер личного дела")

        def personal_file_number(self, value):
            self.set_text(CommissionsLocators.Members.personal_file_number, value, "")

    class Sessions(parent):

        def meeting_date(self, value):
            self.set_text(CommissionsLocators.Sessions.meeting_date, value, "Дата заседания")

        def meeting_time(self, value):
            self.set_text(CommissionsLocators.Sessions.meeting_time, value, "Время заседания")

        def place(self, value):
            self.set_text(CommissionsLocators.Sessions.place, value, "Место проведения")

        def questions_amount(self):
            element = self.wait_for_element_appear((By.XPATH, "//td[normalize-space()='0']"))
            element.find_element(By.XPATH, ".//a").click()

        def content(self, value):
            self.set_text(CommissionsLocators.Sessions.content, value, "Содержание вопроса")

        def reporter(self, value):
            self.set_text(CommissionsLocators.Sessions.reporter, value, "Докладчик")

        def decision(self, value):
            self.set_select2(CommissionsLocators.Sessions.decision, value, "Решение")

        def decision_reason(self, value):
            self.set_text(CommissionsLocators.Sessions.decision_reason, value,
                          "Основание и мотивы принятия такого решения")


class OrdersPage(parent):

    def submit(self, full_name, order, date, by, position):
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_row_checkbox()
        self.click_by_text("Включить в приказ")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[3]"), position, "Должность подписанта")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[2]"), by, "ФИО подписанта")
        self.set_date((By.XPATH, "(//input[@type='text'])[2]"), date, "Дата приказа")
        self.set_text((By.XPATH, "(//input[@type='text'])[1]"), order, "Номер приказа")
        self.click((By.XPATH, "//input[@value='Сохранить']"), "Сохранить")
        self.wait_for_text_appear("Приказ успешно утвержден.")
        self.click((By.XPATH, "//small[.='3']"), "Исполнение приказов ")
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_row_checkbox()
        self.click_by_text("Завершить")

    def submit_business_trips(self, full_name, order, date, by, position):
        self.click_by_text("Фильтр")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[1]"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_row_checkbox()
        self.click_by_text("Включить в приказ")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[3]"), position, "Должность подписанта")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[2]"), by, "ФИО подписанта")
        self.set_date((By.XPATH, "(//input[@type='text'])[2]"), date, "Дата приказа")
        self.set_text((By.XPATH, "(//input[@type='text'])[1]"), order, "Номер приказа")
        self.click((By.XPATH, "//input[@value='Сохранить']"), "Сохранить")
        self.wait_for_text_appear("Приказ успешно утвержден.")
        self.click((By.XPATH, "//small[.='3']"), "Исполнение приказов ")
        self.click_by_text("Фильтр")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[1]"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_row_checkbox()
        self.click_by_text("Завершить")


class AwardsPage(parent):

    def __init__(self, driver, timeout=60, log=True):
        super().__init__(driver, timeout, log)
        self.awards = self.Awards(driver, timeout, log)
        self.state_awards = self.StateAwards(driver, timeout, log)
        self.department_awards = self.DepartmentAwards(driver, timeout, log)

    class Awards(parent):

        def type(self, value):
            self.set_select2(AwardsLocators.Awards.type, value, "Вид")

        def name(self, value):
            self.set_text(AwardsLocators.Awards.name, value, "Наименование")

        def date(self, value):
            self.set_date(AwardsLocators.Awards.date, value, "Дата поощрения")

        def amount(self, value):
            self.set_text(AwardsLocators.Awards.amount, value, "Размер премии")

        def unit(self, value):
            self.set_select2(AwardsLocators.Awards.unit, value, "Единица измерения")

        def note(self, value):
            self.set_text(AwardsLocators.Awards.note, value, "Примечание")

        def should_be(self, value):
            self.set_checkbox(AwardsLocators.Awards.should_be, value, "Служащий должен быть ознакомлен с приказом")

        def submit(self):
            self.click(AwardsLocators.Awards.submit, "Сохранить")
            self.wait_for_element_disappear(AwardsLocators.Awards.submit)

    class StateAwards(parent):

        def type(self, value):
            self.set_select2(AwardsLocators.StateAwards.type, value, "Вид поощрения")

        def name(self, value):
            self.set_text(AwardsLocators.StateAwards.name, value, "Наименование награды")

        def list_date(self, value):
            self.set_date(AwardsLocators.StateAwards.list_date, value, "Дата наградного листа")

        def date(self, value):
            self.set_date(AwardsLocators.StateAwards.date, value, "Дата представления к награде")

        def order_number(self, value):
            self.set_text(AwardsLocators.StateAwards.order_number, value, "Номер указа Президента РФ")

        def order_date(self, value):
            self.set_date(AwardsLocators.StateAwards.order_date, value, "Дата указа")

        def award_number(self, value):
            self.set_text(AwardsLocators.StateAwards.award_number, value, "Номер награды")

        def certificate_number(self, value):
            self.set_text(AwardsLocators.StateAwards.certificate_number, value, "Номер удостоверения награды")

        def awarding_date(self, value):
            self.set_date(AwardsLocators.StateAwards.awarding_date, value, "Дата вручения")

        def note(self, value):
            self.set_text(AwardsLocators.StateAwards.note, value, "Примечание")

        def submit(self):
            self.click(AwardsLocators.StateAwards.submit, "Сохранить")
            self.wait_for_element_disappear(AwardsLocators.StateAwards.submit)

    class DepartmentAwards(parent):

        def type(self, value):
            self.set_select2(AwardsLocators.DepartmentAwards.type, value, "Вид поощрения")

        def name(self, value):
            self.set_text(AwardsLocators.DepartmentAwards.name, value, "Наименование награды")

        def order_number(self, value):
            self.set_text(AwardsLocators.DepartmentAwards.order_number, value, "Номер приказа")

        def order_date(self, value):
            self.set_text(AwardsLocators.DepartmentAwards.order_date, value, "Дата приказа")

        def award_number(self, value):
            self.set_text(AwardsLocators.DepartmentAwards.award_number, value, "Номер награды")

        def certificate_number(self, value):
            self.set_text(AwardsLocators.DepartmentAwards.certificate_number, value, "Номер удостоверения награды")

        def awarding_date(self, value):
            self.set_date(AwardsLocators.DepartmentAwards.awarding_date, value, "Дата вручения")

        def note(self, value):
            self.set_text(AwardsLocators.DepartmentAwards.note, value, "Примечание")

        def submit(self):
            self.click(AwardsLocators.DepartmentAwards.submit, "Сохранить")
            self.wait_for_element_disappear(AwardsLocators.DepartmentAwards.submit)


class EnforcementPage(parent):

    def reason(self, value):
        self.set_select2(EnforcementLocators.reason, value, "Причина проведения проверки")

    def order_number(self, value):
        self.set_text(EnforcementLocators.order_number, value, "Номер приказа")

    def order_date(self, value):
        self.set_date(EnforcementLocators.order_date, value, "Дата приказа")

    def period_from(self, value):
        self.set_date(EnforcementLocators.period_from, value, "Период проведения с")

    def period_to(self, value):
        self.set_date(EnforcementLocators.period_to, value, "Период проведения по")

    def action_date(self, value):
        self.set_date(EnforcementLocators.action_date, value, "Дата проступка")

    def action(self, value):
        self.set_select2(EnforcementLocators.action, value, "Проступок")

    def explanatory_date(self, value):
        self.set_date(EnforcementLocators.explanatory_date, value, "Дата объяснительной записки/акта")

    def enforcement_date(self, value):
        self.set_date(EnforcementLocators.enforcement_date, value, "Дата взыскания")

    def enforcement_reason(self, value):
        self.set_select2(EnforcementLocators.enforcement_reason, value, "Основание")

    def type(self, value):
        self.set_select2(EnforcementLocators.type, value, "Вид")

    def copy_date(self, value):
        self.set_date(EnforcementLocators.copy_date, value, "Дата выдачи копии")

    def enforcement_expire_auto(self, value):
        self.set_date(EnforcementLocators.enforcement_expire_auto, value, "Дата автоматического снятия взыскания")

    def enforcement_expire_date(self, value):
        self.set_date(EnforcementLocators.enforcement_expire_date, value, "Дата снятия взыскания")

    def enforcement_expire_reason(self, value):
        self.set_text(EnforcementLocators.enforcement_expire_reason, value, "Основание")

    def enforcement_expire_order_date(self, value):
        self.set_date(EnforcementLocators.enforcement_expire_order_date, value, "Дата приказа")

    def enforcement_expire_order_number(self, value):
        self.set_text(EnforcementLocators.enforcement_expire_order_number, value, "Номер приказа")

    def should_be(self, value):
        self.set_checkbox(EnforcementLocators.should_be, value, "Служащий должен быть ознакомлен с приказом")


class DispensaryPlanningPage(parent):

    def table_select_user(self, value):
        self.set_checkbox((By.XPATH, "//tr[contains(., '%s')]//input" % value), True, "Выбор сотрудника")

    def date_from(self, value):
        self.set_text(DispensaryPlanningLocators.date_from, value, "Дата начала")

    def date_to(self, value):
        self.set_text(DispensaryPlanningLocators.date_to, value, "Дата окончания")
        self.click((By.ID, "select2-find-dispensary"))

    def submit(self):
        self.click((By.XPATH, "//button[@ng-click='save()']"))


class DispensaryPage(parent):

    def dispensary_date(self, value):
        self.set_date(DispensaryLocators.dispensary_date, value, "Дата прохождения диспансеризации")

    def reference_date(self, value):
        self.set_date(DispensaryLocators.reference_date, value, "Дата справки")

    def reference_number(self, value):
        self.set_text(DispensaryLocators.reference_number, value, "Номер справки")

    def is_healthy(self, value):
        self.set_checkbox(DispensaryLocators.is_healthy, value, "Выявлено отсутствие заболевания")

    def date_from(self, value):
        self.set_date(DispensaryLocators.date_from, value, "Дата начала")

    def date_to(self, value):
        self.set_date(DispensaryLocators.date_to, value, "Дата окончания")

    def order_date(self, value):
        self.set_date(DispensaryLocators.order_date, value, "Дата приказа")

    def order_number(self, value):
        self.set_text(DispensaryLocators.order_number, value, "Номер приказа")

    def institution(self, value):
        self.set_select2(DispensaryLocators.institution, value, "Лечебное учреждение")

    def by(self, value):
        self.set_select2(DispensaryLocators.by, value, "Кто подписал")


class DisabilityPeriodsPage(parent):

    @property
    def editing(self):
        return self.Editing(self.driver)

    def list_number(self, value):
        self.set_text(DisabilityPeriodsLocators.list_number, value, "Номер листка")

    def by(self, value):
        self.set_text(DisabilityPeriodsLocators.by, value, "Кем выдан")

    def note(self, value):
        self.set_text(DisabilityPeriodsLocators.note, value, "Примечание")

    def period_from(self, value):
        self.set_date(DisabilityPeriodsLocators.period_from, value, "Период освобождения с")

    def period_to(self, value):
        self.set_date(DisabilityPeriodsLocators.period_to, value, "Период освобождения по")

    def list_continuing(self, value):
        self.set_select2(DisabilityPeriodsLocators.list_continuing, value, "Продолжение листка")

    def reason(self, value):
        self.set_select2(DisabilityPeriodsLocators.reason, value, "Причина нетрудоспособности")

    def family_member(self, value):
        self.set_select2(DisabilityPeriodsLocators.family_member, value, "Член семьи")

    def insurance_experience(self, value):
        self.set_text(DisabilityPeriodsLocators.insurance_experience, value, "Страховой стаж")

    def not_insurance_periods(self, value):
        self.set_text(DisabilityPeriodsLocators.not_insurance_periods, value, "в т.ч. нестраховые периоды")

    def percent(self, value):
        self.set_text(DisabilityPeriodsLocators.percent, value, "Процент оплаты пособия")

    def submit(self):
        self.click(DisabilityPeriodsLocators.submit, "Сохранить")

    class Editing(parent):

        def list_number(self, value):
            self.set_text(DisabilityPeriodsLocators.Editing.list_number, value, "Номер листка")

        def by(self, value):
            self.set_text(DisabilityPeriodsLocators.Editing.by, value, "Кем выдан")

        def note(self, value):
            self.set_text(DisabilityPeriodsLocators.Editing.note, value, "Примечание")

        def period_from(self, value):
            self.set_date(DisabilityPeriodsLocators.Editing.period_from, value, "Период освобождения с")

        def period_to(self, value):
            self.set_date(DisabilityPeriodsLocators.Editing.period_to, value, "Период освобождения по")

        def list_continuing(self, value):
            self.set_select2(DisabilityPeriodsLocators.Editing.list_continuing, value, "Продолжение листка")

        def reason(self, value):
            self.set_select2(DisabilityPeriodsLocators.Editing.reason, value, "Причина нетрудоспособности")

        def family_member(self, value):
            self.set_select2(DisabilityPeriodsLocators.Editing.family_member, value, "Член семьи")

        def insurance_experience(self, value):
            self.set_text(DisabilityPeriodsLocators.Editing.insurance_experience, value, "Страховой стаж")

        def not_insurance_periods(self, value):
            self.set_text(DisabilityPeriodsLocators.Editing.not_insurance_periods, value, "в т.ч. нестраховые периоды")

        def percent(self, value):
            self.set_text(DisabilityPeriodsLocators.Editing.percent, value, "Процент оплаты пособия")

        def submit(self):
            self.click(DisabilityPeriodsLocators.Editing.submit, "Сохранить")


class BusinessTripPage(parent):

    @property
    def routes(self):
        return self.Routes(self.driver)

    def date_start(self, value):
        self.set_date(BusinessTripLocators.date_start, value, "Дата начала командировки")

    def date_end(self, value):
        self.set_date(BusinessTripLocators.date_end, value, "Дата окончания командировки")

    def date_cancelling(self, value):
        self.set_date(BusinessTripLocators.date_cancelling, value, "Дата отмены")

    def date_expansion(self, value):
        self.set_date(BusinessTripLocators.date_expansion, value, "Дата расширения")

    def days_amount(self, value):
        self.set_text(BusinessTripLocators.days_amount, value, "Количество дней")

    def days_amount_without_road(self, value):
        self.set_text(BusinessTripLocators.days_amount_without_road, value, "Количество дней (без дороги)")

    def holidays_amount(self, value):
        self.set_text(BusinessTripLocators.holidays_amount, value, "Количество выходных")

    def working_days_amount(self, value):
        self.set_text(BusinessTripLocators.working_days_amount, value, "Количество рабочих дней")

    def source_financing(self, value):
        self.set_text(BusinessTripLocators.source_financing, value, "Финансирование")

    def is_off_plan(self, value):
        self.set_checkbox(BusinessTripLocators.is_off_plan, value, "Вне плана")

    def is_foreign_trip(self, value):
        self.set_checkbox(BusinessTripLocators.is_foreign_trip, value, "Зарубежная командировка")

    def event(self, value):
        self.set_select(BusinessTripLocators.event, value, "Мероприятие")

    def purpose(self, value):
        self.set_text(BusinessTripLocators.purpose, value, "Цель командировки")

    def reason(self, value):
        self.set_text(BusinessTripLocators.reason, value, "Основание")

    def route(self, value):
        self.set_text(BusinessTripLocators.route, value, "Маршрут")

    def task_number(self, value):
        self.set_text(BusinessTripLocators.task_number, value, "Номер служебного задания")

    def task_date(self, value):
        self.set_text(BusinessTripLocators.task_date, value, "Дата служебного задания")

    def certificate_number(self, value):
        self.set_text(BusinessTripLocators.certificate_number, value, "Командировочное удостоверение №")

    def certificate_date(self, value):
        self.set_text(BusinessTripLocators.certificate_date, value, "Дата командировочного удостоверения")

    def must_be_notify(self, value):
        self.set_checkbox(BusinessTripLocators.must_be_notify, value, "Служащий должен быть ознакомлен с приказом")

    def submit(self):
        self.click(BusinessTripLocators.submit, "Сохранить")

    class Routes(parent):

        def date_start(self, value):
            self.set_date(BusinessTripLocators.Routes.date_start, value, "Дата начала командировки")

        def date_end(self, value):
            self.set_date(BusinessTripLocators.Routes.date_end, value, "Дата окончания командировки")

        def country(self, value):
            self.set_select2(BusinessTripLocators.Routes.country, value, "Страна")

        def organization(self, value):
            self.set_text(BusinessTripLocators.Routes.organization, value, "Организация")

        def days_amount(self, value):
            self.set_text(BusinessTripLocators.Routes.days_amount, value, "Количество дней")

        def submit(self):
            self.click(BusinessTripLocators.Routes.submit, "Сохранить")


class HolidaysPage(parent):

    def statement_date(self, value):
        self.set_date(HolidaysLocators.statement_date, value, "Дата заявления")

    def base(self, value):
        self.set_text(HolidaysLocators.base, value, "Основание")

    def type(self, value):
        self.set_select2(HolidaysLocators.type, value, "Вид отпуска и выходных дней")

    def date_from(self, value):
        self.set_date(HolidaysLocators.date_from, value, "Период отпуска с")

    def count_days(self, value):
        self.set_text(HolidaysLocators.count_days, value, "Количество дней")

    def is_pay_once(self, value):
        self.set_checkbox(HolidaysLocators.is_pay_once, value, "Единовременная выплата")

    def is_material_aid(self, value):
        self.set_checkbox(HolidaysLocators.is_material_aid, value, "Иптериальная помощь")


class RanksPage(parent):

    def condition(self, value):
        self.set_select2(RanksLocators.condition, value, "Условие")

    def type(self, value):
        self.set_select2(RanksLocators.type, value, "Тип")

    def organization(self, value):
        self.set_select2(RanksLocators.organization, value, "Организация")

    def date(self, value):
        self.set_date(RanksLocators.date, value, "Дата присвоения")


class NewPersonnelFilePage(parent):

    def last_name(self, value):
        self.set_text(NewPersonnelFileLocators.last_name, value, "Фамилия")

    def first_name(self, value):
        self.set_text(NewPersonnelFileLocators.first_name, value, "Имя")

    def middle_name(self, value):
        self.set_text(NewPersonnelFileLocators.middle_name, value, "Отчество")

    def birthday_date(self, value):
        self.set_date(NewPersonnelFileLocators.birthday_date, value, "Дата рождения")

    def certificate_number(self, value):
        self.set_text(NewPersonnelFileLocators.certificate_number, value, "Страховой номер индивидуального лицевого счета (СНИЛС)")

    def account(self, value):
        self.set_text(NewPersonnelFileLocators.account, value, "Учетная запись")
