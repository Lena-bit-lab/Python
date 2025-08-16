from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro'))


input_field = driver.find_element(By.TAG_NAME, 'input')

search_box = driver.find_element(By.ID, 'newButtonName')
search_box.send_keys('SkyPro')


button = driver.find_element(By.ID, 'updatingButton')
button.click()

print(button.text)

driver.quit()

