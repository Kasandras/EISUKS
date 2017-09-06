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
    organization = (By.XPATH, "//div[contains(@id, 's2id')]")
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
    period_from = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//input[@type='text'])[5]")
    period_to = (By.XPATH, "((//div[@class='work-experience-edit'])[1]//input[@type='text'])[6]")
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
    is_require_organization = (By.XPATH, "//input[@type='checkbox']")
    level = (By.XPATH, "//div[contains(@id, 's2id')]")
    roles = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")


class VacancySearchLocators(object):
    type_source_vacancy = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    name_source_vacancy = (By.XPATH, "(//input[@type='text'])[2]")
    name_vacant_position = (By.XPATH, "(//input[@type='text'])[3]")
    type_vacancy = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    profile_activity_organization = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    field_professional_activity = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
    key_word = (By.XPATH, "(//input[@type='text'])[7]")
    category_job = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
    group_job = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
    subject_workplace = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
    region_workplace = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
    salary_from = (By.XPATH, "(//input[@type='text'])[12]")
    salary_to = (By.XPATH, "(//input[@type='text'])[13]")
    business_trip = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
    work_day = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
    day_start_accept_document_from = (By.XPATH, "(//input[@type='text'])[16]")
    day_start_accept_document_to = (By.XPATH, "(//input[@type='text'])[17]")
    day_stop_accept_document_from = (By.XPATH, "(//input[@type='text'])[18]")
    day_stop_accept_document_to = (By.XPATH, "(//input[@type='text'])[19]")
    level_education = (By.XPATH, "(//div[contains(@id, 's2id')])[11]")
    service_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[12]")
    work_experience_speciality = (By.XPATH, "(//div[contains(@id, 's2id')])[13]")


class VacancyControlLocators(object):
    status_response = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    key_word = (By.XPATH, "(//input[@type='text'])[1]")


