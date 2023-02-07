# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
sequence = int(input('Введите длину последовательности: '))
nonrepeating_elements = []
repeating_elements = []

for i in range(sequence):
    number = random.randint(1, 10)
    repeating_elements.append(number)
    if number not in nonrepeating_elements:
        nonrepeating_elements.append(number)
print(f'Все элементы: {repeating_elements}')
print(f'Неповторяющиеся элементы: {nonrepeating_elements}')
