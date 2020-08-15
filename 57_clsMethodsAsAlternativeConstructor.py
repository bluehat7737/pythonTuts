class Emp:
    no_of_leaves = 8

    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_dash(cls, string):
        # 1
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1])

        # 2
        return cls(*string.split("-"))


anshul = Emp("Anshul", "Choursiya")
harry = Emp.from_dash("Harry-Sharma")

print(harry.name)
