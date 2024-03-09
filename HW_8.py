from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount")
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()

# def test(driver):
#     customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))
#     customer_dropdown.select_by_visible_text("Ron Weasly")
#
#     selected_customer = customer_dropdown.first_selected_option.text
#     assert selected_customer == "Ron Weasly"  # опционально
#     driver.save_screenshot(f'customer_name_{selected_customer}.png')
#
# def test_select_currency(driver):
#     # Найти элемент листбокса "Customer" по XPath
#     customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))
#     # Выбрать опцию "Ron Weasly" # аналог element.click()
#     customer_dropdown.select_by_visible_text("Ron Weasly")
#
#     currency_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="currency"]'))
#     currency_dropdown.select_by_visible_text("Pound")
#
#     # Дополнительная проверка, что выбранное значение отображается корректно
#     selected_customer = customer_dropdown.first_selected_option.text
#     assert selected_customer == "Ron Weasly"
#
#     selected_currency = currency_dropdown.first_selected_option.text
#     assert selected_currency == "Pound"
#     driver.save_screenshot(f'customer_name_{selected_customer}/currency_{selected_currency}.png')

def test(driver):
    customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))
    customer_dropdown.select_by_visible_text("Albus Dumbledore")

    selected_customer = customer_dropdown.first_selected_option.text
    assert selected_customer == "Albus Dumbledore"  # опционально
    driver.save_screenshot(f'customer_name_{selected_customer}.png')

def test_select_currency(driver):
    # Найти элемент листбокса "Customer" по XPath
    customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))
        # Выбрать опцию "Ron Weasly" # аналог element.click()
    customer_dropdown.select_by_visible_text("Albus Dumbledore")

    currency_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="currency"]'))
    currency_dropdown.select_by_visible_text("Pound")

        # Дополнительная проверка, что выбранное значение отображается корректно
    selected_customer = customer_dropdown.first_selected_option.text
    assert selected_customer == "Albus Dumbledore"

    selected_currency = currency_dropdown.first_selected_option.text
    assert selected_currency == "Pound"
    driver.save_screenshot(f'customer_name_{selected_customer}/currency_{selected_currency}.png')

    button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
    button.click()

    button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
    button.click()

