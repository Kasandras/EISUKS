
from pages import *
import pytest


class TestSuite:
    """
    Содержание test-suite:
        Учет кадрового состава - Ведение электронных личных дел
        Организационно-штатная структура - Формирование организационно-штатной структуры
        Формирование кадрового состава - Назначение на должность
        Прохождение государственной гражданской службы - Присвоен/ие классных чинов
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
    driver = webdriver.Chrome(Settings.path_to_driver)

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
        execute_script(Queries.delete_from_fruk)
        execute_script(Queries.delete_personal_file)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize("last_name", ["Автоматизация"])
    def test_new_personal_file(self, last_name):
        """
        Учет кадрового состава - Ведение электронных личных дел
        """

        data = get_data_by_value(self.data, "employees", "lastName", last_name)

        AlternativeLoginPage(self.driver).login(data=self.hr)

        page = AlternativePersonalFilePage(self.driver, test='Создание нового пользователя')
        page.go_to(Links.personal_files)
        page.add.click()
        page.new.last_name = data["lastName"]
        page.new.first_name = data["firstName"]
        page.new.middle_name = data["middleName"]
        page.new.birth_date = data["birthday"]
        page.new.insurance_certificate_number = data["insuranceCertificateNumber"]
        page.new.user_name = data["username"]
        page.new.save.click()

        page.wait.text_appear("Личные сведения")

        page.general.general_edit.click()
        page.general.last_name = data["lastName"]
        page.general.first_name = data["firstName"]
        page.general.middle_name = data["middleName"]
        page.general.personal_file_number = data["personalFileNumber"]
        page.general.gender = data["gender"]
        page.general.birth_date = data["birthday"]
        page.general.citizenship = data["citizenship"]
        page.general.birth_place = data["birthPlace"]
        page.general.was_convicted = data["wasConvicted"]
        page.general.name_was_changed = data["nameWasChanged"]
        page.general.insurance_certificate_number = data["insuranceCertificateNumber"]
        page.general.save.click()

        page.wait.text_disappear("Сохранить")
