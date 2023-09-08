from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from QL_project.pages.base_page import BasePage
from QL_project.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), \
            "Add to basket button is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_assert_name_product(self):
        product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        product = product.text
        product_in_basket = self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT_IN_BASKET)
        product_in_basket = product_in_basket.text
        assert product == product_in_basket, 'Error in names of product'

    def should_assert_cost_product(self):
        cost = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        cost = cost.text
        cost_in_basket = self.browser.find_element(
            *ProductPageLocators.COST_PRODUCT_IN_BASKET)
        cost_in_basket = cost_in_basket.text
        assert cost == cost_in_basket, 'Error in costs of product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_assert_name_product()
        self.should_assert_cost_product()

    def should_be_product_page_2(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()
        self.should_assert_name_product()
        self.should_assert_cost_product()
