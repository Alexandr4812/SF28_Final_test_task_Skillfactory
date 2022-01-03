# pytest -v --tb=line test_cart_page.py

from .pages.cart_page import CartPage, url_cart_page

# Обозначение EXP001... - номера тестов в тест-кейсах.

def test_EXP058_guest_should_see_added_item_in_cart_page(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.should_be_added_item_in_cart()

def test_EXP059_the_empty_cart_button_deletes_the_contents_of_the_cart(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.should_be_empty_shopping_cart()

def test_EXP060_the_checkout_button_opens_checkout_page(browser):
    cart_page = CartPage(browser, url_cart_page)
    cart_page.open()
    cart_page.the_checkout_button_opens_the_corresponding_page()