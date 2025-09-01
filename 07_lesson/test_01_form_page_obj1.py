import pytest
from selenium import webdriver
from login_page import LoginPage
from product_page import ProductPage
from shopping_cart_page import ShoppingCartPage
from checkout_page import CheckoutPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total(browser):
    # Переходим на сайт
    browser.get("https://www.saucedemo.com")

    # Авторизуемся (логика авторизации уже в конструкторе LoginPage)
    LoginPage(browser)

    # Ждем загрузки страницы товаров (логика ожидания в конструкторе ProductPage)
    ProductPage(browser)

    # Добавляем товары в корзину (логика добавления в конструкторе ShoppingCartPage)
    ShoppingCartPage(browser)

    # Переходим к checkout
    checkout_page = CheckoutPage(browser)
    checkout_page.click_checkout()
    checkout_page.fill_checkout_info()
    checkout_page.continue_checkout()

    # Проверяем итоговую сумму
    total_amount = checkout_page.get_total_amount()
    assert total_amount == 58.29, f"Ожидалась сумма 58.29, получена {total_amount}"
