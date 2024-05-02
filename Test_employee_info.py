import employee_info as ei

print ("Test_employee_info")

def test_get_employees_by_age_range():
    result = []
    input_lower_age = 0
    input_upper_age = 30

    result = ei.get_employees_by_age_range(input_lower_age, input_upper_age)

    assert (result == [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}])

def test_calculate_average_salary():

    result = ei.calculate_average_salary()

    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    input_department = "Sales"

    result = ei.get_employees_by_dept(input_department)

    assert (result == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000}, {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}])