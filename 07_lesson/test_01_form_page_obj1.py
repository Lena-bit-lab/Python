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
    # product_page.add_item_to_cart("sauce-labs-backpack")
    # product_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    # product_page.add_item_to_cart("sauce-labs-onesie")
    # product_page.navigate_to_cart()

    shopping_cart_page = ShoppingCartPage(browser)
    #shopping_cart_page.click_checkout_button()

    checkout_page = CheckoutPage(browser)
    # checkout_page.input_first_name("Елена")
    # checkout_page.input_last_name("Жанкова")
    # checkout_page.input_zip_code("111111")
    # checkout_page.complete_order()

    assert checkout_page.get_total_amount() == 58.29
