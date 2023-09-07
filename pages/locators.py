from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "product_main, h1")
    NAME_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    COST_PRODUCT = (By.XPATH, '//p[@class="price_color"]')
    COST_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")
