from selenium.webdriver.common.by import By
import allure


class LoginPage:
    @allure.step("Регистрация на странице")
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.username_field = driver.find_element(By.ID, "user-name")
        self.password_field = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "login-button")

        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("secret_sauce")
        self.login_button.click()
