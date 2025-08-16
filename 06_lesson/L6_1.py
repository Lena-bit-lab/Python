from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

button2 = driver.find_element(By.ID, "content")

print(button2)

driver.quit()
