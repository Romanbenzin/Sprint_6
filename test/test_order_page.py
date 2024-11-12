from data.data import url_order
from selenium import webdriver
from locators import text_on_second_page
from pages.order_page import OrderScooterPage

class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        #cls.driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_input_first_page(self):
        self.driver.get(url_order)
        order_page = OrderScooterPage(self.driver)

        order_page.input_data_customer()

        assert self.driver.find_element(*text_on_second_page).text == 'Про аренду'
