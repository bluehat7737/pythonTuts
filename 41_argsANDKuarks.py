import time

s_time = time.time()
print(f"Start time : {s_time}")

# args
def fun(normal, *args):
    print(normal)
    for items in args:
        print(items)


list = [
    "Anshul", "Harshit", "Aryan"
]

n = "this is normal"

fun(n, *list)


# kwarks

def fun2(nor, **kwk):
    print(nor)
    for key, value in kwk.items():
        print(f"{key} and {value}")


dict = {
    "Anshul": "c++",
    "Aryan": "Javascript",
    "Harshit": "Python"
}

fun2(n, **dict)

e_time = time.time()
print(f"End time : {e_time}")
print(f"Execution time : {e_time - s_time}")

