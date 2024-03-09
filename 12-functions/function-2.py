from random import randint
from os import system
def random2dArrays(rows,cols,range1,range2):
    matrix = []
    for ri in range (rows):
        row = []
        for ci in range (cols):
            row.append(randint(range1,range2))
        matrix.append(row)
    return matrix
#HW1 pass value range as arguments

#Hw2 add a header  showing  the size
def print2dArray(matrix):
    l = len(matrix)
    h = len(matrix[0])
    print(f"Size: {l} x {h}\n")
    for ri in range(len(matrix)):
        for ci in range(len(matrix[0])):
            print(f"{matrix[ri][ci]:5}",end='')
        print()
    print()
# HW3 create min max function  return them grupped
def average2dArray(matrix):
    s = 0
    l = len(matrix)
    h = len(matrix[0])
    allnums = []
    for ri in range(l):
        for ci in range(h):
            s+=matrix[ri][ci]            
            allnums.append(matrix[ri][ci])
    average = s / (l * h)
    min_m= min(allnums)
    max_m= max(allnums)
    avgMinMax = [average,min_m,max_m]
    return avgMinMax
system('cls')
columsR= 555
rowsR = 999
data = random2dArrays(5,4,columsR,rowsR)
print2dArray(data)
a=average2dArray(data)
print(f"average is: {a[0]}. minimum is {a[1]}, maximium is {a[2]} " )