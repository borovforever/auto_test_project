from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
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
