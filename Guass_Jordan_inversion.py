import numpy as np

size = int(input("Enter Deminsion of your matrix: "))
if size<=0:
    raise ValueError("your value can not be accepted")
input_matrix = np.zeros((size, size))
print("please enter your matrix : ")
for i in range (size):
    for j in range(size):
        input_matrix[i][j] = int(input(f"element [{i}][{j}]: "))
identity=np.identity(size)

def inversion(input_matrix):
    print("Input Matrix Before Guassian Elimination: \n", input_matrix)
    print("Identity matrix : \n", identity)

    swapped=False
    for i in range(len(input_matrix)):
        if input_matrix[i][i]==0:
            for t in range(i+1, len(input_matrix)):
                if input_matrix[t][i]!=0:                    
                    input_matrix[[i, t]]=input_matrix[[t, i]]
                    identity[[i, t]]=identity[[t, i]]
                    swapped=True
                    break
            if swapped==False:
                    raise ValueError("Wrong matrix given")
            

        for t in range(i+1, len(input_matrix[0])):
            if input_matrix[t][i]!=0:
                temp = -(input_matrix[t][i]/input_matrix[i][i])
                for j in range(i, len(input_matrix)):
                    identity[t][j] = identity[t][j] + (identity[i][j] * temp)
                    input_matrix[t][j]=input_matrix[t][j] + (input_matrix[i][j] * temp)

    print("--------------------------------------------")
    print("Input Matrix After Guassian Elimination: \n", input_matrix)
    print("Identity matrix : \n", identity)

    for j in range(len(input_matrix)-1, -1, -1):
        for i in range(j-1, -1, -1):
            if (input_matrix[i][j] != 0) :
                temp= -(input_matrix[i][j]/input_matrix[j][j])
                for w in range(len(identity)-1, -1, -1):
                    identity[i][w] = identity[i][w] + (identity[j][w] * temp)
                input_matrix[i][j] = input_matrix[i][j] + (input_matrix[j][j] * temp)


    m = np.zeros((4, 4))
    for i in range(len(input_matrix)):
        m[i][i] = (1/input_matrix[i][i])
        input_matrix[i][i]=1


    reverse = []
    for i in range(len(m)):
        reverse.append([identity[i]*m[i][i]])

    print("Input Matrix : \n", input_matrix)
    print("Reversed Matrix : \n", reverse)

inversion(input_matrix)

print("\n","*"*30)
input_matrix = np.array([[0, 0, 2, 3], [0, -1, 1, 3], [1, 3, -1, 0], [1, 2, 0, 0]])
identity = np.identity(4)
inversion(input_matrix)