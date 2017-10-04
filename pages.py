from locators import *
from setup import *
from framework import *
import datetime


def change_date(amount=0):
    date = datetime.date.today()
    delta = datetime.timedelta(days=amount)
    now_date = date + delta
    return '%s.%s.%s' % (now_date.day, now_date.month, now_date.year)


def today():
    return datetime.date.today().strftime("%d.%m.%Y")


parent = Browser


class MainPage(parent):

    pass


class LoginPage(parent):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Имя пользователя")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click(LoginLocators.submit, "Войти")

    def login(self, username=None, password=None, full_name=None, data=None):
        if data:
            username = data["username"]
            password = data["password"]
            full_name = data["fullName"]
        self.go_to(Links.main_page)
        if "Войти" in self.driver.page_source:
            self.click_by_text("Войти")
            try:
                drop_down = Wait(self.driver, 3).element_appear((By.XPATH, "//ul[@class='dropdown-menu pull-right']"))
                drop_down.find_element(By.XPATH, "//a[@href='#/login']").click()
            except TimeoutException:
                pass
            self.username(username)
            self.password(password)
            self.submit()
            self.wait_for_text_appear("Личные данные")
        else:
            current_user = self.driver.find_element(By.XPATH, "//a[@href='/Cabinet']")
            if full_name and (full_name in current_user.text):
                self.go_to(Links.dashboard)
            else:
                self.go_to(Links.main_page)
                self.wait_for_loading()
                self.scroll_to_top()
                self.click((By.XPATH, "//input[@type='submit']"))
                self.login(username, password)


class PersonalFilePage(parent):

    @property
    def new(self):
        return self.New(self.driver, self.timeout, self.log)

    @property
    def general(self):
        return self.General(self.driver, self.timeout, self.log)

    class New(parent):

        def last_name(self, value):
            self.set_text(PersonalFileLocators.New.last_name, value, "Фамилия")

        def first_name(self, value):
            self.set_text(PersonalFileLocators.New.first_name, value, "Имя")

        def middle_name(self, value):
            self.set_text(PersonalFileLocators.New.middle_name, value, "Отчество")

        def birthday(self, value):
            self.set_date(PersonalFileLocators.New.birthday, value, "Дата рождения")

        def insurance_certificate_number(self, value):
            self.set_text(PersonalFileLocators.New.insurance_certificate_number, value, "СНИЛС")

        def username(self, value):
            self.set_text(PersonalFileLocators.New.username, value, "Учетная запись")

    class General(parent):

        def general_edit(self):
            self.click(PersonalFileLocators.General.general_edit, "Редактировать общие сведения")

        def last_name(self, value):
            self.set_text(PersonalFileLocators.General.last_name, value, "Фамилия")

        def first_name(self, value):
            self.set_text(PersonalFileLocators.General.first_name, value, "Имя")

        def middle_name(self, value):
            self.set_text(PersonalFileLocators.General.middle_name, value, "Отчество")

        def gender(self, value):
            self.set_select2(PersonalFileLocators.General.gender, value, "Пол")

        def personal_file_number(self, value):
            self.set_text(PersonalFileLocators.General.personal_file_number, value, "Номер личного дела")

        def birthday(self, value):
            self.set_date(PersonalFileLocators.General.birthday, value, "Дата рождения")

        def okato(self, value):
            self.set_text(PersonalFileLocators.General.okato, value, "Место рождения, код по ОКАТО")

        def criminal_record(self, value):
            self.set_select(value, 1, "Наличие судимости")

        def last_name_changing(self, value):
            self.set_select(value, 2, "Сведения об изменении ФИО")

        def addresses_edit(self):
            self.click(PersonalFileLocators.General.addresses_edit, "Редактировать адреса")

        def contacts_edit(self):
            self.click(PersonalFileLocators.General.contact_edit, "Редактировать контактную информацию")


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

    def projects_check(self, timeout=300, interval=1):
        count = 0
        print("Проверка статусов [Интервал=%sс Таймаут=%sс]:" % (interval, timeout))
        while True:
            flag = True
            self.wait_for_loading()
            self.click_by_text("Показать все")
            sleep(1)
            for i in self.driver.find_elements(By.XPATH, "//small[.='Проект']"):
                if i.is_displayed():
                    webdriver.ActionChains(self.driver).move_to_element(i).perform()
                    flag = False
                    break
            count += interval
            sleep(interval)
            self.driver.refresh()
            if (count >= timeout) or flag:
                break
        return flag


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

    def submit(self, full_name, order="123", date="=",
               by="Иванов Иван Иванович", position="Начальник", data=None):
        if data:
            order = data["orderNumber"]
            date = data["orderDate"]
            by = data["orderBy"]
            position = data["orderByPosition"]
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_row_checkbox()
        self.click_by_text("Включить в приказ")
        count = 0
        while True:
            text = self.wait_for_element_appear((By.XPATH,
                                                "//span[contains(@id, 'select2-chosen')]")).text
            if text and text != "Не выбрано":
                break
            sleep(1)
            count += 1
            if count == self.timeout:
                print("TimeoutException: Поле Организация не заполнено!")
                raise TimeoutException
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

    def submit_business_trips(self, full_name, order="123", date="=",
                              by="Иванов Иван Иванович", position="Начальник", data=None):
        if data:
            order = data["orderNumber"]
            date = data["orderDate"]
            by = data["orderBy"]
            position = data["orderByPosition"]
        self.click_by_text("Фильтр")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[1]"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_row_checkbox()
        self.click_by_text("Включить в приказ")
        count = 0
        while True:
            text = self.wait_for_element_appear((By.XPATH,
                                                "//span[contains(@id, 'select2-chosen')]")).text
            if text and text != "Не выбрано":
                break
            sleep(1)
            count += 1
            if count == self.timeout:
                print("TimeoutException: Поле Организация не заполнено!")
                raise TimeoutException
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
            sleep(1)

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
        sleep(1)
        self.set_checkbox((By.XPATH, "//tr[contains(., '%s')]//input" % value), True, "Выбор сотрудника")
        sleep(1)
        self.scroll_to_top()

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


class RolesManagementPage(parent):

    def search(self, value):
        self.set_text(RolesManagementLocators.search, value+Keys.RETURN, "Роль")

    def name(self, value):
        self.set_text(RolesManagementLocators.name, value, "Наименование")

    def is_require_organization(self, value):
        self.set_checkbox(RolesManagementLocators.is_require_organization,
                          value, "Привязывается к организации/подразделению")

    def level(self, value):
        self.set_select2(RolesManagementLocators.level, value, "Уровень доверия")

    def roles(self, value):
        self.set_select2(RolesManagementLocators.roles, value, "Роли")


class VacancySearchPage(parent):
    def type_source_vacancy(self, value):
        self.set_select2_alt(VacancySearchLocators.type_source_vacancy, value, "Тип источника вакансии")

    def name_source_vacancy(self, value):
        self.set_text(VacancySearchLocators.name_source_vacancy, value, "Наименование источника вакансии")

    def name_vacant_position(self, value):
        self.set_text(VacancySearchLocators.name_vacant_position, value, "Наименование вакантной должности")

    def type_vacancy(self, value):
        self.set_select2_alt(VacancySearchLocators.type_vacancy, value, "Тип вакансии")

    def substitution_competition(self, value):
        self.set_select(value, 1, "Замещение по конкурсу")

    def electronic_documents(self, value):
        self.set_select(value, 2, "Прием документов в ЭВ")

    def profile_activity_organization(self, value):
        self.set_select2_alt(VacancySearchLocators.profile_activity_organization,
                             value, "Профиль деятельности организации")

    def field_professional_activity(self, value):
        self.set_select2_alt(VacancySearchLocators.field_professional_activity,
                             value, "Область профессиональной деятельности")

    def key_word(self, value):
        self.set_text(VacancySearchLocators.key_word, value, "Ключевое слово")

    def category_job(self, value):
        self.set_select2_alt(VacancySearchLocators.category_job, value, "Категория должности")

    def group_job(self, value):
        self.set_select2_alt(VacancySearchLocators.group_job, value, "Группа должности")

    def subject_workplace(self, value):
        self.set_select2(VacancySearchLocators.subject_workplace, value, "Расположение рабочего места (субъект)")

    def region_workplace(self, value):
        self.set_select2(VacancySearchLocators.region_workplace, value, "Расположение рабочего места (регион)")

    def salary_from(self, value):
        self.set_text(VacancySearchLocators.salary_from, value, "Размер оплаты труда от")

    def salary_to(self, value):
        self.set_text(VacancySearchLocators.salary_to, value, "Размер оплаты труда до")

    def business_trip(self, value):
        self.set_select2(VacancySearchLocators.business_trip, value, "Командировки")

    def work_day(self, value):
        self.set_select2(VacancySearchLocators.work_day, value, "Рабочий день")

    def type_service_contract(self, value):
        self.set_select(value, 3, "Тип служебного контракта (трудового договора)")

    def normal_workday(self, value):
        self.set_select(value, 4, "Нормированный рабочий день")

    def day_start_accept_document_from(self, value):
        self.set_date(VacancySearchLocators.day_start_accept_document_from, value, "Дата начала приема документов с")

    def day_start_accept_document_to(self, value):
        self.set_date(VacancySearchLocators.day_start_accept_document_to, value, "Дата начала приема документов по")

    def day_stop_accept_document_from(self, value):
        self.set_date(VacancySearchLocators.day_stop_accept_document_from, value, "Дата окончания приема документов с")

    def day_stop_accept_document_to(self, value):
        self.set_date(VacancySearchLocators.day_stop_accept_document_to, value, "Дата окончания приема документов по")

    def level_education(self, value):
        self.set_select2_alt(VacancySearchLocators.level_education, value, "Уровень образования")

    def service_experience(self, value):
        self.set_select2_alt(VacancySearchLocators.service_experience, value, "Стаж государственной службы")

    def work_experience_speciality(self, value):
        self.set_select2_alt(VacancySearchLocators.work_experience_speciality, value, "Опыт работы по специальности")


