n = int(input("Enter a Decimal Number"))
i = []

while 1:
    if n > 1:
        t = n % 2
        i.append(t)
        n = n // 2
    elif n <= 1:
        i.append(n)
        break

for k in i[::-1]:
    print(k, end="")