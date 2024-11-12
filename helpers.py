import random
from datetime import date

def list_of_index():
    return random.randint(0, 6)

def date_today():
    return date.today().day

def checkbox_return():
    # импорт вынесен в функцию для избежания кругового импорта
    from locators import select_black_checkbox, select_grey_checkbox
    if int(date.today().day) % 2 == 0:
        return select_black_checkbox
    else:
        return select_grey_checkbox

def random_intercom_key():
    return random.randint(100000, 999999)