#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        first_name_field = driver.find_element(By.ID, "first-name")
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys("Елена")
        last_name_field.send_keys("Жанкова")
        postal_code_field.send_keys("111111")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])

        assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, получена {total_cost_value}"

        driver.quit()


