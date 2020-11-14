from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = "//form[@id='login_form']"
    LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    EMAIL_LOGIN = (By.XPATH, "//input[@name='login-username']")
    PASSWORD_LOGIN = (By.XPATH, "//input[@id='id_login-password']")
    LOG_IN_BTN = (By.XPATH, "//button[@name='login_submit']")
    EMAIL_REG = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD_REG = (By.XPATH, "//button[@name='registration_submit']")
    REGISTER_BTN = (By.XPATH, "//button[@name='registration_submit']")
