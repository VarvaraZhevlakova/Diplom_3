import allure
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.main_page import MainPage
from tests.conftest import driver


class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_details_window_after_click(self, driver):
        page = MainPage(driver)

        page.click_order_feed()
        page.click_order()
        page.is_order_modal_visible()

        assert page.is_order_modal_visible(), "Всплывающее окно не появилось после клика на заказ"
        assert page.is_order_modal_visible2(), "Детали заказа не отобразились во всплывающем окне"

    @allure.title('Отображение заказов пользователя в ленте заказов')
    def test_displaying_user_orders_in_the_order_feed(self, driver, create_order):
        page = MainPage(driver)

        page.close_modal_window()
        page.click_on_personal_account()
        page.click_order_history()
        history_orders = page.get_order_history_items()

        page.click_order_feed()
        feed_orders = page.get_order_list()

        history_order_numbers = {order.split()[0] for order in history_orders}
        feed_order_numbers = {order.split()[0] for order in feed_orders}

        assert history_order_numbers & feed_order_numbers, "В ленте заказов нет заказов из истории!"

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_all_time_order_counter(self, driver, login):
        page = MainPage(driver)
        page = login

        page.click_order_feed()
        initial_all_time_count = page.get_completed_all_time()

        page.click_constructor()

        initial_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)
        page.drag_and_drop_ingredient(page.locators.INGREDIENT, page.locators.TARGET_AREA)
        page.wait_for_counter_update(page.locators.INGREDIENT_COUNTER, initial_count)
        page.click_order_button()

        WebDriverWait(page.driver, 10).until(
            lambda driver: page.is_modal_visible() and page.get_order_number() != "")

        page.close_modal_window()
        page.click_order_feed()
        updated_all_time_count = page.get_completed_all_time()

        assert int(updated_all_time_count) == int(initial_all_time_count) + 1, (
            f"Ожидалось, что счётчик 'Выполнено за всё время' увеличится на 1. "
            f"Начальное значение: {initial_all_time_count}, обновленное значение: {updated_all_time_count}")

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_order_counter(self, driver, login):
        page = MainPage(driver)
        page = login

        page.click_order_feed()
        initial_completed_today_count = page.get_completed_today()

        page.click_constructor()
        initial_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)
        page.drag_and_drop_ingredient(page.locators.INGREDIENT, page.locators.TARGET_AREA)
        page.wait_for_counter_update(page.locators.INGREDIENT_COUNTER, initial_count)
        page.click_order_button()

        WebDriverWait(page.driver, 10).until(
            lambda driver: page.is_modal_visible() and page.get_order_number() != "")

        page.close_modal_window()
        page.click_order_feed()
        updated_completed_today = page.get_completed_today()

        assert int(updated_completed_today) == int(initial_completed_today_count) + 1, (
            f"Ожидалось, что счётчик 'Выполнено за всё время' увеличится на 1. "
            f"Начальное значение: {initial_completed_today_count}, обновленное значение: {updated_completed_today}")

    @allure.title('После оформления заказа его номер появляется в разделе В работе.')
    def test_number_of_order_in_work(self, driver, login):
        page = MainPage(driver)
        page = login

        page.click_order_feed()
        initial_orders_in_progress = page.get_orders_in_progress()

        page.click_constructor()
        initial_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)
        page.drag_and_drop_ingredient(page.locators.INGREDIENT, page.locators.TARGET_AREA)
        page.wait_for_counter_update(page.locators.INGREDIENT_COUNTER, initial_count)
        page.click_order_button()

        WebDriverWait(page.driver, 10).until(
            lambda driver: page.is_modal_visible() and page.get_order_number() != "")
        page.close_modal_window()

        page.click_order_feed()

        WebDriverWait(page.driver, 10).until(
            lambda driver: page.get_orders_in_progress() > initial_orders_in_progress)

        orders_in_progress = page.get_orders_in_progress()
        assert orders_in_progress == initial_orders_in_progress + 1, (
            f"Ожидалось, что количество заказов в работе увеличится на 1. "
            f"Начальное количество: {initial_orders_in_progress}, "
            f"Обновленное количество: {orders_in_progress}")