class VacancyControlPage(parent):
    def checkbox_selection_vacancy_second(self):
        self.table_select_row("Выбрана вакансия вторая")

    def status_response(self, value):
        self.set_select2_alt(VacancyControlLocators.status_response, value, "Статус отклика")

    def is_date_vacancy(self):
        self.wait_for_loading()
        elements = self.driver.find_elements_by_xpath("//tr[@class='ng-scope']//td[7]")
        texts = []
        for i in elements:
            texts.append(i.text.split()[0])
        return str(datetime.date.today().day) in texts

    def key_word(self, value):
        self.set_text(VacancyControlLocators.key_word, value, "Ключевое слово")


class DocumentsPage(parent):
    @property
    def documents(self):
        return self.Documents(self.driver, self.timeout, self.log)

    @property
    def personal_main(self):
        return self.PersonalMain(self.driver, self.timeout, self.log)

    @property
    def personal_contact(self):
        return self.PersonalContact(self.driver, self.timeout, self.log)

    @property
    def identification_document(self):
        return self.IdentificationDocument(self.driver, self.timeout, self.log)

    @property
    def education(self):
        return self.Education(self.driver, self.timeout, self.log)

    @property
    def labor_activity(self):
        return self.LaborActivity(self.driver, self.timeout, self.log)

    @property
    def class_rank(self):
        return self.ClassRank(self.driver, self.timeout, self.log)

    @property
    def specialization(self):
        return self.Specialization(self.driver, self.timeout, self.log)

    @property
    def award(self):
        return self.Award(self.driver, self.timeout, self.log)

    @property
    def state_secret(self):
        return self.StateSecret(self.driver, self.timeout, self.log)

    @property
    def military(self):
        return self.Military(self.driver, self.timeout, self.log)

    @property
    def kin(self):
        return self.Kin(self.driver, self.timeout, self.log)

    def has_appform(self):
        self.driver.get(Links.application_form)
        self.wait_for_loading()
        if "Анкета 667" in self.driver.page_source:
            self.click_by_text("Анкета 667")
            self.wait_for_loading()
        else:
            self.click_by_text("Добавить")
            self.wait_for_text_appear("Загрузить")

    class Documents(parent):

        def type_document(self, value):
            self.set_select2(DocumentsLocators.Documents.type_document, value, "Тип документа")

        def name_document(self, value):
            self.set_text(DocumentsLocators.Documents.name_document, value, "Наименование")

    class PersonalMain(parent):

        def last_name(self, value):
            self.set_text(DocumentsLocators.PersonalMain.lastname, value, "Фамилия")

        def first_name(self, value):
            self.set_text(DocumentsLocators.PersonalMain.firstname, value, "Имя")

        def middle_name(self, value):
            self.set_text(DocumentsLocators.PersonalMain.middlename, value, "Отчество")

        def gender(self, value):
            self.set_select2(DocumentsLocators.PersonalMain.gender, value, "Пол")

        def individual_taxpayer_number(self, value):
            self.set_text(DocumentsLocators.PersonalMain.individual_taxpayer_number, value, "СНИЛС")

        def insurance_certificate_number(self, value):
            self.set_text(DocumentsLocators.PersonalMain.insurance_certificate_number, value, "СНИЛС")

        def birth_date(self, value):
            self.set_date(DocumentsLocators.PersonalMain.birthdate, value, "Дата рождения")

        def citizenship(self, value):
            self.set_select2(DocumentsLocators.PersonalMain.citizenship, value, "Гражданство")

        def change_citizenship(self, value):
            self.set_select(value, 1, "Изменение гражданства")

        def birthplace(self, value):
            self.set_text(DocumentsLocators.PersonalMain.birthplace, value, "Место рождения")

        def was_convicted(self, value):
            self.set_select(value, 2, "Наличие судимостей")

        def marital_statuses(self, value):
            self.set_select2(DocumentsLocators.PersonalMain.maritalstatuses, value, "Семейное положение")

        def name_was_changed(self, value):
            self.set_select(value, 3, "Сведения об изменении ФИО")

        def was_abroad(self, value):
            self.set_select(value, 4, "Пребывание за границей")

        def selection_radio(self):
            self.click(DocumentsLocators.PersonalMain.selection_radio, "Выбор анкеты")

    class PersonalContact(parent):

        def work_phone(self, value):
            self.set_text(DocumentsLocators.PersonalContact.work_phone, value, "Рабочий телефон")

        def mobile_phone(self, value):
            self.set_text(DocumentsLocators.PersonalContact.mobile_phone, value, "Мобильный телефон")

        def additional_phone(self, value):
            self.set_text(DocumentsLocators.PersonalContact.additional_phone, value, "Дополнительный телефон")

        def fax(self, value):
            self.set_text(DocumentsLocators.PersonalContact.fax, value, "Факс")

        def work_email(self, value):
            self.set_text(DocumentsLocators.PersonalContact.work_email, value, "Рабочая электронная почта")

        def personal_email(self, value):
            self.set_text(DocumentsLocators.PersonalContact.personal_email, value, "Персональная электронная почта")

        def web_address(self, value):
            self.set_text(DocumentsLocators.PersonalContact.web_address, value, "Персональная интернет-страница")

        def permanent_registration_sub(self, value):
            self.set_select2(
                DocumentsLocators.PersonalContact.permanent_registration, value, "Постоянная регистрация - субъект")

        def permanent_registration_reg(self, value):
            self.set_select2(
                DocumentsLocators.PersonalContact.permanent_registration_reg, value, "Постоянная регистрация - регион")

        def temp_registration_sub(self, value):
            self.set_select2(
                DocumentsLocators.PersonalContact.temp_registration_sub, value, "Временная регистрация - субъект")

        def temp_registration_reg(self, value):
            self.set_select2(
                DocumentsLocators.PersonalContact.temp_registration_reg, value, "Временная регистрация - регион")

        def fact_registration_sub(self, value):
            self.set_select2(
                DocumentsLocators.PersonalContact.fact_registration_sub, value, "Фактическое проживание - субъект")

        def fact_registration_reg(self, value):
            self.set_select2(
                DocumentsLocators.PersonalContact.fact_registration_reg, value, "Фактическое проживание - регион")

    class IdentificationDocument(parent):

        def type_document(self, value):
            self.set_select2(DocumentsLocators.IdentificationDocument.type_document, value, "Тип документа")

        def series(self, value):
            self.set_text(DocumentsLocators.IdentificationDocument.series, value, "Серия")

        def number(self, value):
            self.set_text(DocumentsLocators.IdentificationDocument.number, value, "Номер")

        def date_issued(self, value):
            self.set_date(DocumentsLocators.IdentificationDocument.date_issued, value, "Дата выдачи")

        def date_end(self, value):
            self.set_date(DocumentsLocators.IdentificationDocument.date_end, value, "Дата окончания действия")

        def issue_by(self, value):
            self.set_text(DocumentsLocators.IdentificationDocument.issue_by, value, "Кем выдан")

        def issue_code(self, value):
            self.set_text(DocumentsLocators.IdentificationDocument.issue_code, value, "Код подразделения")

    class Education(parent):

        @property
        def main(self):
            return self.Main(self.driver, self.timeout, self.log)

        @property
        def egc(self):
            return self.Egc(self.driver, self.timeout, self.log)

        @property
        def degree(self):
            return self.Degree(self.driver, self.timeout, self.log)

        @property
        def languages(self):
            return self.Languages(self.driver, self.timeout, self.log)

        @property
        def dpo(self):
            return self.Dpo(self.driver, self.timeout, self.log)

        class Main(parent):
            def education_level(self, value):
                self.set_select2(DocumentsLocators.Education.Main.education_level, value, "Образовательный уровень")

            def education(self, value):
                self.set_select2(DocumentsLocators.Education.Main.education, value, "Образование")

            def education_form(self, value):
                self.set_select2(DocumentsLocators.Education.Main.education_form, value, "Форма обучения")

            def place_institution(self, value):
                self.set_text(
                    DocumentsLocators.Education.Main.place_institution, value, "Расположение учебного заведения")

            def full_name_institution(self, value):
                self.set_select2(
                    DocumentsLocators.Education.Main.full_name_institution, value, "Полное название учебного заведения")

            def start_date_education(self, value):
                self.set_text(DocumentsLocators.Education.Main.start_date_education, value, "Год начала")

            def end_date_education(self, value):
                self.set_text(DocumentsLocators.Education.Main.end_date_education, value, "Год окончания")

            def education_directions(self, value):
                self.set_select2(
                    DocumentsLocators.Education.Main.education_directions, value, "Направление образования (форма 1ГС)")

            def faculty(self, value):
                self.set_text(DocumentsLocators.Education.Main.faculty, value, "Факультет")

            def education_doc_number(self, value):
                self.set_text(DocumentsLocators.Education.Main.education_doc_number, value, "Номер диплома")

            def education_doc_date(self, value):
                self.set_date(DocumentsLocators.Education.Main.education_doc_date, value, "Дата выдачи диплома")

            def speciality(self, value):
                self.set_select2(
                    DocumentsLocators.Education.Main.speciality, value,
                    "Специальность / направление подготовки по диплому")

            def qualification(self, value):
                self.set_select2(DocumentsLocators.Education.Main.qualification, value, "Квалификация по диплому")

            def specialization(self, value):
                self.set_text(DocumentsLocators.Education.Main.specialization, value, "Специализация по диплому")

            def is_main(self, value):
                self.set_checkbox(DocumentsLocators.Education.Main.is_main, value, "Основное")

        class Egc(parent):
            def education(self, value):
                self.set_select2(
                    DocumentsLocators.Education.Egc.egc_education, value, "Послевузовское профессиональное образование")

            def place(self, value):
                self.set_text(DocumentsLocators.Education.Egc.egc_place, value, "Расположение учебного заведения")

            def name_institution(self, value):
                self.set_text(DocumentsLocators.Education.Egc.egc_name_institution, value,
                              "Название учебного заведения")

            def start_date(self, value):
                self.set_text(DocumentsLocators.Education.Egc.egc_start_date, value, "Год начала")

            def end_date(self, value):
                self.set_text(DocumentsLocators.Education.Egc.egc_end_date, value, "Год окончания")

            def academic_degree(self, value):
                self.set_select2(DocumentsLocators.Education.Egc.egc_academic_degree, value, "Ученая степень")

            def academic_degree_date(self, value):
                self.set_date(
                    DocumentsLocators.Education.Egc.egc_academic_degree_date, value, "Дата присвоения ученой степени")

            def knowledge_branches(self, value):
                self.set_select2(DocumentsLocators.Education.Egc.egc_knowledge_branches, value, "Отрасль наук")

            def diplom_number(self, value):
                self.set_text(DocumentsLocators.Education.Egc.egc_diplom_number, value, "Номер диплома")

            def diplom_date(self, value):
                self.set_date(DocumentsLocators.Education.Egc.egc_diplom_date, value, "Дата выдачи диплома")

        class Degree(parent):
            def academic_statuses(self, value):
                self.set_select2(DocumentsLocators.Education.Degree.academic_statuses, value, "Учёное звание")

            def diplom_number(self, value):
                self.set_text(DocumentsLocators.Education.Degree.diplom_number, value, "Номер аттестата")

            def assigment_date(self, value):
                self.set_date(
                    DocumentsLocators.Education.Degree.assigment_date, value, "Дата присвоения ученого звания")

        class Languages(parent):
            def languages(self, value):
                self.set_select2(DocumentsLocators.Education.Languages.languages, value, "Язык")

            def language_degrees(self, value):
                self.set_select2(DocumentsLocators.Education.Languages.language_degrees, value, "Уровень владения")

        class Dpo(parent):
            def education_direction(self, value):
                self.set_select2(DocumentsLocators.Education.Dpo.education_direction, value, "Направление подготовки")

            def education_kind(self, value):
                self.set_select2(DocumentsLocators.Education.Dpo.education_kind, value, "Вид образовательной программы")

            def kind(self, value):
                self.set_text(DocumentsLocators.Education.Dpo.kind, value, "Вид повышения квалификации")

            def name_program(self, value):
                self.set_text(DocumentsLocators.Education.Dpo.name_program, value, "Название программы")

            def education_form(self, value):
                self.set_select2(DocumentsLocators.Education.Dpo.education_form, value, "Форма обучения")

            def place(self, value):
                self.set_text(DocumentsLocators.Education.Dpo.place, value, "Расположение учебного заведения")

            def name_institution(self, value):
                self.set_text(
                    DocumentsLocators.Education.Dpo.name_institution, value, "Наименование учебного заведения")

            def start_date(self, value):
                self.set_select2(DocumentsLocators.Education.Dpo.start_date, value, "Год начала")

            def end_date(self, value):
                self.set_select2(DocumentsLocators.Education.Dpo.end_date, value, "Год окончания")

            def hours(self, value):
                self.set_text(DocumentsLocators.Education.Dpo.hours, value, "Количество часов")

            def document_number(self, value):
                self.set_text(
                    DocumentsLocators.Education.Dpo.document_number, value, "Документ о ДПО (наименование, номер)")

            def document_date(self, value):
                self.set_date(DocumentsLocators.Education.Dpo.document_date, value, "Дата документа о ДПО")

            def funding_sources(self, value):
                self.set_select2(DocumentsLocators.Education.Dpo.funding_sources, value, "Источник финансирования")

    class LaborActivity(parent):

        def start_date(self, value):
            self.set_date(DocumentsLocators.LaborActivity.begin_date, value, "Начало деятельности")

        def end_date(self, value):
            self.set_date(DocumentsLocators.LaborActivity.end_date, value, "Окончание деятельности")

        def post(self, value):
            self.set_text(DocumentsLocators.LaborActivity.post, value, "Должность")

        def organization(self, value):
            self.set_text(DocumentsLocators.LaborActivity.organization, value, "Организация")

        def address_organization(self, value):
            self.set_text(DocumentsLocators.LaborActivity.address_organization, value, "Адрес организации")

        def employees_number(self, value):
            self.set_select2(DocumentsLocators.LaborActivity.employees_number, value, "Количество сотрудников")

        def subject(self, value):
            self.set_select2(DocumentsLocators.LaborActivity.subject, value, "Субъект расположения организации")

        def region(self, value):
            self.set_select2(DocumentsLocators.LaborActivity.region, value, "Регион расположения организации")

        def profile(self, value):
            self.set_select2(DocumentsLocators.LaborActivity.profile, value, "Профиль деятельности организации")

        def is_elective(self, value):
            self.move_to_element(self.wait_for_element_appear((By.XPATH, "//button[.='Сохранить']")))
            self.set_checkbox(DocumentsLocators.LaborActivity.is_elective, value, "Выборная должность")

        def post_level(self, value):
            self.set_select2(DocumentsLocators.LaborActivity.post_level, value, "Уровень должности")

        def activity_area(self, value):
            self.set_select2(
                DocumentsLocators.LaborActivity.activity_area, value, "Область профессиональной деятельности")

        def structural_division(self, value):
            self.set_text(DocumentsLocators.LaborActivity.structural_division, value, "Подразделение")

        def responsibilities(self, value):
            self.set_text(DocumentsLocators.LaborActivity.responsibilities, value, "Функции/обязанности")

    class ClassRank(parent):

        def has_class_rank(self, value):
            self.set_checkbox(DocumentsLocators.ClassRank.has_class_rank, value, "Имеется ли классный чин")

        def class_rank(self, value):
            self.set_text(DocumentsLocators.ClassRank.class_rank, value, "Классный чин")

        def assigned_date(self, value):
            self.set_date(DocumentsLocators.ClassRank.assigned_date, value, "Когда присвоен")

        def assigned_by(self, value):
            self.set_text(DocumentsLocators.ClassRank.assigned_by, value, "Кем присвоен")

        def has_government_service(self, value):
            self.set_checkbox(
                DocumentsLocators.ClassRank.has_government_service, value, "Государственная или муниципальная служба")

        def org_sub_types(self, value):
            self.set_select2(DocumentsLocators.ClassRank.org_sub_types, value, "Направление")

        def organization_name(self, value):
            self.set_text(DocumentsLocators.ClassRank.organization_name, value, "Организация")

        def computer_skills(self, value):
            self.set_text(DocumentsLocators.ClassRank.computer_skills, value, "Владение персональным компьютером")

        def publications(self, value):
            self.set_text(DocumentsLocators.ClassRank.publications, value, "Публикации")

        def recommendations(self, value):
            self.set_text(DocumentsLocators.ClassRank.recommendations, value, "Рекомендации")

    class Specialization(parent):

        def specialization(self, value):
            self.set_select2(DocumentsLocators.Specialization.work, value, "Специализация")

        def is_main(self, value):
            self.set_checkbox(DocumentsLocators.Specialization.is_main, value, "Основная")

        def is_add(self, value):
            self.set_checkbox(DocumentsLocators.Specialization.is_add, value, "Дополнительная")

    class Award(parent):

        def type(self, value):
            self.set_select2(DocumentsLocators.Award.type, value, "Вид")

        def name(self, value):
            self.set_text(DocumentsLocators.Award.name, value, "Наименование")

        def date(self, value):
            self.set_text(DocumentsLocators.Award.date, value, "Дата")

    class StateSecret(parent):

        def admission_form(self, value):
            self.set_select2(DocumentsLocators.StateSecret.admission_form, value, "Форма допуска")

        def approval_number(self, value):
            self.set_text(DocumentsLocators.StateSecret.approval_number, value, "Номер допуска")

        def issue_date(self, value):
            self.set_date(DocumentsLocators.StateSecret.issue_date, value, "Дата")

    class Military(parent):

        def rank(self, value):
            self.set_select2(DocumentsLocators.Military.rank, value, "Воинское звание")

        def duty(self, value):
            self.set_select2(DocumentsLocators.Military.duty, value, "Воинская обязанность")

        def has_service(self, value):
            self.set_checkbox(
                DocumentsLocators.Military.has_service, value, "Проходили ли срочную военную службу?")

        def service_from(self, value):
            self.set_date(DocumentsLocators.Military.service_from, value, "Начало службы")

        def service_to(self, value):
            self.set_date(DocumentsLocators.Military.service_to, value, "Род войск")

        def arm_kind(self, value):
            self.set_text(DocumentsLocators.Military.arm_kind, value, "Окончание службы")

    class Kin(parent):

        def kin_ship(self, value):
            self.set_select2(DocumentsLocators.Kin.ship, value, "Степень родства")

        def last_name(self, value):
            self.set_text(DocumentsLocators.Kin.lastname, value, "Фамилия")

        def first_name(self, value):
            self.set_text(DocumentsLocators.Kin.firstname, value, "Имя")

        def middle_name(self, value):
            self.set_text(DocumentsLocators.Kin.middlename, value, "Отчество")

        def name_changes(self, value):
            self.set_text(
                DocumentsLocators.Kin.name_changes, value, "Изменения ФИО (старое значение, дата, причина)")

        def birth_country(self, value):
            self.set_select2(DocumentsLocators.Kin.birth_country, value, "Место рождения (страна)")

        def birth_region(self, value):
            self.set_select2(DocumentsLocators.Kin.birth_region, value, "Место рождения (субъект)")

        def birth_area(self, value):
            self.set_select2(DocumentsLocators.Kin.birth_area, value, "Место рождения (район)")

        def birth_place(self, value):
            self.set_text(DocumentsLocators.Kin.birth_place, value, "Место рождения")

        def work_place(self, value):
            self.set_text(DocumentsLocators.Kin.work_place, value, "Место работы (наим. и ад. орг.), должность")

        def living_country(self, value):
            self.set_select2(DocumentsLocators.Kin.living_country, value, "Cтрана проживания")

        def living_address(self, value):
            self.set_text(DocumentsLocators.Kin.living_address, value, "Домашний адрес")

        def birth_date(self, value):
            self.set_date(DocumentsLocators.Kin.birth_date, value, "Дата рождения")


