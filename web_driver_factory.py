from selenium import webdriver


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Неизвестный браузер: {browser_name}. Доступны: Chrome, Firefox.")
