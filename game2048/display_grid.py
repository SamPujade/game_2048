import tkinter as tk
from grid_2048 import *

TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = {"Verdana", 40, "bold"}


def graphical_grid_init_2048():

    root = tk.Tk()
    root.title('2048')
    window = tk.Toplevel(root)
    window.title('2048')

    grid_size_2048 = 4
    global grid_game
    grid_game = blank_to_zero(init_game(grid_size_2048))

    background = tk.Frame(window)
    background.pack()
    graphical_grid = [[0 for i in range(grid_size_2048)] for j in range(grid_size_2048)]

    def display_and_update_graphical_grid(frame, number):
        frame.config(bg=TILES_BG_COLOR[number])
        tk.Label(frame, text=number, bg=TILES_BG_COLOR[number], fg=TILES_FG_COLOR[number], width=20, height=10).grid(row=0, column=0)

    for i in range(grid_size_2048):
        for j in range(grid_size_2048):
            new_frame = tk.Frame(background, bg=TILES_BG_COLOR[0], bd=1, relief='groove')
            new_frame.grid(row=i, column=j)
            display_and_update_graphical_grid(new_frame, grid_game[i][j])
            graphical_grid[i][j] = new_frame

    def key_pressed(event):
        global grid_game
        flag = False
        if event.keycode == 37 and move_possible(grid_game)[0]: #left
            grid_game = move_grid(grid_game, 'left')
            flag = True
        if event.keycode == 39 and move_possible(grid_game)[1]: #right
            grid_game = move_grid(grid_game, 'right')
            flag = True
        if event.keycode == 38 and move_possible(grid_game)[2]: #up
            grid_game = move_grid(grid_game, 'up')
            flag = True
        if event.keycode == 40 and move_possible(grid_game)[3]: #down
            grid_game = move_grid(grid_game, 'down')
            flag = True
        if flag:
            grid_game = grid_add_new_tile(grid_game)
            for i in range(grid_size_2048):
                for j in range(grid_size_2048):
                    display_and_update_graphical_grid(graphical_grid[i][j], grid_game[i][j])
            if is_game_over(grid_game):
                print("Perdu!")
            print(move_possible(grid_game))
            print(grid_game)

    window.bind("<KeyPress>", key_pressed)

    root.mainloop()


graphical_grid_init_2048()
