import pygame
import shapes

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
        self.select = []
        self.count = 0
        self.max = 16

    def list_for_grid(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                c_r = i, j
                self.column_row.append(c_r)
                # print(grid.column_row)

        self.grid_colors = [[self.main_color for x in range(self.columns)] for y in range(self.rows)]
        self.select = [[self.main_color for x in range(4)] for y in range(4)]


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
    def draw_creator_grid(self, selected_color):
        start_drawing = 110
        for i in range(0, 4):
            for j in range(0, 4):
                rect = pygame.Rect(self.line_thickness + (i * self.block_side) + start_drawing,
                                   self.line_thickness + (j * self.block_side) + 190,
                                   self.block_side, self.block_side)
                if self.select[j][i] == self.main_color:
                    pygame.draw.rect(self.screen, self.select[j][i], rect, 1)
                else:
                    pygame.draw.rect(self.screen, self.select[j][i], rect, 0)
                # get mouse position
                pos = pygame.mouse.get_pos()

                # check mouseover and clicked conditions
                if rect.collidepoint(pos) and self.count < self.max:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if selected_color != 0 and self.select[j][i] != selected_color:
                            self.count += 1
                            self.select[j][i] = selected_color

                #pygame.draw.rect(self.screen, self.main_color, rect, 1)

    def clear_creator_grid(self, checkboxes):
        for i in range(0, 4):
            for j in range(0, 4):
                self.select[j][i] = self.main_color

                self.count = 0
                for box in checkboxes:
                    box.checked = False


    def clear_grid(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                self.grid_colors[j][i] = self.main_color