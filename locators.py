from selenium.webdriver.common.by import By


class MainLocators(object):
    logout = (By.XPATH, "//input[@value='Выйти']")


class LoginLocators(object):
    username = (By.ID, "UserName")
    password = (By.ID, "Password")
    submit = (By.XPATH, "//input[@type='submit']")


class PersonalFileLocators(object):

    class New(object):
        last_name = (By.ID, "lastName")
        first_name = (By.ID, "firstName")
        middle_name = (By.ID, "middleName")
        birthday = (By.ID, "birthDate")
        insurance_certificate_number = (By.ID, "insuranceCertificateNumber")
        username = (By.ID, "userName")

    class General(object):
        general_edit = (By.XPATH, "(//a[contains(., 'Редактировать')])[1]")
        addresses_edit = (By.XPATH, "(//a[contains(., 'Редактировать')])[2]")
        contact_edit = (By.XPATH, "(//a[contains(., 'Редактировать')])[3]")
        last_name = (By.XPATH, "(//input[@type='text'])[1]")
        first_name = (By.XPATH, "(//input[@type='text'])[2]")
        middle_name = (By.XPATH, "(//input[@type='text'])[3]")
        gender = (By.XPATH, "(//span[contains(@id, 'select2-chosen')])[1]")
        personal_file_number = (By.XPATH, "(//input[@type='text'])[4]")
        birthday = (By.XPATH, "(//input[@type='text'])[7]")
        okato = (By.XPATH, "(//input[@type='text'])[10]")


class StructureInfoLocators(object):
    organization = (By.ID, "select2-chosen-3")
    name = (By.ID, "name")
    fot = (By.ID, "payroll")
    limit = (By.ID, "staffLimit")


class StructureDetailsLocators(object):
    general = (By.XPATH, "//a[contains(., 'Общие')]")
    forming = (By.XPATH, "//a[contains(., 'Формирование организационной')]")
    structure = (By.XPATH, "//a[contains(., 'Штатная структура')]")
    arrangement = (By.XPATH, "//a[contains(., 'Штатная расстановка')]")
    launch = (By.XPATH, "//a[contains(., 'Введение')]")
    order_number = (By.XPATH, "(//input[@type='text'])[1]")
    order_date = (By.XPATH, "(//input[@type='text'])[2]")
    launch_date = (By.XPATH, "(//input[@type='text'])[3]")


class DepartmentLocators(object):
    name = (By.XPATH, "//input[@name='name']")
    name_genitive = (By.XPATH, "//input[@name='nameGenitive']")
    name_dative = (By.XPATH, "//input[@name='nameDative']")
    name_accusative = (By.XPATH, "//input[@name='nameAccusative']")
    limit = (By.XPATH, "(//input[@type='text'])[5]")
    code = (By.XPATH, "(//input[@type='text'])[6]")
    launch_date = (By.XPATH, "(//input[@type='text'])[9]")
    order_number = (By.XPATH, "(//input[@type='text'])[11]")
    order_date = (By.XPATH, "(//input[@type='text'])[12]")
    position = (By.XPATH, "//span[@id='select2-chosen-4']")
    position_input = (By.XPATH, "(//input[@role='combobox'])[4]")
    amount = (By.XPATH, "(//input[@type='text'])[20]")


class AppointmentLocators(object):
    full_name = (By.ID, "select2-chosen-6")
    reason = (By.ID, "select2-chosen-7")
    duration = (By.XPATH, "(//input[@type='radio'])[3]")
    date_from = (By.XPATH, "(//input[@type='text'])[14]")
    trial = (By.XPATH, "(//input[@type='radio'])[5]")
    contract_date = (By.XPATH, "(//input[@type='text'])[19]")
    contract_number = (By.XPATH, "(//input[@type='text'])[20]")


class SalaryPaymentsLocators(object):
    type = (By.ID, "s2id_salaryType")
    amount = (By.XPATH, "//input[@name='value']")
    date_from = (By.ID, "startDate")


class PersonalFileDismissalLocators(object):
    check = (By.XPATH, "//input[@type='radio']")


class DismissalLocators(object):
    date = (By.ID, "dismissalDate")
    reason = (By.ID, "s2id_dismissalReason")


class StagesLocators(object):
    check = (By.XPATH, "(//input[@type='checkbox'])[2]")
    order = (By.XPATH, "(//input[@type='text'])[1]")
    date = (By.XPATH, "(//input[@type='text'])[2]")
    full_name = (By.ID, "s2id_autogen3")
    position = (By.ID, "s2id_autogen5")
    submit = (By.XPATH, "//input[@value='Сохранить']")


