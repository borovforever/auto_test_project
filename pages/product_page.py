from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS), \
            "Success message is presented, but should not be"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS), \
            "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS), \
            "Success message is presented, but should not be"

    def guest_should_see_login_link_on_product_page(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK), \
            "There is no login button on the product page"

    def guest_can_go_to_login_page_from_product_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        login_page_link = self.browser.current_url
        print(login_page_link)
        if "/login" in login_page_link:
            assert True
        else:
            assert False, \
                f"{login_page_link} No 'Login' in the page link"
        time.sleep(10)

    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    print(return_product_price)

    def return_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    print(return_product_name)

    def guest_can_add_product_to_basket(self):
        product_name = self.return_product_name()
        price = self.return_product_price()
        print(product_name)
        print(price)
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        WebDriverWait(self.browser, 5).until(ec.alert_is_present())
        self.solve_quiz_and_get_code()
        price2 = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert price2[5].text == price, \
            f"Price is not {price}"
        product_name2 = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert product_name2[3].text == product_name, \
            f"Product name is not {product_name}"
