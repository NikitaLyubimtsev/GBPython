from random import randint
from math import sqrt

x, y = randint(1, 1000), randint(1, 1000)
sum, comp = x + y, x * y

desc = sum * sum - 4 * comp # находим дискриминант
if desc > 0: 
    sd = int(sqrt(desc))
    y = (sum + sd)/2
    print('X:', int(sum - y), 'Y:', int(y))
else:
    print('Ошибка данных, у урованения нет корней!')