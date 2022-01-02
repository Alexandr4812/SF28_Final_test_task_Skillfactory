# pytest -v --tb=line test_search_page.py

from .pages.search_page import SearchPage, url_search_page
import pytest
from .pages.base_page import BasePage

# Обозначение EXP001... - номера тестов в тест-кейсах.

def test_EXP047_guest_shold_see_search_input(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.shold_be_search_input()

@pytest.mark.parametrize('input_text', ["кружка",
                                        "КРУЖКА",
                                        "rhe;rf"])
def test_EXP048_EXP049_EXP050_search_by_product_name_in_uppercase_and_in_english_layout(browser, input_text):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_product_list(input_text)

def test_EXP051_guest_shold_see_quantity_of_items_found(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_quantity_of_items_found()

def test_EXP052_the_number_of_products_on_the_page_is_equal_to_the_number_of_products_found(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.the_number_of_products_on_the_page_is_equal_to_the_number_of_products_found()


@pytest.mark.parametrize('input_text', ["@#₽&+():;!?∆¶×÷π√\}{=°^¢$€£%©®™℅",
                                        "1234567890",
                                        BasePage.symbols_256('self', 's')])
def test_EXP053_EXP054_EXP055_with_negative_scenario_should_be_product_not_found(browser, input_text):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_product_not_found(input_text)

def test_EXP056_should_be_the_number_of_the_added_product_appears_on_the_Cart_icon(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_the_number_of_the_added_product_appears_on_the_Cart_icon()

def test_EXP57_should_be_the_added_product_is_in_the_cart_tab(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_the_added_product_is_in_the_cart_tab()