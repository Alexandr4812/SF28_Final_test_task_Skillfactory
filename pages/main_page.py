from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from .locators import BasePageLocators, MainPageLocators

url_main_page = "https://besttea.ru/"

class MainPage(BasePage):

    # EXP028 метод проверки, что при добавление одного товара в "список отложенных товаров"
    # на иконке "список отложенных товаров" появляется цифра 1
    def should_by_number_one_in_wish_list_when_adding_product(self):
        action = ActionChains(self.browser)
        product_5 = self.find_element(MainPageLocators.Bestsellers.PRODUCT_5)
        action.move_to_element(product_5).perform()
        add_wish_list = self.find_element(MainPageLocators.Bestsellers.ADD_WISH_LIST_PRODUCT_5)
        add_wish_list.click()
        wish_list_link_count = self.find_element(BasePageLocators.WishList.WISH_LIST_LINK_COUNT)
        result = wish_list_link_count.text
        assert result == "1"
