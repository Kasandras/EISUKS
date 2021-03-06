from time import localtime, strftime, sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import datetime
import os
import requests


def today():
    return datetime.date.today().strftime("%d.%m.%Y")


class Browser(object):

    def __init__(self, driver, timeout=60, log=True, test=None):
        self.driver = driver
        self.timeout = timeout
        self.log = log
        self.root = ""
        self.wait = Wait(self.driver, self.timeout)
        if test:
            print("\nТест: %s\n" % test)

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present())
            self.driver.switch_to_alert().accept()
        except TimeoutException:
            pass

    def decline_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.alert_is_present())
            self.driver.switch_to_alert().decline()
        except TimeoutException:
            pass

    def click(self, locator, label=None):
        self.wait_for_loading()
        element = self.wait.element_be_clickable(locator)
        self.move_to_element(element)
        element.click()
        if label and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), label))

    def click_by_text(self, text, order=1, exactly=False):
        self.wait_for_loading()
        if exactly:
            locator = (By.XPATH, "(//*[self::a or self::button][normalize-space()='%s'])[%s]" % (text, order))
        else:
            locator = (By.XPATH,
                       "(//*[self::a or self::button][contains(normalize-space(), '%s')])[%s]" % (text, order))
        element = self.wait.element_be_clickable(locator)
        self.move_to_element(element)
        element.click()
        if text and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), text))

    def click_by_value(self, value, order=1, exactly=False):
        self.wait_for_loading()
        if exactly:
            locator = (By.XPATH, "(//input[@value='%s'])[%s]" % (value, order))
        else:
            locator = (By.XPATH, "(//input[contains(@value, '%s')])[%s]" % (value, order))
        element = self.wait.element_be_clickable(locator)
        self.move_to_element(element)
        element.click()
        if value and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), value))

    def go_to(self, url):
        while True:
            self.driver.get(url)
            if self.driver.current_url == url:
                break
            sleep(1)
        if self.log:
            print("Переход по ссылке: %s" % url)

    def move_to_element(self, element):
        self.wait_for_loading()
        webdriver.ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to_top(self):
        self.wait_for_loading()
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        self.wait_for_loading()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def search(self, value):
        self.wait_for_loading()
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), value)
        self.click_by_text("Применить")

    def select2_clear(self, locator):
        self.wait_for_loading()
        element = self.wait_for_element_appear(locator)
        while True:
            try:
                element.click()
            except (ec.StaleElementReferenceException, ec.NoSuchElementException):
                break

    def set_text(self, locator, value, label=None):
        if value:
            self.wait_for_loading()
            element = self.wait.element_be_clickable(locator)
            element.clear()
            element.send_keys(value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_text_and_check(self, locator, value, label=None):
        if value:
            self.wait_for_loading()
            element = self.wait.element_be_clickable(locator)
            element.clear()
            element.send_keys(value)
            WebDriverWait(self.driver, self.timeout).until(lambda x: element.get_attribute("value") == value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_date(self, locator, value, label=None):
        if value:
            if value == "=":
                value = today()
            self.wait_for_loading()
            element = self.wait.element_be_clickable(locator)
            element.clear()
            element.send_keys(value + Keys.TAB)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_checkbox(self, locator, value=True, label=None):
        element = self.wait.element_be_clickable(locator)
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    def set_checkbox_by_order(self, order=1, value=True, label=None):
        element = self.wait_for_element_appear((By.XPATH, "(//input[@type='checkbox'])[%s]" % order))
        if element.is_selected() != value:
            self.move_to_element(element)
            element.click()
            if label and self.log:
                print("[%s] [%s] установка флага в положение \"%s\"" % (strftime("%H:%M:%S",
                                                                                 localtime()), label, value))

    def set_radio(self, locator, label=None):
        element = self.wait_for_element_appear(locator)
        element.click()
        if label and self.log:
            print("[%s] [%s] выбор опции" % (strftime("%H:%M:%S", localtime()), label))

    def set_select(self, value, order=1, label=None):
        if value:
            self.wait_for_loading()
            locator = (By.XPATH, "(//select)[%s]" % order)
            element = self.wait_for_element_appear(locator)
            Select(element).select_by_visible_text(value)
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_select_alt(self, locator, value, label=""):
        if value:
            self.wait.loading()
            element = self.wait.element_appear(locator)
            Select(element).select_by_visible_text(value)
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_select2(self, locator, value, label=None):
        if value:
            self.click(locator)
            self.set_text_and_check((By.XPATH, "//div[@id='select2-drop']//input"), value)
            option = self.wait.element_be_clickable(
                (By.XPATH, "//*[@role='option'][contains(normalize-space(), '%s')]" % value))
            option.click()
            self.wait_for_element_disappear((By.ID, "select2-drop"))
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_select2_alt(self, locator, value, label=None):
        if value:
            self.click(locator)
            element = self.wait_for_element_appear(locator)
            input_field = element.find_element(By.XPATH, ".//input")
            input_field.clear()
            input_field.send_keys(value)
            self.click((By.XPATH, "//*[@role='option'][contains(normalize-space(), '%s')]" % value))
            self.wait_for_element_disappear((By.ID, "select2-drop"))
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_radio_by_order(self, order=1, label=None):
        self.click((By.XPATH, "(//input[@type='radio'])[%s]" % order))
        if label and self.log:
            print("[%s] [%s] выбор переключателя" % (strftime("%H:%M:%S", localtime()), label))

    def table_select_row(self, order=1, label=None):
        self.wait_for_loading()
        locator = (By.XPATH, "(//td/input[@type='checkbox'])[%s]" % order)
        self.set_checkbox(locator, True, label)

    def table_row_checkbox(self, order=1):
        self.wait_for_loading()
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='checkbox'])[%s]" % order)
        self.set_checkbox(locator, True)
        sleep(1)

    def tab_close(self, order=1):
        if order != 1:
            self.driver.switch_to.window(self.driver.window_handles[order])
        self.driver.close()

    def tab_switch(self, order):
        self.driver.switch_to.window(self.driver.window_handles[order])

    def table_row_checkbox_by_text(self, text):
        self.wait_for_loading()
        locator = (By.XPATH, "//tr[contains(., '%s')]//input[@type='checkbox']" % text)
        self.set_checkbox(locator, True)

    def table_row_radio_by_text(self, text):
        self.wait_for_loading()
        locator = (By.XPATH, "//tr[contains(., '%s')]//input[@type='radio']" % text)
        self.set_radio(locator)

    def table_row_radio(self, order=1):
        self.wait_for_loading()
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='radio'])[%s]" % order)
        self.set_radio(locator)
        sleep(1)

    def upload_file(self, value, order=1):
        self.wait_for_loading()
        # открываем страницу с формой загрузки файла
        container = self.driver.find_element(By.XPATH, "(//div[@class='qq-uploader'])[%s]" % order)
        input_field = container.find_element(By.XPATH, ".//input[@type='file']")
        input_field.clear()
        input_field.send_keys("%s/sources/%s" % (os.getcwd(), value))
        WebDriverWait(self.driver, 60).until(
            ec.visibility_of_element_located((By.XPATH,
                                              "(//div[@class='qq-uploader'])[%s]//li[contains(., 'Удалить')]" % order)))

    def upload_photo(self, value, order=1):
        self.wait_for_loading()
        # открываем страницу с формой загрузки файла
        element = self.driver.find_element(By.XPATH, "(//input[@type='file'])[%s]" % order)
        element.clear()
        element.send_keys("%s/files/%s" % (os.getcwd(), value))
        WebDriverWait(self.driver, 60).until(
            ec.visibility_of_element_located((By.XPATH, "//*[self::a or self::button][.='Удалить']")))

    def wait_for_text_appear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    def wait_for_text_disappear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    def wait_for_element_appear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_element_disappear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located(locator))

    def wait_for_loading(self):
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//img[@alt='Загрузка']")))

    def is_text_on_page(self, text):
        return text in self.driver.page_source

    def prepare_cookies_for_request(self):
        cookies = self.driver.get_cookies()
        s = requests.Session()
        for cookie in cookies:
            s.cookies.set(cookie['name'], cookie['value'])
        return s.cookies

    @staticmethod
    def today():
        return datetime.date.today().strftime("%d.%m.%Y")


class Wait(object):
    """
    Methods for waiting
    """
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def text_appear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    def text_disappear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    def element_appear(self, locator, msg=""):
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator), msg)

    def element_disappear(self, locator, msg=""):
        return WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located(locator), msg)

    def element_be_clickable(self, locator, msg=""):
        return WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator), msg)

    def lamb(self, exe):
        return WebDriverWait(self.driver, self.timeout).until(exe)

    def loading(self):
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//img[@alt='Загрузка']")))


class Checker(object):
    """
    Methods for checking
    """
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.wait = Wait(self.driver, self.timeout)

    def for_input(self, locator, value):
        element = self.wait.element_appear(locator)
        text = element.get_attribute("value")
        if text == value:
            return True
        else:
            return False
