# config.py - содержит все необходимые настройки для тестирования
from selenium import webdriver


driver = webdriver.Chrome()
base_url = 'https://forsib.ru/contacts/'
# хранит адреса страниц
# перенаправляться на эти страницы
# и т.д.