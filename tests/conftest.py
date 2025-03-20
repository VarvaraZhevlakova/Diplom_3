import pytest

from data import USER_CREDENTIALS
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage

from urls import base_url_burgers
from web_driver_factory import WebDriverFactory


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_driver(browser_name)
    url = base_url_burgers
    driver.get(url)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome, firefox")


@pytest.fixture
def login(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    email = USER_CREDENTIALS["email"]
    password = USER_CREDENTIALS["password"]

    main_page.click_on_personal_account()
    login_page.send_email_to_input2(email)
    login_page.send_password_to_input2(password)
    login_page.click_login_button()
    return login_page














