import pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
# Title and icon
pygame.display.set_caption("TETRIS")
icon = pygame.image.load("resources/TetrisIcon.png")
pygame.display.set_icon(icon)

running = True
# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((192, 192, 192)) # change background color
    pygame.display.update()