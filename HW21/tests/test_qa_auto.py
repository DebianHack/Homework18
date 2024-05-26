import time

from page_objects.garage_page import GaragePage, AddCarModal, AddExpense
from page_objects.home_page import HomePage, CreateUser


# Тест на добавление пользователя, машины, топлива, валидации и удаления
def test_registration_validation_car_expense_user(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_registration_button_is_displayed()

    # Ввод данных пользователя
    add_user = CreateUser(driver)

    user_name = "John"
    user_lastname = "Doe"
    email = "johndoe@example.com"
    password = "Sherlock2018"

    add_user.set_name(user_name)
    add_user.set_lastname(user_lastname)
    add_user.set_email(email)
    add_user.set_password(password)
    add_user.set_repassword(password)
    time.sleep(5)

    # Добавление пользователя
    add_user.click_add_user_button()
    time.sleep(5)

    # Переход в гараж
    garage_page = GaragePage(driver)

    # Переход в профиль
    garage_page.click_profile_button()
    time.sleep(5)

    # Проверка валидации данных пользователя
    garage_page.assert_profile(f"{user_name} {user_lastname}")
    time.sleep(5)

    # Переход в гараж
    garage_page.click_garage_button()

    time.sleep(5)
    # Добавить машину
    garage_page.click_add_car_button()

    time.sleep(5)

    add_car_modal = AddCarModal(driver)

    car_brand_name = "BMW"
    car_model_name = "X5"

    add_car_modal.select_brand(car_brand_name)
    add_car_modal.select_model(car_model_name)
    add_car_modal.set_mileage(5)
    add_car_modal.click_add_button()

    time.sleep(5)
    # Проверка валидации машины
    garage_page.assert_car_in_list(f"{car_brand_name} {car_model_name}")
    time.sleep(5)
    # Добавить топливо
    garage_page.click_add_expense_button()
    time.sleep(5)
    # Ввод данных по топливу
    add_expense = AddExpense(driver)

    liters = 10
    cost = 200

    add_expense.set_liters(liters)
    add_expense.set_cost(cost)

    time.sleep(5)

    # Поставил её в комментарии, поскольку показывает неправильные данные,
    # во время тестирования, суть в том, что когда при добавлении топлива, милли машины, почему то не определяются
    # нужным образом и приходится вводить данные миль заново, а я не знаю как очистить строку от предыдущего значения
    # поскольку новые данные накладываются на старые, потому я и взял такие маленькие данные.
    # Прошу вас рассказать про то, как можно было правильно это сделать, буду благодарен
    # И на всякий случай, сделал кнопку для отмена введенных данных.
    # В общем простите за такое, считайте что нашёл баг (во время прохода теста, вы поймёте о чем я рассказал)

    add_expense.click_add_expense_button()
    time.sleep(5)

    mileage_2 = 5
    liters_2 = 10

    add_expense.set_mileage(mileage_2)
    add_expense.set_liters(liters_2)

    time.sleep(5)

    add_expense.click_add_expense_button()

    # add_expense.click_add_expense_cancel_button()

    time.sleep(5)
    # Переход в настройки
    garage_page.click_settings_button()
    time.sleep(5)
    # Клик по кнопке удаления
    garage_page.click_delete_button()
    time.sleep(5)
    # Подтверждение удаления
    garage_page.click_delete_valid_button()
    time.sleep(5)


