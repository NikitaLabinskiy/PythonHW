# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

if 1 <= quarter <=4 :
    if quarter == 1:
        print(f'Диапозон по оси X от {1} до {float("inf")} \nДиапозон по оси Y > от {1} до {float("inf")}')
    if quarter == 2:
        print(f'Диапозон по оси X > от {-1} до {float("-inf")} \nДиапозон по оси Y > от {1} до {float("inf")}')
    if quarter == 3:
        print(f'Диапозон по оси X > от {-1} до {float("-inf")} \nДиапозон по оси Y > от {-1} до {float("-inf")}')
    if quarter == 4:
        print(f'Диапозон по оси X > от {1} до {float("inf")} \nДиапозон по оси Y > от {-1} до {float("-inf")}')
else:
    print('Координаты не подходят!')