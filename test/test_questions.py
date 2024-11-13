import allure
import pytest

from assertions import assert_expected_equal_actual
from data.data import URL_MAIN_PAGE, FIRST_ANSWER, SECOND_ANSWER, THIRD_ANSWER, \
    FOURTH_ANSWER, FIFTH_ANSWER, SIXTH_ANSWER, SEVENTH_ANSWER, EIGHTH_ANSWER
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
        self.driver.get(URL_MAIN_PAGE)
        self.order_page = MainPageQuestions(self.driver)

    @pytest.mark.parametrize("index, expected_text", [
        (0, FIRST_ANSWER),
        (1, SECOND_ANSWER),
        (2, THIRD_ANSWER),
        (3, FOURTH_ANSWER),
        (4, FIFTH_ANSWER),
        (5, SIXTH_ANSWER),
        (6, SEVENTH_ANSWER),
        (7, EIGHTH_ANSWER)
    ])
    @allure.title("Тест открытия вопросов и сверкой ответов на вопросы")
    def test_questions(self, open_main_page, index, expected_text):
        # Скролл до вопросов
        self.order_page.scroll_to_questions()
        # Прокликивание вопроса по индексу
        expected_value = self.order_page.click_on_question(index)
        assert_expected_equal_actual(expected_value, expected_text)
