def minion_game(s):
    # your code goes here

    # marks var
    vm = 0
    cm = 0

    # string char
    az = list(s)
    vv = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # string combinations
    ccom = []
    vcom = []

    for j in range(len(az)):
        if az[j] in vv:
            for i in range(j, len(az)):
                vcom.append(''.join(az[j:i + 1]))
                vm += 1
        else:
            for i in range(j, len(az)):
                ccom.append(''.join(az[j:i + 1]))
                cm += 1

    print(vcom)
    print(ccom)
    if cm > vm:
        print(f"Stuart {str(cm)}")
    elif vm > cm:
        print(f"Kevin {str(vm)}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


"""
def minion_game(s):
    s1 = 0
    s2 = 0
    vow = 'AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            s1 = s1 + (len(s) - i)
        else:
            s2 = s2 + (len(s) - i)
    if s1 > s2:
        print("Stuart", s1)
    elif s2 > s1:
        print("Kevin", s2)
    else:
        print("Draw")
"""