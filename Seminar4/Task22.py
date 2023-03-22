from random import randint

list_1 = [int(input()) for _ in range(int(input('Введите количество элементов во втором наборе: ')))]
list_2 = [int(input()) for _ in range(int(input('Введите количество элементов в первом наборе: ')))]

list_res = set(list_1) & set(list_2)
if len(list_res) > 0:
    print(*list_res)
else:
    print('У наборов целых чисел нет пересечений!')