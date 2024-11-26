from selenium.webdriver.common.by import By
from helpers import date_today

# main page:
first_button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
second_button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
second_button_order_for_find = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
cookie_button = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"]
scooter_logo = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
yandex_logo = [By.XPATH, ".//img[@src='/assets/ya.svg']"]

# dzen_page
dzen_news = (By.XPATH, ".//button[@class='arrow__button']")

# first order page:
field_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
field_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
field_addresses = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
field_metro_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
select_metro_station = [By.XPATH, "//div[@class='select-search__select']//div[2]"]
field_phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
button_next = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

# second order page
text_on_second_page = [By.XPATH, ".//div[@class='Order_Header__BZXOb' and text()='Про аренду']"]
field_scooter_arrive = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
field_data_picker = [By.XPATH, f".//div[text()='{date_today()}']"]
field_rent_period = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]
select_rent_period = [By.CSS_SELECTOR, ".Dropdown-menu .Dropdown-option"]
select_black_checkbox = [By.XPATH, ".//label[@for='black']"]
select_grey_checkbox = [By.XPATH, ".//label[@for='grey']"]
field_comment = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

# popup window
popup_window = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"]
popup_button = [By.XPATH, ".//button[text()='Да']"]
popup_order_create = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]


