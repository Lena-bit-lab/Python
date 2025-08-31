#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(options=options)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
#         # calc = Calculator(driver)
#         # calc.open_calculator()
#driver.quit()
#
#
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

    # def check_form_submission(self):
    #     self.open()
    #     self.input_field()
    #     self.input_symbols()
    #     self.check()


#
#         def test_slow_calculator():
#             driver = webdriver.Chrome()
#             driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#
#             text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
#             text_input.clear()
#             text_input.send_keys("45")
#
#             driver.find_element(By.XPATH, '//span[text()="7"]').click()
#             driver.find_element(By.XPATH, '//span[text()="+"]').click()
#             driver.find_element(By.XPATH, '//span[text()="8"]').click()
#             driver.find_element(By.XPATH, '//span[text()="="]').click()
#
#             WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
#
            #WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

            # res = driver.find_element(By.CSS_SELECTOR, ".screen").text
            # assert res == "15"
            #
            # driver.quit()