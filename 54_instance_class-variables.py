class Employee:
    emp_numbers = 54
    pass


anshul = Employee()

anshul.name = "Anshul"
anshul.addr = "Baran"

print(f"1. {Employee.emp_numbers}")
Employee.emp_numbers = 67
print(f"2. {Employee.emp_numbers}")

anshul.emp_numbers = 77
print(f"3. {Employee.emp_numbers}")
print(f"4. {anshul.emp_numbers}")
