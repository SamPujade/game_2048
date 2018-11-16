import tkinter as tk
from grid_2048 import *
from copy import deepcopy

TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078",
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b",
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92",
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = {"Verdana", 40, "bold"}

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def graphical_grid_init_2048():

    root = tk.Tk()
    root.title('2048')
    global window
    window = tk.Toplevel(root)
    window.title('2048')

    tk.Label(root, text="Choose grid size").pack()
    spinbox_grid_size = tk.Spinbox(root, from_=2, to=10)
    spinbox_grid_size.delete(0, "end")
    spinbox_grid_size.insert(0, 4)
    spinbox_grid_size.pack()
    tk.Label(root, text="Choose a theme").pack()
    list_of_themes = tk.Listbox(root)
    list_of_themes.insert(0, "Default")
    list_of_themes.insert(1, "Chemistry")
    list_of_themes.insert(2, "Alphabet")
    list_of_themes.select_set(0)
    list_of_themes.pack()

    def start_game():

        global window
        window.destroy()
        window = tk.Toplevel(root)
        window.title('2048')
        background = tk.PanedWindow(window)
        background.pack(side=tk.RIGHT)
        side_of_background = tk.PanedWindow(window, width=100)
        side_of_background.pack(side=tk.LEFT)
        global score
        score = ""
        score_label = tk.Label(side_of_background, text="Score: "+str(score))
        score_label.pack()
        tk.Label(side_of_background, text=100*" ").pack()

        theme = THEMES[str(list_of_themes.curselection()[0])]
        grid_size_2048 = int(spinbox_grid_size.get())
        global grid_game
        grid_game = blank_to_zero(init_game(grid_size_2048))
        global grid_game_before_undo
        grid_game_before_undo = deepcopy(grid_game)
        graphical_grid = [[0 for i in range(grid_size_2048)] for j in range(grid_size_2048)]

        def display_and_update_graphical_grid(frame, number):
            frame.config(bg=TILES_BG_COLOR[number])
            tk.Label(frame, text=theme[number], bg=TILES_BG_COLOR[number], fg=TILES_FG_COLOR[number], width=int(80/grid_size_2048), height=int(40/grid_size_2048), font=TILES_FONT).grid(row=0, column=0)

        for i in range(grid_size_2048):
            for j in range(grid_size_2048):
                new_frame = tk.Frame(background, bg=TILES_BG_COLOR[0], bd=1, relief='groove')
                new_frame.grid(row=i, column=j)
                display_and_update_graphical_grid(new_frame, grid_game[i][j])
                graphical_grid[i][j] = new_frame

        def key_pressed(event):
            global score, grid_game, grid_game_before_undo
            grid_game_before_undo = deepcopy(grid_game)
            flag = False
            if event.keycode == 37 and move_possible(grid_game)[0]:  # left
                grid_game = move_grid(grid_game, 'left')
                flag = True
            if event.keycode == 39 and move_possible(grid_game)[1]:  # right
                grid_game = move_grid(grid_game, 'right')
                flag = True
            if event.keycode == 38 and move_possible(grid_game)[2]:  # up
                grid_game = move_grid(grid_game, 'up')
                flag = True
            if event.keycode == 40 and move_possible(grid_game)[3]:  # down
                grid_game = move_grid(grid_game, 'down')
                flag = True
            if flag:
                grid_game = grid_add_new_tile(grid_game)
                score = 0
                for i in range(grid_size_2048):
                    for j in range(grid_size_2048):
                        display_and_update_graphical_grid(graphical_grid[i][j], grid_game[i][j])
                        score += grid_game[i][j]
                score_label.config(text="Score: "+str(score))
                if is_game_over(grid_game):
                    window_game_over = tk.Toplevel(window)
                    window_game_over.title("Game over")
                    game_over = tk.Label(window_game_over, text="You lose!", bg='black', fg='white')
                    game_over.config(font=("Courier", 70))
                    game_over.grid()

        def undo():
            global grid_game, grid_game_before_undo, score
            grid_game = deepcopy(grid_game_before_undo)
            score = 0 
            for i in range(grid_size_2048):
                for j in range(grid_size_2048):
                    display_and_update_graphical_grid(graphical_grid[i][j], grid_game[i][j])
                    score += grid_game[i][j]
            score_label.config(text="Score: "+str(score))

        undo_button = tk.Button(side_of_background, text="Undo", command=undo)
        undo_button.pack()

        window.bind("<KeyPress>", key_pressed)

    button_quit = tk.Button(root, text="Quit", command=quit)
    button_quit.pack(side=tk.LEFT)
    button_play = tk.Button(root, text="Play", command=start_game)
    button_play.pack(side=tk.RIGHT)

    root.mainloop()


graphical_grid_init_2048()
