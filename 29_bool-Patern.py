# Boolean Patten

n = int(input("Enter a Number : "))
i = int(input("Enter bool value : "))
b = bool(i)

if i == True:
    print("Basic Loop")
    for j in range(0, n + 1):
        print("* " * int(j))
elif i == False:
    print("Reverse loop")
    for j in range(n, 0, -1):
        print("* " * int(j))
else:
    print("You enter wrong bool value!")
