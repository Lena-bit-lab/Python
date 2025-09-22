import pytest
from selenium import webdriver
from login_pageAllure import LoginPage
from product_pageAllure import ProductPage
from shopping_cart_pageAllure import ShoppingCartPage
from checkout_pageAllure import CheckoutPage
import allure

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Тестирование работы интернет-магазина")
@allure.description("Тест проверяет корректность работы интерет-магазина"
                    "с различными последовательными шагами")
@allure.feature("Сайт интернет-магазина")
@allure.severity(allure.severity_level.CRITICAL)

def test_checkout_total(browser):
    """
    Тест проверяет работу сайта интернет-магазина при выполнении последовательных операций.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """

    with allure.step("Открытие сайта"):
        browser.get("https://www.saucedemo.com")

    with allure.step("Авторизация"):
        LoginPage(browser)

    with allure.step("Ожидание загрузки страницы товаров"):
        ProductPage(browser)

    with allure.step("Добавление товаров в корзину"):
        ShoppingCartPage(browser)

    with allure.step("Переход и заполнение информации на странице Checkout"):
        checkout_page = CheckoutPage(browser)
        checkout_page.click_checkout()
        checkout_page.fill_checkout_info()
        checkout_page.continue_checkout()

    with allure.step("Проверка итоговой суммы"):
        total_amount = checkout_page.get_total_amount()
        assert total_amount == 58.29, f"Ожидалась сумма 58.29, получена {total_amount}"
