from random import randint

n = int(input('Введите количество натуральных чисел в массиве: '))
# nums = [randint(1, 10) for n in range(0, n)]
nums = [int(input()) for _ in range(0, n)]
x = int(input('Введите искомое в массиве, натуральное чисело: '))
count = 0

for n in nums:
    if n == x:
        count += 1

print(count)