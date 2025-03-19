import time
import allure
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.main_page import MainPage, OrderPage, IngredientPage
from tests.conftest import driver


class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_details_window_after_click(self, driver):
        order_page = OrderPage(driver)

        order_page.click_order_feed()
        order_page.click_order()
        order_page.is_order_modal_visible()

        assert order_page.is_order_modal_visible(), "Всплывающее окно не появилось после клика на заказ"
        assert order_page.is_order_modal_visible2(), "Детали заказа не отобразились во всплывающем окне"

    @allure.title('Отображение заказов пользователя в ленте заказов')
    def test_displaying_user_orders_in_the_order_feed(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_on_personal_account()
        order_page.click_order_history()
        time.sleep(3)
        history_orders = order_page.get_order_history_items()

        order_page.click_order_feed()
        time.sleep(3)
        feed_orders = order_page.get_order_list()

        history_order_numbers = {order.split()[0] for order in history_orders}
        feed_order_numbers = {order.split()[0] for order in feed_orders}

        assert history_order_numbers & feed_order_numbers, "В ленте заказов нет заказов из истории!"

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_all_time_order_counter(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        ing_page = IngredientPage(driver)

        order_page.click_order_feed()
        initial_all_time_count = order_page.get_completed_all_time()

        main_page.click_constructor()

        initial_count = ing_page.get_ingredient_counter_value()
        ing_page.drag_and_drop_ingredient()
        ing_page.wait_for_counter_update(initial_count)
        order_page.click_order_button()

        WebDriverWait(order_page.driver, 10).until(
            lambda driver: ing_page.is_modal_visible() and order_page.get_order_number() != "")

        order_page.close_modal_window()
        order_page.click_order_feed()
        updated_all_time_count = order_page.get_completed_all_time()

        assert int(updated_all_time_count) > int(initial_all_time_count), (
            f"Ожидалось, что счётчик 'Выполнено за всё время' увеличится. "
            f"Начальное значение: {initial_all_time_count}, обновленное значение: {updated_all_time_count}")

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_order_counter(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        ing_page = IngredientPage(driver)

        order_page.click_order_feed()
        initial_completed_today_count = order_page.get_completed_today()

        main_page.click_constructor()
        initial_count = ing_page.get_ingredient_counter_value()
        ing_page.drag_and_drop_ingredient()

        ing_page.wait_for_counter_update(initial_count)
        order_page.click_order_button()

        order_page.close_modal_window()
        order_page.click_order_feed()
        updated_completed_today = order_page.wait_for_completed_today_update(initial_completed_today_count)

        assert int(updated_completed_today) == int(initial_completed_today_count) + 1, (
            f"Ожидалось, что счётчик 'Выполнено за сегодня' увеличится на 1. "
            f"Начальное значение: {initial_completed_today_count}, обновленное значение: {updated_completed_today}")

    @allure.title('После оформления заказа его номер появляется в разделе В работе.')
    def test_number_of_order_in_work(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        ing_page = IngredientPage(driver)

        order_page.click_order_feed()
        initial_orders_in_progress = order_page.get_orders_in_progress()

        main_page.click_constructor()
        initial_count = ing_page.get_ingredient_counter_value()
        ing_page.drag_and_drop_ingredient()
        ing_page.wait_for_counter_update(initial_count)
        order_page.click_order_button()

        order_page.close_modal_window()
        order_page.click_order_feed()

        order_page.wait_for_completed_today_update(initial_orders_in_progress)
        time.sleep(3)
        orders_in_progress = int(order_page.get_orders_in_progress())
        assert orders_in_progress == initial_orders_in_progress, (
            f"Ожидалось, что количество заказов в работе увеличится. "
            f"Начальное количество: {initial_orders_in_progress}, "
            f"Обновленное количество: {orders_in_progress}")









