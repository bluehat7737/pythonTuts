def fabo(n):
    if n <= 1:
        return 1
    else:
        return fabo(n-1) + fabo(n-2)

n = int(input("Enter a number : "))

print(fabo(n))
