"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
# Python 3.8.3
# 64 - бит
'''
Для тестирования возьму задачу 2 урока 3:
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.'''

from memory_profiler import profile
from random import randint

@profile
def test():
    even = []
    my_list = [randint(0,100) for i in range(100000)]

    for i in range(len(my_list)):
        if  my_list[i] % 2 ==0:
            even.append(i)
    print(even)
test()

'''
Line #    Mem usage    Increment   Line Contents
================================================
    19     10.7 MiB     10.7 MiB   @profile
    20                             def test():
    21     10.7 MiB      0.0 MiB       even = []
    22     11.5 MiB      0.1 MiB       my_list = [randint(0,100) for i in range(100000)]
    23                             
    24     14.1 MiB      0.0 MiB       for i in range(len(my_list)):
    25     14.1 MiB      0.0 MiB           if  my_list[i] % 2 ==0:
    26     14.1 MiB      0.3 MiB               even.append(i)
    27     14.8 MiB      0.7 MiB       print(even)
    
Имеем: увеличение памяти при создании первоначального списка, 
при добавлении в пустой список результата 
и при выводе
'''
# Заменим цыкл на вложенный:

@profile
def test_1():
    my_list = [randint(0,100) for i in range(100000)]

    even = [ind for ind, i in enumerate(my_list) if i % 2 ==0]
    print(even)

test_1()


'''
Line #    Mem usage    Increment   Line Contents
================================================
    56     14.7 MiB     14.7 MiB   @profile
    57                             def test_1():
    58     14.8 MiB      0.0 MiB       my_list = [randint(0,100) for i in range(100000)]
    59                             
    60     14.8 MiB      0.0 MiB       even = [ind for ind, i in enumerate(my_list) if i % 2 ==0]
    61     14.8 MiB      0.0 MiB       print(even)

Тут почему то результат тот же, но если убрать первое решение получается :

Line #    Mem usage    Increment   Line Contents
================================================
    56     10.7 MiB     10.7 MiB   @profile
    57                             def test_1():
    58     11.5 MiB      0.1 MiB       my_list = [randint(0,100) for i in range(100000)]
    59                             
    60     14.1 MiB      0.3 MiB       even = [ind for ind, i in enumerate(my_list) if i % 2 ==0]
    61     14.8 MiB      0.7 MiB       print(even)

такой же результат.
можно убрать принти и выиграть 0.7 MiB
'''

# вложил исходный список в генератор списка, добавил enumerate вместо принта сделал return

@profile
def test_2():

    even = [ind for ind, i in enumerate([randint(0,100) for i in range(100000)]) if i % 2 ==0]
    return even
test_2()

'''
почему то напротив декоратора @profile как будто результат предыдущих расчетов,
Line #    Mem usage    Increment   Line Contents
================================================
    56     14.7 MiB     14.7 MiB   @profile
    57                             def test_1():
    58     14.8 MiB      0.0 MiB       my_list = [randint(0,100) for i in range(100000)]
    59                             
    60     14.9 MiB      0.0 MiB       even = [ind for ind, i in enumerate(my_list) if i % 2 ==0]
    61     14.9 MiB      0.0 MiB       print(even)
    
 и если их убрать, то получается: 
 
 Line #    Mem usage    Increment   Line Contents
================================================
    92     10.7 MiB     10.7 MiB   @profile
    93                             def test_2():
    94                             
    95     14.1 MiB      0.3 MiB       even = [ind for ind, i in enumerate([randint(0,100) for i in range(100000)]) if i % 2 ==0]
    96     14.1 MiB      0.0 MiB       return even
    (с чем может это быть связанно?)
    Улучшение на 0,7 - 0,8 MiB 
'''