class AdvertisementLocators(object):
    # Основная информация
    type = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    organization = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    is_competition = (By.XPATH, "//input[@data-ng-model='vacancy.isCompetition']")
    reason = (By.ID, "withoutCompetitionReason")
    division = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    subdivision = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
    position = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
    # Общие сведения
    profile = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
    okato_region = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
    okato_area = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
    salary_from = (By.ID, "salaryFrom")
    salary_to = (By.ID, "salaryTo")
    buisness_trip = (By.ID, "s2id_businessTrip")
    work_schedule = (By.ID, "s2id_workSchedule")
    is_fixed_schedule = (By.ID, "s2id_isFixedSchedule")
    work_contract = (By.ID, "s2id_workContract")
    guarantee = (By.XPATH, "(//textarea)[1]")
    additional_info = (By.XPATH, "(//textarea)[2]")
    # Должностные обязанности
    job_responsibility = (By.ID, "jobResponsibility")
    # Квалификационные требования
    requirements = (By.XPATH, "(//div[contains(@id, 's2id')])[15]")
    experience = (By.XPATH, "(//div[contains(@id, 's2id')])[16]")
    work_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[17]")
    knowledge_description = (By.XPATH, "//textarea[@name='knowledgeDescription']")
    additional_requirements = (By.XPATH, "//textarea[@data-ng-model='vacancy.additionalRequirements']")
    attach_text = (By.XPATH, "(//div[contains(@id, 's2id')])[18]")
    # Документы
    announcement_date = (By.XPATH, "//input[@name='announcementDate']")
    expiry_date = (By.XPATH, "//input[@name='expiryDate']")
    registration_address = (By.XPATH, "//input[@name='registrationAddress']")
    registration_time = (By.XPATH, "//input[@name='registrationTime']")
    # Контакты
    post_index = (By.XPATH, "(//div[contains(@id, 's2id')])[19]")
    address_mail = (By.XPATH, "//input[@data-ng-model='vacancy.addressMail']")
    phone_1 = (By.XPATH, "//input[@data-ng-model='vacancy.phone']")
    phone_2 = (By.XPATH, "//input[@data-ng-model='vacancy.phone2']")
    phone_3 = (By.XPATH, "//input[@data-ng-model='vacancy.phone3']")
    email = (By.XPATH, "//input[@name='email']")
    person = (By.XPATH, "//input[@name='contactPersonOther']")
    site = (By.XPATH, "//input[@data-ng-model='vacancy.web']")
    additional = (By.XPATH, "//textarea[@data-ng-model='vacancy.additionalInfo.text']")


class CommissionsLocators(object):
    name = (By.XPATH, "//input[@data-ng-model='model.name']")
    organization = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    order_date = (By.ID, "orderDate")
    order_number = (By.XPATH, "//input[@data-ng-model='model.orderNumber']")
    full_name = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    type = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    start_date = (By.ID, "startDate")
    end_date = (By.ID, "endDate")

    class Members(object):
        role = (By.ID, "s2id_role")
        full_name = (By.ID, "s2id_fullName")
        is_independent_expert = (By.XPATH, "//input[@type='checkbox']")
        organization = (By.ID, "organization")
        position = (By.ID, "post")
        department = (By.ID, "department")
        phone = (By.ID, "phone")
        email = (By.ID, "email")
        personal_file_number = (By.ID, "personalFileNumber")

    class Sessions(object):
        meeting_date = (By.ID, "meetingDate")
        meeting_time = (By.ID, "meetingTime")
        place = (By.ID, "place")
        content = (By.ID, "content")
        reporter = (By.ID, "reporter")
        decision = (By.ID, "s2id_decision")
        decision_reason = (By.ID, "decisionReason")


