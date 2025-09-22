import pytest
from selenium import webdriver
from FormPageAllure import FormPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора: {num1} {operation} {num2} "
              "= {expected_result}")
@allure.description("Тест проверяет корректность работу калькулятора "
                    "с различными операциями.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)

def test_form_submission(driver):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param num1: str — первое число для операции.
    :param operation: str — операция (+, -, x, ÷).
    :param num2: str — второе число для операции.
    :param expected_result: str — ожидаемый результат операции.
    :param delay: int — задержка в секундах для выполнения операции.
    """
    form_page = FormPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        form_page.open()

    with allure.step(f"Нажатие кнопки"):
        form_page.input_field()

    with allure.step(f"Нажатие кнопки со значениями"):
           form_page.input_symbols()

    with allure.step(f"Проверка результата"):
        form_page.check()
