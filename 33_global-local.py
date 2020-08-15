x = 50 # global

def func():
    x=20
    print(x)
func()
print(x)

def fun2():
    global x
    x=30
    print(x)

fun2()

def f1():
    x=40
    def f2():
        x=30
        print(x)
    f2()
    print(x)

f1()