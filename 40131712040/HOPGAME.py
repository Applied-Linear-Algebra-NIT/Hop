import random


class HopGame:
    def __init__(self):
        self.listOfScore = []

    def play(self):
        score = 0
        computer_num = random.randint(1, 100)

        if computer_num % 5 != 0:
            print(f"💻:{computer_num}")

            while True:
                player_num = input("👤:")

                if player_num.isdigit():
                    if int(player_num) % 5 == 0:
                        self.listOfScore.append(score)
                        print("player score:", score)
                        self.wrong_move()
                        break

                    computer_num = int(player_num) + 1
                    if computer_num % 5 == 0:
                        computer_num = "hop"
                        print(f"💻: {str(computer_num)}")
                        score += 1
                    else:
                        computer_num = int(player_num)
                        print(f"💻: {computer_num + 1}")
                        score += 1

                elif player_num == "hop":
                    if computer_num == "hop":
                        self.listOfScore.append(score)
                        print("player score:", score)
                        self.wrong_move()
                        break

                    computer_num += 3
                    print(f"💻: {computer_num}")
                    score += 1

                else:
                    if not player_num.isdigit():
                        self.listOfScore.append(score)
                        print("player score:", score)
                        self.wrong_move()
                        break
                    if player_num.isdigit() and player_num != computer_num + 1:
                        self.listOfScore.append(score)
                        print("player score:", score)
                        self.wrong_move()
                        break

    def wrong_move(self):
        print("❌")
        print("Enter another input :)")
        play_again = input("wanna to play again? (Y/N): ")
        if play_again == "Y":
            self.play()
        else:
            print("🏆:", max(self.listOfScore))
            print(" Bye bye! ;)")


print("\n")
print("           WELCOM😊          \n")
game = HopGame()
game.play()



