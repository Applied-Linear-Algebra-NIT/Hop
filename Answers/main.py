from random import randrange

scores = []

while 1:
    score = 0

    c = int(input("Hop : "))

    while 1 :
        start_num = randrange(1,50)
        if(start_num % c != 0):
            break

    pc_num = start_num

    game = True

    while game:

        if(pc_num % c == 0):

            print("PC : HOP")

        else:

            print("PC : ", pc_num)

        
        player_num = input("Player : ")

        num = pc_num + 1

        if(num % c == 0):

            if(player_num.lower() == "hop"):

                pc_num += 2

            else:

                game = False

        else:

            if(int(player_num) == num):

                pc_num += 2
            
            else:

                game = False
        score += 1

    print("-----------------")
    print("Game Over")
    scores.append(score)
    print("Score :  ",score)
    print("High Score :  ",max(scores))

    check = input("Wanna Play again ? (y/n) : ")

    if(check == 'y'):
        print("----------------------")
    else:
        break;

print("have a nice day")