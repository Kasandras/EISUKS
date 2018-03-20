import json
import os
import pymssql
from selenium import webdriver


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


def execute_script(query,
                   server="QTESTEISUKS",
                   database="eisuks_reserve_hr",
                   username="HRUser",
                   password="P@ssw0rd123456"):
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


class Driver(object):

    user = os.environ.get('USERNAME')

    @property
    def chromedriver(self):
        return webdriver.Chrome("C:/Users/{0}/PycharmProject/eisuks/drivers/chromedriver.exe".format(self.user))


class Links(object):
    main_page = "http://gossluzhba.qtestweb.office.quarta-vk.ru/"
    # main_page = "https://test.gossluzhba.gov.ru/"
    dashboard = main_page + "Dashboard/Hr"
    create_personal_file = main_page + "PersonalData/PersonalFile#/00000000-0000-0000-0000-000000000000/generalinfo/create"
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


class Queries(object):
    # скрипт для удаления записи из ФРУКа
    delete_from_fruk = """
    DELETE FROM [eisuks_reserve_hr].[Reserve].[FederalReserve]
    WHERE PersonalFilesID='95b5360a-9507-4fc1-891b-9602d8629063';
    """
    # скрипт для удаления личного дела
    delete_personal_file = """
    Declare     @FistName   nvarchar(500)     = 'Автоматизация'
      ,           @LastName   nvarchar(500)     = 'Автоматизация'
      ,           @MiddleName nvarchar(500)    = 'Автоматизация'
      
      ,           @ID               UNIQUEIDENTIFIER  
      

      Declare DeletePersonalFile Cursor Local For
      select PersonalFiles.ID 
            from Applicant.PersonalFiles
            inner join Applicant.PersonalCardGeneralInformations 
                  on PersonalFiles.CardId = PersonalCardGeneralInformations.ID
                  and PersonalCardGeneralInformations.FirstName = @FistName
                  and PersonalCardGeneralInformations.LastName = @LastName
                  and PersonalCardGeneralInformations.MiddleName = @MiddleName
      Open DeletePersonalFile
      Fetch Next From DeletePersonalFile into @ID
      While @@FETCH_STATUS=0
      Begin
      
            exec [Applicant].[DeletePersonalFile]  @ID
            
            Fetch Next From DeletePersonalFile into @ID
            Continue

      end
      Close DeletePersonalFile
      Deallocate DeletePersonalFile 
    """