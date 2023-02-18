import process_game
import os
def clear(): return os.system('cls')
clear()


def Game(type_game):
    if type_game == 1:
        process_game.Player_vs_Player()
    else:
        process_game.Player_vs_Bot()

type_game = int(input('Введите 1 если хотите играть с игроком, и любую другую цифру, если хотите играть с ботом: '))

Game(type_game)