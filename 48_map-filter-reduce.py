numbers = ['3', '36', '64']

# 1
# using normal logic
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# numbers[1] = numbers[1] + 1
# print(numbers[1])

# 2
# using map
numbers = list(map(int, numbers))
numbers[0] = numbers[0] + 1
print(numbers[0])


# 3
# more example (map)
# def square(a):
#     return a*a
#
# lis = [2,5,6,8,9,7,3]
# lis = list(map(square, lis))
# print(lis)

# 4
# one more example (map)
def square(a):
    return a * a


def cube(a):
    return a * a * a


fun = [square, cube]

for i in range(5):
    val = list(map(lambda x: x(i), fun))
    print(val)

# -------------------------------FILTER----------------------------------
print("------------------------------------------FILTER FUN-----------------------------------------------")
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def greater_than_5(num):
    return num > 5


greater = list(filter(greater_than_5, list_1))
print(greater)

# =================================================REDUCE========================================================
print("=================================================REDUCE========================================================")
list1 = [1, 2, 3, 4]

# classic way
n = 0
for p in list1:
    n = n + p
print(n)

# using reduce function
from functools import reduce

np = reduce(lambda x, y: x + y, list1)
print(np)
