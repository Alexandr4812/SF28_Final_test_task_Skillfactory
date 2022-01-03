from .base_page import BasePage
from .locators import BasePageLocators, SearchPageLocators
import time

url_search_page = 'https://besttea.ru/search/'

class SearchPage(BasePage):
    # EXP047 метод проверки, что присутствует строка поиска
    def shold_be_search_input(self):
        assert self.is_element_present(*BasePageLocators.SearchLokators.SERCH_INPUT), "Wish serch input is not presented"

    # EXP048 EXP049 EXP050 метод проверки, что при вводе товара в поисковую строку на
    # странице выводится найденный товар
    def should_be_product_list(self, input_text):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys(input_text)
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        assert self.is_element_present(*SearchPageLocators.PRODUCT_LIST), "Product not found"

    # EXP051 метод проверки, что на странице видна информация о количестве найденного товара
    def should_be_quantity_of_items_found(self):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys("кружка")
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        naydeno_tovarov = self.find_element(SearchPageLocators.NAYDENO_TOVAROV)
        naydeno_tovarov_text = naydeno_tovarov.text
        result = naydeno_tovarov_text.split()
        assert result[0] == "Найдено"

    # EXP052 метод проверки, количество товара на странице совпадает с количеством в тексте: "Найдено товаров ..."
    def the_number_of_products_on_the_page_is_equal_to_the_number_of_products_found(self):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys("кружка")
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        display_button = self.find_element(SearchPageLocators.COLUMN_DISPLAY_BUTTON)
        display_button.click()
        product_list = self.find_elements(SearchPageLocators.QANTITY_PRODUCTS)
        quantity_in_display = len(product_list)
        quantity_in_display = str(quantity_in_display)
        naydeno_tovarov = self.find_element(SearchPageLocators.NAYDENO_TOVAROV)
        naydeno_tovarov_text = naydeno_tovarov.text
        quantity_in_naydeno_tovarov = naydeno_tovarov_text.split()
        quantity_in_naydeno_tovarov = quantity_in_naydeno_tovarov[2]
        assert quantity_in_display == quantity_in_naydeno_tovarov

    # EXP053 EXP054 EXP055 метод проверки, что при вводе товара (с негативным сценарием) в поисковую строку на
    # странице появляется сообщение "По вашему запросу ничего не найдено"
    def should_be_product_not_found(self, input_text):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys(input_text)
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        searching_result = self.find_element(SearchPageLocators.SEARCHING_RESULT)
        result = searching_result.text
        assert result == 'По вашему запросу ничего не найдено'

    # EXP056 метод проверки, что на иконке "Корзина" появляется число количество добавленного товара
    def should_be_the_number_of_the_added_product_appears_on_the_Cart_icon(self):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys("стакан")
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        display_button = self.find_element(SearchPageLocators.COLUMN_DISPLAY_BUTTON)
        display_button.click()
        buy_button = self.find_element(SearchPageLocators.BUY_BUTTON)
        buy_button.click()
        time.sleep(7)
        cart_status = self.find_element(BasePageLocators.KorzinaLokators.CART_STATUS)
        result = cart_status.text
        assert result == '1'

    # EXP057 метод проверки, что во вкладке корзины присутствует добавленный товар
    def should_be_the_added_product_is_in_the_cart_tab(self):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys("стакан")
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        display_button = self.find_element(SearchPageLocators.COLUMN_DISPLAY_BUTTON)
        display_button.click()
        buy_button = self.find_element(SearchPageLocators.BUY_BUTTON)
        buy_button.click()
        time.sleep(7)
        korzina_button = self.find_element(BasePageLocators.KorzinaLokators.KORZINA_BUTTON)
        korzina_button.click()
        korzina_list_product = self.find_elements(BasePageLocators.KorzinaLokators.KORZINA_LIST_PRODUCT)
        result = len(korzina_list_product)
        assert result == 1



