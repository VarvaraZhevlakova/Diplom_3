from locators import Locators
from page_objects.base_page import BasePage
from helpers.gen_input import DataGenerator
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()
        self.data_generator = DataGenerator()

    @allure.step("Нажать на ссылку восстановления пароля")
    def click_restore_password_link(self):
        self.click_on_element(self.locators.RESTORE_PASSWORD_LINK)

    @allure.step("Ввести email в поле ввода")
    def send_email_to_input(self, locator):
        generate_email = self.data_generator.generate_email()
        self.find_element(locator).send_keys(generate_email)

    @allure.step("Ввести email в поле ввода")
    def send_email_to_input2(self, email):
        self.find_element(self.locators.EMAIL_INPUT).clear()
        self.find_element(self.locators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввести пароль в поле ввода")
    def send_password_to_input(self, locator):
        generate_password = self.data_generator.generate_password()
        self.find_element(locator).send_keys(generate_password)

    @allure.step("Ввести пароль в поле ввода")
    def send_password_to_input2(self, password):
        self.find_element(self.locators.PASSWORD_FIELD).clear()
        self.find_element(self.locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажать на кнопку входа")
    def click_login_button(self):
        self.wait_for_element_to_be_clickable(self.locators.LOGIN_BUTTON).click()

    @allure.step("Нажать на кнопку регистрации")
    def click_register_button(self):
        self.find_element(*self.locators.REGISTER_BUTTON).click()

    @allure.step("Нажать на кнопку выхода")
    def click_logout_button(self):
        self.wait_for_element_to_be_clickable(self.locators.LOGOUT_BUTTON).click()

    @allure.step("Нажать на ссылку регистрации")
    def click_register_link(self):
        self.click_on_element(self.locators.REGISTER_LINK)

    @allure.step("Клик по кнопке переключения видимости пароля")
    def click_toggle_password_visibility(self):
        self.click_on_element(self.locators.ICON_SHOW_HIDE_PASSWORD)

    @allure.step("Ожидание, пока кнопка переключения видимости пароля станет доступной")
    def wait_for_toggle_password_visibility(self):
        element = self.wait_for_element_visibility(self.locators.ICON_SHOW_HIDE_PASSWORD)
        return element

    @allure.step("Нажать на кнопку восстановления пароля")
    def click_restore_button(self):
        self.click_on_element(self.locators.RESTORE_BUTTON)

    @allure.step("Кликает на поле ввода пароля")
    def click_on_password_input(self):
        self.click_on_element(self.locators.PASSWORD_FIELD)

    @allure.step("Ожидание редиректа на страницу логина после выхода")
    def wait_for_logout(self):
        self.wait_for_condition(lambda driver: "/login" in driver.current_url)

