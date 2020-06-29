"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random

size = int(input('Введите число элементов: '))
array = [round(random.uniform(0, 50), 7) for _ in range(size)]
print('Исходный - ',array)

def merge(left, right):
    result = [0] * (len(left) + len(right))
    i = k = n = 0
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result[n] = left[i]; i += 1; n += 1
        else:
            result[n] = right[k]; k += 1; n += 1
    while i < len(left):
        result[n] = left[i]; i += 1; n += 1
    while k < len(right):
        result[n] = right[k]; k += 1; n += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return
    middle = len(array) // 2
    left = [array[i] for i in range(0, middle)]
    right = [array[i] for i in range(middle,len(array))]
    merge_sort(left)
    merge_sort(right)
    res = merge(left, right)
    for i in range(len(array)):
        array[i] = res[i]

merge_sort(array)
print('Отсортированный - ', *array)

'''array.sort()
print(array)'''


'''def merge(left, right):
    result_ = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result_.append(left[i])
            i += 1
        else:
            result_.append(right[j])
            j += 1
    result_ += left[i:] + right[j:]
    return result_


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
    return merge(merge_sort(left), merge_sort(right))


sorted_ = merge_sort(array)
print(sorted_)'''