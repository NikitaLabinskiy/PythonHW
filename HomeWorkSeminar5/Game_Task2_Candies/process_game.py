from random import randint
import functions


def Player_vs_Player():
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')
    candies = int(input('Введите количество конфет: '))
    max_move = 28
    count_for_check_win = candies // max_move
    determining_move = randint(0, 1)
    win = False
    while not win:
        if determining_move % 2 == 0:
            candies = functions.Take_the_candy(name_first_player, candies, max_move)
        else:
            candies = functions.Take_the_candy(name_second_player, candies, max_move)
        if determining_move >= count_for_check_win - 1:
            winner = functions.check_winner(candies, determining_move, name_first_player, name_second_player)
            if winner:
                print(f'Победу одержал - {winner}')
                win = True
        determining_move += 1

def Player_vs_Bot():
    name_first_player = input('Введите ваше имя: ')
    name_second_player = 'Bot'
    candies = int(input('Введите количество конфет: '))
    max_move = 28
    count_for_check_win = candies // max_move
    determining_move = randint(0, 1)
    win = False
    while not win:
        if determining_move % 2 == 0:
            candies = functions.Take_the_candy(name_first_player, candies, max_move)
        else:
            candies = functions.move_bot(candies, max_move)
        if determining_move >= count_for_check_win:
            winner = functions.check_winner(candies, determining_move, name_first_player, name_second_player)
            if winner:
                print(f'Победу одержал - {winner}')
                win = True
        determining_move += 1