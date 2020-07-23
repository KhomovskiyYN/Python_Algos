"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
"""
Задание_2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

# Первоначальный вид 2-ой задачи 3-го урока:
'''even = []
my_list = input('Введите исходный массив: ')
my_list = my_list.split()
my_list = [int(i) for i in my_list]
for i in range(len(my_list)):
    if  my_list[i] % 2 ==0:
        even.append(i)
print(even)
'''
# Чтобы каждый раз не вводить самому цыфры массива отредактировал:
even = []
from random import randint
my_list = [randint(0,100) for i in range(randint(0,10))]
for i in range(len(my_list)):
    if  my_list[i] % 2 ==0:
        even.append(i)
print(even)

# сделаем замер timeit:
print(timeit.timeit('''
even = []
from random import randint
my_list = [randint(0,100) for i in range(randint(0,10))]
for i in range(len(my_list)):
    if  my_list[i] % 2 ==0:
        even.append(i)
''',number=100000))


# Решение через генератор списка:
even_1 = [ind for ind, i in enumerate(my_list) if i % 2 == 0 ]
print(even_1)

# сделаем замер timeit:
print(timeit.timeit('''
from random import randint
my_list = [randint(0,100) for i in range(randint(0,10))]
even_1 = [ind for ind, i in enumerate(my_list) if i % 2 == 0 ]
''', number=100000))


# Решение через генератор списка без счетчика:
even_2 = [i for i in range((len(my_list))) if my_list[i] % 2 == 0]
print(even_2)

# сделаем замер timeit:
print(timeit.timeit('''
from random import randint
my_list = [randint(0,100) for i in range(randint(0,10))]
even_2 = [i for i in range((len(my_list))) if my_list[i] % 2 == 0]
''', number=100000))


"""
Через генератор списка получалось со счетчиком получилось быстрее (2 вариант), как и предполагалось

[0]
0.684879033
[0]
0.6355455289999999
[0]
0.6500459489999999

"""
