from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from QL_project.pages.base_page import BasePage
from QL_project.pages.locators import ProductPageLocators


class ProductPageCheck(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), \
            "Add to basket button is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((By.CLASS_NAME, "alertinner ")))
        except TimeoutException:
            return False
        return True

    def check_message_after_add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()
        self.should_not_be_success_message()

    def check_message_after_add_to_basket_2(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()
        self.is_disappeared()
