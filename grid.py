import pygame

class Grid(object):
    def __init__(self, columns, rows, screen, line_thickness, block_side):
        self.columns = columns
        self.rows = rows
        self.screen = screen
        self.line_thickness = line_thickness
        self.block_side = block_side
        self.color = [255,255,255]
        self.column_row = []

    def list_for_grid(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                c_r = i, j
                self.column_row.append(c_r)
                # print(grid.column_row)

    def draw_grid(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                pygame.draw.rect(self.screen, self.color, [self.line_thickness + (i * self.block_side), self.line_thickness + (j * self.block_side), self.block_side, self.block_side], 1)