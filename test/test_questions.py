import allure
import pytest

from assertions import assert_expected_equal_actual
from data.data import url_main_page, first_answer, second_answer, third_answer, \
    fourth_answer, fifth_answer, sixth_answer, seventh_answer, eighth_answer
from selenium import webdriver
from pages.main_page import MainPageQuestions

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
        self.order_page = MainPageQuestions(self.driver)

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
    @allure.title("Тест открытия вопросов и сверкой ответов на вопросы")
    def test_questions(self, open_main_page, index, expected_text):
        # Скролл до вопросов
        self.order_page.scroll_to_questions()
        # Прокликивание вопроса по индексу
        expected_value = self.order_page.click_on_question(index)
        assert_expected_equal_actual(expected_value, expected_text)
