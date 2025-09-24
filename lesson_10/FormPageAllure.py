from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

class FormPage:
    def __init__(self, driver):
        """
        Конструктор класса FormPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    @allure.step("Установка задержки в секундах")
    def input_field(self):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param self: int — время задержки в секундах.
        """
        number = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        number.clear()
        number.send_keys('45')

    @allure.step("Нажатие кнопки")
    def input_symbols(self):
        """
        Нажимает по очереди на кнопки калькулятора.
        :param self: str — текст на кнопке, которую нужно нажать.
        """
        button_seven = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_seven.click()

        button_plus = self.driver.find_element(By.CSS_SELECTOR,"span.operator.btn.btn-outline-success")
        button_plus.click()

        button_seven = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_seven.click()

        button_equal = self.driver.find_element(By.CSS_SELECTOR,"span.btn.btn-outline-warning")
        button_equal.click()

    @allure.step("Получение результата на экране калькулятора")
    def check(self):
        """
        Получает ожидаемый результат на экране калькулятора.
        :param self: str — ожидаемый результат.
        """
        assert self.driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"
