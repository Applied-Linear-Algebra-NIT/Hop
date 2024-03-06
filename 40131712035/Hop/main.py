import os
from random import randint

recList = []


def gameOver():
    print(">--------------<")
    print("Game Over!")
    print("Record:", rec)
    print("Best Record:", max(recList))
    print(">--------------<")


while True:
    rec = 0
    hop = int(input("What number should Hop be divisible by?"))
    print("game started...")
    print(">--------------<")
    n = randint(0, 100)
    while n % hop == 0:
        n = randint(0, 100)
    while True:
        if n % hop == 0:
            print("CPU: hop")
        else:
            print("CPU:", n)
        player = input("Player:")
        if (n + 1) % hop == 0:
            if player == "hop":
                n += 2
                rec += 1
                continue
            else:
                recList.append(rec)
                gameOver()
                break
        if int(player) == n + 1:
            n += 2
            rec += 1
        else:
            recList.append(rec)
            gameOver()
            break

    again = input("wanna play again? (y/n):")
    if again == "n":
        print("have a nice day!")
        exit()
