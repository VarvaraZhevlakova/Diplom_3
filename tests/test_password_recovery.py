import allure
from page_objects.main_page import MainPage, LoginPage
from tests.conftest import driver
from urls import password_forgot_page, password_reset_page


class TestRecoveryPassword:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_password(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_on_personal_account()
        login_page.click_restore_password_link()

        expected_url = password_forgot_page
        assert expected_url in driver.current_url, "Переход на страницу восстановления пароля не произошел"

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_restore_password_process(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_on_personal_account()
        login_page.click_restore_password_link()
        login_page.send_email_to_input2(login_page.data_generator.generate_email())
        login_page.click_restore_button()

        expected_url = password_reset_page
        assert expected_url is not None, "Сообщение об успешном восстановлении пароля не появилось."

    @allure.title('Клик по кнопке, которая скрывает и показывает пароль')
    def test_toggle_password_visibility(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_on_personal_account()
        login_page.click_restore_password_link()
        login_page.send_email_to_input2(login_page.data_generator.generate_email())
        login_page.click_restore_button()
        login_page.click_on_password_input()
        login_page.send_password_to_input2(login_page.data_generator.generate_password())
        login_page.click_toggle_password_visibility()

        active_field = login_page.wait_for_toggle_password_visibility()

        assert active_field.is_displayed(), "Поле пароля должно быть видно"
        assert active_field.is_enabled(), "Поле пароля должно быть активным после клика по кнопке"





