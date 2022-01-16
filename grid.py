import pygame

class Grid(object):
    def __init__(self, columns, rows, screen, line_thickness, block_side, board_width):
        self.columns = columns
        self.rows = rows
        self.screen = screen
        self.line_thickness = line_thickness
        self.block_side = block_side
        self.main_color = (255,255,255)
        self.column_row = []
        self.grid_colors = []
        self.board_width = board_width

    def list_for_grid(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                c_r = i, j
                self.column_row.append(c_r)
                # print(grid.column_row)

        self.grid_colors = [[self.main_color for x in range(self.columns)] for y in range(self.rows)]


    def draw_grid(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                if self.grid_colors[j][i] == self.main_color:
                    pygame.draw.rect(self.screen, self.grid_colors[j][i], [self.line_thickness + (i * self.block_side),
                                                                      self.line_thickness + (j * self.block_side),
                                                                      self.block_side, self.block_side], 1)
                else:
                    pygame.draw.rect(self.screen, self.grid_colors[j][i], [self.line_thickness + (i * self.block_side),
                                                                      self.line_thickness + (j * self.block_side),
                                                                      self.block_side, self.block_side], 0)
    def draw_small_grid(self):
        start_drawing = self.board_width + self.line_thickness + 30
        for i in range(0, 4):
            for j in range(0, 4):
                pygame.draw.rect(self.screen, self.grid_colors[j][i], [self.line_thickness + (i * self.block_side) + start_drawing,
                                                                  self.line_thickness + (j * self.block_side) + 200,
                                                                  self.block_side, self.block_side], 1)