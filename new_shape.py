import pygame
import shapes

class NewShape(object):
    def __init__(self, grid):
        self.shape = []
        self.full_shape = []
        self.row = ""
        self.grid = grid
        self.new_shapes_colors = [[grid.main_color for x in range(4)] for y in range(4)]
        self.colors = []

    def save_shape(self, grid, nr):
        empty = True
        for i in range(0, 4):
            self.row = ""
            for j in range(0, 4):
                if grid.select[i][j] != grid.main_color:
                    self.new_shapes_colors[i][j] = grid.select[i][j]
                    self.colors.append(grid.select[i][j])
                    self.row = self.row + "1"
                    empty = False
                else:
                    self.row = self.row + "0"
            self.shape.append(self.row)
        if empty is True:
            self.shape.clear()
            self.row = ""
        else:
            shapes.new_colors.append(self.new_shapes_colors)

            for i in range(0, 4):
                self.full_shape.append(self.shape)
            #print(self.full_shape, shapes.shapes.count(self.full_shape))
            if shapes.shapes.count(self.full_shape) == 0:
                shapes.shapes.append(self.full_shape)
                shapes.colors.append(self.colors)
                # check if there are empty spaces between blocks
                for i in range(0, 4):
                    for j in range(0, 4):
                        if 0 < i < 3:
                            if 0 < j < 3:
                                if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and grid.select[i + 1][j] == grid.main_color and grid.select[i][j - 1] == grid.main_color and grid.select[i][j + 1] == grid.main_color:
                                    empty = True
                        elif i == 0:
                            if j == 0:
                                if grid.select[i][j] != grid.main_color and grid.select[i + 1][j] == grid.main_color and grid.select[i][j + 1] == grid.main_color:
                                    empty = True
                            elif j == 3:
                                if grid.select[i][j] != grid.main_color and grid.select[i + 1][j] == grid.main_color and grid.select[i][j - 1] == grid.main_color:
                                    empty = True
                        elif i == 3:
                            if j == 0:
                                if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and grid.select[i][j + 1] == grid.main_color:
                                    empty = True
                            if j == 0:
                                if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and grid.select[i][j - 1] == grid.main_color:
                                    empty = True

                if empty is False:
                    print("saved")
            else:
                empty = True
        return empty