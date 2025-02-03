from prices import price_updater

def test_price_updater_common_case():
    # arrange the test
    price_list = [1.2, 3.1, 9.7]
    increase_rate = 0.5
    expected_value = [1.8, 4.65, 14.55]

    # act - imputting the code we want to test
    result = price_updater(price_list, increase_rate)

    # assert - checking it behaves the way we want
    assert expected_value == result


test_price_updater_common_case()