class DocumentsLocators:

    class Documents(object):
        name_document = (By.XPATH, "//div[contains(@id, 's2id')]")

    class PersonalMain(object):
        selection_radio = (By.XPATH, "//td//input[@type='radio']")
        lastname = (By.XPATH, "//input[@name='lastName']")
        firstname = (By.XPATH, "//input[@name='firstName']")
        middlename = (By.XPATH, "//input[@name='middleName']")
        gender = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        individual_taxpayer_number = (By.XPATH, "//input[@name='taxCertificateNumber']")
        insurance_certificate_number = (By.XPATH, "//input[@name='insuranceCertificateNumber']")
        birthdate = (By.XPATH, "//input[@id='birthDate']")
        citizenship = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        birthplace = (By.XPATH, "//input[@ng-model='model.generalInformation.birthPlace']")
        maritalstatuses = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")

    class PersonalContact(object):
        work_phone = (By.XPATH, "//input[@ng-model='model.workPhone']")
        mobile_phone = (By.XPATH, "//input[@ng-model='model.mobilePhone']")
        additional_phone = (By.XPATH, "//input[@ng-model='model.additionalPhone']")
        fax = (By.XPATH, "//input[@ng-model='model.fax']")
        work_email = (By.XPATH, "//input[@ng-model='model.workEmail']")
        personal_email = (By.XPATH, "//input[@ng-model='model.personalEmail']")
        web_address = (By.XPATH, "//input[@ng-model='model.webAddress']")
        permanent_registration = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        permanent_registration_reg = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        temp_registration_sub = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        temp_registration_reg = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        fact_registration_sub = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        fact_registration_reg = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")

    class IdentificationDocument(object):
        type_document = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        series = (By.XPATH, "//input[@data-ng-model='editmodel.series']")
        number = (By.XPATH, "//input[@data-ng-model='editmodel.number']")
        date_issued = (By.XPATH, "//input[@id='dateIssued']")
        date_end = (By.XPATH, "//input[@id='dateEnd']")
        issue_by = (By.XPATH, "//textarea[@data-ng-model='editmodel.issuedBy']")
        issue_code = (By.XPATH, "//input[@data-ng-model='editmodel.issuedCode']")

    class Education(object):

        class Main(object):
            education_level = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
            education = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
            education_form = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
            place_institution = (By.XPATH, "//input[@data-ng-model='editmodel.place']")
            full_name_institution = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
            start_date_education = (By.XPATH, "//input[@data-ng-model='editmodel.startDate']")
            end_date_education = (By.XPATH, "//input[@data-ng-model='editmodel.endDate']")
            education_directions = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
            faculty = (By.XPATH, "//input[@data-ng-model='editmodel.faculty']")
            education_doc_number = (By.XPATH, "//input[@data-ng-model='editmodel.educationDocNumber']")
            education_doc_date = (By.XPATH, "//input[@id='educationDocDate']")
            speciality = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
            qualification = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
            specialization = (By.XPATH, "//input[@data-ng-model='editmodel.specialization']")
            is_main = (By.XPATH, "//input[@data-ng-model='editmodel.isMain']")

        class Egc(object):
            egc_education = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
            egc_place = (By.XPATH, "(//input[@data-ng-model='editmodel.place'])[2]")
            egc_name_institution = (By.XPATH, "//input[@data-ng-model='editmodel.institutionText']")
            egc_start_date = (By.XPATH, "//input[@id='egc_startDate']")
            egc_end_date = (By.XPATH, "//input[@id='egc_endDate']")
            egc_academic_degree = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
            egc_academic_degree_date = (By.XPATH, "//input[@id='academicDegreeDate']")
            egc_knowledge_branches = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
            egc_diplom_number = (By.XPATH, "//input[@data-ng-model='editmodel.diplomNumber']")
            egc_diplom_date = (By.XPATH, "//input[@id='egc_diplomDate']")

        class Degree(object):
            academic_statuses = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
            diplom_number = (By.XPATH, "(//input[@data-ng-model='editmodel.diplomNumber'])[2]")
            assigment_date = (By.XPATH, "//div[@data-ng-model='editmodel.assigmentDate']/input")

        class Languages(object):
            languages = (By.XPATH, "(//div[contains(@id, 's2id')])[11]")
            language_degrees = (By.XPATH, "(//div[contains(@id, 's2id')])[12]")

        class Dpo(object):
            education_direction = (By.XPATH, "(//div[contains(@id, 's2id')])[13]")
            education_kind = (By.XPATH, "(//div[contains(@id, 's2id')])[14]")
            kind = (By.XPATH, "(//input[@data-ng-model='editmodel.speciality'])[2]")
            name_program = (By.XPATH, "//input[@data-ng-model='editmodel.title']")
            education_form = (By.XPATH, "(//div[contains(@id, 's2id')])[15]")
            place = (By.XPATH, "(//input[@data-ng-model='editmodel.place'])[3]")
            name_institution = (By.XPATH, "(//input[@data-ng-model='editmodel.institutionText'])[2]")
            start_date = (By.XPATH, "(//div[contains(@id, 's2id')])[16]")
            end_date = (By.XPATH, "(//div[contains(@id, 's2id')])[17]")
            hours = (By.XPATH, "//input[@data-ng-model='editmodel.hours']")
            document_number = (By.XPATH, "//input[@data-ng-model='editmodel.documentNumber']")
            document_date = (By.XPATH, "//div[@data-ng-model='editmodel.documentDate']/input")
            funding_sources = (By.XPATH, "(//div[contains(@id, 's2id')])[18]")

    class LaborActivity(object):
        begin_date = (By.XPATH, "//div[@ng-model='lac.editmodel.beginDate']/input")
        end_date = (By.XPATH, "//div[@ng-model='lac.editmodel.endDate']/input")
        post = (By.XPATH, "//input[@ng-model='lac.editmodel.post']")
        organization = (By.XPATH, "//input[@ng-model='lac.editmodel.organization']")
        address_organization = (By.XPATH, "//input[@ng-model='lac.editmodel.addressOrganization']")
        employees_number = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        subject = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        region = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        profile = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        is_elective = (By.XPATH, "//input[@ng-model='lac.editmodel.isElective']")
        post_level = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        activity_area = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
        structural_division = (By.XPATH, "//input[@id='structuralDivision']")
        responsibilities = (By.XPATH, "//input[@id='responsibilities']")

    class ClassRank(object):
        has_class_rank = (By.XPATH, "//input[@ng-model='model.hasClassRank']")
        class_rank = (By.XPATH, "//input[@ng-model='model.classRank']")
        assigned_date = (By.XPATH, "//div[@ng-model='model.classRankAssignedDate']/input")
        assigned_by = (By.XPATH, "//input[@ng-model='model.classRankAssignedBy']")
        has_government_service = (By.XPATH, "//input[@ng-model='model.hasGovernmentService']")
        org_sub_types = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
        organization_name = (By.XPATH, "//input[@ng-model='model.organizationName']")
        computer_skills = (By.XPATH, "//textarea[@ng-model='model.computerSkills']")
        publications = (By.XPATH, "//textarea[@ng-model='model.publications']")
        recommendations = (By.XPATH, "//textarea[@ng-model='model.recommendations']")

    class Specialization(object):
        work = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
        is_main = (By.XPATH, "(//input[@ng-model='editmodel.isMain'])[1]")
        is_add = (By.XPATH, "(//input[@ng-model='model.organizationName'])[2]")

    class Award(object):
        type = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        name = (By.XPATH, "//textarea[@ng-model='awd.editmodel.name']")
        date = (By.XPATH, "//div[@ng-model='awd.editmodel.dateAwarding']/input")

    class StateSecret(object):
        admission_form = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        approval_number = (By.XPATH, "//input[@ng-model='sst.editmodel.approvalNumber']")
        issue_date = (By.XPATH, "//div[@ng-model='sst.editmodel.issueDate']/input")

    class Military(object):
        rank = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        duty = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        has_service = (By.XPATH, "//input[@ng-model='model.hasMilitaryService']")
        service_from = (By.XPATH, "//div[@data-ng-model='model.militaryServiceFrom']/input")
        service_to = (By.XPATH, "//div[@data-ng-model='model.militaryServiceTo']/input")
        arm_kind = (By.XPATH, "//input[@ng-model='model.armKind']")

    class Kin(object):
        ship = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
        lastname = (By.XPATH, "//input[@name='lastName']")
        firstname = (By.XPATH, "//input[@name='firstName']")
        middlename = (By.XPATH, "//input[@name='middleName']")
        name_changes = (By.XPATH, "//textarea[@ng-model='rin.editmodel.nameChanges']")
        birth_date = (By.XPATH, "//div[@ng-model='rin.editmodel.birthDate']/input")
        birth_country = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
        birth_region = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        birth_area = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        birth_place = (By.XPATH, "//input[@data-ng-model='rin.editmodel.birthPlace']")
        work_place = (By.XPATH, "//textarea[@ng-model='rin.editmodel.workPlace']")
        living_country = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        living_address = (By.XPATH, "//input[@data-ng-model='rin.editmodel.livingAddress']")


