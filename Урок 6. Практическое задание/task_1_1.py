
'''
 Буду работать над:
Задание_5. урок 3	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
'''


from memory_profiler import profile
from random import randint
from timeit import timeit

'''@profile
def test():

    my_list = [randint(-100,100) for i in range(100000)]

    index = -1
    for i in range(len(my_list)):
        if my_list[i] < 0 and index == -1:
            index = i
        elif my_list[i] < 0 and my_list[i] > my_list[index]:
            index = i
    print('Максимальный отрицательный элемент в данном массиве = {}, его индекс {}'.format(my_list[index], index + 1))

test()'''

'''
     7     10.6 MiB     10.6 MiB   @profile
     8                             def test():
     9                             
    10     14.1 MiB      0.7 MiB       my_list = [randint(-100,100) for i in range(100000)]
    11                             
    12     14.1 MiB      0.0 MiB       index = -1
    13     14.1 MiB      0.0 MiB       for i in range(len(my_list)):
    14     14.1 MiB      0.0 MiB           if my_list[i] < 0 and index == -1:
    15     14.1 MiB      0.0 MiB               index = i
    16     14.1 MiB      0.0 MiB           elif my_list[i] < 0 and my_list[i] > my_list[index]:
    17     14.1 MiB      0.0 MiB               index = i
    18     14.1 MiB      0.0 MiB       print('Максимальный отрицательный элемент в данном массиве = {}, его индекс {}'.format(my_list[index], index + 1))
'''

@profile
def test_1(my_list):
    print( max([el for el in my_list if el < 0]))

test_1([randint(-100,100) for i in range(100000)])


'''
Вышло хуже:

Line #    Mem usage    Increment   Line Contents
================================================
    42     13.9 MiB     13.9 MiB   @profile
    43                             def test_1(my_list):
    44     14.3 MiB      0.2 MiB       print( max([el for el in my_list if el < 0]))
'''


# но по времени второй вариант работает быстрее:
print(timeit('''
from random import randint
def test():

    my_list = [randint(-100,100) for i in range(100000)]

    index = -1
    for i in range(len(my_list)):
        if my_list[i] < 0 and index == -1:
            index = i
        elif my_list[i] < 0 and my_list[i] > my_list[index]:
            index = i
    print('Максимальный отрицательный элемент в данном массиве = {}, его индекс {}'.format(my_list[index], index + 1))

test()
''',number=100))
# 9.099604712 сек

print(timeit('''
from random import randint

def test_1(my_list):
    print( max([el for el in my_list if el < 0]))

#my_list = [randint(-100,100) for i in range(100000)]

test_1([randint(-100,100) for i in range(100000)])

''',number=100))

# 8.142930109999998 сек