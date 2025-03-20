import allure
from data import USER_CREDENTIALS
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from tests.conftest import driver
from urls import personal_acc, login_url


class TestPersonalAcc:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_acc(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        email = USER_CREDENTIALS["email"]
        password = USER_CREDENTIALS["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()
        main_page.click_on_personal_account()

        expected_url = personal_acc
        assert expected_url is not None, "Данных профиля не появилось."

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_history_orders(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        email = USER_CREDENTIALS["email"]
        password = USER_CREDENTIALS["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()
        main_page.click_on_personal_account()
        order_page.click_order_history()

        current_url = order_page.get_current_url()
        assert "/account/order-history" in current_url, "Не открылась история заказов"

    @allure.title('Выход из аккаунта')
    def test_go_on_logout_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        email = USER_CREDENTIALS["email"]
        password = USER_CREDENTIALS["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()
        main_page.click_on_personal_account()
        login_page.click_logout_button()

        login_page.wait_for_logout()

        current_url = login_page.get_current_url()
        expected_url = login_url

        assert expected_url in current_url, "Логаут пользователя не произошел"








