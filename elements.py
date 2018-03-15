from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
from time import localtime, strftime, sleep


_LOCATOR_MAP = {
    'xpath': By.XPATH,
    'class': By.CLASS_NAME,
    'name': By.NAME,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'id': By.ID,
    'css': By.CSS_SELECTOR,
    'tag_name': By.TAG_NAME
}

_EXPECTED_COND_MAP = {
    'presence': expected_conditions.presence_of_element_located,
    'visible': expected_conditions.visibility_of_element_located,
    'invisible': expected_conditions.invisibility_of_element_located,
    'clickable': expected_conditions.element_to_be_clickable
}

_LOG_PHRASES = {
    'button': '',
    'input': '',
    'date': '',
    'checkbox': '',
    'select': '',
    'select2': '',
    'radio': '',
    'link': ''
}

_LOADING_LOCATORS = [(_LOCATOR_MAP['xpath'], "//img[@alt='Загрузка']")]

_TIMEOUT = 60


class Element(object):

    _label = None
    _locator = None
    _timeout = _TIMEOUT
    _driver = None
    _element = None
    _expected_condition = 'visible'
    _ec = _EXPECTED_COND_MAP

    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError('Please specify a locator')

        for key, value in list(kwargs.items()):
            if key in _LOCATOR_MAP:
                self._locator = (_LOCATOR_MAP[key], value)
            elif key == 'expected_condition':
                self._expected_condition = value
                if value not in self._ec:
                    raise ValueError('Invalid expected condition %s' % value)
            elif key == 'label':
                self._label = value
            elif key == 'timeout':
                self._timeout = value
                if value < 0:
                    raise ValueError('Invalid timeout value %s' % value)
            else:
                raise ValueError('Invalid input: %s' % key)

        if self._locator is None:
            raise ValueError('Please specify a locator')

    def find(self, driver):

        self._driver = driver

        # waiting for loading elements
        for locator in _LOADING_LOCATORS:
            WebDriverWait(driver, self._timeout).until_not(
                self._ec['visible'](locator)
            )

        self._element = WebDriverWait(driver, self._timeout).until(
            self._ec[self._expected_condition](self._locator),
            "Didn't find element by %s: <%s>" % self._locator
        )

        return self._element

    def __eq__(self, other):
        return self.text() == str(other)

    def __ne__(self, other):
        return self.text() != str(other)

    def __get__(self, instance, owner):
        self._element = self.find(instance.driver)
        return self

    def __set__(self, instance, value):
        if value is not None:
            element = self.find(instance.driver)
            value = str(value)
            if len(value) > 0:
                element.clear()
                element.send_keys(value)
                if self._label:
                    print("[%s] [%s] заполнение значением \"%s\"" % (strftime("%H:%M:%S", localtime()),
                                                                     self._label,
                                                                     value))

    def click(self):
        self._element.click()
        if self._label:
            print("[%s] [%s] нажатие на элемент" % (strftime("%H:%M:%S", localtime()), self._label))

    def text(self):
        return self._element.text

    def log(self):
        if self._label:
            print()


class HTMLButton(Element):
    _expected_condition = 'clickable'


class HTMLSelect(Element):

    def __set__(self, instance, value):
        if value is not None:
            element = self.find(instance.driver)
            value = str(value)
            if len(value) > 0:
                Select(element).select_by_visible_text(value)


class HTMLInput(Element):

    def clear(self):
        self._element.clear()

    def send_keys(self, value):
        self._element.send_keys(value)

    def text(self):
        return self._element.get_attribute('value')


class HTMLLink(HTMLButton):
    pass


class HTMLCheckbox(Element):
    _expected_condition = 'clickable'

    def __eq__(self, other):
        if other:
            return self._element.is_selected() == other

    def __ne__(self, other):
        if other:
            return self._element.is_selected() == other

    def __set__(self, instance, value):
        if value:
            element = self.find(instance.driver)
            if element.is_selected() != value:
                element.click()

    def is_selected(self):
        return self._element.is_selected()


class HTMLDate(HTMLInput):

    _format = "%d.%m.%Y"

    def __set__(self, instance, value):
        if value is not None:
            element = self.find(instance.driver)
            value = str(value)
            if len(value) > 0:
                element.clear()
                element.send_keys(value + Keys.TAB)

    def set_today(self):
        self._element.clear()
        self._element.send_keys(datetime.date.today().strftime(self._format) + Keys.TAB)
