"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
my_list = input('Введите исходный массив: ')
my_list = my_list.split()
my_list = [int(i) for i in my_list]

counter = [0, 0]

for i in sorted(my_list):
    cnt = sorted(my_list).count(i)
    if cnt > counter[1]:
        counter = [i, cnt]

print(f'В списке {my_list}\n'
      f'самое частое число {counter[0]}. Оно встречается {counter[1]} раз.')