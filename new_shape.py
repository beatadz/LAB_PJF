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
        self.correct = True
        self.check_r = True

        self.count = 0

    def save_shape(self, grid, nr):
        empty = True
        for i in range(0, 4):
            self.row = ""
            for j in range(0, 4):
                if grid.select[i][j] != grid.main_color:
                    self.new_shapes_colors[i][j] = grid.select[i][j]
                    self.colors.append(grid.select[i][j])
                    self.row = self.row + "1"
                    self.count += 1
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
                    self.check_r = True
                    for j in range(0, 4):
                        self.check_c = True
                        if self.count > 1:

                            if 0 < i < 4:
                                r = 0
                                if 0 < j < 3:
                                    if r > 0:
                                        if grid.select[i][j] != grid.main_color and not (grid.select[i - 1][j] == grid.main_color
                                                                                         and grid.select[i - 1][j - 1] == grid.main_color
                                                                                         and grid.select[i - 1][j + 1] == grid.main_color):
                                            self.check_r = False
                            if 0 < i < 3:
                                for k in range(0, i - 1):
                                    for l in range(0, 4):
                                        if grid.select[i][j] != grid.main_color:
                                            r = 1
                                if 0 < j < 3:
                                    if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and grid.select[i + 1][j] == grid.main_color \
                                            and grid.select[i][j - 1] == grid.main_color and grid.select[i][j + 1] == grid.main_color and grid.select[i + 1][j + 1] == grid.main_color\
                                            and grid.select[i - 1][j - 1] == grid.main_color and grid.select[i - 1][j + 1] == grid.main_color and grid.select[i + 1][j - 1] == grid.main_color:
                                        self.correct = False
                            elif i == 0:
                                if j == 0:
                                    if grid.select[i][j] != grid.main_color and grid.select[i + 1][j] == grid.main_color and grid.select[i][j + 1] == grid.main_color \
                                            and grid.select[i + 1][j + 1] == grid.main_color:
                                        self.correct = False
                                elif j == 3:
                                    if grid.select[i][j] != grid.main_color and grid.select[i + 1][j] == grid.main_color and grid.select[i][j - 1] == grid.main_color \
                                            and grid.select[i + 1][j - 1] == grid.main_color:
                                        self.correct = False
                            elif i == 3:
                                if j == 0:
                                    if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and grid.select[i][j + 1] == grid.main_color \
                                            and grid.select[i - 1][j + 1] == grid.main_color:
                                        self.correct = False
                                if j == 3:
                                    if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and grid.select[i][j - 1] == grid.main_color \
                                            and grid.select[i - 1][j - 1] == grid.main_color:
                                        self.correct = False
                        if self.check_r is True:
                            self.correct = False
                if empty is False and self.correct is True:
                    print("saved")
                else:
                    empty = True
            else:
                empty = True

        return empty