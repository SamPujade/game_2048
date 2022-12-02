# game_2048

This is an implementation of the game 2048 with a Tkinter interface.

## How to play

Access the game2048 folder : `cd game2048/`

### MVP version

For an MVP version that can be played with the terminal, launch `python play_2048.py`.
You then have to chose the size of the grid (`4` for a 4x4 grid) and the play theme (`1` for a classic theme).
```
$ python play_2048.py 
Choisissez la taille de la grille:4
Choisissez votre theme (1 (nombres), 2 (chimie), 3 (alphabet)):1
```

Here is how the interface looks like :

```
         === === === ===
        |   |   |   | 2 |
         === === === ===
        |   |   |   |   |
         === === === ===
        | 4 |   |   |   |
         === === === ===
        | 8 | 4 | 4 |   |
         === === === ===
Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):g
```

Select your move (`g` for left, `d` for right, `h` for up, `g` for down), then press Enter, and repeat it until the end of the game.

### Version with Tkinter interface

You can play with a graphic interface by running `python display_grid.py`. Select the grid size and the theme with the menu, then click `Play`.

<img width="101" alt="2048_select_menu" src="https://user-images.githubusercontent.com/60392311/205367772-fb3306d3-f5ff-488e-b690-6d3597be9136.PNG">

Here is how the graphic interface looks like : 

<img width="585" alt="2048" src="https://user-images.githubusercontent.com/60392311/205367833-48eb6b57-d37c-4649-85ae-04d62864e419.PNG">

You can play by using the regular arrows on your keyboard (↑ ↓ → ←). The button `Undo` allows you to cancel your last move.

## Other themes 

Here are some other play themes that you can use :
- Chemistry : using chemical element symbols instead of numbers (H, He, Li, Be...)
- Alphabet : using alphabet letters instead of numbers (A, B, C, D...)

<p float="left">
  <img width="341" alt="2048_chimie" src="https://user-images.githubusercontent.com/60392311/205368273-4db0c140-c42d-4411-bd98-49ae01b16726.PNG" width="100" />
  <img width="339" alt="2048_alphabet" src="https://user-images.githubusercontent.com/60392311/205368501-c29e5f5e-4bed-4d43-8916-0ed86e2882aa.PNG" width="100" /> 
</p>






