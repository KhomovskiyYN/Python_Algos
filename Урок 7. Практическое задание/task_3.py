"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from collections import Counter
from  random import randint
import math


size = 2 * randint(2,5)+ 1
array = [randint(-10,10) for _ in range(size)]
print(array)


def findMedian(array):
    myDict = Counter(array)
    median = len(array) // 2 + 1
    n = 0
    medianValue = 0

    while n < median:
        min = math.inf  # math.inf - возвращает положительную бесконечность
        for key, value in myDict.items():
            if key < min:
                min = key
        n += myDict[min]
        medianValue = min
        myDict.pop(min)
    return medianValue


median = findMedian(array)
print('Медиана: ', median)