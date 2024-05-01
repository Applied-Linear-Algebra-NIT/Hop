import random

print("Hop Game")
while 1:
    coefficient = int(input("Enter the coefficient you want :"))
    if (coefficient > 0):
        break
    else:
        print("coefficient is not acceptable")
scores = []
highScore = 0
score = 0
turn = "Computer"
gameState = True
gameOver = False
countC = 1
while 1:
    num = random.randint(1,100)
    if num % coefficient != 0:
        break
    
    

while gameState:
    while gameOver != True:
        if turn == "Computer":
            if num % coefficient == 0:
                print("Computer: Hop")
                turn = "Human"
            else:
                print("Computer: ", num)
                turn = "Human"
        elif turn == "Human":
            userInput = input("Your turn: ")
            if num % coefficient == 0:
                userInput = str(userInput)
                if userInput.lower() == "hop":
                    score += 1
                    turn = "Computer"
                else:
                    gameOver = True
            else:
                userInput = int(userInput)
                if userInput == num:
                    score += 1
                    turn = "Computer"
                else:
                    gameOver = True
        num += 1
    print("You lost sucker")
    scores.append(score)
    print("Your score: ", score)
    best = 0
    for s in scores:
        best = max(best, s)
    print("Best Score: ", best)
    answer = input("Do you want to continue? y/n")
    if answer == "y":
        gameOver = False
        score = 0
        turn = "Computer"
        while 1:
            num = random.randint(1,100)
            if num % coefficient != 0:
                break
        while 1:
            coefficient = int(input("Enter the coefficient you want :"))
            if (coefficient > 0):
                break
            else:
                print("coefficient is not acceptable")
    else:
        gameState = False
print("GoozBye")