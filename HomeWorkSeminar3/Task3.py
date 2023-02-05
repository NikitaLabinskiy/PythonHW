# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spisok = ['1.1', '1.2', '3.1', '5', '10.01']
# spisok_new = []
spisok2 = []
temp = 0

number = ('10.02')
number = float(number[::-1])
print((number))

# number = '110.15'
# result = '.'.join(number.split('.')[::-1])

for i in range(6):
    temp = float(spisok[i][::-1])
    if temp > 10:
        spisok2.append(int(temp) * 2)
    else:
        spisok2.append(int(temp))
    temp = 0
print(spisok2)