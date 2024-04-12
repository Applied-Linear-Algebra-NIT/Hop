import numpy as np

size = int(input("Enter Deminsion of your matrix: "))
if size<=0:
    raise ValueError("your value can not be accepted")
input_matrix = np.zeros((size, size))
print("please enter your matrix : ")
for i in range (size):
    for j in range(size):
        input_matrix[i][j] = int(input(f"element [{i}][{j}]: "))
print(input_matrix)

awnser = np.zeros((size, 1))
print("Enter awnser matrix: ")
for i in range(size):
    awnser[i][0] = input(f"Element [{i}][0] : ")
print(awnser,"\n")



def guassianElimination(input_matrix, awnser_matrix):
    swapped=False
    for i in range(len(input_matrix)):
        if input_matrix[i][i]==0:
            for t in range(i+1, len(input_matrix[0])):
                if input_matrix[t][i]!=0:                    
                    input_matrix[[i, t]]=input_matrix[[t, i]]
                    awnser[[i, t]]=awnser[[t, i]]
                    swapped=True
                    break
                if swapped==False:
                    raise ValueError("Wrong matrix given")
        
        for t in range(i+1, len(input_matrix[0])):
            if input_matrix[t][i]!=0:
                temp = -(input_matrix[t][i]/input_matrix[i][i])
                awnser[t][0] = awnser[t][0] + awnser[i][0] * temp
                for j in range(i, len(input_matrix)):
                    input_matrix[t][j]=input_matrix[t][j] + (input_matrix[i][j] * temp)


    print("After elimination:\n","Input Matix :\n",input_matrix)
    print("Awnser Matrix:\n",awnser,"\n")


    s1 = []
    s2 = []
    for i in range(len(input_matrix)-1, -1, -1):
        x=0
        for j in range(len(input_matrix)-1, i, -1):
            y=s1.pop()
            s2.append(y)
            x += y*input_matrix[i][j]
        w = (awnser[i][0]-x)/input_matrix[i][i]
        s1.append(w)
        while (len(s2)!=0):
            s1.append(s2.pop())


    s3 = np.array(s1)
    s3 = s3.reshape((-1, 1))
    print("Result: \n",s3)

guassianElimination(input_matrix, awnser)
print("*"*30)

input_matrix = np.array([[0, 0, 1, 0], [1/4, 1/4, 1/4, 1/4], [0, 0, 1/2, 1/2], [1, 0, 0, 0]])
awnser=np.array([[0], [1/4], [1], [1]])
print(input_matrix)
print(awnser)
guassianElimination(input_matrix, awnser)