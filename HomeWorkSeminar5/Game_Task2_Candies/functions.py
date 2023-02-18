from random import randint


def Take_the_candy(name_player, candies, max_move):
    torn = True
    while torn: 
        print(f'Осталось {candies} конфет!')
        move = int(input(f'{name_player}, cколько конфет берете от 1 до 28?: '))
        if move == str:
            print(f'Введены некорректные данные, введите число от 1 до {max_move}')
        if 0 < move <= max_move and move <= candies:
            print(f'Вы забрали {move} конфет!')
            candies -= move
            torn = False
        else:
            print('Количество взятых конфет должно быть не меньше 1 и не больше 28!')
    return candies

def move_bot(candies, max_move):
    print(f'Осталось {candies} конфет!')
    move = randint(1, max_move) if candies >= max_move else randint(1, candies)
    print(f'Бот забрали {move} конфет!')
    candies -= move
    return candies

def check_winner(candies, determining_move, first_name, second_name):
    if candies == 0:
        return first_name if determining_move % 2 == 0 else second_name
    else:
        return False
