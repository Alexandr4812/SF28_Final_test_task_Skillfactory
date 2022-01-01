from .base_page import BasePage
from .locators import BasePageLocators, MainPageLocators, SearchPageLocators

url_search_page = 'https://besttea.ru/search/'

class SearchPage(BasePage):
    # EXP047 метод проверки, что присутствует строка поиска
    def shold_be_search_input(self):
        assert self.is_element_present(*BasePageLocators.SearchLokators.SERCH_INPUT), "Wish serch input is not presented"

    # EXP048 EXP049 EXP050 метод проверки, что при различных данных ввода названий товаров в поисковую строку на
    # странице выводится найденный товар
    def should_be_product_list(self, input_text):
        search_input = self.find_element(BasePageLocators.SearchLokators.SERCH_INPUT)
        search_input.clear()
        search_input.send_keys(input_text)
        button_search = self.find_element(BasePageLocators.SearchLokators.BUTTON_SERCH)
        button_search.click()
        assert self.is_element_present(*SearchPageLocators.PRODUCT_LIST), "Product not found"
