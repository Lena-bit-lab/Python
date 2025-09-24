from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ProductPage:
    @allure.step("Загрузка страницы с товарами с задержкой до появления всех товаров")
    def __init__(self, driver):
        """
        Конструктор класса ProductPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
