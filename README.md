# Автотесты для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
<!-- В проекте использовался фреймворк Selenium и Pytest -->

1. В файле conftest лежат фикстуры:
   - email_generation <!-- генерирует рандомную электронную почту -->
   - password_generation <!-- генерирует рандомный пароль от 6 до 10 символов -->
   - invalid_password_generation <!-- генерирует невалидный пароль менее 6 символов -->
   - name_generation <!-- генерирует рандомное имя -->
   - get_email <!-- возвращает почту зарегистрированного пользователя -->
   - get_password <!-- возвращает пароль зарегистрированного пользователя -->
1. Файл test_registration содержит автотесты проверки регистрации:
   - test_correct_data_successful_registration <!-- проверяет успешную регистрацию -->
   - test_incorrect_password_failed_registration <!-- проверяет вывод ошибки регистрации из-за некорректного пароля -->
1. Файл test_login содержит автотесты проверки авторизации:
   - test_login_by_button_in_main_successful_login <!-- проверяет авторизацию через кнопку "Войти в аккаунт" на главной странице -->
   - test_login_by_link_in_header_successful_login <!-- проверяет авторизацию через ссылку "Личный кабинет" в "шапке" сайта -->
   - test_login_by_link_on_form_registration_successful_login <!-- проверяет авторизацию через форму регистрации -->
   - test_login_by_link_on_form_password_recovery_successful_login <!-- проверяет авторизацию через форму восстановления пароля -->
1. Файл test_open_personal_account содержит автотест перехода в ЛК:
   - test_successful_redirection_to_personal_account <!-- проверяет переход в ЛК после авторизации -->
1. Файл test_open_constructor_from_personal_account содержит автотесты перехода на главную страницу из ЛК:
   - test_successful_redirection_to_constructor_from_personal_account <!-- проверяет переход на главную из ЛК кликом по ссылке "Конструктор" -->
   - test_successful_redirection_to_main_page_click_on_logo <!-- проверяет переход на главную из ЛК кликом по логотипу -->
1. Файл test_logging_out содержит автотест разлогинивания:
   - test_successful_logging_out <!-- проверяет разлогинивание с сайта из ЛК кликом по кнопке "Выход" -->
1. Файл test_click_to_tab содержит автотесты перехода по табам на главной странице
   - test_successful_switching_on_tab_stuffing <!-- проверяет переход на таб "Начинки" -->
   - test_successful_switching_on_tab_sauce <!-- проверяет переход на таб "Соусы" -->
   - test_successful_switching_on_tab_bread <!-- проверяет, что при переходе на сайт, таб "Булки" по умолчанию активен -->