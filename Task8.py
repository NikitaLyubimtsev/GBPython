h, w, k = int(input('Введите высоту шоколадки в дольках: ')), int(input('Введите ширину шоколадки в дольках: ')), int(input('Введите количество долек: '))

if k < h * w and ((k % h == 0) or (k % w == 0)):
    print('yes')
else:
    print('no')