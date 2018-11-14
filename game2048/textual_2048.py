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
            return size
        else:
            read_size_grid()
    except:
        read_size_grid()

#choix du thème
def read_theme_grid():
    theme=input("Choisissez votre theme (1 (nombres), 2 (chimie), 3 (alphabet)):")
    if theme in ['1','2','3']:
        return theme
    else:
        read_theme_grid()



