import random


def hop_game():
    user_hop = int(input("please enter a number: "))

    score = 0
    computer_number = random.randint(1, 10)
    if computer_number % user_hop == 0:
        print("Computer: Hop")
    else:
        print("Computer:", computer_number)
    while True:
        user_input = input("Player: ")
        if (computer_number + 1) % user_hop == 0:
            if user_input != "hop":
                print("You lost!")
                break
            else:
                score += 1
        if user_input != "hop":
            if int(user_input) <= computer_number:
                print("You lost!")
                break
            elif int(user_input) - computer_number > 1:
                print("You lost!")
                break
            else:
                score +=1
        computer_number = computer_number + 2
        if computer_number % user_hop == 0:
            print("Computer: Hop!")
        else:
            print("Computer:", computer_number)
    print("Your score:", score)

hop_game()
