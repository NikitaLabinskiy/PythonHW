# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
amount_of_ellements = int(input('Введите количество элементов: '))
spisok = []
for i in range(amount_of_ellements):
    spisok.append(int(input('Введите элемент списка: ')))
i1 = 0
i2 = -1
result_spisok = []
for i1 in range(math.ceil(amount_of_ellements / 2)):
    result_spisok.append(spisok[i1]*spisok[i2])
    i2 -= 1
print(f'Сумма элементов = {result_spisok}')
