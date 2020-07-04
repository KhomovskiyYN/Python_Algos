"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""
import hashlib

def count_sub(my_str):
    result = set()
    len_str = len(my_str)
    for i in range(len(my_str)):
        for j in range(len_str):
            if i < j:
                hash_ = hashlib.sha1(my_str[i:j].encode('utf-8')).hexdigest()
                if hash_ not in result:
                    result.add(hash_)
                    print(f'{my_str[i:j]}')
        len_str = len(my_str) + 1

    return len(result)


my_str = str(input('Введите строку: '))
print(f'Итог: {count_sub(my_str)} подстрок')