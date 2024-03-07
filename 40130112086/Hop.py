import random

record = 0
i=0
Best_record =[]
def play():
    print("Game Over!")
    print("Record:" + str(record))
    print("Best Record:", max(Best_record))
    playOrNot=input(">> wanna play again (y/n):")
    if playOrNot=='n':
        print("Thanks for using :)")
    else:
        game()
def game():
    global record
    global i
    record += 1
    print("game started...")
    print(">--------------<")
    number = int(input("Enter the Coefficient:"))
    cpu = random.randint(1, 100)
    while cpu % number == 0:
        cpu = random.randint(1, 100)
    print("Cpu: " + str(cpu))
    while True:
        player = input("Player: ")
        i+=1
        Best_record.append(i)
        if ((cpu + 1) % number == 0 and player != 'hop' or  (cpu + 1) % number != 0 and player == 'hop' or (cpu + 1) % number != 0 and int(player) != cpu + 1):
           play()
           break
        cpu+=2
        if cpu % number == 0:
          print("Cpu: hop")
        else:
           print("Cpu: " + str(cpu))

def main():
    print("Welcome!")
    game()

if __name__ == "__main__":
    main()

