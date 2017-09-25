from pages import *
from setup import *


class TestSuite:
    """
    Тест по сценарию "Профиль".
    Описывает работу с разделом "Профиль" (заполнение формы, изменение пароля)
    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.data = load_data("gossluzhba1")
        cls.account = get_data_by_number(load_data("gossluzhba1"), "accounts", 4)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_profile(self):
        """
        Профиль (тестирование раздела "Профиль")
        """
        page = ProfilePage(self.driver)
        data = get_data_by_value(self.data, "members", "upload_photo", "photo_female.jpg")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["fullName"])
        page.click_by_text("Профиль", 2)
        page.click_by_text("Редактировать")
        page.upload_file(data["upload_photo"])
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
        page.click_by_text("Изменить пароль")
        page.old_password(data["old_password"])
        page.password(data["password"])
        page.password_confirm(data["password_confirm"])
        page.change()
        assert "Пароль изменен" in self.driver.page_source
