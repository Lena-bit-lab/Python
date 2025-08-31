import pytest
from selenium import webdriver
from FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.input_field()
    form_page.input_symbols()
    form_page.check()
