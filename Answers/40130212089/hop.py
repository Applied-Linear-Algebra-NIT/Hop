import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')


def getInt() -> int:
    int_value = None
    while int_value is None:
        try:
            int_value = int(input())
            if int_value < 3:
                int_value = None
                print("Hop Can't be less then 3!")
        except ValueError:
            print("Please enter only numbers!!!")
    return int_value


def hop():
    print("Please enter the Hop value(must be larger than 1): ", end = "")
    hop = getInt()
    print("\n>--------------<")
    record = 0
    progress = random.randint(10, 99)
    player = 0
    typo_chance = 2
    global best_record

    if not progress % hop:  # make sure starting number is not equal to hop
        progress += 1

    correct_answer = True
    while correct_answer:
        # CPU
        if progress % hop:
            print(f"CPU: {progress}")
        else:
            print(f"CPU: hop")
        progress += 1
        player = input("Player: ")
        time.sleep(0.5)
        
        # PLAYER
        if progress % hop:
            try:
                player = int(player)
                if progress != player and typo_chance:
                    typo_chance -= 1
                    print(f"you have {typo_chance +1} more chance(s) to correct your typo.")
                    progress -= 2
                elif progress != player:
                    correct_answer = False
                else:
                    record += 1
            except ValueError:
                correct_answer = False
        else:
            try:
                player = int(player)
                correct_answer = False
            except ValueError:
                if player != "hop" and typo_chance:
                    typo_chance -= 1
                    print(f"you have {typo_chance +1} more chance(s) to correct your typo.")
                    progress -= 2
                elif player != "hop":
                    correct_answer = False
                else:
                    record += 1

        progress += 1
    
    if record > best_record:
        best_record = record
    print(">--------------<")
    print(f"Game Over!\nRecord: {record}\nBest Record: {best_record}\n---------------\n")


play_again = True
best_record = 0

print("game started...")
hop()

    
while play_again:
    ans = input(">> Wanna play again? (Yes/No): ").lower()
    if ans in ['1', 'yes', 'y']:
        hop()
    elif ans in ['0', 'no', 'n']:
        print("\n> OK! have a nice day.")
        play_again = False
    else:
        print("huh?")
