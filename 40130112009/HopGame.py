from random import randint
print("Hop Game")
startgame=True;
ArrayOfScore=[];
while(True):
    if(startgame):
        try:
            print("Choose a number as the hoop factor:")
            factor=int(input())
        except:
            print("Wrong amount!!(The hoop coefficient must be a number for example: 2,10,...)")
            continue
        numberOfGame=randint(0,factor**2)
        if(numberOfGame%factor==0):
            continue;
        else:
            print(f"\nThe hoop coefficient is {factor}")
            print("print hope If it was the hop coefficient\n")
            print("Start Game:")
            startgame=False
            Score=0
    else:
        numberOfGame+=1
    print("CPU:",end =" ")
    if(numberOfGame%factor==0):
        print("hope")
    else:
        print(numberOfGame)

    print("Player:",end =" ")
    try:
        PlayerNumber=input()
        numberOfGame+=1
        if(numberOfGame%factor==0):
            if(PlayerNumber.lower()!="hop"):
                raise
        else:
            PlayerNumber=int(PlayerNumber)
            if(PlayerNumber!=numberOfGame):
                raise
        Score+=1
    except:
        ArrayOfScore.append(Score)
        print("\nWrong amount!!")
        print("Game over!!\n")
        print(f"Record:{Score}")
        print(f"Best Record:{max(ArrayOfScore)}\n")
        print("wanna play again (y/n):")
        answer=input()
        if(answer=="y"):
            startgame=True
            continue
        else:
            print("have a nice day :)")
            break        
