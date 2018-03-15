from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
from time import localtime, strftime
from wait import Wait


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

_USER_LOCATOR_MAP = {
    'ng_model': "//*[@ng-model='{0}']",
    'select2_label': "//label[contains(., '{0}')]/following::*//span[@id]"
}

_EXPECTED_COND_MAP = {
    'presence': expected_conditions.presence_of_element_located,
    'visible': expected_conditions.visibility_of_element_located,
    'invisible': expected_conditions.invisibility_of_element_located,
    'clickable': expected_conditions.element_to_be_clickable
}

_LOG_PHRASES = {
    'default_click': 'нажатие на элемент',
    'default_set': 'присваивание элементу значения',
    'button': 'нажатие на кнопку',
    'link': 'нажатие на гиперссылку',
    'input_click': 'нажатие на текстовое поле',
    'input_set': 'заполнение текстового поля значением',
    'date_click': 'нажатие на поле даты',
    'date_set': 'заполнение поля даты значением',
    'checkbox_click': 'нажатие на флаг',
    'checkbox_set': 'установка флага в положение',
    'radio_click': 'нажатие на переключатель',
    'radio_set': 'установка переключателя в положение',
    'select_click': 'нажатие на выпадающий список',
    'select_set': 'выбор значения из выпадающего списка',
    'select2_click': 'нажатие на справочник',
    'select2_set': 'выбор значения из справочника'
}

_LOADING_LOCATORS = [(_LOCATOR_MAP['xpath'], "//img[@alt='Загрузка']")]

_TIMEOUT = 60


class Element(object):

    _label = None
    _click_log = _LOG_PHRASES['default_click']
    _set_log = _LOG_PHRASES['default_set']
    _locator = None
    _wait = None
    _timeout = _TIMEOUT
    _driver = None
    _element = None
    _expected_condition = 'visible'
    _ec = _EXPECTED_COND_MAP

    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError('Specify a locator.')

        for key, value in list(kwargs.items()):
            if key in _LOCATOR_MAP:
                self._locator = (_LOCATOR_MAP[key], value)
            elif key in _USER_LOCATOR_MAP:
                self._locator = (By.XPATH, _USER_LOCATOR_MAP[key].format(value))
            elif key == 'expected_condition':
                self._expected_condition = value
                if value not in self._ec:
                    raise ValueError('Incorrect expected condition %s' % value)
            elif key == 'label':
                self._label = value
            elif key == 'timeout':
                self._timeout = value
                if value < 0:
                    raise ValueError('%s is a wrong value for timeout.' % value)
            else:
                raise ValueError('Incorrect input: %s' % key)

        if self._locator is None:
            raise ValueError('Specify a locator.')

    def find(self, driver):

        self._driver = driver
        self._wait = Wait(self._driver, self._timeout)

        # waiting for loading elements
        for locator in _LOADING_LOCATORS:
            self._wait.element_disappear(locator)
        self._element = self._wait.element_appear(self._locator, msg="Didn't find element by %s: <%s>" % self._locator)
        return self._element

    def __eq__(self, other):
        return self.text() == str(other)

    def __ne__(self, other):
        return self.text() != str(other)

    def __get__(self, instance, owner):
        self._element = self.find(instance.driver)
        return self

    def __set__(self, instance, value):
        if value:
            element = self.find(instance.driver)
            value = str(value)
            if len(value) > 0:
                element.clear()
                element.send_keys(value)
                self.set_log(value)

    def click(self):
        self._element.click()
        self.click_log()

    def text(self):
        return self._element.text

    def set_log(self, value):
        time = strftime("%H:%M:%S", localtime())
        if self._label:
            print("[%s] [%s] %s \"%s\"" % (time, self._label, self._set_log, value))

    def click_log(self):
        time = strftime("%H:%M:%S", localtime())
        if self._label:
            print("[%s] [%s] %s" % (time, self._label, self._click_log))


class HTMLInput(Element):

    _click_log = _LOG_PHRASES['input_click']
    _set_log = _LOG_PHRASES['input_set']

    def clear(self):
        self._element.clear()

    def send_keys(self, value):
        self._element.send_keys(value)

    def text(self):
        return self._element.get_attribute('value')


class HTMLDate(HTMLInput):

    _click_log = _LOG_PHRASES['date_click']
    _set_log = _LOG_PHRASES['date_set']
    _format = "%d.%m.%Y"

    def __set__(self, instance, value):
        if value:
            element = self.find(instance.driver)
            value = str(value)
            element.clear()
            element.send_keys(value + Keys.TAB)
            self.set_log(value)

    def set_today(self):
        date = datetime.date.today().strftime(self._format)
        self._element.clear()
        self._element.send_keys(date + Keys.TAB)
        self.set_log(date)


class HTMLSelect(Element):

    _click_log = _LOG_PHRASES['select_click']
    _set_log = _LOG_PHRASES['select_set']

    def __set__(self, instance, value):
        if value:
            element = self.find(instance.driver)
            value = str(value)
            Select(element).select_by_visible_text(value)
            self.set_log(value)


class HTMLSelect2(Element):

    _click_log = _LOG_PHRASES['select2_click']
    _set_log = _LOG_PHRASES['select2_set']

    def __set__(self, instance, value):
        if value:
            value = str(value)
            self.find(instance.driver).click()
            _input = self._element.find_element(By.XPATH, "//*[@id='select2-drop']//input")
            _input.clear()
            _input.send_keys(value)
            locator = (By.XPATH, "//*[@role='option' and contains(normalize-space(), '%s')]" % value)
            _option = self._wait.element_appear(locator)
            _option.click()
            self.set_log(value)


class HTMLButton(Element):

    _click_log = _LOG_PHRASES['button']
    _expected_condition = 'clickable'

    def __set__(self, instance, value):
        raise TypeError('%s doesn\'t support this method.' % self.__class__.__name__)


class HTMLLink(HTMLButton):

    _click_log = _LOG_PHRASES['link']


class HTMLCheckbox(Element):

    _click_log = _LOG_PHRASES['checkbox_click']
    _set_log = _LOG_PHRASES['checkbox_set']
    _expected_condition = 'clickable'

    def __eq__(self, other):
        if isinstance(other, bool):
            return self._element.is_selected() == other
        else:
            raise ValueError('Incorrect type of value. Boolean type expected.')

    def __ne__(self, other):
        if isinstance(other, bool):
            return self._element.is_selected() == other
        else:
            raise ValueError('Incorrect type of value. Boolean type expected.')

    def __set__(self, instance, value):
        if isinstance(value, bool):
            element = self.find(instance.driver)
            if element.is_selected() != value:
                element.click()
                self.set_log(value)
        else:
            raise ValueError('Incorrect type of value. Boolean type expected.')

    def is_selected(self):
        return self._element.is_selected()


class HTMLRadioButton(Element):

    _click_log = _LOG_PHRASES['radio_click']
    _set_log = _LOG_PHRASES['radio_set']
