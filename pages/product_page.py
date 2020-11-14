from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


class ProductPage(BasePage):

    def return_product_price(self):
        product_price = self.browser.find_element(By.XPATH, "//p[@class='price_color']")
        return product_price.text


    print(return_product_price)

    def return_product_name(self):
        product_name = self.browser.find_element(By.XPATH, "//h1")
        return product_name.text

    print(return_product_name)

    def guest_can_add_product_to_basket(self):
        product_name = self.return_product_name()
        price = self.return_product_price()
        print(product_name)
        print(price)
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@value='Add to basket']"))).click()
        WebDriverWait(self.browser, 5).until(ec.alert_is_present())
        self.solve_quiz_and_get_code()
        price2 = self.browser.find_elements(By.XPATH, "//div//strong")
        assert price2[5].text == price, \
             f"Price is not {price}"
        print(price2)
        product_name2 = self.browser.find_elements(By.XPATH, "//div//strong")
        assert product_name2[3].text == product_name, \
             f"Product name is not {product_name}"



