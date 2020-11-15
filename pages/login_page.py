from .base_page import BasePage
from .locators import LoginPageLocators
import pytest
import time
from .locators import ProductPageLocators


class LoginPage(BasePage):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser

    def register_new_user(self):
        email = str(time.time()) + "@mailforspam.com"
        self.browser.find_element(*LoginPageLocators.EMAIL_REG).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REG).send_keys("Monster12a")
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys("Monster12a")
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def return_product_price(self):
        product_price = self.browser.find_elements(*ProductPageLocators.PRODUCT_PRICE)
        return product_price[1].text

    def return_product_name(self):
        product_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_USER)
        return product_name[1].text

    def user_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS), \
            "Success message is presented, but should not be"

    def user_can_add_product_to_basket(self):
        product_name = self.return_product_name()
        price = self.return_product_price()
        print(product_name)
        print(price)
        add_to_basket = self.browser.find_elements(*ProductPageLocators.ADD_TO_BASKET_USER)
        add_to_basket[1].click()
        price2 = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        if price2[5].text == price:
            assert True
        else:
            self.allure_report()
            assert False, \
                f"Price is not {price}"
        product_name2 = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        if product_name2[3].text == product_name:
            assert True
        else:
            self.allure_report()
            assert False, \
                f"Product name is not {product_name}"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_page_link = self.browser.current_url
        print(login_page_link)
        if "/login" in login_page_link:
            assert True
        else:
            self.allure_report()
            assert False, \
                f"{login_page_link} No 'Login' in the page link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOG_IN_BTN), "Login btn is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REG), "Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REG), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Login btn is not presented"
