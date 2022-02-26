from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_CURRENT_PRODUCT = (By.XPATH, "//*[@value = 'Add to basket']")
    NAME_PRODUCT_IN_BASKET = (By.XPATH, "(//*[@class='alertinner ']/strong)[1]")
    NAME_PRODUCT = (By.XPATH, "//*[@class='col-sm-6 product_main']/h1")
    BASKET_TOTAL = (By.XPATH, "//*[@class='alertinner ']/p/strong")
    PRODUCT_PRICE = (By.XPATH, "(//*[@class='price_color'])[1]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success") #(By.CSS_SELECTOR, "#messages div:first-child")

class BasketPageLocators():
    BASKET = (By.XPATH, "//*[@class='basket-mini pull-right hidden-xs']/span/a")
    PRODUCT_IN_BASKET = (By.ID, "basket_formset")
    EMPTY_BASKET_MASSAGE = (By.XPATH, "//*[@id='content_inner']/p")