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
        cls.account = get_data_by_number(load_data("drozdovData")["users"], "accounts", 2)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_profile(self):
        """
        Профиль (тестирование раздела "Профиль")
        """
        page = ProfilePage(self.driver)
        profile = get_data_by_value(load_data("drozdovData")["members"], "profiles", "lastName", "Шабанова")

        LoginPage(self.driver).login(self.account["username"], self.account["password"], self.account["full_name"])
        page.click_by_text("Профиль", 2)
        page.click_by_text("Редактировать")
        page.upload_photo(profile["upload_photo"])
        page.last_name(profile["lastName"])
        page.first_name(profile["firstName"])
        page.middle_name(profile["middleName"])
        page.birth_date(profile["birthDate"])
        page.insurance_certificate_number(profile["insurance_certificate_number"])
        page.individual_taxpayer_number(profile["individual_taxpayer_number"])
        page.email(profile["email"])
        page.passport_info(profile['passport_info'])
        page.registration_address(profile["registration_address"])
        page.actual_address(profile["actual_address"])
        page.click_by_text("Сохранить")
        page.click_by_text("Изменить пароль")
        page.old_password(profile["old_password"])
        page.password(profile["password"])
        page.password_confirm(profile["password_confirm"])
        page.change()
        assert "Пароль изменен" in self.driver.page_source
