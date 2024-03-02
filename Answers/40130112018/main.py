import random


def game():
    coeff = input("Enter the coefficient: ")

    while not coeff.isdigit():
        print("Invalid input, please enter a number")
        coeff = input("Enter the coefficient: ")

    coeff = int(coeff)

    curent_number = random.randint(1, 100)

    while curent_number % coeff == 0:
        curent_number = random.randint(1, 100)

    cpu = True
    record = 0
    print("game started...")
    print(">--------------<")
    while True:
        if cpu:
            if curent_number % coeff == 0:
                print(f"CPU : Hop")
            else:
                print(f"CPU : {curent_number}")
            cpu = not cpu
            curent_number += 1
            continue

        player_number = input("Player: ")

        if curent_number % coeff != 0:
            if player_number == "hop":
                print("You lost")
                break
            
            while not player_number.isdigit():
                print("Invalid input, please enter a number")
                player_number = input("Player: ")

            player_number = int(player_number)
            
            if player_number != curent_number:
                print("You lost")
                break
            
            curent_number += 1
            record += 1
            cpu = not cpu
        else:
            if player_number != "hop":
                print("You lost")
                break
            curent_number += 1
            record += 1
            cpu = not cpu
            
    print(">--------------<")
    print("Game over")
    return record    

    

max_record = 0
while True:
    score = game()
    if score > max_record:
        max_record = score
        
    print(f"Your record is: {score}")
    print(f"Best score: {max_record}")
    print("---------------\n")
    choice = input("wanna play again (y/n): ")
    if choice != "y":
        break
