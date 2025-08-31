#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.username_field = driver.find_element(By.ID, "user-name")
        self.password_field = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "login-button")

        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("secret_sauce")
        self.login_button.click()

