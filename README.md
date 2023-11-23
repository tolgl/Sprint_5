# Автотесты для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
*В проекте использовался фреймворк Selenium и Pytest*

1. В файле conftest лежат фикстуры:
   - __email_generation__ - генерирует рандомную электронную почту*
   - __password_generation__ - генерирует рандомный пароль от 6 до 10 символов
   - __invalid_password_generation__ - генерирует невалидный пароль менее 6 символов
   - __name_generation__ - генерирует рандомное имя
   - __get_email__ - возвращает почту зарегистрированного пользователя
   - __get_password__ - возвращает пароль зарегистрированного пользователя
1. Файл test_registration содержит автотесты проверки регистрации:
   - __test_correct_data_successful_registration__ - проверяет успешную регистрацию
   - __test_incorrect_password_failed_registration__ - проверяет вывод ошибки регистрации из-за некорректного пароля
1. Файл test_login содержит автотесты проверки авторизации:
   - __test_login_by_button_in_main_successful_login__ - проверяет авторизацию через кнопку "Войти в аккаунт" на главной странице
   - __test_login_by_link_in_header_successful_login__ - проверяет авторизацию через ссылку "Личный кабинет" в "шапке" сайта
   - __test_login_by_link_on_form_registration_successful_login__ - проверяет авторизацию через форму регистрации
   - __test_login_by_link_on_form_password_recovery_successful_login__ - проверяет авторизацию через форму восстановления пароля
1. Файл test_open_personal_account содержит автотест перехода в ЛК:
   - __test_successful_redirection_to_personal_account__ - проверяет переход в ЛК после авторизации
1. Файл test_open_constructor_from_personal_account содержит автотесты перехода на главную страницу из ЛК:
   - __test_successful_redirection_to_constructor_from_personal_account__ - проверяет переход на главную из ЛК кликом по ссылке "Конструктор"
   - __test_successful_redirection_to_main_page_click_on_logo__ - проверяет переход на главную из ЛК кликом по логотипу
1. Файл test_logging_out содержит автотест разлогинивания:
   - __test_successful_logging_out__ - проверяет разлогинивание с сайта из ЛК кликом по кнопке "Выход"
1. Файл test_click_to_tab содержит автотесты перехода по табам на главной странице
   - __test_successful_switching_on_tab_stuffing__ - проверяет переход на таб "Начинки"
   - __test_successful_switching_on_tab_sauce__ - проверяет переход на таб "Соусы"
   - __test_successful_switching_on_tab_bread__ - проверяет, что при переходе на сайт, таб "Булки" по умолчанию активен