import time
import allure

from helpers import list_of_index, checkbox_return, random_intercom_key
from locators import field_name, field_last_name, field_addresses, field_metro_station, field_phone, button_next, \
    select_metro_station, field_scooter_arrive, field_data_picker, field_rent_period, select_rent_period, field_comment


class OrderScooterPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение поля: Имя")
    def set_name_first_page(self, name):
        self.driver.find_element(*field_name).send_keys(name)

    @allure.step("Заполнение поля: Фамилия")
    def set_last_name_first_page(self, last_name):
        self.driver.find_element(*field_last_name).send_keys(last_name)

    @allure.step("Заполнение поля: Адрес")
    def set_addresses_first_page(self, addresses):
        self.driver.find_element(*field_addresses).send_keys(addresses)

    @allure.step("Заполнение поля: Метр")
    def set_metro_station_first_page(self):
        self.driver.find_element(*field_metro_station).click()
        self.driver.find_element(*select_metro_station).click()

    @allure.step("Заполнение поля: Телефон")
    def set_phone_first_page(self, phone):
        self.driver.find_element(*field_phone).send_keys(phone)

    @allure.step("Нажатие на кнопку: Далее")
    def click_button(self):
        self.driver.find_element(*button_next).click()

    @allure.step("Заполнение поля: Когда привезти самокат")
    def when_arrive_scooter(self):
        self.driver.find_element(*field_scooter_arrive).click()
        self.driver.find_element(*field_data_picker).click()

    @allure.step("Заполнение поля: Срок аренды")
    def rental_period(self):
        self.driver.find_element(*field_rent_period).click()
        self.driver.find_elements(*select_rent_period)[list_of_index()].click()

    @allure.step("Выбор чекбокса: Цвет самоката")
    def random_scooter_color(self):
        self.driver.find_element(*checkbox_return()).click()

    @allure.step("Заполнение поля: Комментарий для курьера")
    def comment_for_courier(self):
        self.driver.find_element(*field_comment).send_keys(f"Код от домофона: {random_intercom_key()}")

    @allure.title("Тест заказа")
    def input_data_customer(self):
        self.set_name_first_page("Тестовое имя")
        self.set_last_name_first_page("ТестоваяФамилия")
        self.set_addresses_first_page("Тестовый адрес 1")
        self.set_phone_first_page("88005553535")
        self.set_metro_station_first_page()
        self.click_button()
        self.when_arrive_scooter()
        self.rental_period()
        self.random_scooter_color()
        self.comment_for_courier()
        time.sleep(2)
