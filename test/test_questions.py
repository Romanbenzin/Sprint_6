import allure
import pytest

from assertions import assert_expected_equal_actual
from data.data import FIRST_ANSWER, SECOND_ANSWER, THIRD_ANSWER, \
    FOURTH_ANSWER, FIFTH_ANSWER, SIXTH_ANSWER, SEVENTH_ANSWER, EIGHTH_ANSWER

@pytest.mark.usefixtures("open_main_page")
class TestOrderPage:

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
        order_page = open_main_page
        order_page.scroll_to_questions()
        # Прокликивание вопроса по индексу
        expected_value = order_page.click_on_question(index)
        assert_expected_equal_actual(expected_value, expected_text)
