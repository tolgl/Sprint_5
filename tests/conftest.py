import pytest
import random
import string


@pytest.fixture()
def email_generation():
    domain = ['ya.ru', 'gmail.com', 'bk.ru']
    random_login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
    random_domain = random.choice(domain)
    email = f'{random_login}@{random_domain}'

    return email


@pytest.fixture()
def password_generation():
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))

    return password


@pytest.fixture()
def invalid_password_generation():
    invalid_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 5)))

    return invalid_password


@pytest.fixture()
def name_generation():
    name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))

    return name

@pytest.fixture()
def get_email():
    email = 'testglinkin1997123@ya.ru'

    return email

@pytest.fixture()
def get_password():
    password = '123456'

    return password