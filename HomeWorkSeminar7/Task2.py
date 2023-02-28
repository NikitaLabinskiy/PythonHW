# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y) 
# Вывод:
#  1  2  3  4  5  6
#  2  4  6  8 10 12
#  3  6  9 12 15 18
#  4  8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

import os
def clear(): return os.system('cls')
clear()

def Create_nested_list(size):
    board_list = [[0 for column in range(size)] for string in range(size)]
    return board_list

def Print_the_table(nested_list):
    for i in range(len(nested_list)):
        for j in range(len(nested_list)):
            nested_list[i][j] += (i + 1) * (j + 1)
            print(nested_list[i][j], end='\t')
        print('')
        print('')
    return nested_list

size = int(input('Введите размер таблицы: '))
print()

Print_the_table(Create_nested_list(size))