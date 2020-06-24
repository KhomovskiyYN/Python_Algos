"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
my_list = input('Введите исходный массив: ')
my_list = my_list.split()
my_list = [int(i) for i in my_list]
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
'''
в программе не учтено наличие дублей в списке
'''
print(my_list)
my_list[max_ind],my_list[min_ind] = my_list[min_ind], my_list[max_ind]

print(my_list)




