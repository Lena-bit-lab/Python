from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        backpack_add_button = driver.find_element(By.XPATH,
                                                  "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
        tshirt_add_button = driver.find_element(By.XPATH,
                                                "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
        onesie_add_button = driver.find_element(By.XPATH,
                                                "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button")

        backpack_add_button.click()
        tshirt_add_button.click()
        onesie_add_button.click()

        cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
