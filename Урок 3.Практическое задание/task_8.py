"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
# на семинаре сказали, что можно зарандомить
import random
M,N = 4,5
matrix = [[random.randrange(0,10) for y in range(M)] for x in range(N)]
for i in range(N):
   print (matrix[i])

for i in range(5):
    sum_row = 0
    for j in range(4):
        sum_row +=matrix[i][j]
    matrix[i].append(sum_row)
for i in range(N):
   print (matrix[i])