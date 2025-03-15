import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.main_page import MainPage
from urls import base_url_burgers


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Неизвестный браузер: {browser_name}. Доступны: Chrome, Firefox.")


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
    return {
        "email": "varvara_bva_17_0302dd@gmail.com",
        "password": "yandexpracticum111"
    }


@pytest.fixture
def login(driver, test_user_credentials):
    page = MainPage(driver)

    email = test_user_credentials["email"]
    password = test_user_credentials["password"]

    page.click_on_personal_account()
    page.send_email_to_input2(email)
    page.send_password_to_input2(password)
    page.click_login_button()
    return page


@pytest.fixture
def create_order(driver, login):
    page = MainPage(driver)
    page = login

    browser_name = driver.capabilities['browserName'].lower()

    if browser_name != 'firefox':
        page.click_constructor()

    initial_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)
    page.drag_and_drop_ingredient(page.locators.INGREDIENT, page.locators.TARGET_AREA)
    page.wait_for_counter_update(page.locators.INGREDIENT_COUNTER, initial_count)
    page.click_order_button()

    WebDriverWait(page.driver, 10).until(
        lambda driver: page.is_modal_visible() and page.get_order_number() != "")

    return page.get_order_number()







