import time

import allure
import pytest


from assertionts import assert_text_in_actual_value, assert_expected_equal_actual
from data.data import url_main_page, url_order_page, url_dzen_page, first_answer, second_answer, third_answer, \
    fourth_answer, fifth_answer, sixth_answer, seventh_answer, eighth_answer
from selenium import webdriver
from locators import popup_order_create, second_button_order, second_button_order_for_find, dzen_news
from locators_for_questions import question, field_questions
from pages.main_page import MainPageQuestions
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
        self.driver.get(url_main_page)
        self.order_page = MainPageQuestions(self.driver)

    @allure.description("Тест открытия вопросов")
    @pytest.mark.parametrize("index, expected_text", [
        (0, first_answer),
        (1, second_answer),
        (2, third_answer),
        (3, fourth_answer),
        (4, fifth_answer),
        (5, sixth_answer),
        (6, seventh_answer),
        (7, eighth_answer)
    ])
    def test_questions(self, open_main_page, index, expected_text):
        # Скролл до вопросов
        self.order_page.scroll_to_questions()
        # Прокликивание вопроса по индексу
        self.order_page.click_first_question(index)

        #assert_expected_equal_actual(expected_value, expected_text)
        time.sleep(2)


