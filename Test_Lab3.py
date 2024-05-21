import Lab3 #don't need as "xxx" since Lab3 is easy and fast to type

print("Test_Lab3")


def test_bubble_sort_ascending():
    #result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) #or (input_array, 0)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) #or (input_array, 1)

    assert (result == test_arr)

def test_bubble_sort_invalid1():
    result = ""
    input_arr = [64, 34, 25, 12, 22, 11, 90, 91, 92, 93]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 1)

def test_bubble_sort_invalid2():
    result = ""
    input_arr = []

    result = Lab3.bubble_sort(input_arr, 4)

    assert (result == 0)

def test_bubble_sort_invalid3():
    result = ""
    input_arr = [''] #variable in array is string aka not integer

    result = Lab3.bubble_sort(input_arr, 5)

    assert (result == 2)
