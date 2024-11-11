import time

from selenium import webdriver
from pages.order_page import OrderScooterPage

class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()

    def test_input_name(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        order_page = OrderScooterPage(self.driver)

        order_page.input_data_customer()

