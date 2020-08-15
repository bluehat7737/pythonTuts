# Exercise 3

guessTime = 5

while 1:
    if guessTime > 0:
        print(str(guessTime) + " guess left")
        print("Enter Guess Number : ", end="")
        inp = int(input())
        if inp > 18:
            print("Lower")
        elif inp < 18:
            print("Higher")
        else:
            print("Congrats! You WON")
            break
        guessTime -= 1
    else:
        print("YOU LOOSE")
        break
