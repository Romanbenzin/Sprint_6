import time

import allure
from selenium.webdriver.common.by import By

from helpers import list_of_index, checkbox_return, random_intercom_key
from locators import field_name, field_last_name, field_addresses, field_metro_station, field_phone, button_next, \
    select_metro_station, field_scooter_arrive, field_data_picker, field_rent_period, select_rent_period, field_comment, \
    button_order, popup_button, first_button_order, second_button_order, cookie_button, scooter_logo, yandex_logo
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

    @allure.step("Клик по вопросу")
    def click_first_question(self, index):
        #Клик по каждому вопросу
        self.driver.find_elements(*question)[index].click()
