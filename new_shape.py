import pygame
import shapes

class NewShape(object):
    def __init__(self):
        self.shape = []
        self.full_shape = []
        self.row = ""

    def save_shape(self, grid):
        empty = True
        for i in range(0, 4):
            self.row = ""
            for j in range(0, 4):
                if grid.select[i][j] != grid.main_color:
                    self.row = self.row + "1"
                    empty = False
                else:
                    self.row = self.row + "0"
            self.shape.append(self.row)
        if empty is True:
            self.shape.clear()
            self.row = ""
        else:
            for i in range(0, 4): # na razie bez obracania
                self.full_shape.append(self.shape)
            print(self.full_shape)
            shapes.shapes.append(self.full_shape)

        return empty