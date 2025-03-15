from selenium.webdriver.common.by import By


class Locators:
    # Определение всех локаторов
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and contains(., 'Личный Кабинет')]")
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    RESTORE_BUTTON = (By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']")
    RESTORE_TEXT = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_INPUT_HIDDEN = (By.XPATH, "//div[contains(@class, 'input_type_password')]//input[@type='password']")
    PASSWORD_INPUT_VISIBLE = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@type='text']")
    ICON_SHOW_HIDE_PASSWORD = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_type_password')]/input[@type='password']")

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    ORDER_HISTORY_SECTION = (By.XPATH, "//a[@href='/account/order-history']")

    REGISTER_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Зарегистрироваться']")
    NAME_INPUT = (By.XPATH, "//div[contains(@class, 'input') and .//label[text()='Имя']]//input")

    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa')
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__') and text()='Выход']")

    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_ITEM_LINK = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r')]//a[contains(@href, '/feed')]")
    ORDER_MODAL = (By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_")
    DETAILS_ORDERS = (By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4')

    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link')]//p[text()='Конструктор']")
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
    MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal_opened__3ISw4")
    MODAL_WINDOW_CLOSE = (By.CSS_SELECTOR, ".Modal_modal__P3_V5")
    CLOSE_MODAL_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")

    TOTAL_COUNTER = (By.CSS_SELECTOR, ".BurgerConstructor_basket__totalContainer__2Z-ho .text_type_digits-medium")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".BurgerConstructor_basket__totalContainer__2Z-ho p")
    TARGET_AREA = (By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_")

    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    MODAL_WINDOW_OF_ORDER = (By.CSS_SELECTOR, "div.Modal_modal__container__Wo2l_")

    ORDER_HISTORY_LIST = (By.CLASS_NAME, "OrderHistory_profileList__374GU")
    ORDER_HISTORY_ITEMS = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")

    ORDER_FEED_LIST = (By.CLASS_NAME, "OrderFeed_list__OLh59")
    ORDER_ITEMS = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")

    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")
    CLOSE_MODAL_BUTTON_OF_ORDER = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS")

    COMPLETED_ALL_TIME_TEXT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    COMPLETED_TODAY_TEXT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    WORK_IN_PROGRESS_TEXT = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")
    WORK_IN_PROGRESS_ORDER_NUMBER = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")

    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")






















