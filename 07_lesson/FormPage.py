from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(options=options)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    def input_field(self):
        number = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        number.clear()
        number.send_keys('45')


    def input_symbols(self):
        button_seven = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_seven.click()


        button_plus = self.driver.find_element(By.CSS_SELECTOR,"span.operator.btn.btn-outline-success")
        button_plus.click()


        button_eight = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_eight.click()


        button_equal = self.driver.find_element(By.CSS_SELECTOR,"span.btn.btn-outline-warning")
        button_equal.click()


    def check(self):
            assert self.driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"
