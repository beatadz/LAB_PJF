import pygame
from pygame.locals import *
from shapes import *
from Piece import Piece
from Piece import random

pygame.init()
screen_height = 810
screen_width = 750

board_height = 810
board_width = 520

block_side = 40

columns = 13
rows = 20

line_thickness = 5

clock = pygame.time.Clock()
FPS = 60
speed = 3000
move_speed = 1000

left = right = top = bottom = stop = 0

rectangles = []

def random_shape():
    return random.choice(shapes)

def draw_frame():
    pygame.draw.rect(screen, [0,0,0], [0, 0, board_width + 2 * line_thickness, board_height], line_thickness)

def draw_grid():
    for i in range(0,columns):
        for j in range(0, rows):
            pygame.draw.rect(screen, [255,255,255], [line_thickness + (i * block_side), line_thickness + (j * block_side), block_side, block_side], 1)
            rect = Rect(line_thickness + (i * block_side), line_thickness + (j * block_side), block_side, block_side)
            #rectangles.append((i * block_side, j * block_side))
            rectangles.append(rect)

def get_tetris_shape():
    return Piece(4, 0, random_shape())

def draw_shape(current_piece, nr):
    i = j = k = 0
    # nr - position, j - row, k - column, i - index of column_row
    #print(current_piece.shape)
    x = current_piece.shape
    while j < 4:
        while k < 4:
            if x[nr][j][k] == '1':
                pygame.draw.rect(screen, current_piece.color, [line_thickness + ((current_piece.column + k) * block_side), line_thickness + ((current_piece.row + j) * block_side), block_side, block_side], 0)
                #rectangle = Rect(line_thick + ((current_piece.column + k) * block_side),line_thick + ((current_piece.row + j) * block_side), block_side, block_side)
                point = line_thickness + ((current_piece.column + k) * block_side), line_thickness + ((current_piece.row + j) * block_side)
                current_piece.positions_list.append(point)
                current_piece.column_row[i] = current_piece.column + k, current_piece.row + j
                i += 1
            k += 1
        j += 1
        k = 0
        #print("\n")

def check_right(current_piece):
    end = True
    for x in current_piece.column_row:
        if x[0] >= 12:
            end = False
    return end

def check_left(current_piece):
    end = True
    for x in current_piece.column_row:
        if x[0] <= 0:
            end = False
    return end

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

screen.fill((192, 192, 192)) # change background color
running = True

# Game Loop
while running:
    key = pygame.key.get_pressed()
    screen.fill((192, 192, 192))
    falling += clock.tick(FPS)

    draw_grid()
    draw_frame()
    draw_shape(current_piece, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if falling / speed > 0.1:
        current_piece.row += 1
        print(current_piece.column, current_piece.row)
        print(check_left(current_piece), check_right(current_piece))
        falling = 0

    c_right = check_right(current_piece)
    c_left = check_left(current_piece)

    if key[pygame.K_SPACE]:
        current_piece.rotation += 1
    if key[pygame.K_DOWN]:
        if bottom == 0:
            current_piece.row += 1
    elif key[pygame.K_RIGHT]:
        if right == 0 and c_right is True:
            current_piece.column += 1
    elif key[pygame.K_LEFT]:
        if left == 0 and c_left is True:
            current_piece.column -= 1



    pygame.display.update()
    clock.tick(FPS)

pygame.quit()