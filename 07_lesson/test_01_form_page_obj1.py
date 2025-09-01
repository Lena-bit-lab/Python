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
    browser.get("https://www.saucedemo.com")

    login_page = LoginPage(browser)


    product_page = ProductPage(browser)


    shopping_cart_page = ShoppingCartPage(browser)


    checkout_page = CheckoutPage(browser)

    assert checkout_page.get_total_amount() == 58.29
