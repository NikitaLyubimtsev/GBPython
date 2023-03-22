from random import randint

n = int(input('Введите число монет: '))
money = [randint(0, 1) for _ in range(n)]

face = 0
for m in money:
    if m == 1:
        face += 1

print(face if face < (len(money)/2) else (len(money) - face))