class ProfilePage(parent):

    def last_name(self, value):
        self.set_text(ProfileLocators.lastname, value, "Фамилия")

    def first_name(self, value):
        self.set_text(ProfileLocators.firstname, value, "Имя")

    def middle_name(self, value):
        self.set_text(ProfileLocators.middlename, value, "Отчество")

    def birth_date(self, value):
        self.set_date(ProfileLocators.birthdate, value, "Дата рождения")

    def insurance_certificate_number(self, value):
        self.set_text(ProfileLocators.insurance_certificate_number, value, "СНИЛС")

    def individual_taxpayer_number(self, value):
        self.set_text(ProfileLocators.individual_taxpayer_number, value, "ИНН")

    def email(self, value):
        self.set_text(ProfileLocators.email, value, "Электронная почта")

    def passport_info(self, value):
        self.set_text(ProfileLocators.passport_info, value, "Паспортные данные")

    def registration_address(self, value):
        self.set_text(ProfileLocators.registration_address, value, "Адрес регистрации")

    def actual_address(self, value):
        self.set_text(ProfileLocators.actual_address, value, "Адрес проживания")

    def old_password(self, value):
        self.set_text(ProfileLocators.old_password, value, "Пароль")

    def password(self, value):
        self.set_text(ProfileLocators.password, value, "Новый пароль")

    def password_confirm(self, value):
        self.set_text(ProfileLocators.password_confirm, value, "Подтверждение пароля")

    def change(self):
        self.click(ProfileLocators.change)


