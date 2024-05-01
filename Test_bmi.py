import Lab2.bmi as bmi

print ("Test_Lab2")

def test_bmi_normal_weight():
    input_height = 1.73
    input_weight = 57
    test_output = 0

    bmi_val = bmi.calculate_bmi(input_height, input_weight)

    assert (bmi_val == test_output)

def test_bmi_over_weight():
    input_height = 1
    input_weight = 57
    test_output = 1

    bmi_val = bmi.calculate_bmi(input_height, input_weight)

    assert (bmi_val == test_output)

def test_bmi_under_weight():
    input_height = 2
    input_weight = 57
    test_output = -1

    bmi_val = bmi.calculate_bmi(input_height, input_weight)

    assert (bmi_val == test_output)