from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_correct_data_successful_registration(name_generation, email_generation, password_generation):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Ссылка "Зарегистрироваться"
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    # Поле "Имя"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(name_generation)
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(email_generation)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(password_generation)
    # Кнопка "Зарегистрироваться"
    driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click()

    # Ожидаем появления кнопки "Войти"
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Войти']")))

    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email_generation)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(password_generation)
    # Кнопка "Войти"
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

    # Ожидаем появления кнопки "Оформить заказ" на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text() = 'Оформить заказ']")))

    # Получаем текст кнопки "Оформить заказ"
    element = driver.find_element(By.XPATH, ".//button[text() = 'Оформить заказ']").text
    # проверяем что появилась кнопка "Оформить заказ" на главной странице
    assert element == 'Оформить заказ'

    driver.quit()


def test_incorrect_password_failed_registration(name_generation, email_generation, invalid_password_generation):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Ссылка "Зарегистрироваться"
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    # Поле "Имя"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(name_generation)
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(email_generation)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(invalid_password_generation)
    # Кнопка "Зарегистрироваться"
    driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click()

    # Ожидаем появление ошибки под полем "Пароль"
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text() = 'Некорректный пароль']")))
    # Текст "Некорректный пароль"
    element = driver.find_element(By.XPATH, ".//p[text() = 'Некорректный пароль']").text

    assert element == 'Некорректный пароль'

    driver.quit()