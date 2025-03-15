from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from helpers.gen_input import DataGenerator
from locators import Locators
from page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()
        self.data_generator = DataGenerator()

    def click_on_personal_account(self):
        try:
            personal_account_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.PERSONAL_ACCOUNT_BUTTON))
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", personal_account_button)
            else:
                personal_account_button.click()
        except TimeoutException:
            pass

    def click_restore_password_link(self):
        self.click_on_element(self.locators.RESTORE_PASSWORD_LINK)

    def click_field_email(self):
        self.click_on_element(self.locators.EMAIL_INPUT)

    def click_field_password(self):
        self.click_on_element(self.locators.PASSWORD_FIELD)

    def send_email_to_input(self, locator):
        generate_email = self.data_generator.generate_email()
        self.driver.find_element(*locator).send_keys(generate_email)

    def send_password_to_input(self, locator):
        generate_password = self.data_generator.generate_password()
        self.driver.find_element(*locator).send_keys(generate_password)

    def send_name_to_input(self):
        name = self.data_generator.generate_name()
        self.send_keys(self.locators.NAME_INPUT, name)

    def click_restore_button(self):
        self.click_on_element(self.locators.RESTORE_BUTTON)

    def wait_for_restore_text_locator(self):
        restore_text_locator = self.locators.RESTORE_TEXT
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(restore_text_locator))

    def toggle_password_visibility(self):
        self.click_on_element(self.locators.ICON_SHOW_HIDE_PASSWORD)
        WebDriverWait(self.driver, 2).until(
            lambda driver: driver.find_element(*self.locators.PASSWORD_INPUT_HIDDEN) or driver.find_element(*self.locators.PASSWORD_INPUT_VISIBLE))

    def click_login_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

    def click_order_history(self):
        try:
            order_history_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.ORDER_HISTORY_SECTION))
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", order_history_link)
            else:
                order_history_link.click()
        except TimeoutException:
            pass

    def click_register_link(self):
        self.click_on_element(self.locators.REGISTER_LINK)

    def click_register_button(self):
        self.driver.find_element(*self.locators.REGISTER_BUTTON).click()

    def send_email_to_input2(self, email):
        self.driver.find_element(*self.locators.EMAIL_INPUT).clear()
        self.driver.find_element(*self.locators.EMAIL_INPUT).send_keys(email)

    def send_password_to_input2(self, password):
        self.driver.find_element(*self.locators.PASSWORD_FIELD).clear()
        self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(password)

    def click_logout_button(self):
        WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable(self.locators.LOGOUT_BUTTON)).click()

    def click_order_feed(self):
        try:
            order_feed_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.ORDER_FEED_LINK))
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", order_feed_link)
            else:
                order_feed_link.click()
        except TimeoutException:
            pass

    def click_order(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.ORDER_ITEM_LINK)).click()

    def is_order_modal_visible(self):
        return self.driver.find_element(*self.locators.DETAILS_ORDERS).is_displayed()

    def is_order_modal_visible2(self):
        return self.driver.find_element(*self.locators.DETAILS_ORDERS).is_displayed()

    def click_constructor(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.CONSTRUCTOR_BUTTON)).click()

    def click_on_ingredient(self):
        ingredient = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.INGREDIENT))
        ingredient.click()

    def is_ingredient_modal_visible(self):
        return self.driver.find_element(*self.locators.MODAL_WINDOW).is_displayed()

    def close_modal(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.CLOSE_MODAL_BUTTON))
            browser_name = self.driver.capabilities['browserName'].lower()
            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", close_button)
            else:
                close_button.click()

        except TimeoutException:
            print("Ошибка: Кнопка закрытия всплывающего окна не стала кликабельной в течение 10 секунд")

    def is_ingredient_modal_disable(self):
        try:
            return not self.driver.find_element(*self.locators.MODAL_WINDOW_CLOSE).is_displayed()
        except NoSuchElementException:
            return True

    def get_ingredient_counter_value(self, counter_locator):
        try:
            counter_element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(counter_locator)
            )
            return counter_element.text.strip()
        except TimeoutException:
            print(f"Ошибка: Не удалось найти {counter_locator} в течение 15 секунд")
            return None
        except NoSuchElementException:
            print(f"Ошибка: Элемент {counter_locator} отсутствует на странице")
            return None

    def drag_and_drop_ingredient(self, ingredient_locator, target_locator):
        ingredient = self.driver.find_element(*ingredient_locator)
        target = self.driver.find_element(*target_locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(ingredient))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(target))
        self.driver.execute_script("""
            var dataTransfer = {
                data: {},
                setData: function(format, data) { this.data[format] = data; },
                getData: function(format) { return this.data[format]; }
            };

            var dragStartEvent = new MouseEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                view: window,
            });

            var dragEndEvent = new MouseEvent('dragend', {
                bubbles: true,
                cancelable: true,
                view: window,
            });

            var dropEvent = new MouseEvent('drop', {
                bubbles: true,
                cancelable: true,
                view: window,
            });

            arguments[0].dispatchEvent(dragStartEvent);
            arguments[1].dispatchEvent(dropEvent);
            arguments[0].dispatchEvent(dragEndEvent);
        """, ingredient, target)

    def wait_for_counter_update(self, counter_locator, initial_count):
        updated_count = str(int(initial_count) + 1)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(counter_locator, updated_count))

    def click_order_button(self):
        order_button = self.driver.find_element(*self.locators.ORDER_BUTTON)
        browser_name = self.driver.capabilities['browserName'].lower()

        if browser_name == 'firefox':
            self.driver.execute_script("arguments[0].click();", order_button)
        else:
            order_button.click()

    def is_modal_visible(self):
        try:
            modal = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.locators.MODAL_WINDOW)
            )
            return modal.is_displayed()
        except Exception:
            return False

    def get_order_history_items(self):
        wait = WebDriverWait(self.driver, 10)

        def get_items():
            try:
                elements = wait.until(EC.presence_of_all_elements_located(self.locators.ORDER_HISTORY_ITEMS))
                return [el.text for el in elements]
            except StaleElementReferenceException:
                return get_items()

        return get_items()

    def get_order_list(self):
        wait = WebDriverWait(self.driver, 10)

        def get_items():
            try:
                elements = wait.until(EC.presence_of_all_elements_located(self.locators.ORDER_ITEMS))
                return [el.text for el in elements]
            except StaleElementReferenceException:
                return get_items()

        return get_items()

    def get_order_number(self):
        try:
            order_number_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.ORDER_NUMBER))
            order_number = order_number_element.text.strip()

            if order_number.isdigit() and int(order_number) != 9999:
                return order_number

            return ""

        except TimeoutException:
            return ""

    def close_modal_window(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.CLOSE_MODAL_BUTTON_OF_ORDER))
            browser_name = self.driver.capabilities['browserName'].lower()

            if browser_name == 'firefox':
                self.driver.execute_script("arguments[0].click();", close_button)
            else:
                close_button.click()

        except TimeoutException:
            pass

    def get_completed_all_time(self):
        try:
            completed_counter_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.COMPLETED_ALL_TIME_TEXT))
            completed_counter = completed_counter_element.text.strip()  #
            return completed_counter
        except TimeoutException:
            return None

    def get_completed_today(self):
        try:
            completed_counter_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.COMPLETED_TODAY_TEXT))
            completed_counter = completed_counter_element.text.strip()
            return completed_counter
        except TimeoutException:
            return None

    def get_orders_in_progress(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.locators.WORK_IN_PROGRESS_TEXT))
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.WORK_IN_PROGRESS_ORDER_NUMBER))
            orders_in_progress_list = self.driver.find_elements(*self.locators.WORK_IN_PROGRESS_ORDER_NUMBER)
            orders_in_progress_numbers = [
                order.text.strip().zfill(7)
                for order in orders_in_progress_list if order.text.strip().isdigit()]
            return len(set(orders_in_progress_numbers))
        except TimeoutException:
            return 0























