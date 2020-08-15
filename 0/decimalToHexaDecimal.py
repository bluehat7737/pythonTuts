dict = {
    10: 'A', 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
}

n = int(input("Enter a Decimal Number"))
i = []
while 1:
    if n >= 16:
        t = round(n % 16)
        if t > 9:
            t = dict[t]
        i.append(t)
        n = n // 16
    elif n < 16:
        if n >= 10:
            n = dict[n]
        i.append(n)
        break

for k in i[::-1]:
    print(k, end="")
