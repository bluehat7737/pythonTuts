# Exercise 2

o = input("Enter Operator : ")

print("Enter two Numbers : ")
v1 = int(input())
v2 = int(input())

if (v1 == 45 or v1 == 3) and (v2 == 45 or v2 == 3) and o == '*':
    print(v1 + v2)
elif (v1 == 56 or v1 == 9) and (v2 == 56 or v2 == 9) and o == '+':
    print(v1 * v2)
elif (v1 == 56 or v1 == 6) and (v2 == 56 or v2 == 6) and o == '/':
    print(v1 - v2)
else:
    if o == '+':
        print(v1 + v2)
    elif o == '/':
        print(v1 / v2)
    elif o == '*':
        print(v1 * v2)
    else:
        print(v1 - v2)