class OrganizationsPage(parent):

    @property
    def filter(self):
        return self.Filter(self.driver, self.timeout, self.log)

    @property
    def new(self):
        return self.New(self.driver, self.timeout, self.log)

    @property
    def edit(self):
        return self.Edit(self.driver, self.timeout, self.log)

    class Filter(parent):

        def status(self, value):
            self.scroll_to_top()
            self.select2_clear((By.XPATH, "//ul[@class='select2-choices']/li/a"))
            self.click((By.XPATH, "//div[contains(@id, 's2id')]"))
            self.set_text((By.XPATH, "//input"), value, "Статус")
            self.click((By.XPATH, "//div[@role='option']"))

        def name(self, value):
            self.set_text((By.XPATH, "//input[@ng-model='query.filter.name']"), value, "Наименование")
            sleep(1)

    class New(parent):

        def code(self, value):
            self.set_text(OrganizationsLocators.New.code, value, "Код")

        def name(self, value):
            self.set_text(OrganizationsLocators.New.name, value, "Наименование")

        def name_genitive(self, value):
            self.set_text(OrganizationsLocators.New.name_genitive, value, "Наименование в родительном падеже")

        def name_dative(self, value):
            self.set_text(OrganizationsLocators.New.name_dative, value, "Наименование в дательном падеже")

        def name_accusative(self, value):
            self.set_text(OrganizationsLocators.New.name_accusative, value, "Наименование в винительном падеже")

        def short_name(self, value):
            self.set_text(OrganizationsLocators.New.short_name, value, "Краткое наименование")

        def source_type(self, value):
            self.set_select2(OrganizationsLocators.New.source_type, value, "Тип источника данных")

        def region(self, value):
            self.set_select2(OrganizationsLocators.New.region, value, "Субъект")

        def area(self, value):
            self.set_select2(OrganizationsLocators.New.area, value, "Район")

        def profile(self, value):
            self.set_select2(OrganizationsLocators.New.profile, value, "Профиль деятельности")

        def code_okogu(self, value):
            self.set_select2(OrganizationsLocators.New.code_okogu, value, "Код ОКОГУ")

        def code_okpo(self, value):
            self.set_text(OrganizationsLocators.New.code_okpo, value, "Код ОКПО")

        def limit(self, value):
            self.set_text(OrganizationsLocators.New.limit,
                          value, "Лимит количества подключаемых к Порталу пользователей")

        def positions_registry(self, value):
            self.set_select2(OrganizationsLocators.New.positions_registry, value, "Раздел реестра должностей")

        def site(self, value):
            self.set_text(OrganizationsLocators.New.site, value, "Официальный сайт")

        def contacts(self, value):
            self.set_text(OrganizationsLocators.New.contacts, value, "Контактные сведения")

        def participate_in_rotation(self, value):
            self.set_checkbox(OrganizationsLocators.New.participate_in_rotation, value, "Участвует в ротации")

        def is_expired(self, value):
            self.set_checkbox(OrganizationsLocators.New.is_expired, value, "Создается на срок")

        def for_public_open_part(self, value):
            self.set_checkbox(OrganizationsLocators.New.for_public_open_part,
                              value, "Опубликовать сведения в открытой части")

        def creation_order_number(self, value):
            self.set_date(OrganizationsLocators.New.creation_order_number, value, "Номер документа")

        def creation_order_date(self, value):
            self.set_date(OrganizationsLocators.New.creation_order_date, value, "Дата документа")

        def creation_date(self, value):
            self.set_date(OrganizationsLocators.New.creation_date, value, "Ввести в действие с")

    class Edit(parent):

        @property
        def attributes(self):
            return self.Attributes(self.driver, self.timeout, self.log)

        @property
        def activity(self):
            return self.Activity(self.driver, self.timeout, self.log)

        @property
        def positions(self):
            return self.Positions(self.driver, self.timeout, self.log)

        @property
        def curator(self):
            return self.Curator(self.driver, self.timeout, self.log)

        @property
        def template(self):
            return self.Template(self.driver, self.timeout, self.log)

        def open(self):
            self.click((By.XPATH, "//td//a//span[@class='custom-icon-edit']"), "Редактировать")

        class Attributes(parent):

            def code(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.code, value, "Код")

            def name(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.name, value, "Наименование")

            def name_genitive(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.name_genitive,
                              value, "Наименование в родительном падеже")

            def name_dative(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.name_dative,
                              value, "Наименование в дательном падеже")

            def name_accusative(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.name_accusative,
                              value, "Наименование в винительном падеже")

            def short_name(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.short_name, value, "Краткое наименование")

            def source_type(self, value):
                self.set_select2(OrganizationsLocators.Edit.Attributes.source_type, value, "Тип источника данных")

            def region(self, value):
                self.set_select2(OrganizationsLocators.Edit.Attributes.region, value, "Субъект")

            def area(self, value):
                self.set_select2(OrganizationsLocators.Edit.Attributes.area, value, "Район")

            def profile(self, value):
                self.set_select2(OrganizationsLocators.Edit.Attributes.profile, value, "Профиль деятельности")

            def code_okogu(self, value):
                self.set_select2(OrganizationsLocators.Edit.Attributes.code_okogu, value, "Код ОКОГУ")

            def code_okpo(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.code_okpo, value, "Код ОКПО")

            def limit(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.limit, value,
                              "Лимит количества подключаемых к Порталу пользователей")

            def positions_registry(self, value):
                self.set_select2(OrganizationsLocators.Edit.Attributes.positions_registry,
                                 value, "Раздел реестра должностей")

            def site(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.site, value, "Официальный сайт")

            def contacts(self, value):
                self.set_text(OrganizationsLocators.Edit.Attributes.contacts, value, "Контактные сведения")

            def participate_in_rotation(self, value):
                self.set_checkbox(OrganizationsLocators.Edit.Attributes.participate_in_rotation,
                                  value, "Участвует в ротации")

            def is_expired(self, value):
                self.set_checkbox(OrganizationsLocators.Edit.Attributes.is_expired, value, "Создается на срок")

            def for_public_open_part(self, value):
                self.set_checkbox(OrganizationsLocators.Edit.Attributes.for_public_open_part, value,
                                  "Опубликовать сведения в открытой части")

            def creation_order_number(self, value):
                self.set_date(OrganizationsLocators.Edit.Attributes.creation_order_number, value, "Номер документа")

            def creation_order_date(self, value):
                self.set_date(OrganizationsLocators.Edit.Attributes.creation_order_date, value, "Дата документа")

            def creation_date(self, value):
                self.set_date(OrganizationsLocators.Edit.Attributes.creation_date, value, "Ввести в действие с")

            def abolition_order_number(self, value):
                self.set_date(OrganizationsLocators.Edit.Attributes.abolition_order_number,
                              value, "Номер документа")

            def abolition_order_date(self, value):
                self.set_date(OrganizationsLocators.Edit.Attributes.abolition_order_date, value, "Дата документа")

            def abolition_date(self, value):
                self.set_date(OrganizationsLocators.Edit.Attributes.abolition_date, value, "Упразднить с")

        class Activity(parent):

            def direction(self, value):
                self.set_select2((By.XPATH, "//*[@id='s2id_activity']"),
                                 value, "Направление деятельности")

        class Positions(parent):

            def filter(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.filter,
                                 value, "Фильтр по разделу реестра должностей")

            def position(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.position, value, "Должность")

            def holiday_for_irregular_day(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.holiday_for_irregular_day,
                              value, "Продолжительность отпуска за ненормированный день")

            def code(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.code, value, "Код")

            def name(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.name, value, "Наименование полное")

            def short_name(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.short_name, value, "Наименование краткое")

            def name_genitive(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.name_genitive,
                              value, "Наименования в родительном падеже")

            def name_dative(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.name_dative,
                              value, "Наименование в дательном падеже")

            def name_accusative(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.name_accusative,
                              value, "Наименование в винительном падеже")

            def name_instrumental(self, value):
                self.set_text(OrganizationsLocators.Edit.Positions.name_instrumental,
                              value, "Наименование в творительном падеже")

            def type(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.type, value, "Вид должности")

            def group(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.group, value, "Группа должности")

            def can_be_rotated(self, value):
                self.set_checkbox(OrganizationsLocators.Edit.Positions.can_be_rotated, value, "Подлежит ротации")

            def submit_information_on_the_income(self, value):
                self.set_checkbox(OrganizationsLocators.Edit.Positions.submit_information_on_the_income, value,
                                  "Назначенные сотрудники подают справки о доходах и расходах")

            def professional_experience(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.professional_experience,
                                 value, "Требования к стажу по специальности")

            def government_experience(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.government_experience,
                                 value, "Требования к стажу государственной службы")

            def education_level(self, value):
                self.set_select2(OrganizationsLocators.Edit.Positions.education_level,
                                 value, "Требования к образованию")

        class Curator(parent):

            def applications(self, value):
                self.set_select2(OrganizationsLocators.Edit.Curator.applications, value, "Заявки на ДПО")

        class Template(parent):

            def region(self, value):
                self.set_select2(OrganizationsLocators.Edit.Template.region, value, "Расположение рабочего места")

            def area(self, value):
                self.set_select2(OrganizationsLocators.Edit.Template.area, value, "Расположение рабочего места")

            def business_trips(self, value):
                self.set_select2(OrganizationsLocators.Edit.Template.business_trips, value, "Командировки")

            def working_days(self, value):
                self.set_select2(OrganizationsLocators.Edit.Template.working_days, value, "Рабочий день")

            def working_schedule(self, value):
                self.set_select2(OrganizationsLocators.Edit.Template.working_schedule, value, "Рабочее время")

            def type(self, value):
                self.set_select2(
                    OrganizationsLocators.Edit.Template.type, value, "Тип служебного контракта (трудового договора)")
                self.set_select2(OrganizationsLocators.Edit.Template.type,
                                 value, "Тип служебного контракта (трудового договора)")

            def location(self, value):
                self.set_text(OrganizationsLocators.Edit.Template.location, value, "Место приема документов")

            def time(self, value):
                self.set_text(OrganizationsLocators.Edit.Template.time, value, "Время приема документов")

            def post_index(self, value):
                self.set_select2(OrganizationsLocators.Edit.Template.post_index, value, "Почтовый адрес")

            def web_site(self, value):
                self.set_text(OrganizationsLocators.Edit.Template.web_site, value, "Интернет-сайт")


