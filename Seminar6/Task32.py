from random import randint

arr = [randint(-50 , 50) for _ in range(30)]

min = int(input('Введите минимальный предел: '))
max = int(input('Введите максимальный предел: '))

res_idx_arr = [i for i in range(len(arr)) if min < arr[i] < max ]