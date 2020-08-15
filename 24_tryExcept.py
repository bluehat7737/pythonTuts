n1 = input()
n2 = input()

try:
    print(int(n1) + int(n2))
except Exception as e:
    print(e)

print("Successful run whole program")