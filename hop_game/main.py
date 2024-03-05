from random import randint


hop = int(input('Enter a number for hop: '))

while hop in [0, 1]:
    print(f'Invalid Entry <{hop}>')
    hop = int(input('Please enter another number for hop: '))


number = randint(1, hop - 1)

done = False
finished = False
record = 0
best_record = 0

while not done:
    print('Game started...')
    print('>------------------------<')
    while not finished:
        if number % hop == 0:
            print(f'CPU: hop')
        else:
            print(f'CPU: {number}')
        number += 1

        answer = input('Player: ')
        if answer == 'hop':
            if number % hop != 0:  # player lose
                finished = True

        else:
            answer = int(answer)
            if answer != number or (answer == number and number % hop == 0):
                finished = True

        if not finished:
            number += 1
            record += 1

    if record > best_record:  # updating best record
        best_record = record

    print('>------------------------<')
    print('Game Over!')
    print('Record:', record)
    print('Best Record:', best_record)
    print('--------------------------')
    is_done = input('wanna play again (y/n): ')

    if is_done == 'n':
        done = True
    else:
        if number % hop == 0:
            number += 1
        finished = False
        record = 0

print('have a nice day')
