import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def click_guest_login_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='header-link -guest']"
        ).click()

        # Кнопка регистрации на главной странице
    def click_registration_button_is_displayed(self):
        self._driver.find_element(
            By.XPATH, "//button [@class='hero-descriptor_btn btn btn-primary']"
        ).click()

class CreateUser(BasePage):
    def set_name(self, user_name: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupName']").send_keys(
            user_name
        )

    def set_lastname(self, user_lastname: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupLastName']").send_keys(
            user_lastname
        )

    def set_email(self, email: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupEmail']").send_keys(
            email
        )

    def set_password(self, password: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupPassword']").send_keys(
            password
        )

    def set_repassword(self, repassword: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupRepeatPassword']").send_keys(
            repassword
        )

    def click_add_user_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary']"
        ).click()
