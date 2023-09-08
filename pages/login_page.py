import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "'login' not in link of login_page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Registration form is not presented"

    def should_see_email_field(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), \
            "email field is not presented"

    def should_enter_email(self, email):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def should_see_password_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), \
            "password field is not presented"

    def should_enter_password(self, password):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def should_see_confirm_password_field(self):
        assert self.is_element_present(
            *LoginPageLocators.CONFIRM_PASSWORD_FIELD), \
            "password field is not presented"

    def should_enter_confirm_password(self, password):
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)

    def should_see_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), \
            "registration button is not presented"

    def should_enter_registration_button(self):
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.browser.execute_script("window.scrollBy(0, 200);")
        self.should_see_email_field()
        self.should_enter_email(email)
        self.should_see_password_field()
        self.should_enter_password(password)
        self.should_see_confirm_password_field()
        self.should_enter_confirm_password(password)
        self.should_see_registration_button()
        self.should_enter_registration_button()
