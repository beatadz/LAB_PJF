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

    def check_new_shape(self, grid):
        empty_column = [True, True, True, True]

        for j in range(0, 4):
            for l in range(0, 4):
                if grid.select[j][l] != grid.main_color:
                    empty_column[l] = False

        if empty_column[1] is True and empty_column[2] is True and empty_column[0] is False and empty_column[3] is False:
            self.correct = False
        elif empty_column[1] is True and empty_column[2] is False and empty_column[0] is False and empty_column[3] is False:
            self.correct = False
        elif empty_column[2] is True and empty_column[3] is False and empty_column[0] is False and empty_column[1] is False:
            self.correct = False

        # check empty spaces between blocks
        if self.count > 1:
            for i in range(0, 4):
                self.check_r = True
                r = 0
                empty_row = True
                for k in range(0, i):
                    for l in range(0, 4):
                        if grid.select[k][l] != grid.main_color:
                            r = 1
                for l in range(0, 4):
                    if grid.select[i][l] != grid.main_color:
                        empty_row = False

                if empty_row is True:
                    self.check_r = False

                for j in range(0, 4):
                    if i == 0:
                        self.check_r = False
                    else:
                        if 0 < j < 3:
                            if r > 0:
                                if grid.select[i][j] != grid.main_color and (
                                        grid.select[i - 1][j] != grid.main_color
                                        or grid.select[i - 1][j - 1] != grid.main_color
                                        or grid.select[i - 1][j + 1] != grid.main_color):

                                    self.check_r = False

                            else:
                                self.check_r = False
                        else:
                            if r > 0:
                                if j == 3:
                                    if grid.select[i][j] != grid.main_color and (
                                            grid.select[i - 1][j] != grid.main_color
                                            or grid.select[i - 1][j - 1] != grid.main_color):
                                        self.check_r = False
                                elif j == 0:
                                    if grid.select[i][j] != grid.main_color and (
                                            grid.select[i - 1][j] != grid.main_color
                                            or grid.select[i - 1][j + 1] != grid.main_color):
                                        self.check_r = False
                            else:
                                self.check_r = False

                        if i == 3:
                            if j == 0:
                                if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and \
                                        grid.select[i][j + 1] == grid.main_color \
                                        and grid.select[i - 1][j + 1] == grid.main_color:
                                    self.correct = False
                                    # print(i, j)
                            if j == 3:
                                if grid.select[i][j] != grid.main_color and grid.select[i - 1][j] == grid.main_color and \
                                        grid.select[i][j - 1] == grid.main_color \
                                        and grid.select[i - 1][j - 1] == grid.main_color:
                                    self.correct = False

                #print(self.check_r, i, j)
                if self.check_r is True:
                    self.correct = False
                #print(r)

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
            self.check_r = False
            self.shape.clear()
            self.row = ""
        else:
            shapes.new_colors.append(self.new_shapes_colors)

            for i in range(0, 4):
                self.full_shape.append(self.shape)

            if shapes.shapes.count(self.full_shape) == 0:
                shapes.shapes.append(self.full_shape)
                shapes.colors.append(self.colors)

                self.check_new_shape(grid)

                if empty is False and self.correct is True:
                    print("saved")
                else:
                    empty = True
            else:
                empty = True

        return empty