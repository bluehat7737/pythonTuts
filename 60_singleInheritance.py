class Emp:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def details(self):
        return f"Employee Name is {self.name} and it's role if {self.role}"


class Prog(Emp):
    def __init__(self, name, role, pLang):
        self.name = name
        self.role = role
        self.pLang = pLang

    def explain(self):
        return f"Programmer's name is {self.name}, it's role is {self.role} and language is {self.pLang}"


harshit = Emp("Harshit", "Manager")
anshul = Prog("Anshul", "Programmer", "C++")

print(anshul.explain())
print(anshul.details())