import time

import pytest

from QL_project.pages.base_page import BasePage
from QL_project.pages.basket_page import BasketPage
from QL_project.pages.locators import ProductPageLocators
from QL_project.pages.product_page import ProductPage
from QL_project.pages.login_page import LoginPage


@pytest.mark.need_review
@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1",
                                   "?promo=offer2", "?promo=offer3",
                                   "?promo=offer4", "?promo=offer5",
                                   "?promo=offer6", pytest.param(
        "?promo=offer7", marks=pytest.mark.xfail),
                                   "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           f"-work_207/{promo}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()

# второй способ
# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# promo = [f"{product_base_link}?promo=offer{no}" for no in range(10)]


# @pytest.mark.parametrize('link', promo)
# @pytest.mark.xfail(reason="Bug in this promo-link")
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"{promo}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_product_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           "-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket(*ProductPageLocators.BASKET_BUTTON)
    page = BasketPage(browser, browser.current_url)
    page.check_basket()


@pytest.mark.login_user
@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(self.browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "fggr345DE7878"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(self.browser, link)
        product_page.open()
        product_page.should_be_product_page_2()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(self.browser, link)
        product_page.open()
        product_page.go_to_basket(*ProductPageLocators.BASKET_BUTTON)
        page = BasketPage(self.browser, self.browser.current_url)
        page.check_basket()

