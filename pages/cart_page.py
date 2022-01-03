from .base_page import BasePage
from .locators import BasePageLocators, SearchPageLocators, CartPageLocators
import time

url_cart_page = 'https://besttea.ru/cart/'

class CartPage(BasePage):
    # EXP058 метод проверки, что на странице корзины содержится добавленный товар
    def should_be_added_item_in_cart(self):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys('стакан')
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        display_button = self.find_element(SearchPageLocators.COLUMN_DISPLAY_BUTTON)
        display_button.click()
        buy_button = self.find_element(SearchPageLocators.BUY_BUTTON)
        buy_button.click()
        time.sleep(7)
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_button.click()
        cart_button = self.find_element(BasePageLocators.KorzinaLokators.CART_BUTTON)
        cart_button.click()
        assert self.is_element_present(*CartPageLocators.CART_ITEMS), 'there is no item in the cart'

    # EXP059 метод проверки, что кнопка "очистить корзину" удаляет содержимое корзины
    def should_be_empty_shopping_cart(self):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys('стакан')
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        display_button = self.find_element(SearchPageLocators.COLUMN_DISPLAY_BUTTON)
        display_button.click()
        buy_button = self.find_element(SearchPageLocators.BUY_BUTTON)
        buy_button.click()
        time.sleep(7)
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_button.click()
        cart_button = self.find_element(BasePageLocators.KorzinaLokators.CART_BUTTON)
        cart_button.click()
        clear_button = self.find_element(CartPageLocators.CLEAR_CART_BUTTON)
        clear_button.click()
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), 'cart is not empty'

    # EXP060 метод проверки, что кнопка "оформить заказ" ведет на страницу оформления заказа
    def the_checkout_button_opens_the_corresponding_page(self):
        url = 'https://besttea.ru/checkout/'
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys('стакан')
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        display_button = self.find_element(SearchPageLocators.COLUMN_DISPLAY_BUTTON)
        display_button.click()
        buy_button = self.find_element(SearchPageLocators.BUY_BUTTON)
        buy_button.click()
        time.sleep(7)
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_button.click()
        cart_button = self.find_element(BasePageLocators.KorzinaLokators.CART_BUTTON)
        cart_button.click()
        checkout_button = self.find_element(CartPageLocators.CHECKOUT_BUTTON)
        checkout_button.click()
        assert self.is_not_element_present(*BasePageLocators.TY_EXCEPTION), "404 Error. Page not found"
        assert url == self.browser.current_url, "url do not match"

