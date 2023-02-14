# Создайте программу для игры в ""Крестики-нолики"".
import os
def clear(): return os.system('cls')
clear()


def Print_Game_Board(board):
    print('-------------')
    for i in range(3):
        print(
            f"| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |")
        print('-------------')


def Fill_the_Game_Board(Player_Token):
    empty_place = True
    while empty_place:
        value = int(input('Заполните свободное место от 1 до 9: ' + Player_Token + ': '))
        if 1 < value > 9:
            print('Ошибка ввода места!')
            continue
        # value = int(value)
        if str(board[value - 1]) in ('XO'):
            print('Место занято')
            continue
        else:
            board[value - 1] = Player_Token
            empty_place = False


def Check_Winner(board):
    winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for each in winning_combinations:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return (board[each[1] - 1])
    else:
        return False


def Main(board):
    torn = 0
    while True:
        Print_Game_Board(board)
        if torn % 2 == 0:
            Fill_the_Game_Board("X")
        else:
            Fill_the_Game_Board("O")
        torn += 1
        if torn > 4:
            temp = Check_Winner(board)
            if temp:
                Print_Game_Board(board)
                print(f'Winner - {temp}')
                break
        if torn >= 9:
            Print_Game_Board(board)
            print('Ничья!')
            break


board = list(range(1, 10))

print(Main(board))
