class Emp:
    no_of_leaves = 8

    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves


anshul = Emp("Anshul", "Choursiya")

print(anshul.no_of_leaves)
print(Emp.no_of_leaves)

anshul.changeLeaves(37)

print(anshul.no_of_leaves)
print(Emp.no_of_leaves)
