import random as rd
import numpy as np
from grid_2048 import *
from textual_2048 import *

#Partie de l'ordinateur qui joue aléatoirement
def random_play():

    grid_size = 4
    game_grid = init_game(grid_size)
    print(grid_to_string(game_grid))
    list_of_moves = ["left", "right", "up", "down"]

    while not is_game_over(game_grid):

        game_grid = blank_to_zero(game_grid)
        list_of_possible_move = []
        for i in range(4):
            if move_possible(game_grid)[i]:
                list_of_possible_move.append(list_of_moves[i])

        aleat = rd.randrange(0,len(list_of_possible_move))
        move = list_of_possible_move[aleat]
        game_grid = move_grid(game_grid,move)
        game_grid = grid_add_new_tile(game_grid)
        game_grid = zero_to_blank(game_grid)
        print(grid_to_string(game_grid))

    if get_grid_tile_max(game_grid) > 2048:
        print("AI wins!")
    else:
        print("AI loses!")


#Partie normale
def game_play():

    THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

    grid_size = read_size_grid()
    theme = read_theme_grid()

    game_grid = init_game(grid_size)
    game_grid = blank_to_zero(game_grid)
    print(grid_to_string_with_size_and_theme(game_grid,theme))
    list_of_moves = ["left", "right", "up", "down"]
    list_of_input_moves =["g", "d", "h", "b"]

    while not is_game_over(game_grid):

        #game_grid = blank_to_zero(game_grid)
        move = read_player_command()
        while not move_possible(game_grid)[list_of_input_moves.index(move)]:
            move = read_player_command()
        move = list_of_moves[list_of_input_moves.index(move)]
        game_grid = move_grid(game_grid,move)
        game_grid = grid_add_new_tile(game_grid)
        #game_grid = zero_to_blank(game_grid)
        print(grid_to_string_with_size_and_theme(game_grid,theme))

    if get_grid_tile_max(game_grid) > 2048:
        print("You win!")
    else:
        print("You lose!")

game_play()