class VacancyCreatePage(parent):
    @property
    def post_is_competition(self):
        return self.PostIsCompetition(self.driver, self.timeout, self.log)

    @property
    def reserve_post(self):
        return self.ReservePost(self.driver, self.timeout, self.log)

    @property
    def reserve_group_posts(self):
        return self.ReserveGroupPosts(self.driver, self.timeout, self.log)

    @property
    def vacant_study(self):
        return self.VacantStudy(self.driver, self.timeout, self.log)

    @property
    def vacant_state(self):
        return self.VacantState(self.driver, self.timeout, self.log)

    def type_vacancy(self, value):
        self.set_select2(VacancyCreateLocators.type_vacancy, value, "Тип объявления")

    def organization(self, value):
        self.set_select2(VacancyCreateLocators.organization, value, "Организация ")

    def is_competition(self, value):
        self.set_checkbox_by_order(1, value, "Замещение по конкурсу")

    def reason(self, value):
        self.set_text(VacancyCreateLocators.reason, value, "Причина")

    def work_type_other_text(self, value):
        self.set_text(VacancyCreateLocators.work_type_other_text, value, "Уточненный профиль деятельности организации")

    def salary_from(self, value):
        self.set_text(
            VacancyCreateLocators.salary_from, value, "Примерный размер денежного содержания (оплаты труда) от")

    def salary_to(self, value):
        self.set_text(VacancyCreateLocators.salary_to, value, "до")

    def social_package_text(self, value):
        self.set_text(VacancyCreateLocators.social_package_text, value, "Гарантии, предоставляемые госслуж./соц. пакет")

    def additional_position_info_text(self, value):
        self.set_text(VacancyCreateLocators.additional_position_info_text, value, "Доп. инф. о вакантной должности")

    def job_responsibility_text(self, value):
        self.set_text(VacancyCreateLocators.job_responsibility_text, value, "Краткое описание должностных обяз.")

    def knowledge_description_text(self, value):
        self.set_text(VacancyCreateLocators.knowledge_description_text, value, "Знания и навыки")

    def additional_requirements(self, value):
        self.set_text(VacancyCreateLocators.additional_requirements, value, "Дополнительные требования к кандидатам")

    def announcement_date(self):
        self.set_date(VacancyCreateLocators.announcement_date, today(), "Дата начала приема документов ")

    def expiry_date(self, value):
        self.set_date(VacancyCreateLocators.expiry_date, value, "Дата окончания приема документов")

    def registration_address(self, value):
        self.set_text(VacancyCreateLocators.registration_address, value, "Место приема документов")

    def registration_time(self, value):
        self.set_text(VacancyCreateLocators.registration_time, value, "Время приема документов")

    def description(self, value):
        self.set_text(VacancyCreateLocators.description, value, "Методическая подсказка (для кандидата)")

    def sel(self):
        self.set_radio(VacancyCreateLocators.sel, "Radio выбора документа из списка")

    def sel_study(self):
        self.set_radio(VacancyCreateLocators.sel_study, "Radio выбора документа из списка")

    def delete(self):
        self.click(VacancyCreateLocators.delete, "Удаление документа")

    def address_mail(self, value):
        self.set_text(VacancyCreateLocators.address_mail, value, "Почтовый адрес (другое)")

    def phone(self, value):
        self.set_text(VacancyCreateLocators.phone, value, "Телефон № 1")

    def phone2(self, value):
        self.set_text(VacancyCreateLocators.phone2, value, "Телефон № 2")

    def phone3(self, value):
        self.set_text(VacancyCreateLocators.phone3, value, "Телефон № 3")

    def email(self, value):
        self.set_text(VacancyCreateLocators.email, value, "Email ")

    def contact_person_other(self, value):
        self.set_text(VacancyCreateLocators.contact_person_other, value, "Контактное лицо")

    def web(self, value):
        self.set_text(VacancyCreateLocators.web, value, "Интернет-сайт органа или организации")

    def additional_info_text(self, value):
        self.set_text(VacancyCreateLocators.additional_info_text, value, "Дополнительная информация")

    class PostIsCompetition(parent):
        def social_package_files(self, value):
            self.upload_file_alt(value)

        def additional_position_info_file(self, value):
            self.upload_file_alt(value, 2, 2)

        def knowledge_description_files(self, value):
            self.upload_file_alt(value, 3, 3)

        def job_responsibility_files(self, value):
            self.upload_file_alt(value, 4, 4)

        def position_rules_files(self, value):
            self.upload_file_alt(value, 5, 5)

        def additional_info_files(self, value):
            self.upload_file_alt(value, 6, 6)

        def template_file(self, value):
            self.upload_file_alt(value, 7, 7)

        def structural_unit(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.structural_unit,
                value, "Структурное подразделение")

        def sub_structural(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.sub_structural,
                value, "Подразделение в структурном подразд.")

        def staff_unit(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.staff_unit, value, "Штатная единица")

        def work_type(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.work_type, value, "Профиль деятельности организации")

        def position_category(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.position_category, value, "Категория вакантной должности")

        def position_group(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.position_group, value, "Группа вакантной должности")

        def okato_region(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.okato_region, value, "Расположение раб. места регион")

        def okato_area(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.okato_area, value, "Расположение раб. места район")

        def business_trip(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.business_trip, value, "Командировки")

        def work_schedule(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.work_schedule, value, "Служебное (рабочее) время")

        def work_day(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.work_day, value, "Нормированность рабочего дня")

        def work_contract(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.work_contract, value, "Тип служебного контракта")

        def education_level(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.education_level, value, "Уровень проф. образования")

        def government_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.government_experience, value, "Стаж государственной службы")

        def professional_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.PostIsCompetition.professional_experience, value, "Стаж работы по специальности")

        def test(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.test, value, "Прикрепить тест")

        def document_type(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.document_type, value, "Название (тип документа)")

        def organization_address(self, value):
            self.set_select2(VacancyCreateLocators.PostIsCompetition.organization_address, value, "Почтовый адрес")

    class ReservePost(parent):
        def social_package_files(self, value):
            self.upload_file_alt(value)

        def additional_position_info_file(self, value):
            self.upload_file_alt(value, 2, 2)

        def knowledge_description_files(self, value):
            self.upload_file_alt(value, 3, 3)

        def job_responsibility_files(self, value):
            self.upload_file_alt(value, 4, 4)

        def position_rules_files(self, value):
            self.upload_file_alt(value, 5, 5)

        def additional_info_files(self, value):
            self.upload_file_alt(value, 6, 6)

        def template_file(self, value):
            self.upload_file_alt(value, 7, 7)

        def reserve(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.reserve, value, "Резерв")

        def structural_unit(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.structural_unit, value, "Структурное подразделение")

        def sub_structural(self, value):
            self.set_select2(
                VacancyCreateLocators.ReservePost.sub_structural, value, "Подразделение в структурном подразделении")

        def post(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.post, value, "Наименование резервируемой должности")

        def work_type(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.work_type, value, "Профиль деятельности организации")

        def reserve_group(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.reserve_group, value, "Группа вакантной должности")

        def okato_region(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.okato_region, value, "Расположение раб. места регион")

        def okato_area(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.okato_area, value, "Расположение раб. места район")

        def business_trip(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.business_trip, value, "Командировки ")

        def work_schedule(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.work_schedule, value, "Служебное (рабочее) время")

        def work_day(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.work_day, value, "Нормированность рабочего дня")

        def work_contract(self, value):
            self.set_select2(
                VacancyCreateLocators.ReservePost.work_contract, value, "Тип служебного контракта")

        def education_level(self, value):
            self.set_select2(
                VacancyCreateLocators.ReservePost.education_level, value, "Уровень проф. образования")

        def government_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.ReservePost.government_experience, value, "Стаж государственной службы")

        def professional_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.ReservePost.professional_experience, value, "Стаж работы по специальности")

        def test(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.test, value, "Прикрепить тест")

        def document_type(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.document_type, value, "Название (тип документа)")

        def organization_address(self, value):
            self.set_select2(VacancyCreateLocators.ReservePost.organization_address, value, "Почтовый адрес")

    class ReserveGroupPosts(parent):
        def social_package_files(self, value):
            self.upload_file_alt(value)

        def additional_position_info_file(self, value):
            self.upload_file_alt(value, 2, 2)

        def knowledge_description_files(self, value):
            self.upload_file_alt(value, 3, 3)

        def job_responsibility_files(self, value):
            self.upload_file_alt(value, 4, 4)

        def position_rules_files(self, value):
            self.upload_file_alt(value, 5, 5)

        def additional_info_files(self, value):
            self.upload_file_alt(value, 6, 6)

        def template_file(self, value):
            self.upload_file_alt(value, 7, 7)

        def reserve(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.reserve, value, "Резерв")

        def structural_unit(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.structural_unit,
                             value, "Структурное подразделение")

        def sub_structural(self, value):
            self.set_select2(
                VacancyCreateLocators.ReserveGroupPosts.sub_structural,
                value, "Подразделение в структурном подразделении")

        def work_type(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.work_type,
                             value, "Профиль деятельности организации")

        def reserve_group(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.reserve_group, value, "Группа вакантной должности")

        def okato_region(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.okato_region,
                             value, "Расположение раб. места регион")

        def okato_area(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.okato_area, value, "Расположение раб. места район")

        def business_trip(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.business_trip, value, "Командировки ")

        def work_schedule(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.work_schedule, value, "Служебное (рабочее) время")

        def work_day(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.work_day, value, "Нормированность рабочего дня")

        def work_contract(self, value):
            self.set_select2(
                VacancyCreateLocators.ReserveGroupPosts.work_contract, value, "Тип служебного контракта")

        def education_level(self, value):
            self.set_select2(
                VacancyCreateLocators.ReserveGroupPosts.education_level, value, "Уровень проф. образования")

        def government_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.ReserveGroupPosts.government_experience, value, "Стаж государственной службы")

        def professional_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.ReserveGroupPosts.professional_experience, value, "Стаж работы по специальности")

        def test(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.test, value, "Прикрепить тест")

        def document_type(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.document_type, value, "Название (тип документа)")

        def organization_address(self, value):
            self.set_select2(VacancyCreateLocators.ReserveGroupPosts.organization_address, value, "Почтовый адрес")

    class VacantStudy(parent):
        def social_package_files(self, value):
            self.upload_file_alt(value)

        def additional_position_info_file(self, value):
            self.upload_file_alt(value, 2, 2)

        def knowledge_description_files(self, value):
            self.upload_file_alt(value, 3, 3)

        def job_responsibility_files(self, value):
            self.upload_file_alt(value, 4, 4)

        def position_rules_files(self, value):
            self.upload_file_alt(value, 5, 5)

        def additional_info_files(self, value):
            self.upload_file_alt(value, 6, 6)

        def template_file(self, value):
            self.upload_file_alt(value, 7, 7)

        def structural_unit(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.structural_unit, value, "Структурное подразделение")

        def sub_structural(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.sub_structural, value, "Подразделение в структурном подразд.")

        def work_type(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.work_type, value, "Профиль деятельности организации")

        def position_category(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.position_category, value, "Категория вакантной должности")

        def position_group(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.position_group, value, "Группа вакантной должности")

        def okato_region(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.okato_region, value, "Расположение раб. места регион")

        def okato_area(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.okato_area, value, "Расположение раб. места район")

        def business_trip(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.business_trip, value, "Командировки ")

        def work_schedule(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.work_schedule, value, "Служебное (рабочее) время")

        def work_day(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.work_day, value, "Нормированность рабочего дня")

        def work_contract(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.work_contract, value, "Тип служебного контракта")

        def education_level(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.education_level, value, "Уровень проф. образования")

        def government_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.government_experience, value, "Стаж государственной службы")

        def professional_experience(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantStudy.professional_experience, value, "Стаж работы по специальности")

        def test(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.test, value, "Прикрепить тест")

        def document_type(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.document_type, value, "Название (тип документа)")

        def organization_address(self, value):
            self.set_select2(VacancyCreateLocators.VacantStudy.organization_address, value, "Почтовый адрес")

    class VacantState(parent):
        def job_responsibility_files(self, value):
            self.upload_file_alt(value)

        def position_rules_files(self, value):
            self.upload_file_alt(value, 2, 2)

        def structural_unit(self, value):
            self.set_select2(VacancyCreateLocators.VacantState.structural_unit, value, "Структурное подразделение")

        def sub_structural(self, value):
            self.set_select2(
                VacancyCreateLocators.VacantState.sub_structural, value, "Подразделение в структурном подразделении")

        def staff_unit(self, value):
            self.set_select2(VacancyCreateLocators.VacantState.staff_unit, value, "Штатная единица")

        def work_type(self, value):
            self.set_select2(VacancyCreateLocators.VacantState.work_type, value, "Профиль деятельности организации")

        def position_category(self, value):
            self.set_select2(VacancyCreateLocators.VacantState.position_category,
                             value, "Категория вакантной должности")

        def position_group(self, value):
            self.set_select2(VacancyCreateLocators.VacantState.position_group, value, "Группа вакантной должности")


