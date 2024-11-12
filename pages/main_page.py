import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators_for_questions import first_question, question, field_questions, answer


class MainPageQuestions:

    def __init__(self, driver):
        self.driver = driver

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
