from random import randint

n = 5

bushes = [{i: randint(1, 10)} for i in range(1, n + 1)]
print(bushes)
# res_dict = dict()
# for i in range(n):
#     if i > 0 and (i + 1) < n:
#         #print(bushes[(i - 1) : (i + 2)])
#         res_dict[i + 1] = sum(bushes[(i - 1) : (i + 2)])
#     elif i == 0:
#         #print(bushes[:i + 2], bushes[n - 1])
#         res_dict[i + 1] = sum(bushes[:i + 2]) + bushes[n - 1]
#     else:
#         #print(bushes[i - 1:], bushes[0])
#         res_dict[i + 1] = sum(bushes[i - 1:]) + bushes[0]

# max_berry = max(res_dict.values())

#print('Максимальное количество собираемых ягод:', max_berry)