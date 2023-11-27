from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_redirection_to_constructor_from_personal_account(driver, get_email, get_password):

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(get_email)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(get_password)
    # Кнопка "Войти"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Оформить заказ']")))

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()

    # Ожидаем появления кнопки "Выход" в ЛК
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Выход']")))

    # Ссылка "Конструктор"
    driver.find_element(By.XPATH, ".//header//li[1]//a").click()

    # Ожидаем появления элемента с продуктами
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

    # Заголовок "Соберите бургер"
    element = driver.find_element(By.XPATH, ".//h1").text

    # проверяем что на странице появился заголовок "Соберите бургер"
    assert element == 'Соберите бургер'


def test_successful_redirection_to_main_page_click_on_logo(driver, get_email, get_password):

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(get_email)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(get_password)
    # Кнопка "Войти"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Оформить заказ']")))

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()

    # Ожидаем появления кнопки "Выход" в ЛК
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Выход']")))

    # Логотип Stellar Burgers
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()

    # Ожидаем появления элемента с продуктами
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

    # Заголовок "Соберите бургер"
    element = driver.find_element(By.XPATH, ".//h1").text

    # проверяем что на странице появился заголовок "Соберите бургер"
    assert element == 'Соберите бургер'
