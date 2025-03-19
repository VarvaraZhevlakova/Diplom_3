import allure
from page_objects.main_page import MainPage, OrderPage, IngredientPage, LoginPage
from tests.conftest import driver
from urls import base_url_burgers, feed


class TestBaseFunctionally:
    @allure.title('Переход по клику на «Конструктор»')
    def test_click_to_constructor(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        order_page.click_order_feed()
        main_page.click_constructor()
        current_url = driver.current_url
        expected_url = base_url_burgers

        assert current_url == expected_url, f"Ожидался URL {expected_url}, но был {current_url}"

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_constructor()
        order_page.click_order_feed()
        current_url = driver.current_url
        expected_url = feed
        assert current_url == expected_url, f"Ожидался URL {expected_url}, но был {current_url}"

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_details_window_after_click_of_ingredient(self, driver):
        ing_page = IngredientPage(driver)

        ing_page.click_on_ingredient()
        assert ing_page.is_ingredient_modal_visible(), "Всплывающее окно с деталями ингредиента не появилось"

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_window_details(self, driver):
        ing_page = IngredientPage(driver)

        ing_page.click_on_ingredient()
        ing_page.close_modal()
        assert not ing_page.is_ingredient_modal_disable(), "Всплывающее окно с деталями не закрыто"

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_to_an_order_the_counter_increases(self, driver):
        ing_page = IngredientPage(driver)

        initial_count = ing_page.get_ingredient_counter_value()
        ing_page.drag_and_drop_ingredient()
        ing_page.wait_for_counter_update(initial_count)
        updated_count = ing_page.get_ingredient_counter_value()
        assert updated_count > initial_count, f"Каунтер не увеличился: {initial_count} -> {updated_count}"

    @allure.title('Залогиненный пользователь может оформить заказ.')
    def test_logged_user_can_place_an_order(self, driver, test_user_credentials):
        ing_page = IngredientPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        email = test_user_credentials["email"]
        password = test_user_credentials["password"]

        main_page.click_on_personal_account()
        login_page.send_email_to_input2(email)
        login_page.send_password_to_input2(password)

        login_page.click_login_button()

        browser_name = driver.capabilities['browserName'].lower()

        if browser_name != 'firefox':
            main_page.click_constructor()

        initial_count = ing_page.get_ingredient_counter_value()
        ing_page.drag_and_drop_ingredient()
        ing_page.wait_for_counter_update(initial_count)
        order_page.click_order_button()

        assert ing_page.is_modal_visible(), "Модальное окно с заказом не появилось"















