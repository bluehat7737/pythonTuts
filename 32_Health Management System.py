from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


while 1:
    # 1. Harry
    # 2. Anshul
    # 3. Aryan

    def date():
        import datetime
        return str(datetime.datetime.now())


    # to read only
    def retrive(r):

        if r == 1 or r == 2 or r == 3:
            if r == 1:
                print("Enter your option : ")
                print("1. Diet\n" + "2. Exercise")
                o = int(input())
                if o == 1:
                    with open("hms/HarryDiet.txt") as f:
                        print(f.read())
                elif o == 2:
                    with open("hms/HarryEx.txt") as f:
                        print(f.read())
            elif r == 2:
                print("Enter your option : ")
                print("1. Diet\n" + "2. Exercise")
                o = int(input())
                if o == 1:
                    with open("hms/AnshulDiet.txt") as f:
                        print(f.read())
                elif o == 2:
                    with open("hms/AnshulEx.txt") as f:
                        print(f.read())
            else:
                print("Enter your option : ")
                print("1. Diet\n" + "2. Exercise")
                o = int(input())
                if o == 1:
                    with open("hms/AryanDiet.txt") as f:
                        print(f.read())
                elif o == 2:
                    with open("hms/AryanEx.txt") as f:
                        print(f.read())
        else:
            print("You Enter a Wrong Choice!")


    # to write
    def write(w):

        if w == 1 or w == 2 or w == 3:
            if w == 1:
                print("Enter your option : ")
                print("1. Diet\n" + "2.Exercise")
                o = int(input())
                if o == 1:
                    with open("hms/HarryDiet.txt", "a") as f:
                        print("Enter Your Diet : ")
                        diet = input()
                        s = "[" + date() + "]" + " " + diet + "\n"
                        f.write(s)
                        print("Successfully Written!")
                else:
                    with open("hms/HarryEx.txt", "a") as f:
                        print("Enter Your Exercise : ")
                        ex = input()
                        s = "[" + date() + "]" + " " + ex + "\n"
                        f.write(s)
                        print("Successfully Written!")
            elif w == 2:
                print("Enter your option : ")
                print("1. Diet\n" + "2.Exercise")
                o = int(input())
                if o == 1:
                    with open("hms/AnshulDiet.txt", "a") as f:
                        print("Enter Your Diet : ")
                        diet = input()
                        s = "[" + date() + "]" + " " + diet + "\n"
                        f.write(s)
                        print("Successfully Written!")
                else:
                    with open("hms/AnshulEx.txt", "a") as f:
                        print("Enter Your Exercise : ")
                        ex = input()
                        s = "[" + date() + "]" + " " + ex + "\n"
                        f.write(s)
                        print("Successfully Written!")
            else:
                print("Enter your option : ")
                print("1. Diet\n" + "2.Exercise")
                o = int(input())
                if o == 1:
                    with open("hms/AryanDiet.txt", "a") as f:
                        print("Enter Your Diet : ")
                        diet = input()
                        s = "[" + date() + "]" + " " + diet + "\n"
                        f.write(s)
                        print("Successfully Written!")
                else:
                    with open("hms/AryanEX.txt", "a") as f:
                        print("Enter Your Exercise : ")
                        ex = input()
                        s = "[" + date() + "]" + " " + ex + "\n"
                        f.write(s)
                        print("Successfully Written!")
        else:
            print("Your Enter a Wrong Option")


    print("What do you want? ")
    print("1. Retrive \n" + "2. Write")
    inp = int(input())

    if inp == 1:
        print("Enter your choice : ")
        print("1. Harry\n" + "2. Anshul\n" + "3. Aryan")
        r = int(input())
        retrive(r)
    elif inp == 2:
        print("Enter your choice : ")
        print("1. Harry\n" + "2. Anshul\n" + "3. Aryan")
        w = int(input())
        write(w)
    else:
        print("You enter a wrong option :: PLZ RESTART")

    rr = input("Rerun Program {Y/N}")
    if rr == 'y' or rr == 'Y':
        clear()
        continue
    else:
        break
