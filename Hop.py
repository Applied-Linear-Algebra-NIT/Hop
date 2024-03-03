from random import randint
BRecord = 0
while(True) :
    Coefficient = int(input("Enter the number: "))
    Start = randint(1, 100)
    while(Start % Coefficient == 0) :
        Start = randint(1, 100)
    print(f"CPU: {Start}")
    Record = 0
    while(True) :
        Player = input("Player: ")
        if Player != 'hop' :
            Player = int(Player)
        if (Start + 1) % Coefficient == 0 :
            if Player != 'hop' :
                BRecord += Record
                print("Game Over!")
                print(f"Record: {Record}")
                print(f"Best Record: {BRecord}")
                break
            else :
                Record += 1
        elif Start + 1 != Player :
            BRecord += Record
            print("Game Over!")
            print(f"Record: {Record}")
            print(f"Best Record: {BRecord}")
            break
        elif Start + 1 == Player :
            Record += 1
        Start += 2
        if Start % Coefficient == 0 :
            print("CPU: hop")
        else :
            print(f"CPU: {Start}")
    Continue = input("wanna play again (y/n): ")
    if Continue == 'n' :
        print("have a nice day")
        break