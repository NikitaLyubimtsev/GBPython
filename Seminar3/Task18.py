from random import randint

n = int(input('Введите количество натуральных чисел в массиве: '))
# nums = [randint(1, 10) for n in range(0, n)]
# print(nums)
nums = [int(input('Введите следующее число: ')) for _ in range(0, n)]
x = int(input('Введите искомое в массиве, натуральное чисело: '))

cur_num = 0
for n in nums:
    if n < x and cur_num < n:
        cur_num = n

print(cur_num)
