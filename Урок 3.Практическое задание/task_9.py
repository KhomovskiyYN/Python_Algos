"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
import random
M = int(input('Задайте количество столбцов в матрице:'))
N = int(input('Задайте количество строк в матрице:'))
matrix = [[random.randrange(0,10) for y in range(M)] for x in range(N)]
for i in range(N):
   print (matrix[i])

maxim = -100
for i in range(M):
    minim = 1000
    for j in range(N):
        if matrix[j][i] < minim:
            minim = matrix[j][i]
            #print(minim)
    if minim > maxim:
        maxim = minim
print('Максимальное среди них = {}'.format(maxim))