class VacancyManagePage(parent):

    def is_date_vacancy(self):
        self.wait_for_loading()
        elements = self.driver.find_elements_by_xpath("//tr[@class='ng-scope']//td[7]")
        texts = []
        for i in elements:
            texts.append(i.text.split()[0])
        return today() in texts

    def status(self, value):
        self.select2_clear(VacancyManageLocators.status)
        self.set_select2_alt(VacancyManageLocators.status, value, "Статус")

    def type(self, value):
        self.select2_clear(VacancyManageLocators.type)
        self.set_select2_alt(VacancyManageLocators.type, value, "Тип вакансии")

    def create_date(self, value):
        self.set_date(VacancyManageLocators.create_date, value, "Дата создания")

    def comment(self, value):
        self.set_text(VacancyManageLocators.comment, value, "Комментарий")

    def create(self):
        self.click(VacancyManageLocators.create, "Создать")

    def approve(self):
        self.click(VacancyManageLocators.approve, "На рассмотрение")

    def publish(self):
        self.click(VacancyManageLocators.publish, "На публикацию")

    def published(self):
        self.click(VacancyManageLocators.published, "Опубликовать")

    def refine(self):
        self.click(VacancyManageLocators.refine, "На доработку")

    def remove(self):
        self.click(VacancyManageLocators.remove, "Удалить")

    def close(self):
        self.click(VacancyManageLocators.close, "Закрыть")

    def archive(self):
        self.click(VacancyManageLocators.archive, "Архив")

    def copy(self):
        self.click(VacancyManageLocators.copy, "Создать по образцу")

    def checkbox(self, value=True):
        self.set_checkbox(VacancyManageLocators.checkbox, value, "Выбор первой записи")


