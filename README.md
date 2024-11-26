# Sprint_6
# Запуск тестов:
pytest test/ --alluredir=allure-results
pytest test/test_order_page.py::TestClickOnLogo::test_example --alluredir=allure-results

# Если тесты не запускаются на Windows через консоль:
$env:PYTHONPATH="."; pytest test/ --alluredir=allure-results -v

# Посмотреть результат в allure
allure serve allure_results

# Посмотреть allure отчет на windows
allure generate allure-results -o allure-report --clean
allure open allure-report

# data/data.py
Статические данные

# pages/main_page.py
Функции для управления главной страницей

# pages/order_page.py
Функции для управления страницей заказов

# test/test_order_page.py
Тесты, которые ведутся на странице заказа

# test/test_questions.py
Тесты, которые ведутся на главной странице

# helpers.py
Небольшие функции, которые помогают в тестах

# assertions.py
Небольшие функции, которые выполняют роль ассертов

# locators_for_order.py
Локаторы для страницы order

# locators_for_questions.py
Локаторы для блока с вопросами на главной странице

# requirements
Внешние зависимости
