import random as rd
import numpy as np

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

# Définition des fonctions

#créé une grille vide
def create_grid(grid_length):
    game_grid = []
    for i in range(grid_length):
        game_grid.append([' ' for k in range(grid_length)])
    return game_grid

#donne une valeur à la nouvelle tuile
def get_value_new_tile():
    aleat = rd.randrange(10)
    if aleat == 0:
        tile_value = 4
    else:
        tile_value = 2
    return tile_value

#donne les valeurs de toutes les tuiles, avec comme convention 0 si il n'y a pas de tuile sur la case
def get_all_tiles(game_grid):
    list_of_tiles = []
    for line in game_grid:
        for case in line:
            if case == ' ':
                list_of_tiles.append(0)
            else:
                list_of_tiles.append(case)
    return list_of_tiles

#donne l'emplacement des cases vides
def get_empty_tiles_positions(game_grid):
    grid_length = len(game_grid)
    list_of_empty_tiles_positions = []
    list_of_tiles = get_all_tiles(game_grid)
    for k in range(len(list_of_tiles)):
        if list_of_tiles[k] == 0:
            x = k // grid_length
            y = k % grid_length
            list_of_empty_tiles_positions.append((x,y))
    return list_of_empty_tiles_positions

#donne la position d'une case libre
def get_new_position(game_grid):
    list_of_empty_tiles_positions = get_empty_tiles_positions(game_grid)
    list_length = len(list_of_empty_tiles_positions)
    aleat = rd.randrange(list_length)
    return list_of_empty_tiles_positions[aleat]

#donne la valeur de la case en la position donnée
def grid_get_value(grid,x,y):
    if grid[x][y] == ' ':
        return 0
    else:
        return grid[x][y]

#ajoute une tuile à la grille
def grid_add_new_tile(game_grid):
    x,y = get_new_position(game_grid)
    tile_value = get_value_new_tile()
    game_grid[x][y] = tile_value
    return game_grid

#créé une grille et ajoute 2 tuiles à l'espace de jeu
def init_game(grid_length):
    game_grid = create_grid(grid_length)
    for i in range(2):
        game_grid = grid_add_new_tile(game_grid)
    return game_grid



#Affichage de la grille

#Converti les 0 en ' '
def zero_to_blank(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = ' '
    return grid

#Converti les ' ' en 0
def blank_to_zero(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ' ':
                grid[i][j] = 0
    return grid

#retourne la taille de la plus grande chaine de caractère de la grille
def long_value(game_grid):
    list_length = len(game_grid)
    length=0
    for i in range(list_length):
        for j in range(list_length):
            if len(str(game_grid[i][j])) > length:
                length = len(str(game_grid[i][j]))
    return length

#Conversion tableau -> grille
def grid_to_string(game_grid):
    n = max(4,long_value(game_grid)+3)
    list_length = len(game_grid)
    game_grid_copy = [[' ' for j in range(list_length)] for i in range(list_length)]
    for i in range(list_length):
        for j in range(list_length):
            m = len(str(game_grid[i][j]))
            if game_grid[i][j] == ' ':
                game_grid_copy[i][j] = (n-3)*' '
            else:
                game_grid_copy[i][j]=(n-m-3)//2*' '+str(game_grid[i][j])+(n-m-2)//2*' '
    string = """ """
    for i in range(list_length):
        string += """
         """
        for j in range(list_length):
            string += (n-1)*"="+" "
        string += """
        | """
        for j in range(list_length):
            string = string + str(game_grid_copy[i][j]) + " | "
    string += """
         """
    for j in range(list_length):
            string += (n-1)*"="+" "
    return string

#conversion tableau -> grille en prenant en compte les thèmes
def grid_to_string_with_size_and_theme(game_grid,theme):
    n = max(4,long_value(game_grid)+3)
    list_length = len(game_grid)
    game_grid_copy = [[' ' for j in range(list_length)] for i in range(list_length)]
    for i in range(list_length):
        for j in range(list_length):
            m = len(str(theme[(game_grid[i][j])]))
            if game_grid[i][j] == ' ':
                game_grid_copy[i][j] = (n-3)*' '
            else:
                game_grid_copy[i][j]=(n-m-3)//2*' '+str(theme[(game_grid[i][j])])+(n-m-2)//2*' '
    string = """ """
    for i in range(list_length):
        string += """
         """
        for j in range(list_length):
            string += (n-1)*"="+" "
        string += """
        | """
        for j in range(list_length):
            string = string + str(game_grid_copy[i][j]) + " | "
    string += """
         """
    for j in range(list_length):
            string += (n-1)*"="+" "
    return string



#Gestion des déplacements

#déplacement à gauche
def move_row_left(line):
    n = len(line)
    fusion = [True for k in range(n)] #liste des cases pouvant fusionner (False si il y a deja eu une fusion)
    for i in range(1,n):
        k = i
        while k > 0 and line[k-1] == 0:
            k -= 1
        line[k],line[i] = line[i],line[k]
        if k > 0 and line[k-1] == line[k] and fusion[k-1]:
            line[k-1],line[k] = 2*line[k],0
            fusion[k-1] = False
    return line


#déplacement à droite
def move_row_right(line):
    n = len(line)
    fusion = [True for k in range(n)] #liste des cases pouvant fusionner (False si il y a deja eu une fusion)
    for i in range(n-1,-1,-1):
        k = i
        while k < n-1 and line[k+1] == 0 :
            k += 1
        line[k],line[i] = line[i],line[k]
        if k < n-1 and line[k+1] == line[k] and fusion[k+1]:
            line[k+1],line[k] = 2*line[k],0
            fusion[k+1] = False
    return line

#déplacement à droite avec commande
def move_grid(grid, move):
    grid_length = len(grid)
    if move == "left":
        for i in range(grid_length):
            grid[i] = move_row_left(grid[i])
    if move == "right":
        for i in range(grid_length):
            grid[i] = move_row_right(grid[i])
    if move == "up":
        grid = np.transpose(grid)
        for i in range(grid_length):
            grid[i] = move_row_left(grid[i])
        grid = np.transpose(grid)
    if move == "down":
        grid = np.transpose(grid)
        for i in range(grid_length):
            grid[i] = move_row_right(grid[i])
        grid = np.transpose(grid)
    grid = [[grid[i][j] for j in range(grid_length)] for i in range(grid_length)]
    return grid

#Teste si la grille est pleine ou non
def is_grid_full(grid):
    return 0 not in get_all_tiles(grid)

#Teste si un mouvement est possible
def move_possible(grid):
    liste = []
    for d in ["left", "right", "up", "down"]:
        grid_copy = np.copy(grid)
        grid_copy2 = np.copy(grid)
        if np.array_equal(np.copy(move_grid(grid_copy2,d)),grid_copy):
            liste.append(False)
        else:
            liste.append(True)
    return liste


#Teste si le jeu est terminé
def is_game_over(grid):
    if is_grid_full(grid):
        return move_possible(grid) == [False, False, False, False]
    else:
        return False

#Donne la valeur de la tuile max
def get_grid_tile_max(grid):
    return max(get_all_tiles(grid))