class ProfileLocators:
    lastname = (By.XPATH, "//input[@ng-model='model.lastName']")
    firstname = (By.XPATH, "//input[@ng-model='model.firstName']")
    middlename = (By.XPATH, "//input[@ng-model='model.middleName']")
    birthdate = (By.XPATH, "//input[@id='birthDate']")
    insurance_certificate_number = (By.XPATH, "//input[@ng-model='model.insuranceCertificateNumber']")
    individual_taxpayer_number = (By.XPATH, "//input[@ng-model='model.inn']")
    email = (By.XPATH, "//input[@ng-model='model.email']")
    passport_info = (By.XPATH, "//input[@ng-model='model.passportInfo']")
    registration_address = (By.XPATH, "//input[@ng-model='model.registrationAddress']")
    actual_address = (By.XPATH, "//input[@ng-model='model.actualAddress']")
    old_password = (By.XPATH, "//input[@name='OldPassword']")
    password = (By.XPATH, "//input[@name='Password']")
    password_confirm = (By.XPATH, "//input[@name='PasswordConfirm']")
    change = (By.XPATH, "//input[@type='submit']")


class OrganizationsLocators(object):

    class New(object):
        code = (By.XPATH, "//input[@name='code']")
        name = (By.XPATH, "//input[@name='name']")
        name_genitive = (By.XPATH, "//input[@name='nameGenitive']")
        name_dative = (By.XPATH, "//input[@name='nameDative']")
        name_accusative = (By.XPATH, "//input[@name='nameAccusative']")
        short_name = (By.XPATH, "//input[@name='shortName']")
        source_type = (By.XPATH, "//div[@id='s2id_subType']")
        region = (By.XPATH, "//div[@id='s2id_okatoRegion']")
        area = (By.XPATH, "//div[@id='s2id_okatoArea']")
        profile = (By.XPATH, "//div[@id='s2id_okved']")
        code_okogu = (By.XPATH, "//*[@id='s2id_okogu']")
        code_okpo = (By.XPATH, "//input[@id='codeOkpo']")
        limit = (By.XPATH, "//input[@name='limitHR']")
        positions_registry = (By.XPATH, "//div[@id='s2id_postSection']")
        site = (By.XPATH, "//input[@name='officialWebsite']")
        contacts = (By.XPATH, "//input[@name='сontactInformation']")
        participate_in_rotation = (By.XPATH, "//*[@name='participateInRotation']")
        is_expired = (By.XPATH, "//*[@name='isExpired']")
        for_public_open_part = (By.XPATH, "//*[@name='forPublicOpenPart']")
        creation_order_number = (By.XPATH, "//*[@id='creationOrderNumber']")
        creation_order_date = (By.XPATH, "//*[@id='creationOrderDate']")
        creation_date = (By.XPATH, "//*[@id='creationDate']")

    class Edit(object):

        class Attributes(object):
            code = (By.XPATH, "//input[@name='code']")
            name = (By.XPATH, "//input[@name='name']")
            name_genitive = (By.XPATH, "//input[@name='nameGenitive']")
            name_dative = (By.XPATH, "//input[@name='nameDative']")
            name_accusative = (By.XPATH, "//input[@name='nameAccusative']")
            short_name = (By.XPATH, "//input[@name='shortName']")
            source_type = (By.XPATH, "//div[@id='s2id_subType']")
            region = (By.XPATH, "//div[@id='s2id_okatoRegion']")
            area = (By.XPATH, "//div[@id='s2id_okatoArea']")
            profile = (By.XPATH, "//div[@id='s2id_okved']")
            code_okogu = (By.XPATH, "//*[@id='s2id_okogu']")
            code_okpo = (By.XPATH, "//input[@id='codeOkpo']")
            limit = (By.XPATH, "//input[@name='limitHR']")
            positions_registry = (By.XPATH, "//div[@id='s2id_postSection']")
            site = (By.XPATH, "//input[@name='officialWebsite']")
            contacts = (By.XPATH, "//input[@name='сontactInformation']")
            participate_in_rotation = (By.XPATH, "//*[@name='participateInRotation']")
            is_expired = (By.XPATH, "//*[@name='isExpired']")
            for_public_open_part = (By.XPATH, "//*[@name='forPublicOpenPart']")
            creation_order_number = (By.XPATH, "//*[@id='creationOrderNumber']")
            creation_order_date = (By.XPATH, "//*[@id='creationOrderDate']")
            creation_date = (By.XPATH, "//*[@id='creationDate']")
            abolition_order_number = (By.XPATH, "//*[@id='abolitionOrderNumber']")
            abolition_order_date = (By.XPATH, "//*[@id='abolitionOrderDate']")
            abolition_date = (By.XPATH, "//*[@id='abolitionDate']")

        class Activity(object):
            pass

        class Positions(object):
            filter = (By.XPATH, "//div[contains(@id, 's2id')]")
            position = (By.XPATH, "//*[@id='s2id_post']")
            holiday_for_irregular_day = (By.XPATH, "//input[@id='holidayForIrregularDay']")
            code = (By.XPATH, "//input[@id='code']")
            name = (By.XPATH, "//input[@id='name']")
            short_name = (By.XPATH, "//input[@id='shortName']")
            name_genitive = (By.XPATH, "//input[@id='nameGenitive']")
            name_dative = (By.XPATH, "//input[@id='nameDative']")
            name_accusative = (By.XPATH, "//input[@id='nameAccusative']")
            name_instrumental = (By.XPATH, "//input[@ng-model='model.nameInstrumental']")
            type = (By.XPATH, "//*[@id='s2id_type']")
            group = (By.XPATH, "//*[@id='s2id_positionGroup']")
            can_be_rotated = (By.XPATH, "//input[@ng-model='model.canBeRotated']")
            submit_information_on_the_income = (By.XPATH, "//*[@ng-model='model.submitInformationOnTheIncome']")
            professional_experience = (By.XPATH, "//*[@id='s2id_professionalExperience']")
            government_experience = (By.XPATH, "//*[@id='s2id_governmentExperience']")
            education_level = (By.XPATH, "//*[@id='s2id_educationLevel']")

        class Curator(object):
            applications = (By.XPATH, "//div[contains(@id, 's2id')]")

        class Template(object):
            region = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
            area = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
            business_trips = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
            working_days = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
            working_schedule = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
            type = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
            location = (By.XPATH, "//input[@data-ng-model='model.registrationAddress']")
            time = (By.XPATH, "//input[@data-ng-model='model.registrationTime']")
            post_index = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
            web_site = (By.XPATH, "//input[@data-ng-model='model.webSite']")


