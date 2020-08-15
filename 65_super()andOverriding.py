class A:
    classvar = "CLASS A"

    def __init__(self):
        self.name = "Anshul"
        self.age = "18"
        self.special = "Special"


class B(A):
    classvar = "CLASS B"

    def __init__(self):
        self.name = "Harshit"
        self.age = "20"
        super().__init__()
        print(super().name)


a = A()
b = B()

print(a.name)
print(b.name)
