import random


def play_hop_game():
    print("Let's play Hop game!")
    player_score = 0
    best_score = 0

    while True:
        hop_factor = input("Enter a hop factor: ")

        while not hop_factor.isdigit():
            print("Invalid input! Please enter a valid number.")
            hop_factor = input("Enter a hop factor: ")

        hop_factor = int(hop_factor)
        print("Game started...")

        cpu_number = random.randint(1, 100)
        while cpu_number % hop_factor == 0:
            cpu_number = random.randint(1, 100)
        print("CPU:", cpu_number)

        while True:
            player_number = input("Player: ")
            while not player_number.isdigit() and player_number.lower() != "hop":
                print("Invalid input! Please enter a valid number.")
                player_number = input("Player: ")

            if player_number.lower() == "hop":
                if (cpu_number + 1) % hop_factor != 0:
                    print("Wrong guess! Game Over!")
                    break
                player_score += 1
                cpu_number += 2
                print("CPU:", cpu_number)
            else:
                player_number = int(player_number)
                if player_number != cpu_number + 1 and player_number.lower() != "hop":
                    print("Wrong guess! Game Over!")
                    break
                if player_number % hop_factor == 0:
                    print("Wrong guess! Game Over!")
                    break

                player_score += 1

                cpu_number = player_number + 1
                if cpu_number % hop_factor == 0:
                    print("CPU: hop")
                else:
                    print("CPU:", cpu_number)

        print(">--------------<")
        print("Game Over!")
        print("Record:", player_score)
        best_score = max(best_score, player_score)
        print("Best Record:", best_score)
        print("---------------")

        play_again = input(">> Wanna play again? (y/n): ")
        if play_again.lower() != "y":
            print("> Have a nice day!")
            break


play_hop_game()