class AwardsLocators(object):

    class Awards(object):
        type = (By.XPATH, "((//div[@role='form'])[1]//div[contains(@id, 's2id')])[1]")
        name = (By.XPATH, "(//input[@type='text'])[2]")
        date = (By.XPATH, "(//input[@type='text'])[3]")
        amount = (By.XPATH, "(//input[@type='text'])[4]")
        unit = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        note = (By.XPATH, "(//textarea)[1]")
        should_be = (By.XPATH, "(//input[@type='checkbox'])[1]")
        submit = (By.XPATH, "(//input[@value='Сохранить'])[1]")

    class StateAwards(object):
        type = (By.XPATH, "((//div[@role='form'])[2]//div[contains(@id, 's2id')])[1]")
        name = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[2]")
        list_date = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[3]")
        date = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[4]")
        order_number = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[5]")
        order_date = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[6]")
        award_number = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[7]")
        certificate_number = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[8]")
        awarding_date = (By.XPATH, "((//div[@role='form'])[2]//input[@type='text'])[9]")
        note = (By.XPATH, "(//textarea)[2]")
        submit = (By.XPATH, "(//input[@value='Сохранить'])[2]")

    class DepartmentAwards(object):
        type = (By.XPATH, "((//div[@role='form'])[3]//div[contains(@id, 's2id')])[1]")
        name = (By.XPATH, "((//div[@role='form'])[3]//input[@type='text'])[2]")
        order_number = (By.XPATH, "((//div[@role='form'])[3]//input[@type='text'])[3]")
        order_date = (By.XPATH, "((//div[@role='form'])[3]//input[@type='text'])[4]")
        award_number = (By.XPATH, "((//div[@role='form'])[3]//input[@type='text'])[5]")
        certificate_number = (By.XPATH, "((//div[@role='form'])[3]//input[@type='text'])[6]")
        awarding_date = (By.XPATH, "((//div[@role='form'])[3]//input[@type='text'])[7]")
        note = (By.XPATH, "(//textarea)[3]")
        submit = (By.XPATH, "(//input[@value='Сохранить'])[3]")


class EnforcementLocators(object):
    # block #1
    reason = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//div[contains(@id, 's2id')])[1]")
    order_number = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//input[@type='text'])[2]")
    order_date = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//input[@type='text'])[3]")
    period_from = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//input[@type='text'])[4]")
    period_to = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//input[@type='text'])[5]")
    # block #2
    action_date = (By.XPATH, "((//div[@class='work-experience-edit'])[2]//input[@type='text'])[1]")
    action = (By.XPATH, "((//div[@class='work-experience-edit'])[2]//div[contains(@id, 's2id')])[1]")
    explanatory_date = (By.XPATH, "((//div[@class='work-experience-edit'])[2]//input[@type='text'])[3]")
    # block #3
    enforcement_date = (By.XPATH, "((//div[@class='work-experience-edit'])[3]//input[@type='text'])[1]")
    enforcement_reason = (By.XPATH, "((//div[@class='work-experience-edit'])[3]//div[contains(@id, 's2id')])[1]")
    type = (By.XPATH, "((//div[@class='work-experience-edit'])[3]//div[contains(@id, 's2id')])[2]")
    copy_date = (By.XPATH, "((//div[@class='work-experience-edit'])[3]//input[@type='text'])[6]")
    # block #4
    enforcement_expire_auto = (By.XPATH, "((//div[@class='work-experience-edit'])[4]//input[@type='text'])[1]")
    enforcement_expire_date = (By.XPATH, "((//div[@class='work-experience-edit'])[4]//input[@type='text'])[2]")
    enforcement_expire_reason = (By.XPATH, "//textarea")
    enforcement_expire_order_date = (By.XPATH, "((//div[@class='work-experience-edit'])[4]//input[@type='text'])[3]")
    enforcement_expire_order_number = (By.XPATH, "((//div[@class='work-experience-edit'])[4]//input[@type='text'])[4]")
    # block #5
    should_be = (By.XPATH, "//input[@type='checkbox']")


class DispensaryPlanningLocators(object):
    date_from = (By.XPATH, "(//input[@type='text'])[5]")
    date_to = (By.XPATH, "(//input[@type='text'])[6]")


class DispensaryLocators(object):
    dispensary_date = (By.XPATH, "(//input[@type='text'])[1]")
    reference_date = (By.XPATH, "(//input[@type='text'])[2]")
    reference_number = (By.XPATH, "(//input[@type='text'])[3]")
    is_healthy = (By.XPATH, "//input[@type='checkbox']")
    date_from = (By.XPATH, "(//input[@type='text'])[1]")
    date_to = (By.XPATH, "(//input[@type='text'])[2]")
    order_date = (By.XPATH, "(//input[@type='text'])[3]")
    order_number = (By.XPATH, "(//input[@type='text'])[4]")
    institution = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    by = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")


