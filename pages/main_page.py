import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators_for_order import first_button_order, second_button_order
from locators_for_questions import first_question, question, answer
from pages.base_page import BasePage


class MainPageQuestions(BasePage):

    @allure.step("Скролл до вопросов")
    def scroll_to_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(first_question))

    @allure.step("Клик по вопросу и возвращает ответ на вопрос")
    def click_on_question(self, index):
        #Клик по каждому вопросу
        self.driver.find_elements(*question)[index].click()
        # Возвращает значение ответа
        return self.driver.find_elements(*answer)[index].text

    @allure.title("Переход на страницу заказа с помощью верхней кнопки")
    def click_on_first_button_order(self):
        self.driver.find_element(*first_button_order).click()

    @allure.title("Переход на страницу заказа с помощью нижней кнопки")
    def click_on_second_button_order(self):
        self.driver.find_element(*second_button_order).click()
