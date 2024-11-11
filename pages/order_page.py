import time

from locators import field_name, field_last_name, field_addresses, field_metro_station, field_phone


class OrderScooterPage:

    def __init__(self, driver):
        self.driver = driver
    #Метод заполняет поле "имя"
    def set_name(self, name):
        self.driver.find_element(*field_name).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*field_last_name).send_keys(last_name)

    def set_addresses(self, addresses):
        self.driver.find_element(*field_addresses).send_keys(addresses)

    def set_metro_station(self):
        self.driver.find_element(*field_metro_station).click()

    def set_phone(self, phone):
        self.driver.find_element(*field_phone).send_keys(phone)

    def input_data_customer(self):
        self.set_name("Тестовое имя")
        self.set_last_name("ТестоваяФамилия")
        self.set_addresses("Тестовый адрес 1")
        self.set_phone("88005553535")
        self.set_metro_station()
        time.sleep(2)
