import random as rand
scoreList = []
def game():
    print("<--Welcome-->")
    while True:
        try:
            factor = int(input("Please enter your preferred hop parameter: "))
            break
        except ValueError:
            print("Please enter a number!")
    
    running = True
    randomNum = generateRand(factor)
    score = 0
    while running:
        if (randomNum % factor == 0):
            print("<---------->\nCPU: HOP!")
        else:
            print("<---------->\nCPU: " + str(randomNum))
        pNum = input("Player: " )
        if pNum.isdigit(): 
            pNum = int(pNum)
            if ((randomNum+1) % factor!=0) and pNum == randomNum+1:
                randomNum = pNum + 1
                score += 1
            else : 
                gameOver(score)
                running = False
        elif pNum.lower() == 'hop':
            if  ((randomNum+1) % factor==0):
                randomNum = randomNum + 2
                score += 1
            else: 
                gameOver(score)
                running = False
        else: 
            gameOver(score)
            running = False

def generateRand(factor):
    num = rand.randint(1, 100)
    while num % factor == 0:
        num = rand.randint(1, 100)
    return num

def gameOver(score):
    print("<-----game over----->")
    scoreList.append(score)
    print("score: " + str(score))
    print("highest: " + str(max(scoreList)))
    pAnswer = input ("<---------->\nWanna play again? (y/n): ")
    while True:
        if pAnswer.lower()=='y':
            game()
            break
        elif pAnswer.lower() == 'n':
            print("<-----GOODGAME----->")
            break
        else:   
            print("Are you mentally challenged my guy?")
            gameOver(score)
        
    
game()