from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
import pytest
import time

# создаем конструктор, который принимает browser — экземпляр webdriver.
# Указываем url, который будет использоваться для открытия страницы.
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 10:
        self.browser.implicitly_wait(timeout)

    # создаем метод find_element (ищет один элемент и возвращает его)
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # создаем метод find_elements (ищет множество элементов и возвращает в виде списка)
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # метод open должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # метод is_element_presentв перехватывает исключение.
    # будет использоваться для проверки присутствия элемента на странице
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд)
    # и собственно что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # метод проверки что в header присутствует телефон магазина чая (общий для всех страниц метод)
    def should_be_telephone_number_tea_shop(self):
        number = self.find_element(BasePageLocators.TEA_SHOP_PHONE)
        result = number.text
        assert "8 (495) 143-35-16 МАГАЗИН ЧАЯ" == result

    # метод проверки что в header присутствует телефон оптового отдела (общий для всех страниц метод)
    def should_be_telephone_number_wholesale_department(self):
        number = self.find_element(BasePageLocators.WHOLESALES_DEPERTAMENT_PHONE)
        result = number.text
        assert "8 (495) 143-35-15 ОПТОВЫЙ ОТДЕЛ" == result

    # метод проверки что в header присутствует кнопка прайс-лист (общий для всех страниц метод)
    def should_be_button_price_list(self):
        button = self.find_element(BasePageLocators.BUTTON_PRISE_LIST)
        result = button.text
        assert "ПРАЙС-ЛИСТ" == result

    # метод проверки что при нажатии кнопки прайс-лист открывается форма прайс-лист
    def the_price_list_button_opens_the_form_for_receiving_price_list(self):
        button = self.find_element(BasePageLocators.BUTTON_PRISE_LIST)
        button.click()
        assert self.is_element_present(*BasePageLocators.FORM_PRISE_LIST), "Form prise_list is not presented"

