from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    LOGIN_PAGE = (By.XPATH, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    EMAIL_LOGIN = (By.XPATH, "//input[@name='login-username']")
    PASSWORD_LOGIN = (By.XPATH, "//input[@id='id_login-password']")
    LOG_IN_BTN = (By.XPATH, "//button[@name='login_submit']")
    EMAIL_REG = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_REG = (By.XPATH, "//button[@name='registration_submit']")
    REGISTER_BTN = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[@value='Add to basket']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_NAME = (By.XPATH, "//h1")
    SUCCESS = (By.XPATH, "//strong[contains(text(),'Deferred benefit offer')]")
    MESSAGES = (By.XPATH, "//div//strong")


class BasketPageLocators():
    BASKET = (By.XPATH, "//a[@class='btn btn-default']")
    BASKET_FILL = (By.XPATH, "//div[@id='content_inner']")
