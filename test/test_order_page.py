import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from assertions import assert_text_in_actual_value, assert_expected_equal_actual
from data.data import url_main_page, url_order_page, url_dzen_page
from selenium import webdriver
from locators_for_order import popup_order_create, second_button_order, second_button_order_for_find
from pages.order_page import OrderScooterPage

class TestOrderPage:

    driver = None

    @classmethod
    #@allure.step("Открытие браузера")
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    #@allure.step("Закрытие браузера")
    def teardown_class(cls):
        try:
            if cls.driver:
                cls.driver.quit()
        except Exception as e:
            print(f"Error closing driver: {e}")

    @pytest.fixture(scope='function')
    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.driver.get(url_main_page)
        self.order_page = OrderScooterPage(self.driver)

    @pytest.fixture(scope='function')
    @allure.step("Открытие страницы заказов")
    def open_order_page(self):
        self.driver.get(url_order_page)
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

        WebDriverWait(self.driver, 10).until(expected_conditions.
                                            element_to_be_clickable(second_button_order_for_find))

        # Клик по кнопке "Заказ"
        self.order_page.click_on_second_button_order()
        # Заполнение полей:
        self.order_page.input_data_customer()

        actual_value = self.driver.find_element(*popup_order_create).text
        assert_text_in_actual_value(actual_value)

class TestClickOnLogo:

    driver = None

    @classmethod
    #@allure.step("Открытие браузера")
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    #@allure.step("Закрытие браузера")
    def teardown_class(cls):
        try:
            if cls.driver:
                cls.driver.quit()
        except Exception as e:
            print(f"Error closing driver: {e}")

    @pytest.fixture(scope='function')
    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.driver.get(url_main_page)
        self.order_page = OrderScooterPage(self.driver)

    @pytest.fixture(scope='function')
    @allure.step("Открытие страницы заказов")
    def open_order_page(self):
        self.driver.get(url_order_page)
        self.order_page = OrderScooterPage(self.driver)

    @allure.description("Тест открытия главной через логотип Самоката")
    def test_scooter_logo(self, open_order_page):
        self.order_page.click_on_scooter_logo()
        current_url = self.driver.current_url

        assert_expected_equal_actual(url_main_page, current_url)

    @allure.description("Тест открытия Дзена через логотип Яндекса")
    def test_yandex_logo(self, open_order_page):
        self.order_page.click_on_yandex_logo()

        main_window = self.driver.current_window_handle
        # Ожидаем, что количество окон станет больше 1
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        # Находим идентификатор нового окна
        new_window = [window for window in self.driver.window_handles if window != main_window][0]
        # Переключаемся на новое окно и ждем
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 30).until(lambda driver: self.driver.current_url == url_dzen_page)

        current_url = self.driver.current_url

        assert_expected_equal_actual(url_dzen_page, current_url)
