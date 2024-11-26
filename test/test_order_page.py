import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from assertions import assert_text_in_actual_value, assert_expected_equal_actual
from data.data import URL_MAIN_PAGE, URL_DZEN_PAGE
from locators_for_order import popup_order_create, second_button_order, second_button_order_for_find

@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("open_main_page")
class TestOrderPage:

    driver = None

    @allure.description("Тест заказа самоката с помощью первой кнопки заказа")
    def test_first_button(self, driver, open_main_page, open_order_page):
        main_page = open_main_page
        order_page = open_order_page
        main_page.click_on_first_button_order()
        order_page.input_data_customer()

        actual_value = driver.find_element(*popup_order_create).text
        assert_text_in_actual_value(actual_value)

    @allure.description("Тест заказа самоката с помощью второй кнопки заказа")
    def test_second_button(self, driver, open_main_page, open_order_page):
        main_page = open_main_page
        order_page = open_order_page
        # Клик по кнопке куки
        main_page.click_on_cookie()
        # Прокрутка до кнопки "Заказ"
        second_button = driver.find_element(*second_button_order)
        driver.execute_script("arguments[0].scrollIntoView(true);", second_button)

        WebDriverWait(driver, 10).until(expected_conditions.
                                            element_to_be_clickable(second_button_order_for_find))

        # Клик по кнопке "Заказ"
        main_page.click_on_second_button_order()
        # Заполнение полей:
        order_page.input_data_customer()

        actual_value = driver.find_element(*popup_order_create).text
        assert_text_in_actual_value(actual_value)

class TestClickOnLogo:

    driver = None

    @allure.description("Тест открытия главной через логотип Самоката")
    def test_scooter_logo(self, driver, open_order_page):
        order_page = open_order_page
        order_page.click_on_scooter_logo()
        current_url = driver.current_url

        assert_expected_equal_actual(URL_MAIN_PAGE, current_url)

    @allure.description("Тест открытия Дзена через логотип Яндекса")
    def test_yandex_logo(self, driver, open_order_page):
        order_page = open_order_page
        order_page.click_on_yandex_logo()

        main_window = driver.current_window_handle
        # Ожидаем, что количество окон станет больше 1
        WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        # Находим идентификатор нового окна
        new_window = [window for window in driver.window_handles if window != main_window][0]
        # Переключаемся на новое окно и ждем
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 30).until(lambda driver_func: driver.current_url == URL_DZEN_PAGE)

        current_url = driver.current_url

        assert_expected_equal_actual(URL_DZEN_PAGE, current_url)