class ReserveViewFederal(parent):

    def permission_read_resume(self, value):
        checkbox = self.wait_for_element_appear(ReserveViewFederalLocators.permission_read_resume)
        if not checkbox.is_selected():
            self.set_checkbox(ReserveViewFederalLocators.permission_read_resume, value, "Чтение любых резюме")
            self.click_by_text("Сохранить")

    def level_reserve(self, value):
        self.set_select2(ReserveViewFederalLocators.level_reserve, value, "Уровень резерва")

    def resume(self):
        self.click(ReserveViewFederalLocators.resume, "Резюме")

    def presentation(self):
        self.click(ReserveViewFederalLocators.presentation, "Представление")

    def check_text_and_close(self, text):
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.wait_for_text_appear(text)
        assert text in self.driver.page_source
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


class ManageReserveBasesPage(parent):

    def code(self, value):
        self.set_text(ManageReserveBasesLocators.code, value, "Code")

    def name(self, value):
        self.set_text(ManageReserveBasesLocators.name, value, "Name")

    def edit(self):
        self.click(ManageReserveBasesLocators.edit, "Edit")

    def delete(self):
        self.click(ManageReserveBasesLocators.delete, "Delete")


class ReserveBasesPreparePage(parent):

    def personal_file(self, value):
        self.set_select2(ReserveBasesPrepareLocators.personal_file, value, "personalFile")

    def presentation_reserve_level(self, value):
        self.set_select2(ReserveBasesPrepareLocators.presentation_reserve_level, value, "presentationReserveLevel")

    def grade_of_post(self, value):
        self.set_select2(ReserveBasesPrepareLocators.grade_of_post, value, "gradeOfPost")

    def save(self):
        self.click(ReserveBasesPrepareLocators.save, "Сохранить")

    def documents(self):
        self.click(ReserveBasesPrepareLocators.documents, "documents")

    def resume(self):
        self.click(ReserveBasesPrepareLocators.resume, "resume")

    def presentation(self):
        self.click(ReserveBasesPrepareLocators.presentation, "presentation")

    def last_name(self, value):
        self.set_text(ReserveBasesPrepareLocators.last_name, value, "lastName")

    def first_name(self, value):
        self.set_text(ReserveBasesPrepareLocators.first_name, value, "firstName")

    def middle_name(self, value):
        self.set_text(ReserveBasesPrepareLocators.middle_name, value, "middleName")

    def gender(self, value):
        self.set_select2(ReserveBasesPrepareLocators.gender, value, "gender")

    def tax_certificate_number(self, value):
        self.set_text(ReserveBasesPrepareLocators.tax_certificate_number, value, "taxCertificateNumber")

    def insurance_certificate_number(self, value):
        self.set_text(ReserveBasesPrepareLocators.insurance_certificate_number, value, "insuranceCertificateNumber")

    def birth_date(self, value):
        self.set_date(ReserveBasesPrepareLocators.birth_date, value, "birthDate")

    def citizenship(self, value):
        self.set_select2(ReserveBasesPrepareLocators.citizenship, value, "citizenship")

    def birth_place(self, value):
        self.set_text(ReserveBasesPrepareLocators.birth_place, value, "birthPlace")

    def was_convicted(self, value):
        self.set_select(value, label="wasConvicted")

    def marital_statuses(self, value):
        self.set_select2(ReserveBasesPrepareLocators.marital_statuses, value, "maritalStatuses")

    def name_was_changed(self, value):
        self.set_select(value, 2, "nameWasChanged")

    def work_phone(self, value):
        self.set_text(ReserveBasesPrepareLocators.work_phone, value, "workPhone")

    def mobile_phone(self, value):
        self.set_text(ReserveBasesPrepareLocators.mobile_phone, value, "mobilePhone")

    def additional_phone(self, value):
        self.set_text(ReserveBasesPrepareLocators.additional_phone, value, "additionalPhone")

    def residence_phone(self, value):
        self.set_text(ReserveBasesPrepareLocators.residence_phone, value, "residencePhone")

    def fax(self, value):
        self.set_text(ReserveBasesPrepareLocators.fax, value, "fax")

    def work_email(self, value):
        self.set_text(ReserveBasesPrepareLocators.work_email, value, "workEmail")

    def personal_email(self, value):
        self.set_text(ReserveBasesPrepareLocators.personal_email, value, "personalEmail")

    def web(self, value):
        self.set_text(ReserveBasesPrepareLocators.web, value, "web")

    def registration_region(self, value):
        self.set_select2(ReserveBasesPrepareLocators.registration_region, value, "registrationRegion")

    def registration_area(self, value):
        self.set_select2(ReserveBasesPrepareLocators.registration_area, value, "registrationArea")

    def residence_region(self, value):
        self.set_select2(ReserveBasesPrepareLocators.residence_region, value, "residenceRegion")

    def residence_area(self, value):
        self.set_select2(ReserveBasesPrepareLocators.residence_area, value, "residenceArea")

    def education_level(self, value):
        self.set_select2(ReserveBasesPrepareLocators.education_level, value, "educationLevel")

    def education_kinds(self, value):
        self.set_select2(ReserveBasesPrepareLocators.education_kinds, value, "educationKinds")

    def education_forms(self, value):
        self.set_select2(ReserveBasesPrepareLocators.education_forms, value, "educationForms")

    def place(self, value):
        self.set_text(ReserveBasesPrepareLocators.place, value, "place")

    def temp_institution(self, value):
        self.set_select2(ReserveBasesPrepareLocators.temp_institution, value, "tempInstitution")

    def start_date(self, value):
        self.set_text(ReserveBasesPrepareLocators.start_date, value, "startDate")

    def end_date(self, value):
        self.set_text(ReserveBasesPrepareLocators.end_date, value, "endDate")

    def faculty(self, value):
        self.set_text(ReserveBasesPrepareLocators.faculty, value, "faculty")

    def education_doc_number(self, value):
        self.set_text(ReserveBasesPrepareLocators.education_doc_number, value, "educationDocNumber")

    def speciality(self, value):
        self.set_select2(ReserveBasesPrepareLocators.speciality, value, "speciality")

    def qualification(self, value):
        self.set_select2(ReserveBasesPrepareLocators.qualification, value, "qualification")

    def specialization(self, value):
        self.set_text(ReserveBasesPrepareLocators.specialization, value, "specialization")

    def begin_date(self, value):
        self.set_date(ReserveBasesPrepareLocators.begin_date, value, "beginDate")

    def stop_date(self, value):
        self.set_date(ReserveBasesPrepareLocators.stop_date, value, "endDate")

    def organization_work(self, value):
        self.set_text(ReserveBasesPrepareLocators.organization_work, value, "organization_work")

    def address_organization(self, value):
        self.set_text(ReserveBasesPrepareLocators.address_organization, value, "addressOrganization")

    def structural_division(self, value):
        self.set_text(ReserveBasesPrepareLocators.structural_division, value, "structuralDivision")

    def post(self, value):
        self.set_text(ReserveBasesPrepareLocators.post, value, "post")

    def post_levels(self, value):
        self.set_select2(ReserveBasesPrepareLocators.post_levels, value, "postLevels")

    def employees_numbers(self, value):
        self.set_select2(ReserveBasesPrepareLocators.employees_numbers, value, "employeesNumbers")

    def profile(self, value):
        self.set_select2(ReserveBasesPrepareLocators.profile, value, "profile")

    def professional_activity_area(self, value):
        self.set_select2(ReserveBasesPrepareLocators.professional_activity_area, value, "professionalActivityArea")

    def responsibilities(self, value):
        self.set_text(ReserveBasesPrepareLocators.responsibilities, value, "responsibilities")

    def job_types(self, value):
        self.set_select2(ReserveBasesPrepareLocators.job_types, value, "jobTypes")

    def expectations(self, value):
        self.set_text(ReserveBasesPrepareLocators.expectations, value, "expectations")

    def organization_sub_type(self, value):
        self.set_select2(ReserveBasesPrepareLocators.organization_sub_type, value, "organizationSubType")

    def organization(self, value):
        self.set_select2(ReserveBasesPrepareLocators.organization, value, "organization")

    def organization_other(self, value):
        self.set_text(ReserveBasesPrepareLocators.organization_other, value, "organizationOther")

    def ready_to_move(self, value):
        self.set_select(value)

    def salary_from(self, value):
        self.set_text(ReserveBasesPrepareLocators.salary_from, value, "salaryFrom")

    def salary_to(self, value):
        self.set_text(ReserveBasesPrepareLocators.salary_to, value, "salaryTo")

    def computer_skills(self, value):
        self.set_text(ReserveBasesPrepareLocators.computer_skills, value, "computerSkills")

    def publications(self, value):
        self.set_text(ReserveBasesPrepareLocators.publications, value, "publications")

    def recommendations(self, value):
        self.set_text(ReserveBasesPrepareLocators.recommendations, value, "recommendations")

    def additional_info(self, value):
        self.set_text(ReserveBasesPrepareLocators.additional_info, value, "additionalInfo")

    def agree_to_process_data(self, value):
        self.set_checkbox_by_order(1, value, "agreeToProcessData")

    def availability_degree(self, value):
        self.set_select2(ReserveBasesPrepareLocators.availability_degree, value, "availabilityDegree")

    def position(self, value):
        self.set_text(ReserveBasesPrepareLocators.position, value, "position")

    def recomendations(self, value):
        self.set_text(ReserveBasesPrepareLocators.recomendations, value, "recomendations")

    def professional_achievements(self, value):
        self.set_text(ReserveBasesPrepareLocators.professional_achievements, value, "professionalAchievements")

    def developement_area(self, value):
        self.set_text(ReserveBasesPrepareLocators.developement_area, value, "developementArea")

    def additional_preperation_text(self, value):
        self.set_text(ReserveBasesPrepareLocators.additional_preperation_text, value, "additionalPreperationText")
