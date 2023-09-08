from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET = (By.CLASS_NAME, "basket_summary")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "product_main, h1")
    NAME_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    COST_PRODUCT = (By.XPATH, '//p[@class="price_color"]')
    COST_PRODUCT_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")