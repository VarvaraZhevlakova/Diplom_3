import pytest
from data import USER_CREDENTIALS
from page_objects.base_page import BasePage
from page_objects.main_page import LoginPage, MainPage

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


@pytest.fixture(scope="session")
def test_user_credentials():
    return USER_CREDENTIALS


@pytest.fixture
def login(driver, test_user_credentials):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    email = test_user_credentials["email"]
    password = test_user_credentials["password"]

    main_page.click_on_personal_account()
    login_page.send_email_to_input2(email)
    login_page.send_password_to_input2(password)
    login_page.click_login_button()
    return login_page














