# pytest -v --tb=line test_cart_page.py

from .pages.cart_page import CartPage, url_cart_page
import pytest
from .pages.base_page import BasePage

# Обозначение EXP001... - номера тестов в тест-кейсах.

def test_EXP058_guest_should_see_added_item_in_cart_page(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.should_be_added_item_in_cart()
