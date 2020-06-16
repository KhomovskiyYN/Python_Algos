"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
# много лишних переменных - потом оптимизировать!

def my_row(n, origin_num, score, result_num):

    if n == 0:
        return print('Количество элементов - {}, их сумма - {}'.format(score, result_num))
    else:
        result_num += origin_num
        origin_num  = (origin_num / (-2))
        n -= 1
        score +=1
        return my_row(n, origin_num, score, result_num)

score = 0
origin_num = 1
result_num = 0
n = int(input('Введите количество элементов: '))
my_row(n, origin_num, score, result_num)