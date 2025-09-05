from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """Нажимаем кнопку checkout"""
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

    def fill_checkout_info(self, first_name="Елена", last_name="Жанкова", postal_code="111111"):
        """Заполняем информацию для checkout"""
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)

    def continue_checkout(self):
        """Продолжаем процесс checkout"""
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def get_total_amount(self):
        """Получаем итоговую сумму заказа"""
        total_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        # Извлекаем число из текста типа "Total: $58.29"
        total_value = float(total_text.split("$")[1])
        return total_value
