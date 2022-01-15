import pygame
import button

def make_title_screen(screen_width, screen_height, screen):
    start_button_image = pygame.image.load("resources/blue_button.png")
    start_button = button.Button("START", (screen_width/2, screen_height/2), "arial", (0, 0, 0), 20, start_button_image, 1, screen)
    tetris_title = pygame.image.load("resources/Tetris.png")
    screen.fill((255, 255, 255))
    screen.blit(tetris_title, (0, 0))
    x = start_button.create_button()