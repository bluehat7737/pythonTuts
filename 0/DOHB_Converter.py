def print_formatted(number):
    # your code goes here
    def octal(e):
        o = []
        while 1:
            if e >= 8:
                o.append(round(e % 8))
                e = e // 8
            elif e < 8:
                o.append(e)
                break
        return convert(o)

    def hexa(e):
        dict = {
            10: 'A', 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
        }

        h = []
        while 1:
            if e >= 16:
                t = round(e % 16)
                if t > 9:
                    t = dict[t]
                h.append(t)
                e = e // 16
            elif e < 16:
                if e >= 10:
                    e = dict[e]
                h.append(e)
                break

        return convert(h)

    def binary(e):
        b = []

        while 1:
            if e > 1:
                t = e % 2
                b.append(t)
                e = e // 2
            elif e <= 1:
                b.append(e)
                break
        return convert(b)

    def convert(l):
        s = [str(k) for k in l[::-1]]
        res = ''.join(s)
        return res

    for i in range(1, number + 1):
        oo = octal(i)
        hh = hexa(i)
        bb = binary(i)
        print(i, end="")
        print(oo, end="")
        print(hh, end="")
        print(bb, end="")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
