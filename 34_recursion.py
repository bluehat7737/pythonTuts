def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120

o = int(input("Enter a number : "))
print("Iterative method : ", factorial_iterative(o))
print("Recursive Method : ", factorial_recursive(o))

# n! = n * (n-1) * (n-2) * (n-3).....1


