import random

scores = []


while True:
    initial_number = random.randint(1, 100)
    current_number = initial_number
    score = 0
    cofficient = int(input("Enter the hop coefficient: "))
    print('game started...')
    print(">--------------<")
    print('CPU: ', initial_number)

    while True:
        user_input = input('Player: ')
        if user_input.lower() == 'hop':
            if (current_number + 1) % cofficient == 0:
                score += 1
                current_number += 2
            else:
                print('>--------------<')
                print('Game Over!')
                break
        else:
            user_input = int(user_input)
            if user_input != current_number + 1:
                print('>--------------<')
                print('Game Over!')
                break
            else:
                score += 1
                current_number += 2

            if user_input % cofficient == 0:
                print('>--------------<')
                print('Game Over!')
                break

        if current_number % cofficient == 0:
            print('CPU: hop')
        else:
            print('CPU: ', current_number)

    scores.append(score)
    print('Record: ', score)
    print('Best Record: ', max(scores))
    print('---------------')

    answer = input('>> wanna play again (y/n):')
    if answer == 'n':
        print('> have a nice day')
        break
