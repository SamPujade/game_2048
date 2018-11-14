THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

#choix de mouvement du joueur
def read_player_command():
    move = ''
    while move not in ['g', 'd', 'h', 'b']:
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

#choix de la taille
def read_size_grid():
    size=input("Choisissez la taille de la grille:")
    try:
        if float(size) == int(size):
            return int(size)
        else:
            read_size_grid()
    except:
        read_size_grid()

#choix du thème
def read_theme_grid():

    theme=input("Choisissez votre theme (1 (nombres), 2 (chimie), 3 (alphabet)):")
    theme_list = [THEMES["0"],THEMES["1"],THEMES["2"]]
    if theme in ['1','2','3']:
        return theme_list[int(theme)-1]
    else:
        read_theme_grid()


