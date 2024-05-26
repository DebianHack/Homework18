import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class GaragePage(BasePage):

    # Переход в профиль
    def click_profile_button(self):
        profile = self._driver.find_element(
            By.XPATH, "//nav[@class='sidebar d-flex flex-column']//div[@class='sidebar_btn-group']//a[@class='btn btn-white btn-sidebar sidebar_btn -profile']"
        ).click()

    # Проверка валидации данных
    def assert_profile(self, expected_profile):
        fullname = self._driver.find_element(
            By.XPATH, "//p[@class='profile_name display-4']"
        ).text
        assert fullname == expected_profile

    # Переход в гараж
    def click_garage_button(self):
        garage = self._driver.find_element(
            By.XPATH, "//nav[@class='sidebar d-flex flex-column']//a[@class='btn btn-white btn-sidebar sidebar_btn']"
        ).click()

    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-primary']"
        ).click()

    def assert_car_in_list(self, expected_car_title):
        car_title = self._driver.find_element(
            By.XPATH, "//li[@class='car-item']//p"
        ).text
        assert car_title == expected_car_title

    # Добавления топлива
    def click_add_expense_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='car_add-expense btn btn-success']"
        ).click()

    # Переход в настройки
    def click_settings_button(self):
        self._driver.find_element(
            By.XPATH, "//nav[@class='sidebar d-flex flex-column']//div[@class='sidebar_btn-group']//a[@class='btn btn-white btn-sidebar sidebar_btn']"
        ).click()
    # Клик на кнопку Удалить
    def click_delete_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='user-settings_item -form -remove-account']//button[@class='btn btn-danger-bg']"
        ).click()
    # Подтверждение удаления
    def click_delete_valid_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-danger']"
        ).click()

class AddCarModal(BasePage):
    def select_brand(self, car_brand_name: str):
        time.sleep(1)
        self._driver.find_element(By.XPATH, "//select[@id='addCarBrand']").send_keys(
            car_brand_name
        )

    def select_model(self, car_model_name: str):
        time.sleep(1)
        self._driver.find_element(By.XPATH, "//select[@id='addCarModel']").send_keys(
            car_model_name
        )

    def set_mileage(self, mileage: int):
        self._driver.find_element(By.XPATH, "//input[@id='addCarMileage']").send_keys(
            mileage
        )

    def click_add_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary']"
        ).click()

class AddExpense(BasePage):
    # Добавление литров
    def set_liters(self, liters: int):
        time.sleep(1)
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseLiters']").send_keys(
            liters
        )
    # Добавление цены за машину
    def set_cost(self, cost: int):
        time.sleep(1)
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseTotalCost']").send_keys(
            cost
        )

    def set_mileage(self, mileage_2: int):
        time.sleep(1)
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseMileage']").send_keys(
            mileage_2
        )
    # Добавить данные топлива и цены
    def click_add_expense_button(self):
        self._driver.find_element(
                By.XPATH, "//div[@class='modal-footer d-flex justify-content-end']//button[@class='btn btn-primary']"
            ).click()
    # Отмена введенных данных (в моем на всякий случай, поскольку не сразу могу угадать валидные данные)
    def click_add_expense_cancel_button(self):
        self._driver.find_element(
                By.XPATH, "//div[@class='modal-footer d-flex justify-content-end']//button[@class='btn btn-secondary']"
            ).click()
