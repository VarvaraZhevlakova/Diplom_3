import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage
from tests.conftest import driver
from urls import password_forgot_page, password_reset_page


class TestRecoveryPassword:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_password(self, driver):
        page = MainPage(driver)

        page.click_on_personal_account()
        page.click_restore_password_link()

        expected_url = password_forgot_page
        assert expected_url in driver.current_url, "Переход на страницу восстановления пароля не произошел"

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_restore_password_process(self, driver):
        page = MainPage(driver)

        page.click_on_personal_account()
        page.click_restore_password_link()
        page.send_email_to_input(page.locators.EMAIL_INPUT)
        page.click_restore_button()

        expected_url = password_reset_page
        assert expected_url is not None, "Сообщение об успешном восстановлении пароля не появилось."

    @allure.title('Клик по кнопке, которая скрывает и показывает пароль')
    def test_high_password(self, driver):
        page = MainPage(driver)

        page.click_on_personal_account()
        page.click_restore_password_link()
        page.send_email_to_input(page.locators.EMAIL_INPUT)
        page.click_restore_button()
        page.click_on_element(page.locators.PASSWORD_FIELD)
        page.send_password_to_input(page.locators.PASSWORD_FIELD)
        page.click_on_element(page.locators.ICON_SHOW_HIDE_PASSWORD)
        active_field = WebDriverWait(page.driver, 5).until(
            EC.presence_of_element_located(page.locators.ICON_SHOW_HIDE_PASSWORD))

        assert active_field.get_attribute, "Поле пароля должно быть подсвечено или активным"
        assert active_field.is_enabled(), "Поле пароля должно быть активным после клика по кнопке"





