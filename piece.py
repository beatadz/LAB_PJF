import shapes
import random
import pygame

class Piece(object):
    def __init__(self, column, row, shape, screen, block_side, line_thickness, color, grid, columns, rows, g_score):
        self.column = column
        self.row = row
        self.shape = shape
        self.screen = screen
        self.block_side = block_side
        self.line_thickness = line_thickness
        self.color = color
        self.rotation = 0
        self.column_row = [(1,1),(1,1),(1,1),(1,1)]
        self.next_column_row = [(1, 1), (1, 1), (1, 1), (1, 1)]
        self.grid = grid
        self.stop = True
        self.columns = columns
        self.rows = rows
        self.g_score = g_score
        self.empty = []

    def draw_shape(self):
        i = j = k = count = 0
        s_row = s_column = 4
        nr = self.rotation
        if nr >= 4:
            nr = self.rotation = 0

        # nr - position, j - row, k - column, i - index of column_row
        # print(current_piece.shape)
        x = self.shape

        # check if the first row is empty
        for a in range(s_column):
            if x[nr][0][a] == '0':
                count += 1

        if count == 4:
            j = 1
        # ACTUAL SHAPE
        while j < s_row:
            while k < s_column:
                if x[nr][j][k] == '1':
                    pygame.draw.rect(self.screen, self.color, [self.line_thickness + ((self.column + k) * self.block_side),
                                                               self.line_thickness + ((self.row + j) * self.block_side),
                                                               self.block_side, self.block_side], 0)
                    self.column_row[i] = self.column + k, self.row + j

                    i += 1
                k += 1
            j += 1
            k = 0

        j = k = i = 0

        # NEXT SHAPE
        while j < s_row:
            while k < s_column:
                if nr < 3:
                    if x[nr + 1][j][k] == '1':
                        self.next_column_row[i] = self.column + k, self.row + j
                        i += 1
                else:
                    if x[0][j][k] == '1':
                        self.next_column_row[i] = self.column + k, self.row + j
                        i += 1
                k += 1
            j += 1
            k = 0

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
                self.stop = False
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
                self.color = shapes.shape_colors[random.randint(0, len(shapes.shape_colors) - 1)]
                self.shape = random.choice(shapes.shapes)
                #self.shape = shapes.shapes[0] # - do testów
                if self.shape == shapes.S2:
                    self.column += 1

        return end

    def check_rotation(self):
        end = True
        #print(self.next_column_row)
        for x in self.next_column_row:
            if x[0] >= self.columns:
                end = False
            elif x[0] < 0:
                end = False

            if x[1] >= self.rows:
                end = False
            elif x[1] < 0 :
                end = False
        return end

    def check_full_line(self):
        count = 0
        empty = []

        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid.grid_colors[i][j] != self.grid.main_color:
                    count += 1
            if count == self.columns:
                empty.append(i)
                self.g_score.game_score += self.g_score.points
                for k in range(self.columns):
                    self.grid.grid_colors[i][k] = self.grid.main_color

            count = 0
        self.empty = empty

    def fix_empty_lines(self):
        for empty_row in self.empty:
            r = empty_row
            while r >= 1:
                #print(r)
                for c in range(self.columns):
                    if self.grid.grid_colors[r][c] != self.grid.main_color or r == empty_row:
                        self.grid.grid_colors[r][c] = self.grid.grid_colors[r-1][c]
                r -= 1