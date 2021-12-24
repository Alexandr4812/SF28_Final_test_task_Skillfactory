#  pytest -v --tb=line test_main_page.py
from .pages.main_page import MainPage, url_main_page

def test_guest_should_see_in_header_telephon_number_tea_shop(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_telephone_number_tea_shop()

def test_guest_should_see_in_header_telephon_number_wholesale_department(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_telephone_number_wholesale_department()

def test_guest_should_see_in_header_button_price_list(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_button_price_list()

def test_the_price_list_button_opens_the_price_list_form(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_price_list_button_opens_the_form_for_receiving_price_list()