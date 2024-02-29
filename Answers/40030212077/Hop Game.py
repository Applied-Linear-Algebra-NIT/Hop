import random

def coefficient():
    print("Enter a coefficient to start the game:")
    x = int(input())
    y = x%2
    while x<2 or y==0:
        print("Enter an other coefficient. The coefficient must be an even number greater than 2:")
        x = int(input())
        y = x%2
    return x

def startNum(x):
    y = random.randint(1, 99)
    z = y%x
    while z==0:
        y = random.randint(1, 99)
        z = y%x
    return y

def startGame(x,y,scores):
    status = True
    counter = 0
    while status:

        # نوبت سیستم
        z = y%x
        if z==0:
            print("CPU: hop")
        else:
            print(f"CPU: {y}")
        y+=1
        z = y%x

        # نوبت بازیکن
        i = input()
        if i!="hop" and i!="Hop":
            int_i = int(i)
        else:
            int_i = i
        
        if z==0:
            if i!="hop" and i!="Hop":
                status = False
            else:
                counter+=1
        elif int_i!=y:
            status = False
        else:
            counter+=1

        print(f"Player: {i}")
        y+=1

    scores.append(counter)
    print(f">--------------<\nGame Over!\nRecord: {counter}\nBest Record: {max(scores)}\n---------------")

    return scores

def gameHop(scores):

    # ضریب
    x = coefficient()
    print("game started...\n>--------------<")
    
    # عدد رندوم برای شروع
    y = startNum(x)

    # شروع بازی
    scores = startGame(x,y,scores)

    # بررسی برای شروع دوباره ی بازی
    print(">> wanna play again (y/n):")
    status = input()
    while status!="y" and status!="n":
        print("Enter a valid answer (y/n):")
        status = input()
    
    if status=="y":
        gameHop(scores)
    else:
        print("> have a nice day")
    
    return scores


# امتیازات
scores = []

scores = gameHop(scores)

print(f"All scores:\n{scores}")