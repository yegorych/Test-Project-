import time

from .base_page import BasePage
from .locators import  LoginPageLocators
from random_word import RandomWords

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #assert "login" in self.browser.current_url , "substr 'login' is not in URL"
        self.is_correct_url("login")


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "login username not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "login password not found"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "registration email not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "registration password #1 not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "registration password #2 not found"

    def register_new_user(self):
        r = RandomWords()
        email = str(r.get_random_word()) + "@fakemail.org"
        password = str(time.time())
        print(f'Your email and password : {email} ; {password}')
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()