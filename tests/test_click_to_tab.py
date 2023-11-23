from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_switching_on_tab_stuffing():

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ожидаем появления элемента с продуктами
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

    # Таб "Начинки"
    driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()

    # проверяем что появился заголовок "Начинки"
    assert driver.find_element(By.XPATH, ".//h2[text() = 'Начинки']").is_displayed()

    driver.quit()


def test_successful_switching_on_tab_sauce():

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ожидаем появления элемента с продуктами
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

    # Таб "Соусы"
    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click()

    # проверяем что появился заголовок "Соусы"
    assert driver.find_element(By.XPATH, ".//h2[text() = 'Соусы']").is_displayed()

    driver.quit()


def test_successful_switching_on_tab_bread():

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ожидаем появления элемента с продуктами
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

    # Таб "Начинки"
    driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()
    # Таб "Булки"
    driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click()
    
    # проверяем что появился заголовок "Булки"
    assert driver.find_element(By.XPATH, ".//h2[text() = 'Булки']").is_displayed()

    driver.quit()
