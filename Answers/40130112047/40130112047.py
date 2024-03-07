import random
scores = []
print("Welcome to the game")
print("Please notice to write \'hope\' word correctly")

while 1:
    coffiesient = int(input("Please Enter coffiesient number: "))
    if (coffiesient>1):
        break
    else:
        print("Unallowed Number")
counter=1
score=0
lose = False
i=random.randint(0, 100)
hope=counter*coffiesient
turn="Computer"
finishGame=False

while finishGame!=True:
    while lose!=True:
        if turn=="Computer":
            if i==hope:
                print("Computer: hope")
                counter+=1
                hope=counter*coffiesient
            else:
                print("Computer: ", i)
            turn="Human"

        elif turn=="Human":
            inp = input("Human: ")
            if i==hope:
                if inp!="hope":
                    lost=True
                else:
                    turn="Computer"
                    score+=1
                    counter+=1
                    hope=counter*coffiesient
            else:
                try:
                    inp=int(inp)
                except ValueError as v:
                    lose=True
                if inp!=i:
                    lose=True
                else:
                    turn="Computer"
                    score+=1
        i+=1

    print("You Lost :(")
    scores.append(score)
    print("Your score: ", score)
    m=0
    for i in scores:
        m=max(m, i)
    print("Best Score: ", m)
    awn = input("Do you want to continue? Y/N ")
    if awn=="N":
        finishGame=True
    else:
        lose=False
        score=0
        turn="Computer"
        i=1
        counter=1
        while 1:
            coffiesient = int(input("Please Enter coffiesient number: "))
            if (coffiesient>0):
                break
            else:
                print("Unallowed Number")
        hope=counter*coffiesient
print("Thanks for Choosing Our Game")