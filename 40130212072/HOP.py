import random


def wrong_move():
    print("\t\t\t\t\tWrong input!!")
    play_again = input("\t\t\t\t\tDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hop()
    else:
        print("\t\t\t\t\tMax score:", max(score_list))
        print("\t\t\t\t\tEnd of game!!")


def hop():
    score = 0
    cpu_number = random.randint(1, 100)
    if cpu_number % 5 != 0:
        print(f"\t\t\t\t\tCPU:{cpu_number}")

        while True:
            user_number = input("\t\t\t\t\tYOU:")

            if user_number.isdigit():
                if int(user_number) % 5 == 0:
                    score_list.append(score)
                    print("\t\t\t\t\tyour score:", score)
                    wrong_move()
                    break
                cpu_number = int(user_number) + 1
                if cpu_number % 5 == 0:
                    cpu_number = "hop"
                    print(f"\t\t\t\t\tCPU:{str(cpu_number)}")
                    score += 1

                else:
                    cpu_number = int(user_number)
                    print(f"\t\t\t\t\tCPU:{cpu_number + 1}")
                    score += 1

            elif user_number == "hop":
                if cpu_number == "hop":
                    score_list.append(score)
                    print("\t\t\t\t\tyour score:", score)
                    wrong_move()
                    break

                cpu_number += 3
                print(f"\t\t\t\t\tCPU:{cpu_number}")
                score += 1

            else:
                if not user_number.isdigit():
                    score_list.append(score)
                    print("\t\t\t\t\tyour score:", score)
                    wrong_move()
                    break
                if user_number.isdigit() and user_number != cpu_number + 1:
                    score_list.append(score)
                    print("\t\t\t\t\tyour score:", score)
                    wrong_move()
                    break
    else:
        hop()


print("\n\t\t\t\t***** HOP_GAME START!! *****")
score_list = []
hop()