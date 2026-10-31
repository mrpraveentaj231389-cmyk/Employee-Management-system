from main import Employee

def test_employee_name():
    emp = Employee(
        1,
        "rahul kumar",
        25,
        "IT",
        50000,
        ["Python"]
    )

    assert emp.name == "Rahul Kumar"