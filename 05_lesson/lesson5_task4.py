from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/login")
input_field = driver.find_element(By.TAG_NAME, "input")


input_field.send_keys('tomsmith')
input_field.send_keys('SuperSecretPassword!')
button = driver.find_element(By.CSS_SELECTOR, "Login")
button.click()

print("fork_me_on_github")

driver.quit()
