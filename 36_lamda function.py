def add(a, b):
    return a + b


add1 = lambda a, b: a + b

print(add(2, 2))
print(add1(3, 3))


def a_sort(a):
    return a[1]


a = [
    [1, 14],
    [5, 6],
    [23, 8]
]

a.sort(key=a_sort)

print(a)
