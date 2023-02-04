# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
amount_of_ellements = int(input('Введите количество эллементов: '))
spisok = []
for i in range(amount_of_ellements):
    spisok.append(int(input('Введите эллемент списка: ')))

count = 0
for i in range(amount_of_ellements):
    if i % 2 != 0:
        count += spisok[i]
print(f'Сумма всех четных эллементов = {count}')