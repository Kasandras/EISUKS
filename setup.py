import json
import os


def load_data(file):
    filename = "%s/data/%s.json" % (os.getcwd(), file)
    return json.loads(open(filename, encoding="utf8").read())


def get_data_by_value(data, parent, key, value):
    for i in data[parent]:
        if value == i[key]:
            return i
    return None


def get_data_by_number(data, parent, number=0):
    return data[parent][number]


class Settings(object):
    path_to_driver = "drivers/chromedriver.exe"


# def execute_script(query, server="QTESTEISUKS2", database="eisuks_reserve_hr", username="HRUser", password="P@ssw0rd123456"):
#     conn = pymssql.connect(server=server, user=username, password=password, database=database)
#     cursor = conn.cursor()
#     cursor.execute(query)
#     conn.close()


class Links(object):
    main_page = "http://gossluzhba1.qtestweb.office.quarta-vk.ru/"
    dashboard = main_page + "Dashboard/Hr"
    personal_files = main_page + "PersonalData/PersonalFile#/list"
    staff_structure = main_page + "Staff/Structure#/"
    appointment = main_page + "Staff/AppointmentStaffProcedure"
    dismissal = main_page + "Staff/DismissalStaffProcedure"
    salary_payments = main_page + "Staff/SalaryStaffProcedure"
    vacancy_list = main_page + "Recruitment/Vacancy#/list"
    vacancy_selection = main_page + "Recruitment/Vacancy#/selection"
    commissions = main_page + "Commissions#/commission/list"
    independent_experts = main_page + "Commissions#/member/independent-expert/list"
    awards = main_page + "Staff/AwardStaffProcedure"
    enforcement = main_page + "Staff/DisciplineStaffProcedure"
    dispensary_planning = main_page + "Dispensary/Dispensary/#/plan"
    dispensary_list = main_page + "Dispensary#/list"
    business_trips = main_page + "Staff/BusinessTripStaffProcedure"
    business_trips_index = main_page + "StaffProcedure/BusinessTrip#/index"
    holidays = main_page + "Staff/HolidayStaffProcedure"
    holidays_schedule = main_page + "TimeSheet/HolidaySchedule#/list"
    ranks = main_page + "Staff/RankStaffProcedure"
    application_form = main_page + "Documents/Home#/layout/applicationForm/list"
    profile = main_page + "Member/Profile#/view"
    reserve_view_federal = main_page + "Reserve/View#/federal"
    reserve_bases_prepare = main_page + "Reserve/Prepare#/federal"
    permission_read_resume = main_page + "Admin/Role#/permissions/00000000-0000-0002-ffff-ffffffffffff/permission/d1eb4a97-a6fc-4f12-89fe-21d472926148"
    manage_reserve_bases = main_page + "Classifier/Classifier#/reservebases/list"
