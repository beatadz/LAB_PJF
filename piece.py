import shapes
import random
import pygame
import grid
class Piece(object):
    def __init__(self, column, row, shape, screen, block_side, line_thickness, color, grid):
        self.column = column
        self.row = row
        self.shape = shape
        self.screen = screen
        self.block_side = block_side
        self.line_thickness = line_thickness
        self.color = color
        self.rotation = 0
        self.column_row = [(1,1),(1,1),(1,1),(1,1)]
        self.grid = grid

    def draw_shape(self):
        i = j = k = 0
        nr = self.rotation
        if nr >= 4:
            nr = self.rotation = 0

        # nr - position, j - row, k - column, i - index of column_row
        # print(current_piece.shape)
        x = self.shape
        while j < 4:
            while k < 4:
                if x[nr][j][k] == '1':
                    pygame.draw.rect(self.screen, self.color, [self.line_thickness + ((self.column + k) * self.block_side), self.line_thickness + ((self.row + j) * self.block_side), self.block_side, self.block_side], 0)
                    # rectangle = Rect(self.line_thickness + ((self.column + k) * self.block_side), self.line_thickness + ((self.row + j) * self.block_side), self.block_side, self.block_side)
                    self.column_row[i] = self.column + k, self.row + j
                    i += 1
                k += 1
            j += 1
            k = 0
            # print("\n")

    def check_right(self):
        end = True
        for x in self.column_row:
            if x[0] >= 12:
                end = False
            else:
                if self.grid.grid_colors[x[1]][x[0] + 1] != self.grid.main_color:
                    end = False
        return end

    def check_left(self):
        end = True
        for x in self.column_row:
            if x[0] <= 0:
                end = False
            else:
                if self.grid.grid_colors[x[1]][x[0] - 1] != self.grid.main_color:
                    end = False
        return end

    def check_bottom(self):
        c = self.color
        end = True

        for x in self.column_row:
            if x[1] >= 19:
                end = False
            elif x[1] == 0 and self.grid.grid_colors[x[1] + 1][x[0]] != self.grid.main_color:
                print("KONIEC") #tu dodać koniec gry
            else:
                if self.grid.grid_colors[x[1] + 1][x[0]] != self.grid.main_color:
                    end = False

        if end is False:
            #print(self.column_row)
            for x in self.column_row:
                self.grid.grid_colors[x[1]][x[0]] = c
                #print(x[1], x[0])
                self.column = 4
                self.row = 0
                self.color = shapes.shape_colors[random.randint(0, 6)]
                self.shape = random.choice(shapes.shapes)

            #for x in range(0, len(grid.grid_colors)):
                #for y in range(0, len(grid.grid_colors[0])):
                    #print(grid.grid_colors[x][y])
        return end
