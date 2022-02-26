import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import ProductPageLocators



class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_CURRENT_PRODUCT)
        add_to_product.click()
        self.solve_quiz_and_get_code()
        #self.is_correct_name_product()
        #self.is_correct_basket_total()

        

    def is_correct_name_product(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET)
        product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert product_in_basket.text == product.text, "product's name in basket is not equal real product's name"

    def is_correct_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert basket_total.text == product_price.text, "basket total is not equal product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappear, but should"