import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET).click()
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Item is in the basket, but should not be"
        item = self.browser.find_element(*BasketPageLocators.BASKET_FILL)
        if item.text == "Your basket is empty. Continue shopping":
            assert True
        else:
            self.allure_report()
            assert False

    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET).click()
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Item is in the basket, but should not be"
        item = self.browser.find_element(*BasketPageLocators.BASKET_FILL)
        if item.text == "Your basket is empty. Continue shopping":
            assert True
        else:
            self.allure_report()
            assert False
