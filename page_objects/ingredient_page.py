from selenium.common import TimeoutException, NoSuchElementException
from locators import Locators
from page_objects.base_page import BasePage
import allure


class IngredientPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    @allure.step("Нажать на ингредиент")
    def click_on_ingredient(self):
        ingredient = self.wait_for_element_to_be_clickable(self.locators.INGREDIENT)
        ingredient.click()

    @allure.step("Перетащить ингредиент в цель")
    def drag_and_drop_ingredient(self):
        ingredient_locator = self.locators.INGREDIENT
        target_locator = self.locators.TARGET_AREA

        ingredient = self.wait_for_element_visibility(ingredient_locator)
        target = self.wait_for_element_visibility(target_locator)

        self.driver.execute_script("""
            var dataTransfer = { data: {},
                setData: function(format, data) { this.data[format] = data; },
                getData: function(format) { return this.data[format]; }
            };

            var dragStartEvent = new MouseEvent('dragstart', { bubbles: true, cancelable: true, view: window, });
            var dragEndEvent = new MouseEvent('dragend', { bubbles: true, cancelable: true, view: window, });
            var dropEvent = new MouseEvent('drop', { bubbles: true, cancelable: true, view: window, });

            arguments[0].dispatchEvent(dragStartEvent);
            arguments[1].dispatchEvent(dropEvent);
            arguments[0].dispatchEvent(dragEndEvent);
        """, ingredient, target)

    @allure.step("Получить значение счетчика ингредиентов")
    def get_ingredient_counter_value(self):
        counter_element = self.wait_for_element_visibility(self.locators.INGREDIENT_COUNTER)
        return int(counter_element.text)

    @allure.step("Проверить видимость модального окна ингредиента")
    def is_ingredient_modal_visible(self):
        modal_window = self.find_element(self.locators.MODAL_WINDOW)
        return modal_window.is_displayed()

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            close_button = self.wait_for_element_to_be_clickable(self.locators.CLOSE_MODAL_BUTTON)
            self.click_element_by_browser(close_button)
        except TimeoutException:
            print("Ошибка: Кнопка закрытия всплывающего окна не стала кликабельной в течение 10 секунд")

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_disable(self):
        try:
            modal_window_close = self.find_element(self.locators.MODAL_WINDOW_CLOSE)
            return not modal_window_close.is_displayed()
        except NoSuchElementException:
            return True

    @allure.step("Ожидать обновление счетчика ингредиентов")
    def wait_for_counter_update(self, initial_count):
        updated_count = str(int(initial_count) + 1)
        self.wait_for_text_in_element(self.locators.INGREDIENT_COUNTER, updated_count)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        try:
            modal = self.wait_for_element_visibility(self.locators.MODAL_WINDOW)
            return modal.is_displayed()
        except Exception:
            return False
