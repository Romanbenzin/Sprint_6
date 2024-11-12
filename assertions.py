def assert_text_in_actual_value(actual):
    expected = "Заказ оформлен"
    assert expected in actual


def assert_expected_equal_actual(expected, actual):
    assert expected == actual