class VacancyCreateLocators(object):
    type_vacancy = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    organization = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    # reserve = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    reason = (By.XPATH, "//input[@id='withoutCompetitionReason']")
    # structural_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
    # sub_structural = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
    # staff_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
    # post = (By.XPATH, "//div[contains(@id, 's2id')]")
    # work_type = (By.XPATH, "//div[contains(@id, 's2id')]")
    work_type_other_text = (By.XPATH, "//input[@name='workTypeOtherText']")
    # position_category = (By.XPATH, "//div[contains(@id, 's2id')]")
    # position_group = (By.XPATH, "//div[contains(@id, 's2id')]")
    # reserve_group = (By.XPATH, "//div[contains(@id, 's2id')]")
    # okato_region = (By.XPATH, "//div[contains(@id, 's2id')]")
    # okato_area = (By.XPATH, "//div[contains(@id, 's2id')]")
    salary_from = (By.XPATH, "//input[@id='salaryFrom']")
    salary_to = (By.XPATH, "//input[@id='salaryTo']")
    # business_trip = (By.XPATH, "//div[contains(@id, 's2id')]")
    # work_schedule = (By.XPATH, "//div[contains(@id, 's2id')]")
    # work_day = (By.XPATH, "//div[contains(@id, 's2id')]")
    # work_contract = (By.XPATH, "//div[contains(@id, 's2id')]")
    social_package_text = (By.XPATH, "//textarea[@data-ng-model='vacancy.socialPackage.text']")
    additional_position_info_text = (By.XPATH, "//textarea[@data-ng-model='vacancy.additionalPositionInfo.text']")
    job_responsibility_text = (By.XPATH, "//textarea[@id='jobResponsibility']")
    # education_level = (By.XPATH, "//div[contains(@id, 's2id')]")
    # government_experience = (By.XPATH, "//div[contains(@id, 's2id')]")
    # professional_experience = (By.XPATH, "//div[contains(@id, 's2id')]")
    knowledge_description_text = (By.XPATH, "//textarea[@name='knowledgeDescription']")
    additional_requirements = (By.XPATH, "//textarea[@data-ng-model='vacancy.additionalRequirements']")
    # test = (By.XPATH, "//div[contains(@id, 's2id')]")
    announcement_date = (By.XPATH, "//div[@data-ng-model='vacancy.announcementDate']/input")
    expiry_date = (By.XPATH, "//div[@data-ng-model='vacancy.expiryDate']/input")
    registration_address = (By.XPATH, "//input[@name='registrationAddress']")
    registration_time = (By.XPATH, "//input[@name='registrationTime']")
    # document_type = (By.XPATH, "//div[contains(@id, 's2id')]")
    description = (By.XPATH, "//input[@name='description']")
    sel = (By.XPATH, "(//input[@name='sel'])[2]")
    sel_study = (By.XPATH, "(//input[@name='sel'])[1]")
    delete = (By.XPATH, "//*[self::a or self::button][@data-ng-click='removeVacancyDocument()']")
    # organization_address = (By.XPATH, "//div[contains(@id, 's2id')]")
    address_mail = (By.XPATH, "//input[@name='addressMail']")
    phone = (By.XPATH, "//input[@name='phone']")
    phone2 = (By.XPATH, "//input[@data-ng-model='vacancy.phone2']")
    phone3 = (By.XPATH, "//input[@data-ng-model='vacancy.phone3']")
    email = (By.XPATH, "//input[@name='email']")
    contact_person_other = (By.XPATH, "//input[@name='contactPersonOther']")
    web = (By.XPATH, "//input[@data-ng-model='vacancy.web']")
    additional_info_text = (By.XPATH, "//textarea[@data-ng-model='vacancy.additionalInfo.text']")

    class PostIsCompetition(object):
        structural_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        sub_structural = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        staff_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        work_type = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
        position_category = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
        position_group = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
        okato_region = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
        okato_area = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
        business_trip = (By.XPATH, "(//div[contains(@id, 's2id')])[11]")
        work_schedule = (By.XPATH, "(//div[contains(@id, 's2id')])[12]")
        work_day = (By.XPATH, "(//div[contains(@id, 's2id')])[13]")
        work_contract = (By.XPATH, "(//div[contains(@id, 's2id')])[14]")
        education_level = (By.XPATH, "(//div[contains(@id, 's2id')])[15]")
        government_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[16]")
        professional_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[17]")
        test = (By.XPATH, "(//div[contains(@id, 's2id')])[18]")
        document_type = (By.XPATH, "(//div[contains(@id, 's2id')])[20]")
        organization_address = (By.XPATH, "(//div[contains(@id, 's2id')])[19]")

    class ReservePost(object):
        reserve = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        structural_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        sub_structural = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        post = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
        work_type = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
        reserve_group = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
        okato_region = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
        okato_area = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
        business_trip = (By.XPATH, "(//div[contains(@id, 's2id')])[11]")
        work_day = (By.XPATH, "(//div[contains(@id, 's2id')])[12]")
        work_schedule = (By.XPATH, "(//div[contains(@id, 's2id')])[13]")
        work_contract = (By.XPATH, "(//div[contains(@id, 's2id')])[14]")
        education_level = (By.XPATH, "(//div[contains(@id, 's2id')])[15]")
        government_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[16]")
        professional_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[17]")
        test = (By.XPATH, "(//div[contains(@id, 's2id')])[18]")
        document_type = (By.XPATH, "(//div[contains(@id, 's2id')])[20]")
        organization_address = (By.XPATH, "(//div[contains(@id, 's2id')])[19]")

    class ReserveGroupPosts(object):
        reserve = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        structural_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        sub_structural = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        work_type = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
        reserve_group = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
        okato_region = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
        okato_area = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
        business_trip = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
        work_day = (By.XPATH, "(//div[contains(@id, 's2id')])[11]")
        work_schedule = (By.XPATH, "(//div[contains(@id, 's2id')])[12]")
        work_contract = (By.XPATH, "(//div[contains(@id, 's2id')])[13]")
        education_level = (By.XPATH, "(//div[contains(@id, 's2id')])[14]")
        government_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[15]")
        professional_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[16]")
        test = (By.XPATH, "(//div[contains(@id, 's2id')])[17]")
        document_type = (By.XPATH, "(//div[contains(@id, 's2id')])[19]")
        organization_address = (By.XPATH, "(//div[contains(@id, 's2id')])[18]")

    class VacantStudy(object):
        structural_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        sub_structural = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        work_type = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        position_category = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
        position_group = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
        okato_region = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
        okato_area = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
        business_trip = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
        work_schedule = (By.XPATH, "(//div[contains(@id, 's2id')])[11]")
        work_day = (By.XPATH, "(//div[contains(@id, 's2id')])[12]")
        work_contract = (By.XPATH, "(//div[contains(@id, 's2id')])[13]")
        education_level = (By.XPATH, "(//div[contains(@id, 's2id')])[14]")
        government_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[15]")
        professional_experience = (By.XPATH, "(//div[contains(@id, 's2id')])[16]")
        test = (By.XPATH, "(//div[contains(@id, 's2id')])[17]")
        document_type = (By.XPATH, "(//div[contains(@id, 's2id')])[19]")
        organization_address = (By.XPATH, "(//div[contains(@id, 's2id')])[18]")

    class VacantState(object):
        structural_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
        sub_structural = (By.XPATH, "(//div[contains(@id, 's2id')])[4]")
        staff_unit = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
        work_type = (By.XPATH, "(//div[contains(@id, 's2id')])[6]")
        position_category = (By.XPATH, "(//div[contains(@id, 's2id')])[7]")
        position_group = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")


