class A:
    def pri(self):
        print("Class A")


class B(A):
    def pri(self):
        print("Class B")


class C(A):
    def pri(self):
        print("Class C")


class D(C, B):
    pass
    # def pri(self):
    #     print("Class D")


a = A()
b = B()
c = C()
d = D()

d.pri()
