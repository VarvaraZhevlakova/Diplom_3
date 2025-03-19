import allure
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.main_page import MainPage, LoginPage, OrderPage
from tests.conftest import driver
from urls import personal_acc, login_url


class TestPersonalAcc:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_acc(self, driver, test_user_credentials):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        email = test_user_credentials["email"]
        password = test_user_credentials["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()
        main_page.click_on_personal_account()

        expected_url = personal_acc
        assert expected_url is not None, "Данных профиля не появилось."

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_history_orders(self, driver, test_user_credentials):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        email = test_user_credentials["email"]
        password = test_user_credentials["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()
        main_page.click_on_personal_account()
        order_page.click_order_history()

        assert "/account/order-history" in order_page.driver.current_url, "Не открылась история заказов"

    @allure.title('Выход из аккаунта')
    def test_go_on_logout_button(self, driver, test_user_credentials):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        email = test_user_credentials["email"]
        password = test_user_credentials["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()
        main_page.click_on_personal_account()
        login_page.click_logout_button()

        WebDriverWait(login_page.driver, 5).until(lambda d: "/login" in d.current_url)

        expected_url = login_url
        assert expected_url in driver.current_url, "Логаут пользователя не произошел"







