# #from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def run_test():
#     # Инициализируем драйвер браузера (используется Chrome)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com")
#
#     try:
#         # Страница авторизации
#         login_page = LoginPage(driver)
#         login_page.enter_username("standard_user")
#         login_page.enter_password("secret_sauce")
#         login_page.click_login_button()
#
#         # Главная страница магазина
#         product_page = ProductPage(driver)
#         product_page.add_item_to_cart("sauce-labs-backpack")
#         product_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
#         product_page.add_item_to_cart("sauce-labs-onesie")
#         product_page.navigate_to_cart()
#
#         # Корзина
#         shopping_cart_page = ShoppingCartPage(driver)
#         shopping_cart_page.click_checkout_button()
#
#         # Оформление заказа
#         checkout_page = CheckoutPage(driver)
#         checkout_page.input_first_name("Иван")
#         checkout_page.input_last_name("Иванов")
#         checkout_page.input_zip_code("12345")
#         checkout_page.complete_order()
#
#         # Проверка итоговой суммы
#         final_total = checkout_page.get_total_amount()
#         assert round(final_total, 2) == 58.29, f"Тест провален! Ожидаемая итоговая сумма: $58.29, фактическая: ${final_total}"
#         print(f"Успешная проверка итоговой суммы: ${final_total}")
#
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#
#     finally:
#         # Закрываем браузер
#         driver.quit()
#
# run_test()
#
#             from selenium import webdriver
#             from selenium.webdriver.common.by import By
#             from selenium.webdriver.support.ui import WebDriverWait
#             from selenium.webdriver.support import expected_conditions as EC
#
#             def test_purchase():
#                 driver = webdriver.Firefox()
#                 driver.get("https://www.saucedemo.com/")
#
#                 # Авторизация
#                 username_field = driver.find_element(By.ID, "user-name")
#                 password_field = driver.find_element(By.ID, "password")
#                 login_button = driver.find_element(By.ID, "login-button")
#
#                 username_field.send_keys("standard_user")
#                 password_field.send_keys("secret_sauce")
#                 login_button.click()
#
#                 # Ожидание загрузки страницы с товарами
#                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
#
#                 # Добавление товаров в корзину
#                 backpack_add_button = driver.find_element(By.XPATH,
#                                                           "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
#                 tshirt_add_button = driver.find_element(By.XPATH,
#                                                         "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
#                 onesie_add_button = driver.find_element(By.XPATH,
#                                                         "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button")
#
#                 backpack_add_button.click()
#                 tshirt_add_button.click()
#                 onesie_add_button.click()
#
#                 # Переходим в корзину
#                 cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
#                 cart_link.click()
#
#                 # Нажимаем Checkout
#                 checkout_button = driver.find_element(By.ID, "checkout")
#                 checkout_button.click()
#
#                 # Заполнение формы вашими данными
#                 first_name_field = driver.find_element(By.ID, "first-name")
#                 last_name_field = driver.find_element(By.ID, "last-name")
#                 postal_code_field = driver.find_element(By.ID, "postal-code")
#
#                 first_name_field.send_keys("Елена")
#                 last_name_field.send_keys("Жанкова")
#                 postal_code_field.send_keys("111111")
#
#                 continue_button = driver.find_element(By.ID, "continue")
#                 continue_button.click()
#
#                 # Чтение итоговой стоимости
#                 total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
#                 total_cost_value = float(total_cost.split("$")[1])
#
#                 # Проверка итоговой суммы
#                 assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, получена {total_cost_value}"
#
#                 driver.quit()
