import time

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from assertionts import assert_text_in_actual_value
from data.data import url_order
from selenium import webdriver
from locators import popup_order_create, second_button_order, second_button_order_for_find
from pages.order_page import OrderScooterPage

class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        try:
            if cls.driver:
                cls.driver.quit()
        except Exception as e:
            print(f"Error closing driver: {e}")

    @pytest.fixture(scope='function')
    def open_main_page(self):
        self.driver.get(url_order)
        self.order_page = OrderScooterPage(self.driver)

    @allure.description("Тест заказа самоката с помощью первой кнопки заказа")
    def test_first_button(self, open_main_page):
        self.order_page.click_on_first_button_order()
        self.order_page.input_data_customer()

        actual_value = self.driver.find_element(*popup_order_create).text
        assert_text_in_actual_value(actual_value)

    @allure.description("Тест заказа самоката с помощью второй кнопки заказа")
    def test_second_button(self, open_main_page):
        # Клик по кнопке куки
        self.order_page.click_on_cookie()
        # Прокрутка до кнопки "Заказ"
        second_button = self.driver.find_element(*second_button_order)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", second_button)

        WebDriverWait(self.driver, 3).until(expected_conditions.
                                            element_to_be_clickable(second_button_order_for_find))

        # Клик по кнопке "Заказ"
        self.order_page.click_on_second_button_order()
        # Заполнение полей:
        self.order_page.input_data_customer()

        actual_value = self.driver.find_element(*popup_order_create).text
        assert_text_in_actual_value(actual_value)

