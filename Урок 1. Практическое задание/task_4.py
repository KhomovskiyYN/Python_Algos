"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""
from random import randrange, random
min_num = int(input('введите нижннюю границу'))
max_num = int(input('введите верхнюю границу'))
print('Случайное целое число в Вашем диапазоне = {}'.format(randrange(min_num,max_num)))
min_num = int(input('введите нижннюю границу'))
max_num = int(input('введите верхнюю границу'))
print('Случайное вещественное число в Вашем диапазоне = {}'.format((random() * (max_num - min_num) + min_num)))
print('для вывода букв от "a" до "z" использовать цифры от 0 до 27:')

min_num = int(input('введите нижннюю границу'))
max_num = int(input('введите верхнюю границу'))
print('Случайный символ в Вашем диапазоне = {}'.format(chr(ord('a') + randrange(min_num,max_num) - 1)))

