"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
from random import randint

my_list = []
num_elem = int(input('Введите количество элементов в массиве: '))
for i in range(num_elem):
    my_list.append(randint(0, 100))
print('Массив: {}'.format(my_list))

min_list = my_list[0]
min_ind = 0
max_list = my_list[0]
max_ind = 0

for i in range(1,len(my_list)):
    if  my_list[i]> max_list:
        max_list = my_list[i]
        max_ind = i
    if  my_list[i] < min_list:
        min_list = my_list[i]
        min_ind = i

# print(max_ind,max_list, min_ind, min_list)
count = 0

if max_ind < min_ind:
    elem = max_ind + 1
    while elem < min_ind:
        count += my_list[elem]
        elem +=1

elif max_ind > min_ind:
    elem = min_ind + 1
    while elem < max_ind:
        count += my_list[elem]
        elem += 1
print('Сумма элементов между минимальным ({})  и максимальным ({}) элементами: {}'.format(min_list, max_list, count))