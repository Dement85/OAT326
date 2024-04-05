from selenium.webdriver.common.by import By

class SimpleForm:
    def __init__(self, driver):
        self.CLIENT_NAME = driver.find_element(By.CSS_SELECTOR, 'CLIENT_NAME')