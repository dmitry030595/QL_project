from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from QL_project.pages.base_page import BasePage
from QL_project.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        try:
            self.browser.find_element(*BasketPageLocators.NOT_EMPTY_BASKET)
            raise AssertionError("Products are presented, but should not be")
        except NoSuchElementException:
            print("Basket is empty")

    def should_see_text_of_empty_basket(self):
        text_empty_basket = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_TEXT)
        text_empty_basket = text_empty_basket.text
        assert text_empty_basket == "Your basket is empty. Continue " \
                                    "shopping", "text of empty basket is not is presented"

    def check_basket(self):
        self.should_not_be_products_in_basket()
        self.should_see_text_of_empty_basket()