class VacancyManageLocators(object):
    status = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    type = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
    create_date = (By.XPATH, "(//input[@type='text'])[7]")
    comment = (By.XPATH, "(//textarea)[1]")
    create = (By.XPATH, "//*[self::a or self::button][normalize-space()='Создать']")
    approve = (By.XPATH, "//*[self::a or self::button][normalize-space()='На рассмотрение']")
    publish = (By.XPATH, "//*[self::a or self::button][normalize-space()='На публикацию']")
    published = (By.XPATH, "//*[self::a or self::button][normalize-space()='Опубликовать']")
    refine = (By.XPATH, "//*[self::a or self::button][normalize-space()='На доработку']")
    remove = (By.XPATH, "//*[self::a or self::button][normalize-space()='Удалить']")
    archive = (By.XPATH, "//*[self::a or self::button][normalize-space()='В архив']")
    copy = (By.XPATH, "//*[self::a or self::button][normalize-space()='Создать по образцу']")
    close = (By.XPATH, "//*[self::a or self::button][normalize-space()='Закрыть']")
    checkbox = (By.XPATH, "(//tr/td/input[@type='checkbox'])[1]")


class ReserveViewFederalLocators(object):
    permission_read_resume = (By.XPATH, "(//input[@type='checkbox'])[7]")
    level_reserve = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    resume = (By.XPATH, "//a[@class='custom-icon-doc']")
    presentation = (By.XPATH, "//span[@class='custom-icon-doc']")


