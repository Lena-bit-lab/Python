from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

#input_field = driver.find_element(By.TAG_NAME, 'input')

input = driver.find_element(By.ID, 'newButtonName')
input.send_keys('SkyPro')

#WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.ID, 'newButtonName'), 'SkyPro'))

button = driver.find_element(By.ID, 'updatingButton')
button.click()

WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro'))

txt = driver.find_element(By.ID, 'updatingButton')
print(txt)

driver.quit()
