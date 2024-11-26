import allure

from locators_for_order import cookie_button, scooter_logo, yandex_logo

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по кнопке куки")
    def click_on_cookie(self):
        self.driver.find_element(*cookie_button).click()

    @allure.step("Клик по лого Самокат")
    def click_on_scooter_logo(self):
        self.driver.find_element(*scooter_logo).click()

    @allure.step("Клик по лого Яндекс")
    def click_on_yandex_logo(self):
        self.driver.find_element(*yandex_logo).click()
