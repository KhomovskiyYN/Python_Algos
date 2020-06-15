"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import randint

def guess_my_num(my_num, score):
    if score == 10:
        print('не уложились в 10 попыток! моё число было {}'.format(my_num))
        exit()
    your_choice = int(input('Угадай мое число : ' ))
    score += 1
    if your_choice == my_num:
        print('Success!!!')
        exit()
    elif your_choice < my_num:
        print('Моё число побольше будет')
        return guess_my_num(my_num, score)
    elif your_choice > my_num:
        print('Моё число поменьше будет')
        return guess_my_num(my_num, score)

score = 0
my_num = randint(0, 100)
guess_my_num(my_num, score)