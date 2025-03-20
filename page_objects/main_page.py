from selenium.common import TimeoutException
from locators import Locators
from page_objects.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    @allure.step("Нажать на кнопку конструктора")
    def click_constructor(self):
        self.wait_for_element_to_be_clickable(self.locators.CONSTRUCTOR_BUTTON).click()

    @allure.step("Нажать на кнопку личного кабинета")
    def click_on_personal_account(self):
        try:
            personal_account_button = self.wait_for_element_to_be_clickable(self.locators.PERSONAL_ACCOUNT_BUTTON)
            self.click_element_by_browser(personal_account_button)

        except TimeoutException:
            pass






































