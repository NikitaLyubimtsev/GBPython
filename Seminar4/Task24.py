from random import randint

bushes = [randint(15, 40) for i in range(int(input('Введите количество кустов: ')))]
# Преобразуем список присоединяя крайние элементы
full_bushes = bushes[-1:] + bushes + bushes[:1]
# Суммируемые элементы и ищем максимальный по значению из элемент списка
max_berry = max([sum(full_bushes[(i - 1) : (i + 2)]) for i in range(1, (len(bushes) + 1))])

print('Максимальное возможное количество ягод:', max_berry)