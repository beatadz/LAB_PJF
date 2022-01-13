import pygame
from pygame.locals import *
import shapes
import piece
import grid
import random

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
move_speed = 2
rotation_speed = 10
rotation_counter = 0
move_counter = 0

rectangles = []

def draw_frame():
    pygame.draw.rect(screen, [0,0,0], [0, 0, board_width + 2 * line_thickness, board_height], line_thickness)


# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)
# Title and icon
pygame.display.set_caption("TETRIS")
icon = pygame.image.load("resources/TetrisIcon.png")
pygame.display.set_icon(icon)

#Load images
#Tu kiedyś dodam logo i guziki

grid1 = grid.Grid(columns, rows, screen, line_thickness, block_side)
current_piece = piece.Piece(4, 0, random.choice(shapes.shapes), screen, block_side, line_thickness,shapes.shape_colors[random.randint(0, 6)], grid1)

#next_piece = get_tetris_shape()
falling = clock.tick(FPS)

screen.fill((192, 192, 192)) # change background color
running = True

grid1.list_for_grid()

# Game Loop
while running:
    key = pygame.key.get_pressed()
    screen.fill((192, 192, 192))
    falling += clock.tick(FPS)
    rotation_counter += 1
    move_counter += 1
    is_down = False

    grid1.draw_grid()
    draw_frame()
    current_piece.draw_shape()

    #ESC OR GAME OVER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_piece.stop is False:
        running = False

    c_right = current_piece.check_right()
    c_left = current_piece.check_left()
    c_bottom = current_piece.check_bottom()

    if key[pygame.K_SPACE]:
        if rotation_counter > rotation_speed:
            current_piece.rotation += 1
            rotation_counter = 0
    if key[pygame.K_DOWN]:
        is_down = True
        if move_counter > move_speed and c_bottom is True:
            current_piece.row += 1
            move_counter = 0
    elif key[pygame.K_RIGHT]:
        if move_counter > move_speed and c_right is True:
            current_piece.column += 1
            move_counter = 0
    elif key[pygame.K_LEFT]:
        if move_counter > move_speed and c_left is True:
            current_piece.column -= 1
            move_counter = 0

    if falling / speed > 0.1 and is_down is False:
        current_piece.row += 1
        #print(current_piece.column, current_piece.row)
        #print(current_piece.check_left(), current_piece.check_right())
        falling = 0

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()