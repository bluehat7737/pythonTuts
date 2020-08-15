n = int(input("Enter a Decimal Number"))
i = []
while 1:
    if n >= 8:
        i.append(round(n % 8))
        n = n // 8
    elif n < 8:
        i.append(n)
        break

for k in i[::-1]:
    print(k, end="")


