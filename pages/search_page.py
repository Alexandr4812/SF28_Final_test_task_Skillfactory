from .base_page import BasePage
from .locators import BasePageLocators, MainPageLocators, SearchPageLocators

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

