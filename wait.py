from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


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

    def lamb(self, exe):
        return WebDriverWait(self.driver, self.timeout).until(exe)

    def loading(self):
        WebDriverWait(self.driver, self.timeout).until_not(
            ec.visibility_of_element_located((By.XPATH, "//img[@alt='Загрузка']")))