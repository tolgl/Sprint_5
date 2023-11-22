from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_logging_out(email, password):

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ссылка "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    # Поле "Email"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email)
    # Поле "Пароль"
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(password)
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

    # Кнопка "Выход"
    driver.find_element(By.XPATH, ".//button[text() = 'Выход']").click()

    # Ожидаем появления формы авторизации
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_form__3qKeq")))

    # Заголовок "Вход"
    element = driver.find_element(By.XPATH, ".//h2[text() = 'Вход']").text

    # проверяем что на странице появился заголовок "Вход"
    assert element == 'Вход'

    driver.quit()


test_successful_logging_out('testglinkin1997123@ya.ru', '123456')
