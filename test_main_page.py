#  pytest -v --tb=line test_main_page.py
from .pages.main_page import MainPage

def test_guest_should_see_in_header_telephon_number_tea_shop(browser):
    url = "https://besttea.ru/"
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_telephone_number_tea_shop()

def test_guest_should_see_in_header_telephon_number_wholesale_department(browser):
    url = "https://besttea.ru/"
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_telephone_number_wholesale_department()

def test_guest_should_see_in_header_button_price_list(browser):
    url = "https://besttea.ru/"
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_button_price_list()