import allure
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.locators = Locators()
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Кликаем по элементу с локатором {locator}")
    def click_on_element(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    @allure.step("Ожидаем, что элемент с локатором {locator} станет кликабельным в течение {timeout} секунд")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Ожидаем, что элемент с локатором {locator} станет видимым в течение {timeout} секунд")
    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Вводим текст '{text}' в поле с локатором {locator}")
    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверяем, отображается ли элемент с локатором {locator}")
    def is_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step("Получаем текст из элемента с локатором {locator}")
    def get_element_text(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.text.strip()
        except NoSuchElementException:
            return ""

    @allure.step("Кликаем по элементу с использованием JavaScript: {element}")
    def click_using_js(self, element):
        browser_name = self.driver.capabilities['browserName'].lower()
        if browser_name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Ожидание элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    @allure.step("Ожидание элемента пока он станет кликабельным")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Ожидание появляения текста")
    def wait_for_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text))

    @allure.step("Получение текста элементов с локатора {locator}")
    def get_items(self, locator):
        elements = self.driver.find_elements(*locator)
        return [element.text.strip() for element in elements if element.text.strip()]

    @allure.step("Ожидание выполнения условия с тайм-аутом {timeout} секунд")
    def wait_for_condition(self, condition, timeout=10, poll_frequency=0.5):
        WebDriverWait(self.driver, timeout, poll_frequency).until(lambda driver: condition(driver))

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Клик на элемент черз браузер")
    def click_element_by_browser(self, element):
        browser_name = self.driver.capabilities['browserName'].lower()
        if browser_name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Поиск элемента")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Поиск нескольких элементов")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))



















