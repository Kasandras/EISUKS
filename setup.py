import json


def load_data(file):
    return json.loads(open('%s.json' % file, encoding="utf8").read())


def get_data_by_value(data, parent, key, value):
    for i in data[parent]:
        if value == i[key]:
            return i
    return None


def get_data_by_number(data, parent, number=0):
    return data[parent][number]


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
    appform = main_page + "Documents/Home#/layout/applicationForm/list"
    profile = main_page + "Member/Profile#/view"
