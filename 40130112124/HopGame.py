import random

run = True
record = 0
Best_record = []


def game_over(record):
    print('GAME OVER!')
    print('Record: ', record)
    print('Best record: ', max(Best_record))
    print('______________________')


def askToPlayAgain():
    answer = input('Wanna play again?(y/n): ')
    if answer == 'n':
        run = False
        print('HAVE A NICE DAY!;)')
        exit()
    else:
        print('WELCOME BACK ^*^')


number = int(input('Enter the number: '))
cpu_number = random.randint(1, 100)
while cpu_number % number == 0:
    cpu_number = random.randint(1, 100)
print('CPU:', cpu_number)

print('GAME STARTED...!')
print('______________________')
while run:
    player_input = input('Player: ')
    record += 1

    if (cpu_number + 1) % number == 0 and player_input != 'hop' or (
            cpu_number + 1) % number != 0 and player_input == 'hop':
        Best_record.append(record)
        game_over(record)
        askToPlayAgain()
        record = 0
        cpu_number += 1
    else:
        cpu_number += 2
        if cpu_number % number == 0:
            print('CPU: hop')
        else:
            print('CPU:', cpu_number)
