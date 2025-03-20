from selenium.common import TimeoutException
from locators import Locators
from page_objects.base_page import BasePage
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    @allure.step("Нажать на заказ")
    def click_order(self):
        self.click_on_element(self.locators.ORDER_ITEM_LINK)

    @allure.step("Нажать на кнопку заказа")
    def click_order_button(self):
        order_button = self.find_element(self.locators.ORDER_BUTTON)
        self.click_element_by_browser(order_button)

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
        self.click_element_by_browser(close_button)

    @allure.step("Нажать на раздел истории заказов")
    def click_order_history(self):
        try:
            order_history_link = self.wait_for_element_to_be_clickable(self.locators.ORDER_HISTORY_SECTION)
            self.click_element_by_browser(order_history_link)
        except TimeoutException:
            pass

    @allure.step("Нажать на ссылку ленты заказов")
    def click_order_feed(self):
        try:
            order_feed_link = self.wait_for_element_to_be_clickable(self.locators.ORDER_FEED_LINK)
            self.click_element_by_browser(order_feed_link)
        except TimeoutException:
            pass

    @allure.step("Проверить видимость модального окна заказа")
    def is_order_modal_visible(self):
        return self.find_element(self.locators.DETAILS_ORDERS).is_displayed()

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
                lambda driver: not self.find_element(self.locators.WORK_IN_PROGRESS_TEXT).is_displayed(),
                timeout=5)
            self.wait_for_condition(
                lambda driver: self.find_element(self.locators.WORK_IN_PROGRESS_ORDER_NUMBER).is_displayed(),
                timeout=5)

            orders_in_progress_list = self.find_element(self.locators.WORK_IN_PROGRESS_ORDER_NUMBER)
            orders_in_progress_numbers = [
                order.text.strip().zfill(7)
                for order in orders_in_progress_list if order.text.strip().isdigit()]
            return len(set(orders_in_progress_numbers))
        except TimeoutException:
            return 0

    @allure.step("Ожидание обновления счетчика заказов за сегодня")
    def wait_for_completed_today_update(self, initial_value, timeout=10):
        self.wait_for_condition(lambda driver: int(self.get_completed_today()) > int(initial_value), timeout)
        return self.get_completed_today()

    @allure.step("Ожидание появления истории заказов")
    def wait_for_order_history(self):
        self.wait_for_element_visibility(self.locators.ORDER_HISTORY_LIST)

    @allure.step("Ожидание появления ленты заказов")
    def wait_for_order_feed(self):
        self.wait_for_element_visibility(self.locators.ORDER_FEED_LIST)

    @allure.step("Ожидание появления номера заказа")
    def wait_for_order_number_update(self):
        self.wait_for_condition(lambda driver: self.get_order_number() != "")




