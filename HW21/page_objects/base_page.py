from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver
