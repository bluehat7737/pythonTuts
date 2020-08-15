import random
import time

s_time = time.time()
print(f"Start time : {s_time}")

game = [
    "snake",
    "water",
    "gun"
]

o = [0, 1, 2]

i = 1
cm = 0
pm = 0
while i <= 10:
    print("----------------------------")
    print("Game " + str(i) + " :")
    cgrv = random.choice(o)
    com = game[cgrv]
    print("computer : " + com)
    print("Enter your choice : ")
    print("0. snake\n1. water\n2. gun")
    inp = int(input())
    ply = game[inp]
    if ply == com:
        print("Tie")
        print("computer : " + str(cm) + " player : " + str(pm))
    elif ply == "snake" and com == "water":
        pm += 1
        print("You win! " + str(pm) + " times")
    elif ply == "water" and com == "gun":
        pm += 1
        print("You win! " + str(pm) + " times")
    elif ply == "gun" and com == "snake":
        pm += 1
        print("You win! " + str(pm) + " times")
    else:
        cm += 1
        print("You loose! " + str(cm) + " times")
    if i == 10:
        print("============================")
        print("FINAL SCORE ::")
        print("computer : " + str(cm) + " player : " + str(pm))
        if pm > cm:
            print("PLAYER WIN!")
        elif pm==cm:
            print(":: GAME TIE ::")
        else:
            print("COMPUTER WIN!")

        break
    else:
        i += 1

e_time = time.time()
print(f"End time : {e_time}")
print(f"Execution time : {e_time - s_time}")