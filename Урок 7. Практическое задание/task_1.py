"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from  random import randint
from memory_profiler import profile
from timeit import timeit


#@profile()
def bubbleSort(some_list):
    for i in range(len(my_list)):
        for j in range(0, len(my_list)-i-1):
            if my_list[j] < my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    return my_list

my_list = [randint(-100,100) for _ in range(10)]
print('Исходный массив: ',my_list)
print('Отсортированный массив: ',bubbleSort(my_list))

print(timeit('''
from  random import randint
def bubbleSort(some_list):
    for i in range(len(my_list)):
        for j in range(0, len(my_list)-i-1):
            if my_list[j] < my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    return my_list

''',number=10000))


def bubbleSort_1(some_list):
    for i in range(len(my_list)):
        isNotOrdered = True
        while isNotOrdered:
            isNotOrdered = False
            for j in range(0, len(my_list)-i-1):
                if my_list[j] < my_list[j+1]:
                    my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
                    isNotOrdered = True
    return my_list

my_list = [randint(-100,100) for _ in range(10)]
print('Исходный массив: ',my_list)
print('Отсортированный массив: ',bubbleSort_1(my_list))

print(timeit('''
from  random import randint
def bubbleSort_1(some_list):
    for i in range(len(my_list)):
        isNotOrdered = True
        while isNotOrdered:
            isNotOrdered = False
            for j in range(0, len(my_list)-i-1):
                if my_list[j] < my_list[j+1]:
                    my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
                    isNotOrdered = True
    return my_list

''',number=10000))

# немного быстрее, в зависимости от первоначального массива