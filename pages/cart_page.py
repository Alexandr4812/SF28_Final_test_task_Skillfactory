from .base_page import BasePage
from .locators import BasePageLocators, MainPageLocators, SearchPageLocators, CartPageLocators
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
        time.sleep(5)
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_button.click()
        cart_button = self.find_element(BasePageLocators.KorzinaLokators.CART_BUTTON)
        cart_button.click()
        assert self.is_element_present(*CartPageLocators.CART_ITEMS), 'there is no item in the cart'
