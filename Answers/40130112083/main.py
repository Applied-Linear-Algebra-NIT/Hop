import random

def save_record(record):
    record += 1
    return record

def save_best_record(record,best_record):
    if record > best_record:
        return record
    return best_record

def gameplay(best_record):
    n = int(input('write a number : '))
    record = 0
    while True:
        cpu = random.randint(1, 100)
        if cpu%n != 0:
            break
    flag = True
    while flag == True:
        player = input(f'''cpu : {cpu}
player : ''')

        if f'{cpu}' == 'hop':
            cpu = int(player) - 1

        if (cpu+1)%n == 0 and player != 'hop':
            flag = game_over(record, best_record, flag)

        if (cpu+1)%n != 0 and f'{cpu + 1}' != player:
            flag = game_over(record, best_record, flag)

        record = save_record(record)
        best_record = save_best_record(record, best_record)

        if f'{cpu}' != 'hop':
            if (cpu + 2) % n == 0:
                cpu = 'hop'
            else:
                cpu += 2


def game_over(record, best_record, flag):
    print(f'''Game over
Record : {record}
Best record : {best_record}''')

    replay = input('wanna play again (y/n):')
    if replay == 'n' :
        return flag == False
    gameplay(best_record)

best_record = 0
gameplay(best_record)
print('have a nice day')