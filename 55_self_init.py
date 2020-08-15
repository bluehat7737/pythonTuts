class Employee:
    # constructor
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def explain(self):
        return f"Name is {self.name} and address is {self.addr}"


# anshul = Employee()
# anshul.name = "Anshul"
# anshul.addr = "Baran"

anshul = Employee("Anshul", "Baran")
print(anshul.explain())

harshit = Employee("Harshit", "Tonk")
print(harshit.explain())
