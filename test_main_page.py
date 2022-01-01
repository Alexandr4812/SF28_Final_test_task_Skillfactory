#  pytest -v --tb=line test_main_page.py
from .pages.main_page import MainPage, url_main_page
import pytest

# Обозначение EXP001... - номера тестов в тест-кейсах.

def test_EXP001_guest_should_see_in_header_button_price_list(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_button_price_list()

def test_EXP002_the_price_list_button_opens_the_price_list_form(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_price_list_button_opens_the_form_for_receiving_price_list()

@pytest.mark.information_list
class TestInformationListFromMainPage():
    def test_EXP003_guest_should_see_in_header_information_list(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_information_list()
    def test_EXP004_guest_should_see_in_information_list_three_elements(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_information_list_has_three_elements()
    def test_EXP005_the_link_dostavka_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_dostavka_opens_the_corresponding_page()
    def test_EXP006_the_link_oplata_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_oplata_opens_the_corresponding_page()
    def test_EXP007_the_link_obmen_vozvrat_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_obmen_vozvrat_opens_the_corresponding_page()

        # pytest -v --tb=line -m information_list test_main_page.py

def test_EXP008_guest_should_see_geolocation_map_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_geolocation_map()

def test_EXP009_link_geolocation_map_opens_window_with_geolocation_map(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_link_geolocation_map_opens_window_with_geolocation_map()

def test_EXP010_guest_should_see_in_header_novinki_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_novinki_link()

def test_EXP011_novinki_link_open_page_noviepostupleniya(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_novinki_link_open_page_noviepostupleniya()

def test_EXP012_guest_should_see_in_header_sale_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_by_sale_link()

def test_EXP013_sale_link_open_page_noviepostupleniya(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_sale_link_opens_the_corresponding_page()

@pytest.mark.optovikam_list
class TestOptovikamListFromMainPage():
    def test_EXP014_guest_should_see_in_header_optovikam_list(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_optovikam_list()
    def test_EXP015_guest_should_see_in_optovikam_list_seven_elements(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_optovikam_list_has_seven_elements()
    def test_EXP016_the_link_chai_optom_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_chai_optom_opens_the_corresponding_page()
    def test_EXP017_the_link_kofe_optom_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_kofe_optom_opens_the_corresponding_page()
    def test_EXP018_the_link_posuda_optom_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_posuda_optom_opens_the_corresponding_page()
    def test_EXP019_the_link_proizvodstvo_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_proizvodstvo_opens_the_corresponding_page()
    def test_EXP020_the_link_chai_i_kofe_pod_stm_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_chai_i_kofe_pod_stm_opens_the_corresponding_page()
    def test_EXP021_the_link_fasovka_sipuchih_produktov_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_fasovka_sipuchih_produktov_opens_the_corresponding_page()
    def test_EXP022_the_link_sertifikaty_i_deklaracii_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_sertifikaty_i_deklaracii_opens_the_corresponding_page()

        # pytest -v --tb=line -m optovikam_list test_main_page.py

def test_EXP023_guest_should_see_in_header_kontakty_link(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_by_Kontakty_link()

def test_EXP024_the_link_kontakty_opens_the_corresponding_page(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.the_link_kontakty_opens_the_corresponding_page()

@pytest.mark.wish_list
class TestWishListMainPage():
    def test_EXP025_guest_should_see_wish_list_link(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_wish_list_link()
    def test_EXP026_the_link_wish_list_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_wish_list_opens_the_corresponding_page()
    def test_EXP027_guest_not_should_see_in_wish_list_link_number(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.not_should_by_number_in_wish_list_if_not_adding_product()
    def test_EXP028_guest_should_see_in_wish_list_link_number_one(self,browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_number_one_in_wish_list_when_adding_product()

        # pytest -v --tb=line -m wish_list test_main_page.py

@pytest.mark.katalog_tovarov_list
class TestKatalogTovarovListMainPage():
    def test_EXP029_guest_should_see_katalog_tovarov_list_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_by_katalog_tovarov_list()
    def test_EXP030_guest_should_see_in_katalog_tovarov_list_six_links(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_katalog_tovarov_list_six_elements()
    def test_EXP031_the_link_chai_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_chai_opens_the_corresponding_page()
    def test_EXP032_the_link_kofe_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_kofe_opens_the_corresponding_page()
    def test_EXP033_the_link_mate_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_mate_opens_the_corresponding_page()
    def test_EXP034_the_link_sladosti_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_sladosti_opens_the_corresponding_page()
    def test_EXP035_the_link_posuda_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_posuda_opens_the_corresponding_page()
    def test_EXP036_the_link_upakovka_opens_the_corresponding_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_link_upakovka_opens_the_corresponding_page()

        # pytest -v --tb=line -m katalog_tovarov_list test_main_page.py

@pytest.mark.search_input
class TestSerchInputMainPage():
    def test_EXP037_guest_should_see_search_input(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_search_input()
    def test_EXP038_the_search_icon_opens_the_search_page_when_you_press(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.the_search_icon_opens_the_serch_page()

        # pytest -v --tb=line -m search_input test_main_page.py

@pytest.mark.account_list
class TestAccountList():
    def test_EXP039_guest_should_see_account_list_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_account_list()
    def test_EXP040_should_be_in_account_list_three_links(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_account_list_three_links()
    def test_EXP041_guest_should_see_in_account_list_login_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_account_list_login_button()
    def test_EXP042_guest_should_see_in_account_list_registration_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_account_list_registration_button()
    def test_EXP043_button_login_in_account_list_opens_login_dialog_box(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.button_login_in_account_list_opens_login_dialog_box()
    def test_EXP044_button_registration_in_account_list_opens_registration_page(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.button_registration_in_account_list_opens_registration_page()

        # pytest -v --tb=line -m account_list test_main_page.py

@pytest.mark.korzina_list
class TestKorzinaList():
    def test_EXP045_guest_should_see_korzina_list_button(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_korzina_list()
    def test_EXP046_guest_should_see_in_korzina_list_text_korzina_pusta(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_in_korzina_list_text_korzina_pusta()

        # pytest -v --tb=line -m korzina_list test_main_page.py
