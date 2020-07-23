"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def proof_equality_row(my_num, score):
    if my_num == 0:
        return print('1+2+...+n = {} '. format(score))
    else:
        score += my_num
        my_num -= 1
        return proof_equality_row(my_num, score)


score = 0
my_num = int(input('Введите n: '))
proof_equality_row(my_num, score)

print('n(n+1)/2 = {}'.format(int(my_num * (my_num + 1) / 2)))