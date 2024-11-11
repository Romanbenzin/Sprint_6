from selenium.webdriver.common.by import By

# orders page:
field_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
field_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
field_addresses = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
field_metro_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
field_phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]