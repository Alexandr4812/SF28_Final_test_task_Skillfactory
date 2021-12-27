#  pytest -v --tb=line test_main_page.py
from .pages.main_page import MainPage, url_main_page
import pytest

# Обозначение EXP001... - номера тестов в тест-кейсах.

def test_EXP001_guest_should_see_in_header_telephon_number_tea_shop(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_telephone_number_tea_shop()

def test_EXP002_guest_should_see_in_header_telephon_number_wholesale_department(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_telephone_number_wholesale_department()

def test_EXP003_guest_should_see_in_header_button_price_list(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_button_price_list()

def test_EXP004_the_price_list_button_opens_the_price_list_form(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_price_list_button_opens_the_form_for_receiving_price_list()

@pytest.mark.information_list
class TestInformationListFromMainPage():
    def test_EXP005_guest_should_see_in_header_information_list(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_information_list()
    def test_EXP006_guest_should_see_in_information_list_three_elements(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_information_list_has_three_elements()
    def test_EXP007_the_link_dostavka_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_dostavka_opens_the_corresponding_page()
    def test_EXP008_the_link_oplata_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_oplata_opens_the_corresponding_page()
    def test_EXP009_the_link_obmen_vozvrat_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_obmen_vozvrat_opens_the_corresponding_page()

        # pytest - v - -tb = line - m information_list test_main_page.py

def test_EXP010_guest_should_see_geolocation_map_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_geolocation_map()

def test_EXP011_link_geolocation_map_opens_window_with_geolocation_map(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_link_geolocation_map_opens_window_with_geolocation_map()

def test_EXP012_guest_should_see_in_header_novinki_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_novinki_link()

def test_EXP013_novinki_link_open_page_noviepostupleniya(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_novinki_link_open_page_noviepostupleniya()

def test_EXP014_guest_should_see_in_header_sale_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_by_sale_link()

def test_EXP015_sale_link_open_page_noviepostupleniya(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_sale_link_opens_the_corresponding_page()