from game2048.grid_2048 import *
from pytest import *

def test_move_possible():
    assert get_grid_tile_max([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == 16




if __name__=="__main__":
    test_move_possible()


