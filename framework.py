from time import localtime, strftime, sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import datetime


class Browser(object):

    def __init__(self, driver, timeout=60, log=True):
        self.driver = driver
        self.timeout = timeout
        self.log = log

    def search(self, value):
        self.wait_for_loading()
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), value)
        self.click_by_text("Применить")

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            self.driver.switch_to_alert().accept()
        except TimeoutException:
            pass

    def set_text(self, locator, value, label=None):
        if value:
            self.wait_for_loading()
            element = self.wait_for_element_appear(locator)
            element.clear()
            element.send_keys(value)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_date(self, locator, value, label=None):
        if value:
            self.wait_for_loading()
            element = self.wait_for_element_appear(locator)
            element.clear()
            element.send_keys(value + Keys.LEFT_ALT)
            if label and self.log:
                print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def set_checkbox(self, locator, value, label=None):
        element = self.wait_for_element_appear(locator)
        if element.is_selected() != value:
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

    def set_select2(self, locator, value, label=None):
        if value:
            self.click(locator)
            s2_drop = self.driver.find_element(By.XPATH, "//div[@id='select2-drop']")
            s2_input = s2_drop.find_element(By.XPATH, ".//input[@type='text']")
            s2_input.clear()
            s2_input.send_keys(value)
            option = (By.XPATH, "//*[@role='option'][contains(normalize-space(), '%s')]" % value)
            li = self.wait_for_element_appear(option)
            li.click()
            self.wait_for_element_disappear((By.ID, "select2-drop"))
            if label and self.log:
                print("[%s] [%s] выбор из списка значения \"%s\"" % (strftime("%H:%M:%S", localtime()), label, value))

    def table_row_checkbox(self, order=1):
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='checkbox'])[%s]" % order)
        self.set_checkbox(locator, True)
        sleep(1)

    def table_row_radio(self, order=1):
        sleep(1)
        locator = (By.XPATH, "(//td/input[@type='radio'])[%s]" % order)
        self.set_radio(locator)
        sleep(1)

    def click(self, locator, label=None):
        self.wait_for_loading()
        element = self.wait_for_element_appear(locator)
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
        element = self.wait_for_element_appear(locator)
        self.move_to_element(element)
        element.click()
        if text and self.log:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), text))

    def move_to_element(self, element):
        self.wait_for_loading()
        webdriver.ActionChains(self.driver).move_to_element(element).perform()

    def scroll_to_top(self):
        self.wait_for_loading()
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        self.wait_for_loading()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def go_to(self, url):
        while self.driver.current_url != url:
            self.driver.get(url)
            sleep(.1)
        print("Переход по ссылке: %s" % url)

    def wait_for_text_appear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    def wait_for_text_disappear(self, text):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(., '%s')]" % text)))

    def wait_for_element_appear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_disappear(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_loading(self):
        WebDriverWait(self.driver, self.timeout).until_not(
            EC.visibility_of_element_located((By.XPATH, "//img[@alt='Загрузка']")))
