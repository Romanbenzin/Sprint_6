from selenium.webdriver.common.by import By

field_questions = [By.XPATH, ".//div[text()='Вопросы о важном']"]
first_question = (By.XPATH, ".//div[@id='accordion__heading-0']")
question = [By.XPATH, ".//div[@class='accordion__item']"]
answer = [By.XPATH, ".//div[@class='accordion__panel']/*"]