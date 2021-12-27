from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
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

    # метод is_element_present перехватывает исключение.
    # будет использоваться для проверки присутствия элемента на странице
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд)
    # и собственно что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

######################## ДАЛЕЕ ИДУТ ОБЩИЕ ДЛЯ ВСЕХ СТРАНИЦ МЕТОДЫ ПРОВЕРОК #############################

    # метод проверки что в header присутствует телефон магазина чая
    def should_be_telephone_number_tea_shop(self):
        number = self.find_element(BasePageLocators.TEA_SHOP_PHONE)
        result = number.text
        assert "8 (495) 143-35-16 МАГАЗИН ЧАЯ" == result

    # метод проверки что в header присутствует телефон оптового отдела
    def should_be_telephone_number_wholesale_department(self):
        number = self.find_element(BasePageLocators.WHOLESALES_DEPERTAMENT_PHONE)
        result = number.text
        assert "8 (495) 143-35-15 ОПТОВЫЙ ОТДЕЛ" == result

    # метод проверки что в header присутствует кнопка прайс-лист
    def should_be_button_price_list(self):
        button = self.find_element(BasePageLocators.BUTTON_PRISE_LIST)
        result = button.text
        assert "ПРАЙС-ЛИСТ" == result

    # метод проверки что при нажатии кнопки прайс-лист открывается форма прайс-лист
    def the_price_list_button_opens_the_form_for_receiving_price_list(self):
        button = self.find_element(BasePageLocators.BUTTON_PRISE_LIST)
        button.click()
        assert self.is_element_present(*BasePageLocators.FORM_PRISE_LIST), "Form prise_list is not presented"

    # метод проверки, что в header присутствует кнопка выпадающего списка "ИНФОРМАЦИЯ"
    def should_be_information_list(self):
        button = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        button.click()
        result = button.text
        assert "ИНФОРМАЦИЯ" == result

    # метод проверки, что в выпадающем списке "ИНФОРМАЦИЯ" есть три элемента
    def should_be_information_list_has_three_elements(self):
        button = self.find_elements(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        result = len(button) - 1
        assert result == 3

    # метод проверки, что ссылка "Доставка" в выпадающем списке "ИНФОРМАЦИЯ"
    # ведет на соответствующую страницу
    def the_link_dostavka_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/dostavka/"
        link = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        link.click()
        dostavka_link = self.find_element(BasePageLocators.InformationListLocators.DOSTAVKA_LINK)
        dostavka_link.click()
        assert url == self.browser.current_url, "url do not match"

    # метод проверки, что ссылка "Оплата" в выпадающем списке "ИНФОРМАЦИЯ"
    # ведет на соответствующую страницу
    def the_link_oplata_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/oplata/"
        link = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        link.click()
        oplata_link =self.find_element(BasePageLocators.InformationListLocators.OPLATA_LINK)
        oplata_link.click()
        assert url == self.browser.current_url, "url do not match"

    # метод проверки, что ссылка "Обмен и возврат" в выпадающем списке "ИНФОРМАЦИЯ"
    # ведет на соответствующую страницу
    def the_link_obmen_vozvrat_opens_the_corresponding_page(self):
        url = "https://besttea.ru/info/usloviya-vozvrata/"
        link = self.find_element(BasePageLocators.InformationListLocators.INFORMATION_LIST)
        link.click()
        obmen_vozvrat_link = self.find_element(BasePageLocators.InformationListLocators.OBMEN_VOZVRAT_LINK)
        obmen_vozvrat_link.click()
        assert url == self.browser.current_url, "url do not match"

    # метод проверки, что в header присутствует ссылка на геолокацию
    def should_be_geolocation_map(self):
        map = self.find_element(BasePageLocators.GEOLOCATION_MAP)
        result = map.text
        assert result != ''

    # метод проверки, что ссылка на геолокацию открывает окно геолокации
    def the_link_geolocation_map_opens_window_with_geolocation_map(self):
        link = self.find_element(BasePageLocators.GEOLOCATION_MAP)
        link.click()
        assert self.is_element_present(By.CSS_SELECTOR, "#ui-id-1"), "Window with geolocation map is not presented"

    # метод проверки, что в header присутствует ссылка "новинки"
    def should_be_novinki_link(self):
        link = self.find_element(BasePageLocators.NOVINKI_LINK)
        result = link.text
        assert "Новинки" == result

    # метод проверки, что ссылка "новинки" открывает страницу с новыми поступлениями
    def the_novinki_link_open_page_noviepostupleniya(self):
        url = "https://besttea.ru/noviepostupleniya/"
        link = self.find_element(BasePageLocators.NOVINKI_LINK)
        link.click()
        assert url == self.browser.current_url, "url do not match"

    # метод проверки, что в header присутствует ссылка "Скидки"
    def should_by_sale_link(self):
        link = self.find_element(BasePageLocators.SALE_LINK)
        result = link.text
        assert "Скидки" == result

    # метод проверки, что ссылка "Скидки" открывает соответствующую страницу
    def the_sale_link_opens_the_corresponding_page(self):
        url = "https://besttea.ru/sale/"
        link = self.find_element(BasePageLocators.SALE_LINK)
        link.click()
        assert url == self.browser.current_url, "url do not match"

    # метод проверки, что в header присутствует кнопка выпадающего списка "Оптовикам"
    def should_by_optovikam_list(self):
        optovikam_list = self.find_element(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        optovikam_list.click()
        result = optovikam_list.text
        assert "Оптовикам" == result

    # метод проверки, что в выпадающем списке "Оптовикам" есть семь элементов
    def should_be_optovikam_list_has_seven_elements(self):
        button = self.find_elements(BasePageLocators.OptovikamListLocators.OPTOVIKAM_LIST)
        result = len(button) - 1
        assert result == 7





