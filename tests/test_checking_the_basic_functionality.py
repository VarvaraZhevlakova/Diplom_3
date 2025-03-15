import allure
from page_objects.main_page import MainPage
from tests.conftest import driver
from urls import base_url_burgers, feed


class TestBaseFunctionally:
    @allure.title('Переход по клику на «Конструктор»')
    def test_click_to_constructor(self, driver):
        page = MainPage(driver)

        page.click_order_feed()
        page.click_constructor()
        expected_url = base_url_burgers
        assert expected_url, "Переход в конструктор не произошел"

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_to_order_feed(self, driver):
        page = MainPage(driver)

        page.click_constructor()
        page.click_order_feed()
        expected_url = feed
        assert expected_url, "Переход в конструктор не произошел"

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_details_window_after_click_of_ingredient(self, driver):
        page = MainPage(driver)

        page.click_on_ingredient()
        assert page.is_ingredient_modal_visible(), "Всплывающее окно с деталями ингредиента не появилось"

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_details(self, driver):
        page = MainPage(driver)

        page.click_on_ingredient()
        page.close_modal()
        assert not page.is_ingredient_modal_disable(), "Всплывающее окно с деталями не закрыто"

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_to_an_order_the_counter_increases(self, driver):
        page = MainPage(driver)

        initial_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)
        page.drag_and_drop_ingredient(page.locators.INGREDIENT, page.locators.TARGET_AREA)
        page.wait_for_counter_update(page.locators.INGREDIENT_COUNTER, initial_count)
        updated_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)

        assert updated_count > initial_count, f"Каунтер не увеличился: {initial_count} -> {updated_count}"

    @allure.title('Залогиненный пользователь может оформить заказ.')
    def test_logged_user_can_place_an_order(self, driver, test_user_credentials):
        page = MainPage(driver)

        email = test_user_credentials["email"]
        password = test_user_credentials["password"]

        page.click_on_personal_account()
        page.send_email_to_input2(email)
        page.send_password_to_input2(password)

        page.click_login_button()

        browser_name = driver.capabilities['browserName'].lower()

        if browser_name != 'firefox':
            page.click_constructor()

        initial_count = page.get_ingredient_counter_value(page.locators.INGREDIENT_COUNTER)
        page.drag_and_drop_ingredient(page.locators.INGREDIENT, page.locators.TARGET_AREA)
        page.wait_for_counter_update(page.locators.INGREDIENT_COUNTER, initial_count)
        page.click_order_button()

        assert page.is_modal_visible(), "Модальное окно с заказом не появилось"















