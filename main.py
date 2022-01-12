import pygame
from pygame.locals import *
import random

pygame.init()
screen_height = 810
screen_width = 750

board_height = 810
board_width = 520

block_side = 40

columns = 13
rows = 20

line_thick = 5

clock = pygame.time.Clock()
FPS = 60
speed = 3000
move_speed = 1000

# Shapes
S1 = [['0000',
       '1111',
       '0000',
       '0000'],
      ['1000',
       '1000',
       '1000',
       '1000'],
      ['0000',
       '1111',
       '0000',
       '0000'],
      ['1000',
       '1000',
       '1000',
       '1000']]

S2 = [['1100',
       '1100',
       '0000',
       '0000'],
      ['1100',
       '1100',
       '0000',
       '0000'],
      ['1100',
       '1100',
       '0000',
       '0000'],
      ['1100',
       '1100',
       '0000',
       '0000']]

S3 = [['0111',
       '0010',
       '0000',
       '0000'],
      ['0010',
       '0110',
       '0010',
       '0000'],
      ['0010',
       '0111',
       '0000',
       '0000'],
      ['0100',
       '0110',
       '0100',
       '0000']]

S4 = [['0000',
       '0111',
       '0100',
       '0000'],
      ['0110',
       '0010',
       '0010',
       '0000'],
      ['0001',
       '0111',
       '0000',
       '0000'],
      ['0010',
       '0010',
       '0011',
       '0000']]

S5 = [['0000',
       '0111',
       '0001',
       '0000'],
      ['0010',
       '0010',
       '0110',
       '0000'],
      ['0100',
       '0111',
       '0000',
       '0000'],
      ['0011',
       '0010',
       '0010',
       '0000']]

S6 = [['0110',
       '0011',
       '0000',
       '0000'],
      ['0010',
       '0110',
       '0100',
       '0000'],
      ['0110',
       '0011',
       '0000',
       '0000'],
      ['0010',
       '0110',
       '0100',
       '0000']]

S7 = [['0011',
       '0110',
       '0000',
       '0000'],
      ['0010',
       '0011',
       '0001',
       '0000'],
      ['0011',
       '0110',
       '0000',
       '0000'],
      ['0010',
       '0011',
       '0001',
       '0000']]

shapes = [S1, S2, S3, S4, S5, S6, S7]
shape_colors = [(255, 140, 0), (154,205,50), (0,206,209), (147,112,219), (255,105,180), (255,255,0), (135,206,250)]
rectangles = []

class Piece(object):
    def __init__(self, column, row, shape):
        self.column = column
        self.row = row
        self.shape = shape
        self.color = shape_colors[random.randint(0, 6)]
        self.rotation = 0
        self.positions_list = []

def random_shape():
    return random.choice(shapes)

def draw_frame():
    pygame.draw.rect(screen, [0,0,0], [0, 0, board_width + 2*line_thick, board_height], line_thick)

def draw_grid():
    for i in range(0,columns):
        for j in range(0, rows):
            pygame.draw.rect(screen, [255,255,255], [line_thick + (i * block_side), line_thick + (j * block_side), block_side, block_side], 1)
            rect = Rect(line_thick + (i * block_side), line_thick + (j * block_side), block_side, block_side)
            #rectangles.append((i * block_side, j * block_side))
            rectangles.append(rect)

def get_tetris_shape():
    return Piece(4, 0, random_shape())

def draw_shape(current_piece):
    i = j = k = 0
    # i - position, j - row, k - column
    #print(current_piece.shape)
    x = current_piece.shape
    while j < 4:
        while k < 4:
            #print(x[i][j][k] + ' ')
            if x[i][j][k] == '1':
                pygame.draw.rect(screen, current_piece.color, [line_thick + ((current_piece.column + k) * block_side), line_thick + ((current_piece.row + j) * block_side), block_side, block_side], 0)
                #rectangle = Rect(line_thick + ((current_piece.column + k) * block_side),line_thick + ((current_piece.row + j) * block_side), block_side, block_side)
                point = line_thick + ((current_piece.column + k) * block_side),line_thick + ((current_piece.row + j) * block_side)
                current_piece.positions_list.append(point)
            k += 1
        j += 1
        k = 0
        #print("\n")

def collision(current_piece, falling):
    i = 0
    for z in current_piece.positions_list:
        #print(z[0], z[1])
        if z[0] <= line_thick:
            current_piece.column += 1
        if z[0] >= board_width:
            current_piece.column -= 1
        if z[1] <= line_thick:
            current_piece.row += 1
        if z[1] >= board_height:
            current_piece.row -= 1

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)
# Title and icon
pygame.display.set_caption("TETRIS")
icon = pygame.image.load("resources/TetrisIcon.png")
pygame.display.set_icon(icon)
#Load images
#Tu kiedyś dodam logo i guziki

current_piece = get_tetris_shape()
next_piece = get_tetris_shape()
falling = clock.tick(FPS)

#draw_grid()
#print(rectangles)
screen.fill((192, 192, 192)) # change background color

#draw_shape(current_piece)
running = True
# Game Loop
while running:
    key = pygame.key.get_pressed()
    screen.fill((192, 192, 192))
    falling += clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if falling / speed > 0.1:
        current_piece.row += 1
        falling = 0

    if key[pygame.K_SPACE]:
        current_piece.rotation += 1
    if key[pygame.K_DOWN]:
        current_piece.row += 1
    if key[pygame.K_RIGHT]:
        current_piece.column += 1
    if key[pygame.K_LEFT]:
        current_piece.column -= 1

    draw_grid()
    draw_frame()
    draw_shape(current_piece)
    #collision(current_piece)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()