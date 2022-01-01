#  pytest -v --tb=line test_search_page.py
from .pages.search_page import SearchPage, url_search_page
import pytest

# Обозначение EXP001... - номера тестов в тест-кейсах.
def test_EXP047_guest_shold_be_search_input(browser):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.shold_be_search_input()

@pytest.mark.parametrize('input_text', ["кружка", "КРУЖКА", "rhe;rf"])
def test_EXP048_EXP049_EXP050_search_by_product_name_in_uppercase_and_in_English_layout(browser, input_text):
    search_page = SearchPage(browser, url_search_page)
    search_page.open()
    search_page.should_be_product_list(input_text)