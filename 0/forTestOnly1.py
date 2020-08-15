# def minion_game(s):
#     # your code goes here
#
#     vm = 0
#     cm = 0
#
#     vov = 'AEIOU'
#
#     for i in range(len(s)):
#         if s[i] not in vov:
#             cm = cm + (len(s) -i)
#         else:
#             vm = vm + (len(s) -i)
#
#     if cm > vm:
#         print("Stuart",cm)
#     elif vm > cm:
#         print("Kevin",vm)
#     else:
#         print("Draw")

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


if __name__ == '__main__':
    s = input()
    minion_game(s)
