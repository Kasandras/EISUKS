from pages import *


class TestSuite:
    """
    Содержание test-suite:

    """
    driver = webdriver.Chrome(Settings.path_to_driver)

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_news(self):
        p = MainPage(self.driver)
        p.click_by_text("Новости")
        p.click((By.XPATH, "//a[contains(@href, 'News/Details/')]"))
        same_news = self.driver.find_element(By.ID, "affix")
        same_news.find_element(By.XPATH, ".//a").click()
        p.click_by_text("Новости")
        p.set_date((By.ID, "newsFrom"), "30.07.2015")
        p.set_date((By.ID, "newsTo"), "30.07.2016")
        sleep(1)
        p.click_by_text("Поиск")

    def test_documents(self):
        p = MainPage(self.driver)
        p.click_by_text("Документы")
        p.set_date((By.XPATH, "//input[@type='text']"), "Методический материал № 324")
        p.click_by_text("Методический материал № 324")
        p.click_by_text("Очистить")
        assert self.driver.find_element(By.XPATH, "//input[@type='text']").text == ""

    def test_vacancies(self):
        p = MainPage(self.driver)
        p.click_by_text("Вакансии")
        # sort
        caret_xpath = "//span[contains(@class, 'caret')]"
        p.click((By.XPATH, caret_xpath))
        p.click((By.XPATH, caret_xpath))
        p.click_by_text("Дата окончания приема документов")
        p.click_by_text("Дата начала приема документов")
        p.click((By.XPATH, caret_xpath))
        p.click((By.XPATH, caret_xpath))
        p.click_by_text("Дата начала приема документов")
        p.click_by_text("Заработная плата")
        p.click((By.XPATH, caret_xpath))
        p.click((By.XPATH, caret_xpath))
        # search
        p.click((By.ID, "s2id_autogen1"))
        p.click((By.XPATH, "//div[.='Алтайский край']"))
        p.click_by_text("Поиск")
        # apply
        p.click((By.XPATH, "//p[@class='title']"))
        p.click_by_text("Подать документы")
        sleep(1)
        assert "Вход" in self.driver.page_source
        p.click((By.XPATH, "//input[@value='Отмена']"))
        sleep(1)

    def test_analytics(self):
        p = MainPage(self.driver)
        p.click_by_text("Аналитика")
        p.click_by_text("Работа с Порталом")
        p.click_by_text("Работа с Порталом")
        p.click_by_text("Аналитика")
        p.click((By.ID, "select2-chosen-1"))
        p.click((By.XPATH, "//li[@role='presentation'][2]"))
        sleep(1)
        assert "Численность работников, замещавших должности гражданских и " \
               "муниципальных служащих, и укомплектованность этих должностей" in self.driver.page_source

    def test_reserve(self):
        p = MainPage(self.driver)
        p.scroll_to_top()
        p.click_by_text("Резерв кадров")
        p.click_by_text("Дополнительная информация")
        self.driver.back()
        sleep(1)
        assert self.driver.find_element(By.XPATH,
                                        "//div[@class='PieChart']") and self.driver.find_element(By.ID, "canvas")

    def test_about_site(self):
        p = MainPage(self.driver)
        p.click_by_text("Что такое портал")
        self.driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        p.click((By.XPATH, "//button[@class='btn btn-up']"))
        sleep(1)

    def test_site_in_numbers(self):
        p = MainPage(self.driver)
        p.click_by_text("Статистика")
        p.set_select("Количество посещений за последнюю неделю")
        sleep(1)
        p.set_select("Количество посещений в целом")
        sleep(1)
        p.set_select("Количество актуальных вакансий")
        sleep(1)
        p.set_select("Количество граждан РФ, разместивших анкету")
        sleep(1)
        assert self.driver.find_element(By.ID, "canvas")

    def test_registration(self):
        p = MainPage(self.driver)
        p.click_by_text("Регистрация граждан")
        p.click_by_text("Зарегистрироваться")
        p.set_text((By.ID, "LastName"), "Иванов")
        p.set_text((By.ID, "FirstName"), "Иван")
        p.set_text((By.ID, "MiddleName"), "Иванович")
        p.set_date((By.ID, "BirthDate"), "04.04.1966")
        p.set_text((By.ID, "Snils"), "123-456-789 00")
        p.set_text((By.ID, "Email"), "mail@mail.com")
        p.set_text((By.ID, "EmailConfirm"), "mail@mail.com")
        p.set_text((By.ID, "Password"), "password")
        p.set_text((By.ID, "PasswordConfirm"), "password")
        p.set_text((By.ID, "_decryptCapcha"), "12345")
        p.click((By.XPATH, "//input[@type='checkbox']"))
        p.click((By.XPATH, "//input[@value='Очистить']"))
        sleep(1)

    def test_faq(self):
        p = MainPage(self.driver)
        p.click_by_text("Часто задаваемые вопросы")
        self.driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        p.click((By.XPATH, "//button[@class='btn btn-up']"))
        sleep(1)

    def test_access_to_site(self):
        p = MainPage(self.driver)
        p.click_by_text("Подключение органов и организаций")
        p.click_by_text("Номинация «Кадровый учет»")
        sleep(1)
        p.click_by_text("Номинация «Кадровый учет»")
        sleep(1)
        p.click_by_text("Номинация «Профессиональное развитие и оценка кадров»")
        sleep(1)
        p.click_by_text("Номинация «Профессиональное развитие и оценка кадров»")
        sleep(1)
        p.click_by_text("Номинация «Противодействие коррупции»")
        sleep(1)
        p.click_by_text("Номинация «Противодействие коррупции»")
        sleep(1)
        p.click_by_text("Практическая работа с Федеральным порталом государственной службы и управленческих кадров")
        sleep(1)
        p.click_by_text("Практическая работа с Федеральным порталом государственной службы и управленческих кадров")

    def test_system_of_service(self):
        p = MainPage(self.driver)
        p.click_by_text("Система госслужбы")
        p.click_by_text("Информация о")
        sleep(1)
        p.click_by_text("Принципы госслужбы")
        sleep(1)
        p.click_by_text("Государственные гарантии госслужащих")
        sleep(1)
        p.click_by_text("Должности госслужбы")
        sleep(1)

    def test_enrollment_to_service(self):
        p = MainPage(self.driver)
        p.click_by_text("Поступление на госслужбу")
        self.driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        p.click((By.XPATH, "//button[@class='btn btn-up']"))
        sleep(1)
        p.click_by_text("Поступление на")
        sleep(1)
        p.click_by_text("Требования к кандидатам на замещение вакантных должностей госслужбы")
        sleep(1)
        p.click_by_text("Испытание при поступлении на")
        sleep(1)

    def test_service_passing(self):
        p = MainPage(self.driver)
        p.click_by_text("Прохождение госслужбы")
        self.driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        p.click((By.XPATH, "//button[@class='btn btn-up']"))
        sleep(1)
        p.click_by_text("Основные права и обязанности госслужащего")
        sleep(1)
        p.click_by_text("Ограничения и запреты, связанные с госслужбой")
        sleep(1)
        p.click_by_text("Классные чины")
        sleep(1)
        p.click_by_text("Должностной регламент")
        sleep(1)
        p.click_by_text("Служебный контракт")
        sleep(1)
        p.click_by_text("Аттестация госслужащего")
        sleep(1)
        p.click_by_text("Квалификационный экзамен")
        sleep(1)
        p.click_by_text("Оплата труда госслужащего")
        sleep(1)
        p.click_by_text("Служебное время, время отдыха и отпуск на госслужбе")
        sleep(1)
        p.click_by_text("Поощрения и награждения за госслужбу")
        sleep(1)
        p.click_by_text("Дисциплинарные взыскания")
        sleep(1)
        p.click_by_text("Кадровый резерв на госслужбе")
        sleep(1)
        p.click_by_text("Отстранение от замещаемой должности госслужбы")
        sleep(1)

    def test_against_corruption(self):
        p = MainPage(self.driver)
        p.click_by_text("О противодействии коррупции")
        self.driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        p.click((By.XPATH, "//button[@class='btn btn-up']"))
        sleep(1)
        p.click_by_text("противодействии коррупции")
        sleep(1)
        p.click_by_text("Конфликт интересов")
        sleep(1)

    def test_education_organizations(self):
        p = MainPage(self.driver)
        p.click_by_text("Образовательные организации")

        p.click_by_text("Московский государственный университет имени М.В. Ломоносова")
        sleep(1)
        self.driver.back()
        p.click_by_text("Национальный исследовательский университет \"Высшая школа экономики\"")
        sleep(1)
        self.driver.back()
        p.click_by_text("Российская академия народного хозяйства и "
                        "государственной службы при Президенте Российской Федерации")
        sleep(1)
        self.driver.back()
        p.click_by_text("Финансовый университет при Правительстве Российской Федерации")
        sleep(1)
        self.driver.back()

    def test_processing_reserve(self):
        p = MainPage(self.driver)
        p.click_by_text("Подготовка резерва")
        p.click((By.XPATH, "//h3[.='Высший уровень резерва']"))
        sleep(1)
        p.click((By.XPATH, "//label[.='Второй поток обучения ']"))
        sleep(1)
        p.click((By.XPATH, "//a[.='График обучения']"))
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        sleep(1)
        p.click((By.XPATH, "//button[@class='btn btn-up']"))
        sleep(1)
        p.click_by_text("Скачать")
        sleep(5)

    def test_test_for_control(self):
        self.driver.get("http://gossluzhba1.qtestweb.office.quarta-vk.ru/"
                        "testing/app#/testing/run/action/3e13a2e8-2594-484a-8d81-7238b10af68c")
        p = MainPage(self.driver)
        p.click((By.XPATH, "(//input[@type='radio'])[4]"), "Выбор варианта ответа")
        sleep(1)
        p.click_by_text("Следующий")
        p.click((By.XPATH, "(//input[@type='radio'])[3]"), "Выбор варианта ответа")
        sleep(1)
        p.click_by_text("Следующий")
        p.click((By.XPATH, "(//input[@type='radio'])[4]"), "Выбор варианта ответа")
        sleep(1)
        p.click((By.XPATH, "//input[@type='button']"))
        sleep(5)
        assert "Отвечено верно на 1 из 3 вопросов, что составляет 33%" \
               " от общего числа заданных вопросов в тесте" in self.driver.page_source