class DisabilityPeriodsLocators(object):
    list_number = (By.XPATH, "//input[@data-ng-model='editmodel.number']")
    by = (By.XPATH, "//input[@data-ng-model='editmodel.issuedBy']")
    note = (By.XPATH, "//textarea")
    period_from = (By.XPATH, "//input[@id='dateStart']")
    period_to = (By.XPATH, "//input[@id='dateEnd']")
    list_continuing = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    reason = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    family_member = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    insurance_experience = (By.XPATH, "//input[@data-ng-model='editmodel.experienceInsurance']")
    not_insurance_periods = (By.XPATH, "//input[@data-ng-model='editmodel.experienceNoInsurance']")
    percent = (By.XPATH, "//input[@data-ng-model='editmodel.percentPayment']")
    submit = (By.XPATH, "//input[@value='Сохранить']")

    class Editing(object):
        list_number = (By.XPATH, "//input[@id='number']")
        by = (By.XPATH, "//input[@id='issuedBy']")
        note = (By.XPATH, "//textarea")
        period_from = (By.XPATH, "//input[@id='dateStart']")
        period_to = (By.XPATH, "//input[@id='dateEnd']")
        list_continuing = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        reason = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        family_member = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        insurance_experience = (By.XPATH, "//input[@data-ng-model='model.experienceInsurance']")
        not_insurance_periods = (By.XPATH, "//input[@data-ng-model='model.experienceNoInsurance']")
        percent = (By.XPATH, "//input[@data-ng-model='model.percentPayment']")
        submit = (By.XPATH, "//input[@value='Сохранить']")


class BusinessTripLocators(object):
    date_start = (By.XPATH, "//input[@id='dateDeparture']")
    date_end = (By.XPATH, "//input[@id='dateReturn']")
    date_cancelling = (By.XPATH, "(//input[@type='text'])[3]")
    date_expansion = (By.XPATH, "(//input[@type='text'])[4]")
    days_amount = (By.XPATH, "//input[@data-ng-model='editedTrip.countDays']")
    days_amount_without_road = (By.XPATH, "//input[@data-ng-model='editedTrip.countDaysWithNoRoad']")
    holidays_amount = (By.XPATH, "//input[@data-ng-model='editedTrip.countHolidays']")
    working_days_amount = (By.XPATH, "//input[@data-ng-model='editedTrip.countWorkingDays']")
    source_financing = (By.XPATH, "//input[@data-ng-model='editedTrip.sourceFinancing']")
    is_off_plan = (By.XPATH, "//input[@data-ng-model='editedTrip.isOffPlan']")
    is_foreign_trip = (By.XPATH, "//input[@data-ng-model='editedTrip.isForeignTrip']")
    event = (By.XPATH, "//input[@data-ng-model='editedTrip.purposeBusinessTripID']")
    purpose = (By.XPATH, "//input[@data-ng-model='editedTrip.purposeBusinessTripName']")
    reason = (By.XPATH, "//input[@data-ng-model='editedTrip.baseBusinessTrip']")
    route = (By.XPATH, "//input[@data-ng-model='editedTrip.routeBusinessTrip']")
    task_number = (By.XPATH, "//input[@data-ng-model='editedTrip.serviceJobNumb']")
    task_date = (By.XPATH, "//div[@ng-model='editedTrip.serviceJobDate']/input")
    certificate_number = (By.XPATH, "//input[@data-ng-model='editedTrip.certificateNumb']")
    certificate_date = (By.XPATH, "//div[@data-ng-model='editedTrip.certificateDate']/input")
    must_be_notify = (By.XPATH, "//input[@data-ng-model='editedTrip.mustBeNotify']")
    submit = (By.XPATH, "(//button[.='Сохранить'])[1]")

    class Routes(object):
        date_start = (By.XPATH, "//input[@id='routes.dateDeparture']")
        date_end = (By.XPATH, "//input[@id='routes.dateReturn']")
        country = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        organization = (By.XPATH, "//input[@data-ng-model='editedRoute.organizationBusinessTrip']")
        days_amount = (By.XPATH, "//input[@data-ng-model='editedRoute.countDays']")
        submit = (By.XPATH, "(//button[.='Сохранить'])[2]")


class HolidaysLocators(object):
    statement_date = (By.XPATH, "//input[@id='statementDate']")
    base = (By.XPATH, "//input[@id='base']")
    type = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    date_from = (By.XPATH, "//input[@id='dateFrom']")
    count_days = (By.XPATH, "//input[@id='countDays']")
    is_pay_once = (By.XPATH, "//input[@id='isPayOnce']")
    is_material_aid = (By.XPATH, "//input[@id='isMaterialAid']")


class RanksLocators(object):
    condition = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    type = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    organization = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
    date = (By.XPATH, "//div[@data-ng-model='orc.editmodel.dateStart']/input")


class RolesManagementLocators(object):
    search = (By.XPATH, "//input[@type='search']")
    name = (By.XPATH, "//input[@name='caption']")
    level = (By.XPATH, "//div[contains(@id, 's2id')]")
