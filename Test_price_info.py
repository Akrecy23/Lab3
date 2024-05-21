import price_info

print ("Test_price_info")

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()

    assert (result == 46.75)


def test_cost_of_fruit():
    input_fruit = 'apple'
    input_quantity = 10

    result = price_info.cost_of_fruits(input_fruit, input_quantity)
    
    assert (result == 12)