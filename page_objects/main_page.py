from selenium.common import TimeoutException, NoSuchElementException
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
        self.driver.find_element(*locator).send_keys(generate_email)

    @allure.step("Ввести email в поле ввода")
    def send_email_to_input2(self, email):
        self.driver.find_element(*self.locators.EMAIL_INPUT).clear()
        self.driver.find_element(*self.locators.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввести пароль в поле ввода")
    def send_password_to_input(self, locator):
        generate_password = self.data_generator.generate_password()
        self.driver.find_element(*locator).send_keys(generate_password)

    @allure.step("Ввести пароль в поле ввода")
    def send_password_to_input2(self, password):
        self.driver.find_element(*self.locators.PASSWORD_FIELD).clear()
        self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажать на кнопку входа")
    def click_login_button(self):
        self.wait_for_element_to_be_clickable(self.locators.LOGIN_BUTTON).click()

    @allure.step("Нажать на кнопку регистрации")
    def click_register_button(self):
        self.driver.find_element(*self.locators.REGISTER_BUTTON).click()

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


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    @allure.step("Нажать на заказ")
    def click_order(self):
        self.wait_for_element_to_be_clickable(self.locators.ORDER_ITEM_LINK).click()

    @allure.step("Нажать на кнопку заказа")
    def click_order_button(self):
        order_button = self.driver.find_element(*self.locators.ORDER_BUTTON)
        browser_name = self.driver.capabilities['browserName'].lower()
        if browser_name == 'firefox':
            self.driver.execute_script("arguments[0].click();", order_button)
        else:
            order_button.click()

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        try:
            order_number_element = self.wait_for_element_visibility(self.locators.ORDER_NUMBER)
            order_number = order_number_element.text.strip()
            return order_number if order_number.isdigit() and int(order_number) != 9999 else ""
        except TimeoutException:
            return ""

    @allure.step("Закрыть модальное окно заказа")
    def close_modal_window(self):
        order_number = self.get_order_number()
        while not order_number:
            order_number = self.get_order_number()
        close_button = self.wait_for_element_to_be_clickable(self.locators.CLOSE_MODAL_BUTTON_OF_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
        browser_name = self.driver.capabilities['browserName'].lower()
        if browser_name == 'firefox':
            self.driver.execute_script("arguments[0].click();", close_button)
        else:
            close_button.click()

    @allure.step("Нажать на раздел истории заказов")
    def click_order_history(self):
        try:
            order_history_link = self.wait_for_element_to_be_clickable(self.locators.ORDER_HISTORY_SECTION)
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", order_history_link)
            else:
                order_history_link.click()
        except TimeoutException:
            pass

    @allure.step("Нажать на ссылку ленты заказов")
    def click_order_feed(self):
        try:
            order_feed_link = self.wait_for_element_to_be_clickable(self.locators.ORDER_FEED_LINK)
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", order_feed_link)
            else:
                order_feed_link.click()
        except TimeoutException:
            pass

    @allure.step("Проверить видимость модального окна заказа")
    def is_order_modal_visible(self):
        return self.driver.find_element(*self.locators.DETAILS_ORDERS).is_displayed()

    @allure.step("Проверить видимость модального окна заказа 2")
    def is_order_modal_visible2(self):
        return self.driver.find_element(*self.locators.DETAILS_ORDERS).is_displayed()

    @allure.step("Получить список истории заказов")
    def get_order_history_items(self):
        return self.get_items(self.locators.ORDER_HISTORY_ITEMS)

    @allure.step("Получить список заказов")
    def get_order_list(self):
        return self.get_items(self.locators.ORDER_ITEMS)

    @allure.step("Получить количество выполненных заказов за все время")
    def get_completed_all_time(self):
        try:
            completed_counter_element = self.wait_for_element_visibility(self.locators.COMPLETED_ALL_TIME_TEXT)
            completed_counter = completed_counter_element.text.strip()
            return completed_counter
        except TimeoutException:
            return None

    @allure.step("Получить количество выполненных заказов сегодня")
    def get_completed_today(self):
        try:
            completed_counter_element = self.wait_for_element_visibility(self.locators.COMPLETED_TODAY_TEXT)
            completed_counter = completed_counter_element.text.strip()
            return completed_counter
        except TimeoutException:
            return None

    @allure.step("Получить количество заказов в процессе")
    def get_orders_in_progress(self):
        try:
            self.wait_for_condition(
                lambda driver: not driver.find_element(*self.locators.WORK_IN_PROGRESS_TEXT).is_displayed(),
                timeout=5)
            self.wait_for_condition(
                lambda driver: driver.find_element(*self.locators.WORK_IN_PROGRESS_ORDER_NUMBER).is_displayed(),
                timeout=5)

            orders_in_progress_list = self.driver.find_elements(*self.locators.WORK_IN_PROGRESS_ORDER_NUMBER)
            orders_in_progress_numbers = [
                order.text.strip().zfill(7)
                for order in orders_in_progress_list if order.text.strip().isdigit()]
            return len(set(orders_in_progress_numbers))
        except TimeoutException:
            return 0

    @allure.step("Получить количество выполненных заказов сегодня")
    def get_completed_today(self):
        try:
            completed_counter_element = self.wait_for_element_visibility(self.locators.COMPLETED_TODAY_TEXT)
            completed_counter = completed_counter_element.text.strip()
            return completed_counter
        except TimeoutException:
            return None

    @allure.step("Ожидание обнлвления счетчика заказов за сегодня")
    def wait_for_completed_today_update(self, initial_value, timeout=10):
        self.wait_for_condition(
            lambda driver: int(self.get_completed_today()) > int(initial_value),
            timeout)
        return self.get_completed_today()


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
        return self.driver.find_element(*self.locators.MODAL_WINDOW).is_displayed()

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            close_button = self.wait_for_element_to_be_clickable(self.locators.CLOSE_MODAL_BUTTON)
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", close_button)
            else:
                close_button.click()
        except TimeoutException:
            print("Ошибка: Кнопка закрытия всплывающего окна не стала кликабельной в течение 10 секунд")

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_disable(self):
        try:
            return not self.driver.find_element(*self.locators.MODAL_WINDOW_CLOSE).is_displayed()
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
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", personal_account_button)
            else:
                personal_account_button.click()
        except TimeoutException:
            pass






































