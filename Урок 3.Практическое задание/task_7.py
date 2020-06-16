"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
from random import randint

my_list = []
num_elem = int(input('Введите количество элементов в массиве: '))
for i in range(num_elem):
    my_list.append(randint(-100, 100))
print('Исходный массив: {}'.format(my_list))
if my_list[0] > my_list[1]:
    ind_min_1 = 0
    ind_min_2 = 1
else:
    ind_min_1 = 1
    ind_min_2 = 0

for i in range(2, len(my_list)):
    # print(i,my_list[i])

    if my_list[i] < my_list[ind_min_1]:
        box = ind_min_1
        ind_min_1 = i
        if my_list[box] < my_list[ind_min_2]:
            ind_min_2 = box
    elif my_list[i] < my_list[ind_min_2]:
        ind_min_2 = i
print('Первый наименьший элемент: {}'.format(my_list[ind_min_1]))
print('Второй наименьший элемент: {}'.format(my_list[ind_min_2]))