class ManageReserveBasesLocators(object):
    code = (By.XPATH, "//input[@name='code']")
    name = (By.XPATH, "//input[@name='name']")
    edit = (By.XPATH, "(//a[@ng-click='edit(base.id)'])[1]")
    delete = (By.XPATH, "(//a[@ng-click='del(base)'])[1]")


class CertificatePlanningLocators(object):
    name = (By.XPATH, "//input[@id='name']")
    organization = (By.XPATH, "//div[@id='s2id_organization']")
    order_date = (By.XPATH, "//input[@id='orderDate']")
    order_number = (By.XPATH, "//input[@id='orderNumber']")
    by = (By.XPATH, "//div[@id='s2id_signer']")
    type = (By.XPATH, "//div[@id='s2id_commissionType']")
    date_from = (By.XPATH, "//input[@id='startDate']")
    date_to = (By.XPATH, "//input[@id='endDate']")
    role = (By.XPATH, "//div[@id='role']")
    fullname = (By.XPATH, "//div[@id='fullname']")
    phone = (By.XPATH, "//input[@id='phone']")
    email = (By.XPATH, "//input[@id='email']")
    number = (By.XPATH, "//input[@id='number']")


class ReserveBasesPrepareLocators(object):
    personal_file = (By.XPATH, "(//div[contains(@id, 's2id')])[8]")
    presentation_reserve_level = (By.XPATH, "(//div[contains(@id, 's2id')])[9]")
    grade_of_post = (By.XPATH, "(//div[contains(@id, 's2id')])[10]")
    documents = (By.XPATH, "//a[@class='ng-binding ng-isolate-scope']")
    resume = (By.XPATH, "(//a[@class='custom-icon-doc'])[1]")
    presentation = (By.XPATH, "(//a[@class='custom-icon-doc'])[2]")
    last_name = (By.XPATH, "//input[@name='lastName']")
    first_name = (By.XPATH, "//input[@name='firstName']")
    middle_name = (By.XPATH, "//input[@name='middleName']")
    gender = (By.XPATH, "(//div[contains(@id, 's2id')])[1]")
    tax_certificate_number = (By.XPATH, "//input[@name='taxCertificateNumber']")
    insurance_certificate_number = (By.XPATH, "//input[@name='insuranceCertificateNumber']")
    birth_date = (By.XPATH, "//input[@id='birthDate']")
    citizenship = (By.XPATH, "(//div[contains(@id, 's2id')])[2]")
    birth_place = (By.XPATH, "//input[@ng-model='model.generalInformation.birthPlace']")
    marital_statuses = (By.XPATH, "(//div[contains(@id, 's2id')])[3]")
    work_phone = (By.XPATH, "//input[@id='workPhone']")
    mobile_phone = (By.XPATH, "//input[@ng-model='model.mobilePhone']")
    additional_phone = (By.XPATH, "//input[@ng-model='model.additionalPhone']")
    residence_phone = (By.XPATH, "//input[@ng-model='model.residencePhone']")
    fax = (By.XPATH, "//input[@ng-model='model.fax']")
    work_email = (By.XPATH, "//input[@id='workEmail']")
    personal_email = (By.XPATH, "//input[@id='personalEmail']")
    web = (By.XPATH, "//input[@id='web']")
    registration_region = (By.XPATH, "//div[@id='s2id_registrationRegion']")
    registration_area = (By.XPATH, "//div[@id='s2id_registrationArea']")
    residence_region = (By.XPATH, "//div[@id='s2id_residenceRegion']")
    residence_area = (By.XPATH, "//div[@id='s2id_residenceArea']")
    education_level = (By.XPATH, "//div[@id='educationLevel']")
    education_kinds = (By.XPATH, "//div[@id='educationKinds']")
    education_forms = (By.XPATH, "//div[@id='educationForms']")
    place = (By.XPATH, "//input[@id='place']")
    temp_institution = (By.XPATH, "//input[@id='tempInstitution']")
    start_date = (By.XPATH, "//input[@id='startDate']")
    end_date = (By.XPATH, "//input[@id='endDate']")
    faculty = (By.XPATH, "//input[@id='faculty']")
    education_doc_number = (By.XPATH, "//input[@id='educationDocNumber']")
    speciality = (By.XPATH, "//div[@id='speciality']")
    qualification = (By.XPATH, "//div[@id='qualification']")
    specialization = (By.XPATH, "//div[@id='specialization']")
    begin_date = (By.XPATH, "//input[@id='beginDate']")
    end_date = (By.XPATH, "//input[@id='endDate']")
    organization = (By.XPATH, "//input[@id='organization']")
    address_organization = (By.XPATH, "//input[@id='addressOrganization']")
    structural_division = (By.XPATH, "//input[@id='structuralDivision']")
    post = (By.XPATH, "//input[@id='post']")
    post_levels = (By.XPATH, "//div[@id='postLevels']")
    employees_numbers = (By.XPATH, "//div[@id='employeesNumbers']")
    profile = (By.XPATH, "//div[@id='profile']")
    professional_activity_area = (By.XPATH, "//div[@id='professionalActivityArea']")
    responsibilities = (By.XPATH, "//input[@id='responsibilities']")
    job_types = (By.XPATH, "//div[@id='jobTypes']")
    expectations = (By.XPATH, "//textarea[@id='expectations']")
    organization_sub_type = (By.XPATH, "//div[@id='organizationSubType']")
    organization = (By.XPATH, "//div[@id='organization']")
    organization_other = (By.XPATH, "//input[@id='organizationOther']")
    ready_to_move = (By.XPATH, "//select[@id='readyToMove']")
    salary_from = (By.XPATH, "//input[@id='salaryFrom']")
    salary_to = (By.XPATH, "//input[@id='salaryTo']")
    computer_skills = (By.XPATH, "//input[@id='computerSkills']")
    publications = (By.XPATH, "//input[@id='publications']")
    recommendations = (By.XPATH, "//input[@id='recommendations']")
    additional_info = (By.XPATH, "//input[@id='additionalInfo']")
    availability_degree = (By.XPATH, "(//div[contains(@id, 's2id')])[5]")
    position = (By.XPATH, "(//input[@type='text'])[15]")
    recomendations = (By.XPATH, "(//textarea)[1]")
    professional_achievements = (By.XPATH, "(//textarea)[2]")
    developement_area = (By.XPATH, "(//textarea)[3]")
    additional_preperation_text = (By.XPATH, "(//textarea)[4]")
