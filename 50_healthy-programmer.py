# healthy programmer
from datetime import datetime
from pygame import mixer
from time import sleep


def date():
    import datetime
    return str(datetime.datetime.now())


def start(startTime):
    print("Application started at : ", end="")
    print(startTime)
    drink = 0
    exercise = 0
    eyes = 0
    while 1:
        time = datetime.now()
        now = time.strftime('%M')
        nowI = int(now)
        if nowI == 20 or nowI == 40 or nowI == 60:
            drink += 1
            print("===========DRINK TIME============")
            mixer.init()
            mixer.music.load('beep.ogg')
            mixer.music.set_volume(0.7)
            mixer.music.play()
            print("Enter your water drinking log :: ")
            with open('drank.txt') as f:
                inp = "[" + date() + "]" + input()
                f.write(inp)
                print(":: Successfully logged your drinking time ::")
                print(f"This day you drink {drink} times")
            mixer.music.stop()
        elif nowI == 30 or nowI == 60:
            eyes += 1
            print("===========EYE EXERCISE TIME============")
            mixer.init()
            mixer.music.load('beep.ogg')
            mixer.music.set_volume(0.7)
            mixer.music.play()
            print("Enter your EYES exercise log :: ")
            with open('eyes.txt') as f:
                inp = "[" + date() + "]" + input()
                f.write(inp)
                print(":: Successfully logged your EYES Exercise ::")
                print(f"This day : EYES Exercise : {eyes} times")
            mixer.music.stop()
        elif (nowI == 45 or nowI == 30 or nowI == 15 or nowI == 60) and drink > 2:
            exercise += 1
            print("===========EXERCISE TIME============")
            mixer.init()
            mixer.music.load('beep.ogg')
            mixer.music.set_volume(0.7)
            mixer.music.play()
            print("Enter your Exercise log :: ")
            with open('exercise.txt') as f:
                inp = "[" + date() + "]" + input()
                f.write(inp)
                print(":: Successfully logged your drinking time ::")
                print(f"This day you exercise {exercise} times")
            mixer.music.stop()


while 1:
    time = datetime.now()
    now = time.strftime('%H:%M:%S')
    nowS = now.split(":")
    nowI = int(nowS[0])
    if nowI >= 9 and nowI <= 17:
        start(now)
        break
    elif nowI >=17:
        break
