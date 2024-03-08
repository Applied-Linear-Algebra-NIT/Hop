import random

#student number : 40030112073

def hop_game():
    k = int(input("enter hop coeficient: "))
    start = random.randint(1,99)
    while True:
        if start % 5 == 0: start = random.randint(1,99)
        else:
            break
    counter = start
    cpu_turn = start % 2
    player_turn = 1 - cpu_turn
    turn = cpu_turn
    while True:
        if turn == cpu_turn:
            output = "Hop" if counter % k == 0 else str(counter)
            print(output)
            counter = counter + 1
            turn = 1 - turn
        else:
            next = "hop" if counter % k == 0 else str(counter)
            answer = input("enter next:")
            if answer == next:
                counter = counter + 1
                turn = 1 - turn
            else :
                break
    print("-----------------")
    print("Game Over")
    return int((counter - start )/2)

scores = []

score = hop_game()
scores.append(score)
print(f"score: {score}")
print(f"best score: {max(scores)}")
while True:
    i = input("wanna play again? [Y/n]:")
    if i == "" or i == "y":
        score = hop_game()
        scores.append(score)
        print(f"score: {score}")
        print(f"best score: {max(scores)}")
    else:
        break