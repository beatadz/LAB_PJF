from shapes import shape_colors
import random

class Piece(object):
    def __init__(self, column, row, shape):
        self.column = column
        self.row = row
        self.shape = shape
        self.color = shape_colors[random.randint(0, 6)]
        self.rotation = 0
        self.positions_list = []
        self.column_row_list = []