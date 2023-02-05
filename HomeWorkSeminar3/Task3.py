# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spisok = [1.1, 1.2, 3.1, 5, 10.01]
spisok2 = []

for i in range(5):
    spisok[i] = float(spisok[i] - int(spisok[i]))
    spisok2.append(round(spisok[i], 2))

maxi = 0
mini = 1000000000000

for i in range(5):
    if spisok2[i] == 0:
        continue
    else:
        if maxi < spisok2[i]:
            maxi = round(spisok2[i], 2)
        if mini > spisok2[i]:
            mini = round(spisok2[i], 2)         
print(spisok2, end=" => ")
print(maxi - mini)

