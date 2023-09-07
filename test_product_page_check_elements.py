import pytest

from QL_project.pages.product_page_check_elements import ProductPageCheck


@pytest.mark.xfail(reason="This is not bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPageCheck(browser, link, 0)
    product_page.open()
    product_page.check_message_after_add_to_basket()


@pytest.mark.xfail(reason="This is not bug")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPageCheck(browser, link, 0)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="This is not bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPageCheck(browser, link, 0)
    product_page.open()
    product_page.check_message_after_add_to_basket_2()

