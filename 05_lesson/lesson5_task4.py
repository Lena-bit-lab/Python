from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/login")
input_field = driver.find_element(By.TAG_NAME, "input")


search_box = driver.find_element(By.NAME, "username")
search_box.send_keys('tomsmith')
search_box = driver.find_element(By.NAME, "password")
search_box.send_keys('SuperSecretPassword!')

driver.find_element(By.LINK_TEXT, "Login"). click()

print("fork_me_on_github")

driver.quit()
