import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help='Choose preferred language for the browser (e.g., en, es, fr)')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == "chrome":
        options = Options()
        if user_language:
            options.add_experimental_option('prefs',
                                            {
                                                'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        if user_language:
            firefox_profile.set_preference('intl.accept_languages',
                                           user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
