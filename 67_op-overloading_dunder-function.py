class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def details(self):
        return f"Employee name is {self.name}, role if {self.role}, and salary is {self.salary}"

    # dunder functions and operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    # dunder functions
    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee({self.name}, {self.salary}, {self.role})"

    def __str__(self):
        return f"Employee({self.name}, {self.salary}, and role is {self.role})"


emp1 = Employee("Anshul", 5000, "Programmer")
emp2 = Employee("Harshit", 6000, "Manager")

print(emp1 + emp2)
print(emp1 / emp1)
print(repr(emp1))
print(emp1)
print(str(emp1))
