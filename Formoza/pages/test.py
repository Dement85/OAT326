from pages.Simple_Form_3 import SimpleForm
#from config import driver, base_url
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    base_url = 'https://forsib.ru/contacts/'
    # Перейти на указанную страницу
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

import time
# это тест
@pytest.mark.parametrize('CLIENT_NAME', [('Dmitriy')])
def test_Simple_Form_3(driver, CLIENT_NAME):

    # находим все элементы для заполнения
    Simple_Form_3 = SimpleForm(driver) # driver - фикстура

    #  заполняем
    Simple_Form_3.simple(CLIENT_NAME) # username - параметр передается
    time.sleep(5)
    # проверка на успешную авторизации