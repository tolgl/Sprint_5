from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_by_button_in_main_successful_login(driver, get_email, get_password):

    # Кнопка "Войти в аккаунт"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(get_email)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(get_password)
    # Кнопка "Войти"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Оформить заказ']")))

    # Получаем текст кнопки "Оформить заказ"
    element = driver.find_element(By.XPATH, ".//button[text() = 'Оформить заказ']").text

    # проверяем что появилась кнопка "Оформить заказ" на главной странице
    assert element == 'Оформить заказ'


def test_login_by_link_in_header_successful_login(driver, get_email, get_password):

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

    # Получаем текст кнопки "Оформить заказ"
    element = driver.find_element(By.XPATH, ".//button[text() = 'Оформить заказ']").text

    # проверяем что появилась кнопка "Оформить заказ" на главной странице
    assert element == 'Оформить заказ'


def test_login_by_link_on_form_registration_successful_login(driver, get_email, get_password):

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Ссылка "Зарегистрироваться"
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    # Ссылка "Войти"
    driver.find_element(By.LINK_TEXT, "Войти").click()
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(get_email)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(get_password)
    # Кнопка "Войти"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Оформить заказ']")))

    # Получаем текст кнопки "Оформить заказ"
    element = driver.find_element(By.XPATH, ".//button[text() = 'Оформить заказ']").text

    # проверяем что появилась кнопка "Оформить заказ" на главной странице
    assert element == 'Оформить заказ'


def test_login_by_link_on_form_password_recovery_successful_login(driver, get_email, get_password):

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Ссылка "Восстановить пароль"
    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
    # Ссылка "Войти"
    driver.find_element(By.LINK_TEXT, "Войти").click()
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(get_email)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(get_password)
    # Кнопка "Войти"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Оформить заказ']")))

    # Получаем текст кнопки "Оформить заказ"
    element = driver.find_element(By.XPATH, ".//button[text() = 'Оформить заказ']").text

    # проверяем что появилась кнопка "Оформить заказ" на главной странице
    assert element == 'Оформить заказ'
