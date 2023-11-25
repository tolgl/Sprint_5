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
    # получение атрибута таба "Начинки"
    attribute = driver.find_element(By.XPATH, ".//span[text() = 'Начинки']//parent::div").get_attribute('class')

    # проверяем что значение атрибута при активном табе есть в нажатом табе
    assert 'tab_tab_type_current__2BEPc' in attribute

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
    # получение атрибута таба "Соусы"
    attribute = driver.find_element(By.XPATH, ".//span[text() = 'Соусы']//parent::div").get_attribute('class')

    # проверяем что значение атрибута при активном табе есть в нажатом табе
    assert 'tab_tab_type_current__2BEPc' in attribute

    driver.quit()


def test_successful_switching_on_tab_bread():

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Ожидаем появления элемента с продуктами
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

    # получение атрибута таба "Булки"
    attribute = driver.find_element(By.XPATH, ".//span[text() = 'Булки']//parent::div").get_attribute('class')

    # проверяем что значение атрибута при активном табе есть в нажатом табе
    assert 'tab_tab_type_current__2BEPc' in attribute

    driver.quit()
