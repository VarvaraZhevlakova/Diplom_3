from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementAction:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, timeout=10):
        """Общий метод для ожидания и клика по элементу."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element = self.driver.find_element(*locator)
            element.click()
        except Exception as e:
            print(f"Не удалось кликнуть по элементу: {e}")
