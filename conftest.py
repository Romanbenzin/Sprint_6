import allure
import pytest
from selenium import webdriver

from data.data import URL_MAIN_PAGE, URL_ORDER_PAGE
from pages.main_page import MainPageQuestions
from pages.order_page import OrderScooterPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver

    #Закрыть браузер:
    try:
        if driver:
            driver.quit()
    except Exception as e:
        print(f"Error closing driver: {e}")

@pytest.fixture()
@allure.step("Открытие главной страницы")
def open_main_page(driver):
    driver.get(URL_MAIN_PAGE)
    return MainPageQuestions(driver)

@pytest.fixture()
@allure.step("Открытие страницы заказов")
def open_order_page(driver):
    driver.get(URL_ORDER_PAGE)
    return OrderScooterPage(driver)
