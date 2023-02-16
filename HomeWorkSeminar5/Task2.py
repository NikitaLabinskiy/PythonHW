# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
def clear(): return os.system('cls')
clear()

candis_bank = int(input('Введите количество конфет: '))


def Take_the_candy(candis):
    torn = True
    count = 0
    while candis > 0:
        if count % 2 == 0: 
            print(f'Осталось {candis} конфет!')
            move = int(input('Player_1 Сколько конфет берете от 1 до 28?: '))
            if 0 < move > 28:
                print('Введены некорректные данные!')
                continue
            candis -= move
            count += 1
            continue
        if count % 2 == 1:
            print(f'Осталось {candis} конфет!')
            move = int(input('Player_2 Сколько конфет берете от 1 до 28?: '))
            if 0 < move > 28:
                print('Введены некорректные данные!')
                continue
            candis -= move
            count += 1
            continue
    if candis == 0:
        if count % 2 == 0:
            print('Выиграл - Player_1')
        else:
            print('Выиграл - Player_2')
        
    
        
Take_the_candy(candis_bank)    

